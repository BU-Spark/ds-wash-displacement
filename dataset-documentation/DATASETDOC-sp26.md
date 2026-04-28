# Project Information

**What is the project name?**
WASH: Center of Forced Displacement

**What is the link to your project's GitHub repository?**
https://github.com/BU-Spark/ds-wash-displacement

**What is the link to your project's Google Drive folder? \*\* This should be a Spark! Owned Google Drive folder - please contact your PM if you do not have access\*\***
https://drive.google.com/drive/u/0/folders/1Gtkj4HSNeKy4oQICiC25yWalChnC5w3A

**In your own words, what is this project about? What is the goal of this project?**
Create a centralized database to track WASH related indicators to facilitate future analysis

**Who is the client for the project?**
Amira Aker

**Who are the client contacts for the project?**
amaker@bu.edu

**What class was this project part of?**
DS539: Data Science Practicum

# Dataset Information

**What data sets did you use in your project? Please provide a link to the data sets, this could be a link to a folder in your GitHub Repo, Spark! owned Google Drive Folder for this project, or a path on the SCC, etc.**

* **EWARS Unified Disease Dashboard**
    * **Source:** https://bi.sehatty.ps/public/dashboard/881c87a0-f2c6-440a-bab4-9996b5c0fb8c?all_epidemiological_weeks=&epidemiological_weeks=&governorate=Khan+Yunis&grouping=Weekly&health_facilty=&location_type=&organization=&tab=4-epidemiological-overview&years=
    * **Processed:** https://drive.google.com/drive/folders/1-ObNtE5IJKNaC5yxLv5p2xbjMRcqy1M7?usp=drive_link
* **WHO/UNICEF JMP**
    * **Source:** https://washdata.org/data
    * **Processed:** https://drive.google.com/drive/folders/1WuFMe5BeR3IrWfFNpl110WIS6GR9cul?usp=drive_link
* **State of Palestine (HDX)**
    * **Source:** https://data.humdata.org/dataset/opt-violent-and-threatening-incidents-against-healthcare
    * **Processed:** https://drive.google.com/drive/folders/1n64UOJcolDcSWydl5iAoiQ-Dj12iCE7Z?usp=drive_link
* **Gaza Joint WASH**
    * **Source:** https://reliefweb.int/report/occupied-palestinian-territory/gaza-joint-wash-assessment-round-3
    * **Processed:** https://drive.google.com/drive/folders/1gjfupRAQGVN4dmE-vOYkUe1jonFb0JQ?usp=drive_link

**Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project.**
*(Not provided in document)*

**What keywords or tags would you attach to the data set?**
Domain(s) of Application: Computer Vision, Object Detection, OCR, Image Classification, Image Segmentation, Facial Recognition, NLP, Topic Modeling, Sentiment Analysis, Named Entity Recognition, Text Classification, Summarization, Anomaly Detection, Other Predictive Modeling, OCR, Data Integration, ETL, Geospatial Data Sustainability, Health, Civic Tech, Voting, Housing, Policing, Budget, Education, Transportation, etc.
**Selected tags:** Health, Civic Tech, Sustainability, WASH, Disease Surveillance, Infrastructure

---

## Motivation

**For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.**
The datasets were integrated to address a critical gap in centralized WASH and infectious disease monitoring for the State of Palestine. Previously, data was fragmented across static PDFs, interactive PowerBI dashboards, and different CSVs. This project provides a unified master database to support predictive health modeling and infrastructure damage assessment.

## Composition

**What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances?**
The instances represent health facility reports (EWARS), household, health facility, schools survey responses/reports (JMP/Gaza Joint WASH), and specific incidents [violent/sanitation] (HDX). The format is: Primarily tabular data (CSV/Excel) extracted from web dashboards and textual/tabular data parsed from PDFs via OCR.

**How many instances are there in total (of each type, if appropriate)?**
* **EWARS:** Weekly reports from 100+ health facilities (consistent starting Dec 2024)
* **HDX:** Hundreds of incident logs dating back to Jan 2017.
* **JMP:** Yearly data from 2019-2024 for household and 2019-2023 for schools and healthcare facilities
* **Gaza Joint:** 3 rounds report from 2024 to 2025 for 13 indicators, 39 instances in total

**Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set?**
* **EWARS:** All possible instances of EWARS-mobile reported consultations in the region, but that does not necessarily include all cases that occur
* **HDX:** It is a sample of reported incidents. While it aims to be a comprehensive record of violence and obstruction against healthcare, it relies on reported data from partners (Insecurity Insight/SHCC).
* **JMP:** It is a sample, there are previous years too. It is representative of the larger dataset as it is a part of all the data that was surveyed.
* **Gaza Joint:** All possible instances of Gaza Joint Wash Assessment report file

**What data does each instance consist of? "Raw" data (e.g., unprocessed text or images) or features?**
* **EWARS:** Processed features but underlying dataset not easily accessible
* **HDX:** Primarily "Raw" incident logs structured into features.
* **JMP:** Processed features with the underlying data from Multiple Indicator Cluster Surveys (MICS) and Demographic and Health Surveys (DHS)
* **Gaza Joint:** Processed features without declaring the exact source

**Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing...**
* **EWARS:** For some reports location type was not recorded properly, likely because the reporting system for those aggregated metrics (surveillance timeliness/completion) was not built out to handle those detailed values
* **HDX:** Yes. There are significant "blanks" in several columns across different years. As noted in the client meetings, it is often unclear if a blank represents a zero (no incidents), a missing value (incident happened but details weren't captured), or an unrecorded indicator for that specific reporting period.
* **JMP:** No missing data from original data, but there is data labeled as insufficient data. But blanks due to difference in the indicators from merging datasets.
* **Gaza Joint:** 6 instances value missing, claimed it was source-based missing

**Are there recommended data splits (e.g., training, development/validation, testing)?**
N/A

**Are there any errors, sources of noise, or redundancies in the dataset?**
* **EWARS:** N/A
* **HDX:** Noise exists in the form of inconsistent reporting granularity over time.
* **JMP:** Maybe, there is data labeled as insufficient. Household data is surveyed so there could be noise.
* **Gaza Joint:** N/A

**Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? Are there guarantees that they will exist, and remain constant, over time?**
* **EWARS:** Relies on EWARS mobile reporting system, which is maintained by the World Health Organization
* **HDX:** It relies on the Humanitarian Data Exchange (HDX) platform and the Safeguarding Health in Conflict Coalition (SHCC)
* **JMP:** Linked to WHO/UNICEF JMP; should remain constant
* **Gaza Joint:** Stated the data are supported by multiple sources in acknowledgements

**Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?**
* **EWARS:** Not available, only able to see certain visuals as presented in the dashboard
* **HDX:** These are managed by OCHA and Insecurity Insight, which generally maintain long-term archival versions
* **JMP:** Not available
* **Gaza Joint:** Not available

**Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer?**
* **EWARS:** N/A
* **HDX:** N/A
* **JMP:** N/A
* **Gaza Joint:** N/A

**Does the dataset contain data that might be considered confidential...?**
* **EWARS:** Data is aggregated so underlying personal information of individual consultations does not exist in the dataset
* **HDX:** The data is provided under a Creative Commons Attribution license (CC BY-SA 4.0), allowing for sharing and adaptation with proper credit
* **JMP:** No
* **Gaza Joint:** No

**Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?**
N/A

**Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?**
N/A

---

## Dataset Snapshots

### EWARS
| EPI Week | time_group | governorate | location_type | Total Consultations | ARI Cases | ARI Deaths | AWD Cases (Over 5) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2023-WE33 (13-Aug to 19-Aug) | 2023-08-18 | Deir Al-Balah | Medical Point | 25 | 0 | 0 | 0 |
| 2023-WE48 (26-Nov to 02-Dec) | 2023-11-29 | Rafah | PHC | 0 | 0 | 0 | 0 |
| 2023-WE50 (10-Dec to 16-Dec) | 2023-12-13 | Khan Yunis | Medical Point | 0 | 0 | 0 | 0 |
| 2023-WE52 (24-Dec to 30-Dec) | 2023-12-29 | Deir Al-Balah | Medical Point | 106 | 42 | 0 | 0 |
| 2023-WE52 (24-Dec to 30-Dec) | 2023-12-29 | Rafah | PHC | 0 | 0 | 0 | 0 |
| 2023-WE52 (24-Dec to 30-Dec) | 2023-12-30 | Deir Al-Balah | Medical Point | 112 | 10 | 0 | 0 |
| 2023-WE52 (24-Dec to 30-Dec) | 2023-12-30 | Rafah | PHC | 0 | 0 | 0 | 0 |
| 2023-WE52 (31-Dec to 06-Jan) | 2023-12-31 | Deir Al-Balah | PHC | 1486 | 707 | 0 | 189 |
| 2023-WE52 (31-Dec to 06-Jan) | 2023-12-31 | Khan Yunis | Medical Point | 23 | 15 | 0 | 0 |
| 2024-WE01 (07-Jan to 13-Jan) | 2024-01-07 | Khan Yunis | Medical Point | 23 | 3 | 0 | 1 |
| 2024-WE02 (07-Jan to 13-Jan) | 2024-01-10 | Gaza | PHC | 0 | 0 | 0 | 0 |
| 2024-WE03 (14-Jan to 20-Jan) | 2024-01-17 | Deir Al-Balah | PHC | 0 | 0 | 0 | 0 |

### WHO/UNICEF JMP
| Country | Year | Sector | Residence/Schools/Facility Type | Service Type | Service Level Facility Type | Safely Managed Element | Coverage | Population |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| State of Palestine | 2019 | Households | total | Drinking water | Non-piped improved | | 41.84262 | 2074460.1573 |
| State of Palestine | 2019 | Households | rural | Drinking water | Non-piped improved | | 13.25638 | 154841.1588 |
| State of Palestine | 2019 | Households | urban | Drinking water | Non-piped improved | | 50.65335 | 1919619.10386 |
| State of Palestine | 2019 | Households | total | Sanitation | Improved latrine and other | | 9.81783 | 486745.13495 |
| State of Palestine | 2019 | Households | rural | Sanitation | Improved latrine and other | | 18.28948 | 213830.29421 |
| State of Palestine | 2019 | Households | urban | Sanitation | Improved latrine and other | | 7.20673 | 273114.84400 |
| State of Palestine | 2019 | Households | total | Drinking water | Piped improved | | 58.15738 | 2883307.78704 |
| State of Palestine | 2019 | Households | rural | Drinking water | Piped improved | | 86.74362 | 1013208.9412 |
| State of Palestine | 2019 | Households | urban | Drinking water | Piped improved | | 49.34665 | 1870098.89614 |
| State of Palestine | 2019 | Households | total | Sanitation | Septic tank | | 36.23015 | 1796206.86472 |
| State of Palestine | 2019 | Households | rural | Sanitation | Septic tank | | 65.35229 | 763347.43233 |
| State of Palestine | 2019 | Households | urban | Sanitation | Septic tank | | 27.25426 | 1032859.44781 |
| State of Palestine | 2019 | Households | total | Sanitation | Sewer | | 53.57796 | 2656270.88968 |
| State of Palestine | 2019 | Households | rural | Sanitation | Sewer | | 14.8722 | 173714.73796 |
| State of Palestine | 2019 | Households | urban | Sanitation | Sewer | | 65.50768 | 2482556.28959 |
| State of Palestine | 2020 | Households | total | Drinking water | Non-piped improved | | 43.46789 | 2203678.07829 |

### Gaza Joint WASH Assessment
| indicator | August 2024 | January 2025 | August 2025 | source page | source table |
| :--- | :--- | :--- | :--- | :--- | :--- |
| % of households with less than 6 lppd of drinking water | 64% | 65% | 49% | 17 | Table 1 |
| % of households with less than 9 lppd of domestic water | 46% | 34% | 28% | 17 | Table 1 |
| % of households with less than 15 lppd of water for all purposes | 46% | 36% | 25% | 17 | Table 1 |
| % of households practicing open defecation | 6% | 3% | | 17 | Table 1 |
| % of households with unimproved sanitation facilities | | 12% | 9% | 17 | Table 1 |
| % of households with basic sanitation facilities | | 53% | 53% | 17 | Table 1 |
| % of household with safely managed sanitation facilities | 0% | 0% | 0% | 17 | Table 1 |
| % of households with sewage or feces within 10 m | 79% | 63% | 57% | 17 | Table 1 |
| % of household with waste piled within 10 m | 54% | 42% | 42% | 17 | Table 1 |
| % of households NOT having soap at accommodation | 76% | 19% | 63% | 17 | Table 1 |
| % of assessed households reported that at least one household member had lice in the 30 days prior to data collection | | 39% | 15% | 17 | Table 1 |
| % of assessed households reported that at least one household member had bedbugs in the 30 days prior to data collection | | | 13% | 17 | Table 1 |
| % of assessed households reported that at least one household member had skin rashes or scabies in the 30 days prior to data collection | | | 57% | 17 | Table 1 |

### State of Palestine (HDX) / Dataset Sizes Overview
| Metric | EWARS (Daily) | State of Palestine / (Weekly) | Gaza Joint Wash (Monthly) | WHO/UNICEF JMP (Yearly) |
| :--- | :--- | :--- | :--- | :--- |
| **Number of instances** | 8,108 | 138,424 | 39 | 1,252 |
| **Number of fields** | 40 | 26 | 7 | 12 |

---

## Collection Process

**What mechanisms or procedures were used to collect the data? How were these mechanisms or procedures validated?**
* **EWARS:** API calls made to dashboard
* **HDX:** Data is collected through a combination of API access and structured file downloads from the Humanitarian Data Exchange. The underlying data is compiled by Insecurity Insight and the Safeguarding Health in Conflict Coalition (SHCC)
* **JMP:** Filed download from website
* **Gaza Joint:** File downloads and OCR extraction code

**If the dataset is a sample from a larger set, what was the sampling strategy?**
* **EWARS:** N/A
* **HDX:** Non-probabilistic / Incident-based sampling. This is not a random sample; it is a collection of all reported and verified incidents.
* **JMP:** Client just wanted data from recent years, so the sample consists of all data of recent years
* **Gaza Joint:** N/A

**Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances?**
* **EWARS:** 2023/08/13 - 2026/04/11
* **HDX:** 2016/01/06 - 2026/03/21
* **JMP:** 2019-2024
* **Gaza Joint:** 2024/08 - 2025/08

---

## Preprocessing/cleaning/labeling

**Was any preprocessing/cleaning/labeling of the data done?**
* **EWARS:** Data was preprocessed after API calls to correctly format values into their actual forms instead of display values for the visuals
* **HDX:** Data cleaning focused on handling blank cells. Documentation was reviewed to distinguish between zero-values and missing information to avoid skewing incident counts.
* **JMP:** No
* **Gaza Joint:** Data are extracted from tables in the file by correspondent indicator name

**Were any transformations applied to the data?**
* **EWARS:** All visuals were saved separately for every possible combination of filters, then those filters were added back as enrichment columns, and then all visuals were joined back together on date and those enriched filter values
* **HDX:** Data aggregation was performed to group individual incident reports by epidemiological week and governorate to allow for direct merging with the EWARS disease surveillance data.
* **JMP:** Data aggregation of 5 different datasets, renamed columns
* **Gaza Joint:** Original data was separated and grouped by reported date and indicator name

**Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data?**
* **EWARS:** Raw data was not permanently saved, but is saved by the extraction script and could be recreated by rerunning that script
* **HDX:** Raw data was not permanently saved in the final repository, but is saved by the extraction script and could be recreated by rerunning the script.
* **JMP:** Raw data was not permanently saved, but it could be retrieved through website
* **Gaza Joint:** Raw data was not permanently saved, but is saved by the extraction script and could be recreated by rerunning that script

**Is the code that was used to preprocess/clean the data available?**
*(Not explicitly provided)*

---

## Uses

**What tasks has the dataset been used for so far?**
N/A

**What (other) tasks could the dataset be used for?**
Analysis of WASH-related trends across time, facilities, and regions of Palestine including disease data, damages to infrastructure, attacks on healthcare, and other recorded indicators

**Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?**
Many of these sources are updated regularly, so rerunning our extraction and merging scripts when applicable is advised to be analyzing the most updated version of the dataset

**Are there tasks for which the dataset should not be used?**
N/A

---

## Distribution

**Based on discussions with the client, what access type should this dataset be given?**
All of our original data sources are publicly available, so the combined master datasets should also be available externally with no restrictions

---

## Maintenance & Other

**If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?**
The main way to augment our master dataset would be to incorporate more data sources into it, pertaining to the same indicators to double-check values or further expand the list of indicators that our dataset covers

**Is there any other additional information that you would like to provide that has not already been covered in other sections?**
N/A