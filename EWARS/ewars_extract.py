import requests
import os
import time
import urllib.parse
import json
import copy
import itertools

DASHBOARD_UUID = "881c87a0-f2c6-440a-bab4-9996b5c0fb8c"
BASE_URL = "https://bi.sehatty.ps"

### Change to card_filters_health_facility.json to extract health facility names (will result in ~1 week long script runtime)
with open("card_filters.json", "r") as f:
    CARD_SPECIFIC_FILTERS = json.load(f)

def generate_dynamic_payload(base_parameters, current_filters):
    params_copy = copy.deepcopy(base_parameters)
    
    for param in params_copy:
        param_slug = str(param.get("slug", "")).lower()
        param_name = str(param.get("name", "")).lower()
        
        for key, value in current_filters.items():
            key_lower = key.lower().strip()
            
            if key_lower == param_slug or key_lower == param_name:
                param["value"] = [value] 
                
    encoded_params = urllib.parse.quote(json.dumps(params_copy))
    return f"parameters={encoded_params}&format_rows=false&pivot_results=false"

def export_dashboard():
    session = requests.Session()
    
    headers = {
        'Host': 'bi.sehatty.ps',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:149.0) Gecko/20100101 Firefox/149.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': f'{BASE_URL}/public/dashboard/{DASHBOARD_UUID}',
        'Connection': 'keep-alive',
        'Cookie': 'metabase.DEVICE=6bd2c134-9605-429f-9089-88de9ebbe763',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0, i',
        'TE': 'trailers'
    }

    print("Fetching master dashboard configuration...")
    meta_url = f"{BASE_URL}/api/public/dashboard/{DASHBOARD_UUID}"
    meta_res = session.get(meta_url, headers=headers)
    
    if meta_res.status_code != 200:
        print(f"Failed to fetch metadata. Status: {meta_res.status_code}")
        return

    dashboard_json = meta_res.json()
    cards = dashboard_json.get('dashcards', [])
    base_parameters = dashboard_json.get('parameters', [])
    
    print(f"Found {len(cards)} total cards.")

    for item in cards:
        card_info = item.get('card')
        if not card_info or 'id' not in card_info:
            continue

        dashcard_id = item.get('id')
        card_id = card_info.get('id')
        card_name = card_info.get('name', f"card_{card_id}")
        safe_card_name = "".join(c for c in card_name if c.isalnum() or c in (' ', '_')).strip().replace(" ", "_")
        
        options_for_this_card = {}
        for keyword, options in CARD_SPECIFIC_FILTERS.items():
            if keyword.strip().lower() == card_name.strip().lower():
                options_for_this_card = options
                break
        
        if not options_for_this_card:
            print(f"\n--- Skipping Card: {card_name} (No filters defined) ---")
            continue

        keys, values = zip(*options_for_this_card.items())
        combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]
        
        print(f"\n--- Processing Card: {card_name} ---")
        print(f"    Running {len(combinations)} specific filter combinations...")

        for combo in combinations:
            combo_label = "_".join([str(v).lower().replace(" ", "") for v in combo.values()])
            folder_path = f"raw-data/{safe_card_name}"
            os.makedirs(folder_path, exist_ok=True)
            
            custom_payload = generate_dynamic_payload(base_parameters, combo)
            query_url = f"{BASE_URL}/api/public/dashboard/{DASHBOARD_UUID}/dashcard/{dashcard_id}/card/{card_id}/csv"

            try:
                response = session.post(query_url, headers=headers, data=custom_payload)

                if response.status_code == 200:
                    filepath = f"{folder_path}/{combo_label}.csv"
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    print(f"  [SUCCESS] {combo_label}")
                else:
                    print(f"  [FAILED] {combo_label} -> Status: {response.status_code}")
                    
            except Exception as e:
                print(f"  [ERROR] {combo_label} -> {e}")
            
            time.sleep(1.5)

if __name__ == "__main__":
    export_dashboard()