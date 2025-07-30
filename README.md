## 🎬 IMDB Movie Data ETL Pipeline

A comprehensive Extract, Transform, Load (ETL) system that scrapes currently popular movies from IMDB, performs sentiment analysis on reviews, and provides a complete data pipeline solution with web interface.

## 🚀 Features

### Core ETL Components
- **Data Extraction**: Web scraping from IMDB using BeautifulSoup4 to collect popular movie information[1][2][3]
- **Data Transformation**: Python scripts convert raw text data into structured formats with proper data types[4][5]  
- **Machine Learning Integration**: TensorFlow-powered sentiment analysis classifying movie reviews as positive, neutral, or negative[1][2]
- **Data Loading**: Automated CSV file generation and PostgreSQL database integration[1][6]

### Web Application
- **Flask Web Framework**: Interactive dashboard for browsing scraped movie data[1][7]
- **Dockerized PostgreSQL**: Containerized database solution for easy deployment[1][8]
- **Bootstrap UI**: Responsive web interface with DataTables for enhanced user experience[1][7]

## 🛠 Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Backend | Python | Main programming language for ETL operations[1] |
| Web Scraping | BeautifulSoup4 | HTML parsing and data extraction from IMDB[1][2] |
| Machine Learning | TensorFlow | Sentiment analysis of movie reviews[1] |
| Database | PostgreSQL | Data storage and management[1] |
| Containerization | Docker | Database deployment and environment management[1] |
| Web Framework | Flask | API and web interface development[1] |
| Frontend | Bootstrap + DataTables | User interface and data visualization[1] |

## 📋 Prerequisites

- Python 3.x
- Docker
- PostgreSQL

## 🔧 Quick Setup

### 1. Database Setup
```bash
docker run --name etl_imdb -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=imdb -d -p 5432:5432 postgres
```

### 2. Install Dependencies
```bash
pip install -r ./etl_process/requirements.txt
```

### 3. Run Application
```bash
python wsgi.py
```

## 📊 Data Pipeline Overview

The ETL process follows industry best practices for data governance and documentation[4][5][9]:

1. **Extract**: Scrapes movie details from IMDB's most popular movies list
2. **Transform**: Processes raw HTML data into structured formats with data validation
3. **Load**: Stores processed data in both CSV files and PostgreSQL database
4. **Analyze**: Applies machine learning models for sentiment analysis on reviews

## 🎯 Use Cases

- **Movie Industry Analysis**: Track trending movies and audience sentiment
- **Data Science Projects**: Clean, structured movie dataset for analysis
- **Web Scraping Education**: Learn BeautifulSoup4 and ethical scraping practices
- **ETL Learning**: Understand complete data pipeline implementation

## 📈 Data Sources

- **Primary**: IMDB popular movies listings
- **Secondary**: Movie reviews and ratings for sentiment analysis
- **Output**: Structured CSV files and PostgreSQL database tables

## 🔍 Key Insights

This project demonstrates professional ETL development practices including proper data documentation, version control, and modular code structure[4][5][10]. The integration of machine learning capabilities makes it suitable for both educational purposes and production data analysis workflows.

**Topics**: `etl`, `web-scraping`, `imdb`, `python`, `flask`, `postgresql`, `docker`, `beautifulsoup`, `tensorflow`, `sentiment-analysis`, `data-pipeline`, `machine-learning`
