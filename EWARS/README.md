# EWARS Data Extraction and Merging Pipeline

This repository contains Python scripts and configuration files designed to automate the extraction, processing, and merging of Early Warning, Alert and Response System (EWARS) data from the Sehatty BI dashboard. 

The pipeline dynamically generates API requests based on specific filter combinations (e.g., governorate, location type, disease trend) to download raw CSV reports, and then aggregates this raw data into clean, merged datasets.

## Pipeline Contents

* **`ewars_extract.py`**: The main extraction script. It reads the JSON filter configurations, generates dynamic API payloads, and downloads the individual raw CSV files for every filter permutation into a `raw-data/` directory.
* **`ewars_merge.py`**: The data aggregation script. It processes the downloaded raw CSV files, calculates official EPI weeks, groups the trend data, and merges everything into unified datasets suitable for analysis.
* **`card_filters.json`**: The default configuration file. It contains the basic filter permutations used to scrape the dashboard, focusing on `governorate` (e.g., Gaza, Khan Yunis, Rafah), `location_type` (e.g., Hospital, PHC, Mobile Clinic), and sets the default grouping to "Daily".
* **`card_filters_health_facility.json`**: An expanded, highly granular configuration file that includes the names of hundreds of individual health facilities (e.g., "Al Ahli Arab Hospital", "European Gaza Hospital", "PMRS Medical point Mawasi Rafah"). 
* **`ewars_daily.csv`**: An output CSV file representing the combined daily granular data.
* **`ewars_weekly.csv`**: An output CSV file containing the final, fully merged dataset aggregated by EPI Week.

---

## How to Run the Pipeline

### Prerequisites
Ensure you have Python 3 installed along with the required standard libraries. You can install the necessary dependencies using `pip`:
```bash
pip install requests pandas
```

### Step 1: Extract the Data
Run the extraction script to download the raw data from the BI dashboard. This script will automatically generate a `raw-data/` folder in your directory and populate it with individual CSV files for each tracked indicator and filter combination.

```bash
python ewars_extract.py
```
*Note: Ensure you have a stable internet connection. The script includes delays (`time.sleep`) to prevent overloading the Sehatty BI servers or flagging your IP address as scaping too quickly. On occasion request headers may need to be changed to be allowed in by the dashboard server.*
Here is a section you can add to your `README.md` (perhaps under a new **Maintenance** or **Troubleshooting** heading) to explain how to update the request headers. 

***

### Updating Request Headers

Because the dashboard relies on active session tokens and specific browser configurations, the request headers hardcoded in the script will eventually expire. If the script starts returning `Status: 401 (Unauthorized)`, `403 (Forbidden)`, or simply failing to download the CSVs, you will need to update the headers in `ewars_extract.py`.

**How to update the headers:**

1. Open your web browser (Chrome, Firefox, Edge) and navigate to the Sehatty BI dashboard.
2. Open the **Developer Tools** (Press `F12` or Right-click anywhere on the page and select **Inspect**).
3. Navigate to the **Network** tab within the Developer Tools.
4. Refresh the dashboard page or manually click a button to download a CSV to trigger a network request.
5. In the Network tab list, look for a request made to the API (often a `POST` request starting with `?parameters=...` or pointing to `/api/public/dashboard/`). Click on it.
6. In the panel that opens, scroll down to the **Request Headers** section. 
7. Open `ewars_extract.py` in your text editor and locate the `headers` dictionary inside the `export_dashboard()` function:

   ```python
   headers = {
       'Host': 'bi.sehatty.ps',
       'User-Agent': 'Mozilla/5.0 ...',
       # Update the Cookie, tokens, or any other necessary fields below:
       'Cookie': 'YOUR_NEW_COOKIE_STRING_HERE',
       # ...
   }
   ```
8. Copy the updated values (especially the `Cookie` or any authentication tokens) from your browser's Developer Tools and paste them into this dictionary. Save the file and rerun the script.

### Step 2: Merge the Data
Once the extraction is completely finished, run the merge script. This script will crawl through the `raw-data/` folder, format dates into official EPI Weeks, aggregate the daily trends, and output the final consolidated CSV files.

```bash
python ewars_merge.py
```

---

## Configuration: Toggling Health Facility Extraction

By default, the scripts aggregate data broadly by **Governorate** and **Location Type** to keep the script execution time manageable. However, you can configure the pipeline to extract data down to the individual **Health Facility** level.

**WARNING: Extended Runtime** Because there are hundreds of registered health facilities, running the extraction at the facility level creates a massive number of API request permutations. **Using the health facility configuration will result in a script runtime of approximately 1 week.**

### How to enable Health Facility tracking:
1. Open `ewars_extract.py` in your text editor.
2. Locate the file reading block near the top of the file:
   ```python
   ### Change to card_filters_health_facility.json to extract health facility names...
   with open("card_filters.json", "r") as f:
       CARD_SPECIFIC_FILTERS = json.load(f)
   ```
3. Change `"card_filters.json"` to `"card_filters_health_facility.json"`.
4. Open `ewars_merge.py` and make the exact same change so the merger script knows to include the health facility parameters during aggregation.

To revert back to the faster, standard extraction at the governorate level, simply change the loaded file in both scripts back to `"card_filters.json"`.

---

## Overview of Resulting CSVs

The pipeline ultimately produces two finalized datasets depending on the granularity of analysis required.

### 1. `ewars_daily.csv`
This file represents the granular, daily reporting data across the monitored regions.
* **Granularity:** Daily
* **Key Columns:** * **Identifiers:** `date`, `governorate`, `location_type`, `EPI Week`.
  * **Aggregations:** `Total Consultations`.
  * **Disease Tracking:** Specific case and death counts (Over 5 / Under 5 where applicable) for ARI, AWD, Bloody Diarrhoea, AJS, AFP, Suspected Measles, Suspected Viral/Bacterial Meningitis, Cholera, Chickenpox, and other unusual events.
* **Use Case:** Ideal for analyzing day-to-day spikes in specific diseases, monitoring daily consultation volumes, or performing daily time-series forecasting.

### 2. `ewars_weekly.csv`
This file is the heavily aggregated output produced by the merging script, designed for higher-level epidemiological review.
* **Granularity:** EPI Week (e.g., `2023-WE33 (13-Aug to 19-Aug)`).
* **Key Columns:** * **Time & Location:** `EPI Week`, `governorate`, `Start Date`, `End Date`.
  * **System Performance:** `Expected Reports`, `Actual Reports`, `Completeness Percentage`, `Actual Timely Reports`, `Timeliness Percentage`, `Average Delay Reporting (Days)`.
  * **Percentage Metrics:** Percentages of suspected diseases relative to total consultations (e.g., `% Suspected ARI`, `% Suspected AWD`).
  * **Total Counts:** Aggregated weekly case counts and deaths for all tracked diseases.
* **Use Case:** Ideal for official weekly epidemiological bulletins, assessing the overall health system reporting compliance (completeness and timeliness), and viewing broader regional health trends over standardized epidemiological weeks.