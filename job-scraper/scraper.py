import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of a beginner-friendly static job board
URL = "https://www.python.org/jobs/"

# Fetch the page
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)

if response.status_code != 200:
    print(f"Failed to fetch page: {response.status_code}")
    exit()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all job listings
jobs = []
job_cards = soup.find_all("ol", class_="list-recent-jobs")[0].find_all("li")

for job in job_cards:
    title_tag = job.find("h2")
    company_tag = job.find("span", class_="listing-company-name")
    location_tag = job.find("span", class_="listing-location")
    date_tag = job.find("time")
    link_tag = title_tag.find("a") if title_tag else None

    jobs.append({
        "Title": title_tag.get_text(strip=True) if title_tag else None,
        "Company": company_tag.get_text(strip=True) if company_tag else None,
        "Location": location_tag.get_text(strip=True) if location_tag else None,
        "Date Posted": date_tag.get_text(strip=True) if date_tag else None,
        "Link": f"https://www.python.org{link_tag['href']}" if link_tag else None
    })

# Save to CSV & Excel
df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False)
df.to_excel("jobs.xlsx", index=False)

print(f"Scraped {len(jobs)} jobs. Saved to jobs.csv and jobs.xlsx.")
