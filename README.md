# 🚢 Titanic Dataset Local ETL & Automation Pipeline

An automated data pipeline that orchestrates an End-to-End ETL (Extract, Transform, Load) workflow entirely on a local machine (C: Drive). The pipeline uses Python to dynamically extract live cloud data, clean and transform it, and feed a live Power BI dashboard.

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3
* **Libraries:** Pandas (Data Engineering & Transformation)
* **Visualization:** Power BI Desktop
* **Storage Environment:** Local File System (Windows C: Drive Workspace)

## 🔄 Data Pipeline Workflow
1. **Extraction:** Python extracts raw data from a remote GitHub repository.
2. **Transformation (ETL Engine):** * Imputes missing `Age` values utilizing the dataset's median age.
   * Standardizes textual dimensions (`Sex` and `Embarked`) by removing white spaces and normalizing casing.
   * Handles empty fields in categorical data (e.g., `Cabin` placeholders) and drops critical null entries.
3. **Loading:** Saves the pristine dataset as a local `.csv` file.
4. **Business Intelligence:** Power BI consumes the processed local file to update key visual metrics dynamically.

## 🏃‍♂️ How to Run and Test the Pipeline Locally
1. Clone or download this project folder to your local computer.
2. Run the automated data cleaning script in your terminal:
   ```bash
   python pipeline.py
