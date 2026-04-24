
<h1 align="center">
  <br>
  <a href="https://www.bu.edu/spark/" target="_blank"><img src="https://www.bu.edu/spark/files/2023/08/logo.png" alt="BUSpark" width="200"></a>
  <br>
  Project README Template <change to project name>
  <br>
</h1>

<h4 align="center">A template for the project readme file. </h4> <change to repo short description>

<p align="center">
  <a href="#about-the-project">About</a> •
  <a href="#dataset-snapshot">Dataset</a> •
  <a href="#preprocessing--cleaning">Preprocessing</a> •
  <a href="#pipeline">Pipeline</a> •
  <a href="#deliverables">Deliverables</a> •
  <a href="#known-gaps--recommended-next-steps">Known Gaps</a>
</p>
# WASH — Center for Forced Displacement
## HDX State of Palestine Data Pipeline
**Spring 2026 | BU Spark! | CDS**

---

## Project Information

| Field | Details |
|---|---|
| **Project Name** | WASH — Center for Forced Displacement (HDX Pipeline) |
| **GitHub Repository** | [ds-wash-displacement](https://github.com/BU-Spark/ds-wash-displacement) |
| **Google Drive Folder** | [Google Drive](https://drive.google.com/drive/folders/1Gtkj4HSNeKy4oQICiC25yWaIChnC5w3A) |
| **Client** | Dr. Amira Aker, BU School of Public Health |
| **Client Contact** | amaker@bu.edu |
| **Class** | SPARK / CDS / Spring 2026 |

### About the Project
This project consolidates fragmented humanitarian data related to WASH (Water, Sanitation, and Hygiene) conditions in Palestine into one centralized master dataset. Data on attacks against healthcare, food systems, water infrastructure, and displaced persons camps was scattered across multiple HDX Excel files with inconsistent structures. We built an automated Python pipeline to merge all sources into one clean, analysis-ready dataset — replacing manual collection workflows and laying the foundation for future outbreak monitoring and analysis.

---

## Dataset Information

| Field | Details |
|---|---|
| **Dataset Location** | [Google Drive](https://drive.google.com/drive/folders/1Gtkj4HSNeKy4oQICiC25yWaIChnC5w3A) |
| **Tags** | ETL, Data Integration, Humanitarian, WASH, Health, Civic Tech |
| **Access Type** | Open Access |

---

## Dataset Snapshot

| Field | Full Dataset | Gaza Strip Only |
|---|---|---|
| **Size** | ~56 MB | ~23 MB |
| **Number of instances** | 138,424 | 85,283 |
| **Number of fields** | 26 | 15 |
| **Date range** | 2016–2026 | 2016–2026 |
| **Labeled classes** | N/A | N/A |

---

## Composition

### What each instance represents
Each row represents **one indicator value for one reported incident**. The dataset is in long format — meaning if one incident had 14 indicators recorded, it becomes 14 rows.

### Columns

| Column | Description |
|---|---|
| `record_id` | Unique row ID prefixed by source (e.g. HEALTH-000042) |
| `data_source` | Full source and managing org name |
| `source_file` | Original HDX filename |
| `indicator_code` | Short unique code per indicator (e.g. HDX_H_W_KILLED) |
| `indicator_name` | Human-readable indicator name |
| `indicator_category` | Thematic group (e.g. Healthcare Personnel, Water Infrastructure) |
| `date` | Incident date (YYYY-MM-DD) |
| `year` | Calendar year |
| `admin_1` | Admin 1 region (Gaza Strip, West Bank, etc.) |
| `reported_perpetrator` | Perpetrator category |
| `reported_perpetrator_name` | Named perpetrator entity |
| `weapon_used` | Weapon type used in incident |
| `population_subgroup` | Affected population group |
| `value` | Numeric indicator value (NULL if missing) |
| `unit` | Unit of measurement (count, incident count) |
| `missingness_flag` | NOT_MISSING or MISSING_AMBIGUOUS |

### Source Files

| Source File | Theme | Date Range | Raw Incidents | Rows After Unpivot | Indicators |
|---|---|---|---|---|---|
| 2016-2026-pse-attacks-on-health-care | Health | 2016–2026 | 4,259 | 59,626 | 14 |
| 2020-2026-pse-protection-in-danger | Protection | 2020–2026 | 6,897 | 75,867 | 11 |
| 2024-2026-pse-food-systems | Food Security | 2023–2026 | 1,833 | 1,833 | 1 |
| 2025-2026-pse-water-systems | Water | 2023–2026 | 122 | 1,098 | 9 |

---

## Collection Process

- Data downloaded directly from the **Humanitarian Data Exchange (HDX)** as public Excel files
- No scraping required for these 4 sources — HDX provides direct downloads
- **Data collected:** April 2026
- **Incident records span:** January 2016 – March 2026

---

## Preprocessing & Cleaning

### Steps taken

- Loaded all 4 raw Excel files using `pandas`
- Extracted shared base columns (date, location, perpetrator, weapon) from each file into a standardized format
- **Unpivoted (melted) indicator columns** from wide format to long format
  - Before: one row per incident, one column per indicator
  - After: one row per indicator per incident
- Converted boolean indicator columns to `0/1`
- Standardized column names across all 4 sources
- Flagged all null/blank values as `MISSING_AMBIGUOUS` instead of dropping or assuming zero
- Raw Excel files are preserved and not modified

### Missingness Codebook

| Flag | Definition | How to Handle |
|---|---|---|
| `NOT_MISSING` | Value is present and valid | Use as-is |
| `MISSING_AMBIGUOUS` | Blank — unclear if zero, not recorded, or truly missing | Do NOT assume zero. Flag in analysis. |
| `MISSING_NOT_COLLECTED` | Previously tracked but absent this period | Exclude from trend analysis or impute with justification |
| `MISSING_NEVER_TRACKED` | Never collected for this region or period | Exclude entirely. Note as structural gap. |

---

## Pipeline

The full pipeline is available in [`hdx_pipeline.ipynb`](https://github.com/BU-Spark/ds-wash-displacement/blob/aymentig-patch-1/hdx_pipeline.ipynb).

Running the notebook will:

1. Load the 4 raw HDX Excel files
2. Standardize and merge all sources
3. Export `hdx_master_dataset.csv` (full, 138k rows)
4. Export `hdx_master_gaza.csv` (Gaza Strip only, 85k rows)

To update the dataset when HDX publishes new files — download the latest Excel files and re-run the notebook.

---

## Deliverables

| File | Description |
|---|---|
| `hdx_master_dataset.csv` | Full master dataset, 138,424 rows, 26 columns |
| `hdx_master_gaza.csv` | Gaza Strip only, 85,283 rows, 22.8 MB |
| `hdx_master_schema.xlsx` | Column dictionary, missingness codebook, indicator catalog, source summary |
| `hdx_pipeline.ipynb` | Reproducible Jupyter notebook to regenerate dataset |

---

## Known Gaps & Recommended Next Steps

- **EWARS dashboard** — live Metabase dashboard with no direct download, requires a scraping script. Not yet completed.
- **Sources not yet integrated:** UNICEF JMP, WHO oPt, Gaza Joint WASH Assessment, daily casualties dataset, geographic shapefiles
- **Dataset structure** may need reshaping depending on how the client wants to run downstream analysis

---

## Authors

| Name | Role | Contact |
|---|---|---|
| Aymen | Data Engineer — HDX Pipeline | aymentig@bu.edu |

**Client:** Dr. Amira Aker — amaker@bu.edu
