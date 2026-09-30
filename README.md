# E-commerce Sales & Customer Analysis

## 📌 Project Overview

This project analyzes e-commerce sales and customer data using Python and SQL. The objective is to identify sales trends, profitable products, top customers, regional performance, and discount patterns.

## 🎯 Objectives

- Clean and prepare the e-commerce dataset
- Analyze sales and profit
- Identify top-performing products
- Identify top customers
- Analyze product categories
- Analyze regional sales performance
- Study discount patterns
- Perform customer-level analysis
- Store cleaned data in a SQLite database
- Perform business analysis using SQL queries

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL
- SQLite

## 📂 Project Structure

```text
ecommerce_sales_customer_analysis/
│
├── data/
│   ├── ecommerce_sales.csv
│   ├── cleaned_ecommerce_sales.csv
│   └── ecommerce.db
│
├── python/
│   ├── analysis.py
│   └── create_database.py
│
├── sql/
│   └── ecommerce_queries.sql
│
├── README.md
└── requirements.txt
```

## 🔍 Analysis Performed

### Python Analysis

- Data cleaning
- Sales analysis
- Profit analysis
- Category analysis
- Regional analysis
- Product analysis
- Customer analysis
- Discount analysis

### SQL Analysis

- Total sales and profit
- Category performance
- Regional performance
- Top products
- Top customers
- Customer-level analysis
- Discount analysis

## 🗄️ Database

The cleaned e-commerce dataset is stored in a SQLite database:

`data/ecommerce.db`

The database contains the `ecommerce_sales` table.

## ▶️ How to Run

### Install required libraries

```bash
pip install -r requirements.txt
```

### Run Python analysis

```bash
python python/analysis.py
```

### Create/update the SQLite database

```bash
python python/create_database.py
```

## 📊 Key Outputs

The analysis generates information such as:

- Top 10 customers
- Top 10 products
- Sales and profit performance
- Regional sales performance
- Category performance
- Discount analysis

## 💡 Business Insights

The project helps businesses understand:

- Which products generate higher sales
- Which customers contribute significant revenue
- Which regions perform better
- How discounts relate to sales and profit
- Where business performance can be improved

## 👩‍💻 Author

Pravalika Battala
