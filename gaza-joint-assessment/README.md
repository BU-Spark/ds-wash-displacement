# Gaza Joint WASH Assessment Extraction

This notebook extracts indicator values from the **Gaza Joint WASH Assessment Round 3** PDF, reshapes the extracted table data into a structured long-format CSV, checks for inconsistent duplicate matches, and saves the results for downstream integration into the broader WASH master dataset. The larger project goal is to create a centralized database of WASH-related indicators for future analysis.

## Project Context

This work is part of **WASH: Center of Forced Displacement**, a DS539 Data Science Practicum project for client **Amira Aker**. The broader project focuses on integrating fragmented WASH and infectious disease data sources into a centralized database.

The Gaza Joint WASH Assessment source is one of the core project datasets. It is a PDF report from UNICEF and the WASH Cluster that provides a household-level snapshot of WASH conditions in Gaza, including indicators such as water access, sanitation, soap availability, and household health conditions.

## What This Notebook Does

This notebook:

1. Opens the Gaza Joint WASH Assessment PDF.
2. Extracts tables from the PDF using `pdfplumber`.
3. Cleans table rows and text.
4. Searches extracted rows for a fixed set of target indicators defined in `INDICATOR_MAP`.
5. Detects nearby column headers that represent time periods such as `August 2024`, `January 2025`, and `August 2025`.
6. Builds a structured output table using the first matched row for each indicator.
7. Reshapes the output from wide format to long format.
8. Splits the extracted `date` field into separate `month` and `year` columns.
9. Adds a source column containing the PDF filename.
10. Generates an inconsistency report if the same indicator is found with conflicting values in multiple tables.
11. Saves the extracted dataset and the inconsistency report as CSV files.

## Input File

The notebook expects this PDF file in the working directory:

```python
pdf_path = "2025-08_Gaza Joint WASH Assessment Report.pdf"