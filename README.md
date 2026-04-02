# Customer-Segmentation-RFM-Analysis
Segmented 4,300+ customers using RFM scoring, K-Means clustering, cohort analysis &amp; CLV — Python, SQL, Power BI
# 🏪 Project_3 — Customer Segmentation & RFM Analysis

## 📌 Project Overview

A UK-based online retail company wants to understand its customer base better to improve marketing efficiency and reduce churn. Using **2 years of real transactional data (1M+ rows)**, this project segments customers using RFM scoring, K-Means clustering, and cohort analysis — then calculates Customer Lifetime Value (CLV) to quantify the business impact of each segment.

**Business Problem:** The company treats all customers the same, sending identical promotions to everyone. This wastes marketing budget and misses opportunities to retain high-value customers or re-engage those slipping away.

**Solution:** Data-driven customer segmentation that enables targeted marketing strategies for each customer group.

---

## 🔧 Tools & Technologies

| Category | Tools |
|----------|-------|
| **Language** | Python 3.x |
| **Database** | SQL (SQLite) |
| **Visualisation** | Power BI |
| **Libraries** | pandas, numpy, matplotlib, seaborn, scikit-learn, sqlite3 |
| **Environment** | Jupyter Notebook / VS Code |

---

## 📊 Dataset

- **Source:** [Online Retail II — UCI Machine Learning Repository](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)
- **Records:** ~1,067,371 transactions
- **Period:** December 2009 – December 2011
- **Context:** Real transactional data from a UK-based non-store online retailer selling gift-ware
- **License:** CC BY 4.0

| Column | Description |
|--------|-------------|
| Invoice | 6-digit invoice number ('C' prefix = cancellation) |
| StockCode | 5-digit product code |
| Description | Product name |
| Quantity | Quantity per transaction |
| InvoiceDate | Date and time of transaction |
| Price | Unit price in GBP (£) |
| Customer ID | Unique 5-digit customer identifier |
| Country | Customer's country of residence |

---

## 🧪 Methodology

### 1. Data Cleaning & Preparation
- Removed cancellations (invoices starting with 'C')
- Handled missing Customer IDs (~25% of rows)
- Removed negative/zero quantities and prices
- Filtered out non-product stock codes (POST, DOT, BANK CHARGES, etc.)
- Created `TotalPrice` column (Quantity × Price)

### 2. Exploratory Data Analysis (EDA)
- Monthly revenue trends and seasonality patterns
- Top-selling products and revenue drivers
- Geographic distribution of customers
- Purchase frequency distribution

### 3. RFM Analysis (Rule-Based Segmentation)
- Calculated **Recency** (days since last purchase), **Frequency** (total purchases), and **Monetary** (total spend) per customer
- Scored each metric 1–5 using quintiles
- Created customer segments: Champions, Loyal Customers, Potential Loyalists, At Risk, Can't Lose Them, Lost, and more

### 4. K-Means Clustering (ML-Based Segmentation)
- Standardised RFM features using StandardScaler
- Determined optimal clusters using Elbow Method + Silhouette Score
- Applied K-Means clustering and compared results with rule-based RFM segments

### 5. Cohort Analysis
- Assigned customers to monthly cohorts based on first purchase date
- Built customer retention matrix
- Visualised retention trends using a heatmap

### 6. Customer Lifetime Value (CLV)
- Calculated CLV per segment: `Avg Order Value × Purchase Frequency × Customer Lifespan`
- Quantified revenue at risk from churning segments
- Identified highest-value segments for priority treatment

### 7. SQL Analysis
- Loaded cleaned data into SQLite database
- Wrote SQL queries for RFM calculations, aggregations, and segmentation
- Demonstrated ability to perform the same analysis in SQL (industry's #1 demanded skill)

---

## 📈 Key Findings

> *(To be updated after analysis is complete)*

1. **Finding 1:** [e.g., Top 20% of customers drive X% of total revenue]
2. **Finding 2:** [e.g., X customers identified as "At Risk" representing $X in annual revenue]
3. **Finding 3:** [e.g., Customer retention drops by X% after month 3 across all cohorts]
4. **Finding 4:** [e.g., Champions have Xx higher CLV than average customers]
5. **Finding 5:** [e.g., Targeted strategies could recover an estimated $X from at-risk segments]

---

## 💡 Business Recommendations

> *(To be updated after analysis is complete)*

| Segment | Strategy | Expected Impact |
|---------|----------|-----------------|
| Champions | VIP loyalty program, early access to new products | Increase retention & advocacy |
| At Risk | Win-back email campaign with personalised offers | Recover X% of at-risk revenue |
| Lost | Low-cost re-engagement (survey + discount) | Reactivate X% of dormant customers |
| Potential Loyalists | Upsell/cross-sell recommendations | Increase average order value by X% |

---

## 📁 Project Structure

```
P3-Customer-Segmentation-RFM/
│
├── README.md
├── requirements.txt
├── data/
│   └── online_retail_II.csv
├── notebooks/
│   └── exploration.ipynb
├── scripts/
│   ├── 01_data_cleaning.py
│   ├── 02_eda.py
│   ├── 03_rfm_scoring.py
│   ├── 04_kmeans_clustering.py
│   ├── 05_cohort_analysis.py
│   └── 06_clv_calculation.py
├── sql/
│   ├── create_tables.sql
│   ├── rfm_queries.sql
│   └── segmentation_queries.sql
├── dashboard/
│   └── P3_Customer_Segmentation.pbix
└── outputs/
    ├── cleaned_data.csv
    ├── rfm_segments.csv
    ├── cohort_heatmap.png
    └── cluster_visualization.png
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ahmed-Al-Rafsan/P3-Customer-Segmentation-RFM.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) and place it in `data/`
4. Run scripts in order:
   ```bash
   python scripts/01_data_cleaning.py
   python scripts/02_eda.py
   python scripts/03_rfm_scoring.py
   python scripts/04_kmeans_clustering.py
   python scripts/05_cohort_analysis.py
   python scripts/06_clv_calculation.py
   ```
5. Open `dashboard/P3_Customer_Segmentation.pbix` in Power BI Desktop

---

## 📺 Video Walkthrough

> *(YouTube link to be added)*

---

## 👤 Author

**Ahmed Al Rafsan**
- [GitHub](https://github.com/Ahmed-Al-Rafsan)
- [LinkedIn](https://www.linkedin.com/in/ahmed-al-rafsan/)

---

## 📄 Citation

Chen, D. (2012). *Online Retail II* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D
