# 🧹 Project 2 — Data Cleaning Script

This project cleans messy CSV data using **Pandas**.

## Features
- Removes duplicate rows
- Drops completely empty rows
- Trims extra spaces
- Standardizes casing (Name, Email, Country)
- Fills missing Age values with the mean

## Before Cleaning
![Before](screenshots/before.png)

## After Cleaning
![After](screenshots/after.png)

## Usage
```bash
pip install -r requirements.txt
python scripts/clean_data.py
