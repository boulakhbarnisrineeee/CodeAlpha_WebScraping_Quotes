# 🕸️ Web Scraping & Data Analysis – Quotes Dataset

This project is part of the CodeAlpha Data Analytics Internship – Task 1 (Web Scraping).  
The objective is to automatically collect data from a public website, clean the dataset, analyze it, and visualize meaningful insights.

---

## 🎯 Project Objectives
- Scrape quotes data from a public website.
- Build a structured dataset in CSV format.
- Clean and prepare the data for analysis.
- Perform exploratory analysis and feature engineering.
- Create visualizations to highlight patterns and trends.
- Export clean datasets and analytical results.

---

## 🌐 Data Source
- Website: https://quotes.toscrape.com  
- Data collected:
  - Quote text  
  - Author  
  - Tags  

Total records scraped: **100 quotes**

---

## 🛠️ Tools & Technologies
- Python  
- Requests  
- BeautifulSoup4  
- Pandas  
- Matplotlib  
- Jupyter Notebook  

---

## 📂 Project Structure
CodeAlpha_Task1_WebScraping/
├── data/
│ └── quotes.csv
├── outputs/
│ ├── figures/
│ └── tables/
├── analysis.ipynb
├── scraper.py
├── README.md
└── requirements.txt

## 🧹 Data Cleaning
- Removed duplicate quotes.
- Normalized text formatting (spaces and quotes).
- Standardized tags formatting.
- Created new features:
  - Quote length
  - Number of tags per quote

---

## 📊 Analysis & Visualizations
- Top 10 authors by number of quotes.
- Top 10 most frequent tags.
- Distribution of quote lengths.
- Summary statistics for generated features.

Visual outputs are saved in: outputs/figures/


## ✅ Key Insights
- A small number of authors contribute a large portion of quotes.
- Certain tags appear significantly more often than others.
- Most quotes have a moderate length, with a few longer outliers.
- Data cleaning improved consistency and usability of the dataset.



##Project developed for learning and portfolio purposes as part of the CodeAlpha Internship.

