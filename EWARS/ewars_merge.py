import os
import pandas as pd
import itertools
import json

with open("card_filters.json", "r") as f:
    CARD_SPECIFIC_FILTERS = json.load(f)

def format_epi_week(date_val):
    if pd.isnull(date_val): 
        return date_val
        
    start_date = date_val - pd.Timedelta(days=(date_val.weekday() + 1) % 7)
    end_date = start_date + pd.Timedelta(days=6)
    
    year = date_val.isocalendar().year
    week = date_val.isocalendar().week
    
    return f"{year}-WE{week:02d} ({start_date.strftime('%d-%b')} to {end_date.strftime('%d-%b')})"

def merge_csvs():
    trend_dataframes = []
    other_dataframes = []
    total_files_processed = 0

    print("Starting data merge...")

    for card_name, options in CARD_SPECIFIC_FILTERS.items():
        safe_card_name = "".join(c for c in card_name if c.isalnum() or c in (' ', '_')).strip().replace(" ", "_")
        folder_path = f"raw-data/{safe_card_name}"
        raw_dataframes = []
        
        if not os.path.exists(folder_path):
            print(f"\nSkipping {folder_path}, no folder found")
            continue

        keys, values = zip(*options.items())
        combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]

        for combo in combinations:
            combo_label = "_".join([str(v).lower().replace(" ", "") for v in combo.values()])
            filepath = f"{folder_path}/{combo_label}.csv"
            
            if os.path.exists(filepath):
                try:
                    df = pd.read_csv(filepath)
                    
                    if df.empty:
                        print(f"\nSkipping {filepath}, no data found")
                        continue

                    for filter_key, filter_value in combo.items():
                        if filter_key != "grouping":
                            df[filter_key] = filter_value
                        
                    df['source_card'] = card_name
                    
                    raw_dataframes.append(df)
                    total_files_processed += 1
                    
                except Exception as e:
                    print(f"  [ERROR] Could not read {filepath}: {e}")

        card_df = pd.concat(raw_dataframes, ignore_index=True)
        if 'cases' in df.columns:
            card_df = card_df.rename(columns={'cases': f'{safe_card_name.removesuffix("_Trend")}_Cases'.replace("_", " ")})
        if 'deaths' in df.columns:
            card_df = card_df.rename(columns={'deaths': f'{safe_card_name.removesuffix("_Trend")}_Deaths'.replace("_", " ")})
        if 'grouping' in options:
            print("\nappending to trend")
            trend_dataframes.append(card_df)
        else:
            print("\nappending to other")
            other_dataframes.append(card_df)

    if trend_dataframes:
        print(f"\nCombining trend files into one dataset...")

        trend_df = trend_dataframes[0]
        if 'source_card' in trend_df.columns:
            trend_df.drop(columns=['source_card'], inplace=True)
        cols = ['time_group', 'governorate', 'location_type','Total Consultations'] + [c for c in trend_df.columns if c not in ['time_group', 'governorate', 'location_type','Total Consultations']]
        trend_df = trend_df[cols]
        for i in range(1, len(trend_dataframes)):
            incoming_df = trend_dataframes[i].copy()
            
            card_source_name = incoming_df['source_card'].iloc[0] if 'source_card' in incoming_df.columns else f"File #{i}"
            
            if 'source_card' in incoming_df.columns:
                incoming_df.drop(columns=['source_card'], inplace=True)
            
            try:
                trend_df = pd.merge(
                    trend_df, 
                    incoming_df, 
                    on=['time_group', 'governorate', 'location_type','Total Consultations'], 
                    how='outer'
                )
            except KeyError as e:
                print(f"\n[MERGE ERROR] Skipping card: '{card_source_name}'")
                print(f"  Missing required column: {e}")
                print(f"  Columns it actually has: {list(incoming_df.columns)}")
                # other_dataframes.append(incoming_df)
                continue

        trend_df['EPI Week'] = pd.to_datetime(trend_df['time_group']).apply(format_epi_week)
        cols = ['EPI Week'] + [c for c in trend_df.columns if c != 'EPI Week']
        trend_df = trend_df[cols]
        trend_df.to_csv("ewars_trends.csv", index=False)
        
        print("\n[SUCCESS] Saved to ewars_trends.csv")
        print(f"Total Rows: {len(trend_df)}")
        print(f"Total Columns: {len(trend_df.columns)}")
    else:
        print("\n[FAILED] No daily CSV files found to merge")
    if other_dataframes:
        print(f"\nCombining other files into one dataset...")
        other_df = other_dataframes[0]
        if 'source_card' in other_df.columns:
            other_df.drop(columns=['source_card'], inplace=True)
        if 'epi_week_label' in other_df.columns:
            other_df = other_df.rename(columns={'epi_week_label': 'EPI Week'})
        for i in range(1, len(other_dataframes)):
            incoming_df = other_dataframes[i].copy()
            
            card_source_name = incoming_df['source_card'].iloc[0] if 'source_card' in incoming_df.columns else f"File #{i}"
            
            if 'source_card' in incoming_df.columns:
                incoming_df.drop(columns=['source_card'], inplace=True)
            if 'epi_week_label' in incoming_df.columns:
                incoming_df = incoming_df.rename(columns={'epi_week_label': 'EPI Week'})
            if 'EPI Weeks' in incoming_df.columns:
                incoming_df.drop(columns=['EPI Weeks'], inplace=True)
            if 'Start Date' in incoming_df.columns:
                incoming_df['EPI Week'] = pd.to_datetime(incoming_df['Start Date']).apply(format_epi_week)
                incoming_df.drop(columns=['Start Date', 'End Date'], inplace=True)
            if 'Active Locations' in incoming_df.columns:
                incoming_df.drop(columns=['Active Locations'], inplace=True)
            if 'Expected Reports' in incoming_df.columns and card_source_name == 'Surveillance Completeness':
                incoming_df.drop(columns=['Expected Reports'], inplace=True)
            try:
                other_df = pd.merge(
                    other_df,  
                    incoming_df, 
                    on=['EPI Week', 'governorate'], 
                    how='outer'
                )
            except KeyError as e:
                print(f"\n[MERGE ERROR] Skipping card: '{card_source_name}'")
                print(f"  Missing required column: {e}")
                print(f"  Columns it actually has: {list(incoming_df.columns)}")
                continue
        
        other_df.to_csv("ewars_other.csv", index=False)
        
        print("\n[SUCCESS] Saved to ewars_other.csv")
        print(f"Total Rows: {len(other_df)}")
        print(f"Total Columns: {len(other_df.columns)}")
    else:
        print("\n[FAILED] No weekly CSV files found to merge")
    print(f"\nAggregating trend data into weeks for merging...")
    trend_df.drop(columns=['time_group','location_type','Total Consultations'], inplace=True)
    weekly_trend_df = trend_df.groupby(['EPI Week','governorate']).sum()
    weekly_df = pd.merge(
                other_df,  
                weekly_trend_df, 
                on=['EPI Week', 'governorate'], 
                how='outer'
            )
    cols = ['EPI Week', 'governorate', 'Reporting Locations', 'Total Consultations', 'Expected Reports', 'Actual Reports', 'Completeness Percentage', 'Actual Timely Reports', 'Timeliness Percentage', 'Average Delay Reporting (Days)'] + [c for c in weekly_df.columns if c not in ['EPI Week', 'governorate', 'Reporting Locations', 'Total Consultations', 'Expected Reports', 'Actual Reports', 'Completeness Percentage', 'Actual Timely Reports', 'Timeliness Percentage', 'Average Delay Reporting (Days)']]
    weekly_df = weekly_df[cols]
    weekly_df.to_csv("ewars_weekly.csv", index=False)
        
    print("\n[SUCCESS] Saved to ewars_weekly.csv")
    print(f"Total Rows: {len(weekly_df)}")
    print(f"Total Columns: {len(weekly_df.columns)}")
if __name__ == "__main__":
    merge_csvs()