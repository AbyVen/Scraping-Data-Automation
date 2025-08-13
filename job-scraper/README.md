# Python.org Job Scraper

A beginner-friendly Python web scraper that collects job listings from [python.org/jobs](https://www.python.org/jobs/) and exports them to **CSV** and **Excel** formats.

## 📌 Features
- Scrapes job title, company, location, date posted, and link.
- Exports results to:
  - `jobs.csv`
  - `jobs.xlsx`
- Works with static HTML (no complex anti-bot measures).

## 🛠️ Requirements
- Python 3.x
- pipenv (for virtual environments)
- Libraries:
  - requests
  - beautifulsoup4
  - pandas
  - openpyxl

## 🚀 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/job-scraper.git
cd job-scraper
