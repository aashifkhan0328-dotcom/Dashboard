# Financial Performance & Risk Analysis Dashboard: Walmart vs. Target

## 📊 Project Overview

This comprehensive project analyzes the financial performance of two major U.S. retailers—**Walmart** and **Target**—using 5 years of public financial statement data (FY 2020-2024). The analysis compares profitability, liquidity, solvency, operational efficiency, and cash flow to determine which company is financially stronger.

### 🎯 Business Question
**Which company is financially stronger, Walmart or Target, based on profitability, liquidity, efficiency, solvency, cash flow, and market performance?**

---

## 📁 Project Structure

```
financial-statement-analysis-dashboard/
│
├── data/
│   ├── raw/                          # Original SEC EDGAR and Yahoo Finance data
│   │   ├── walmart_financial_statements.csv
│   │   └── target_financial_statements.csv
│   │
│   └── cleaned/                      # Processed and standardized data
│       ├── walmart_cleaned.csv
│       ├── target_cleaned.csv
│       ├── walmart_target_combined.csv
│       ├── financial_ratios.csv
│       └── dashboard_export.csv
│
├── notebooks/
│   └── financial_analysis.ipynb      # Comprehensive analysis notebook
│
├── scripts/
│   ├── extract_sec_data.py          # Extract financial data from SEC EDGAR
│   ├── clean_data.py                # Data cleaning and preparation
│   └── calculate_ratios.py          # Calculate 15+ financial ratios
│
├── dashboard/
│   └── walmart_target_dashboard.pbix # Power BI interactive dashboard
│
├── reports/
│   └── financial_analysis_report.pdf # Detailed business analysis report
│
├── images/
│   └── dashboard_screenshots/        # Dashboard screenshots for portfolio
│
├── README.md                         # This file
├── requirements.txt                  # Python dependencies
└── .gitignore                       # Git configuration
```

---

## 🚀 Quick Start

### 1. **Set Up Python Environment**
```bash
# Navigate to project directory
cd financial-statement-analysis-dashboard

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. **Run Data Pipeline**
```bash
# Step 1: Extract financial data from SEC EDGAR
python scripts/extract_sec_data.py

# Step 2: Clean and prepare data
python scripts/clean_data.py

# Step 3: Calculate financial ratios
python scripts/calculate_ratios.py
```

### 3. **Open Jupyter Notebook**
```bash
jupyter notebook notebooks/financial_analysis.ipynb
```

### 4. **Create Power BI Dashboard**
- Open `dashboard/walmart_target_dashboard.pbix` in Power BI Desktop
- Connect to cleaned data from `data/cleaned/dashboard_export.csv`
- Use pre-built visualizations or customize as needed

---

## 📊 Key Metrics & Ratios Analyzed

### **Profitability Ratios** (5)
- Gross Profit Margin = Gross Profit ÷ Revenue
- Operating Profit Margin = Operating Income ÷ Revenue
- Net Profit Margin = Net Income ÷ Revenue
- Return on Assets (ROA) = Net Income ÷ Average Total Assets
- Return on Equity (ROE) = Net Income ÷ Average Shareholders' Equity

### **Liquidity Ratios** (2)
- Current Ratio = Current Assets ÷ Current Liabilities
- Quick Ratio = (Current Assets - Inventory) ÷ Current Liabilities

### **Solvency Ratios** (3)
- Debt-to-Equity Ratio = Total Liabilities ÷ Shareholders' Equity
- Debt Ratio = Total Liabilities ÷ Total Assets
- Equity Ratio = Shareholders' Equity ÷ Total Assets

### **Efficiency Ratios** (3)
- Inventory Turnover = COGS ÷ Average Inventory
- Asset Turnover = Revenue ÷ Average Total Assets
- Receivables Turnover = Revenue ÷ Average Accounts Receivable

### **Cash Flow Ratios** (2)
- Operating Cash Flow Margin = Operating Cash Flow ÷ Revenue
- Free Cash Flow Margin = Free Cash Flow ÷ Revenue

---

## 💡 Key Findings

### **1. Revenue & Scale**
- **Walmart**: $648.1B (FY 2024) — 6x larger than Target
- **Target**: $109.1B (FY 2024)
- **Insight**: Walmart dominates in absolute scale and market reach

### **2. Profitability**
| Metric | Walmart | Target |
|--------|---------|--------|
| Gross Margin | ~25.3% | ~33.7% |
| Net Margin | ~2.4% | ~3.8% |
| ROE | ~17.6% | ~16.9% |

**Insight**: While Target has higher margin percentages, Walmart's scale drives higher absolute profits.

### **3. Liquidity**
| Metric | Walmart | Target |
|--------|---------|--------|
| Current Ratio | 0.76 | 0.87 |
| Quick Ratio | 0.40 | 0.39 |

**Insight**: Both companies maintain adequate short-term liquidity for retail operations.

### **4. Solvency & Risk**
| Metric | Walmart | Target |
|--------|---------|--------|
| Debt-to-Equity | 1.83 | 1.58 |
| Debt Ratio | 64.7% | 61.2% |

**Insight**: Both leverage debt effectively; Target carries slightly less relative debt.

### **5. Operational Efficiency**
| Metric | Walmart | Target |
|--------|---------|--------|
| Inventory Turnover | 8.4x | 6.2x |
| Asset Turnover | 2.57x | 1.74x |

**Insight**: Walmart manages inventory more efficiently, critical for retail success.

### **6. Cash Flow**
| Metric | Walmart | Target |
|--------|---------|--------|
| Operating Cash Flow | $26.8B | $6.2B |
| Free Cash Flow | $16.0B | $2.8B |
| OCF Margin | 4.1% | 5.7% |

**Insight**: Walmart generates significantly more cash; both companies are financially stable.

---

## 🎯 Overall Assessment

### **Walmart is Financially Stronger**

**Strengths:**
✅ Superior revenue scale ($648B vs $109B)  
✅ Higher absolute profitability ($15.5B net income vs $4.1B)  
✅ Better inventory management (8.4x turnover)  
✅ Stronger cash generation ($26.8B operating cash flow)  
✅ Greater financial flexibility for investments and growth  

### **Target is Financially Sound**

**Strengths:**
✅ Healthy profit margins (3.8% net margin)  
✅ Sustainable liquidity position  
✅ Manageable debt levels (D/E: 1.58)  
✅ Consistent profitability  
✅ Strong market position in mid-market retail  

---

## 📈 Dashboard Pages

### **Page 1: Executive Summary**
KPIs, company comparison, key metrics overview

### **Page 2: Profitability Analysis**
Revenue trends, profit margins, ROA/ROE, growth analysis

### **Page 3: Liquidity, Solvency & Risk**
Current ratio, debt-to-equity, debt ratio, financial risk assessment

### **Page 4: Efficiency & Market Performance**
Inventory turnover, asset turnover, cash flow analysis, operational metrics

---

## 🛠️ Technologies Used

| Task | Tool |
|------|------|
| Data Extraction | SEC EDGAR API, Yahoo Finance |
| Data Cleaning | Python (Pandas, NumPy) |
| Analysis | Jupyter Notebook, Python |
| Visualization | Plotly, Seaborn, Matplotlib |
| Dashboard | Power BI |
| Documentation | GitHub, Markdown |
| Version Control | Git |

---

## 📚 Data Sources

1. **SEC EDGAR** - Official financial statements (10-K filings)
   - Company Facts API: `https://data.sec.gov/submissions/CIK{cik}.json`
   - Reliable, audited financial data

2. **Yahoo Finance** - Historical stock data
   - Stock prices, dividends, market data
   - Market performance context

3. **Public Financial Reports**
   - FY 2020-2024 annual reports
   - Standardized accounting data

---

## 📋 Deliverables Checklist

- ✅ Clean financial dataset (CSV)
- ✅ Python scripts for data pipeline
- ✅ Jupyter notebook with analysis
- ✅ 15+ financial ratios calculated
- ✅ Power BI dashboard structure
- ✅ Business analysis documentation
- ✅ GitHub repository setup
- ✅ README and project documentation

---

## 🎓 Learning Outcomes

This project demonstrates:

1. **Financial Analysis Skills**
   - Understanding of income statement, balance sheet, cash flow
   - Ability to calculate and interpret financial ratios
   - Financial decision-making framework

2. **Data Analytics Skills**
   - Data extraction from APIs
   - Data cleaning and standardization
   - Time-series analysis
   - Comparative analysis

3. **Technical Skills**
   - Python (Pandas, NumPy, Matplotlib, Plotly)
   - SQL/data querying
   - Jupyter notebooks
   - Power BI dashboard creation

4. **Business Analysis Skills**
   - Financial ratio interpretation
   - Competitor analysis
   - Investment decision-making
   - Business reporting

---

## 📖 How to Use This Project

### **For Learning**
1. Review this README for project context
2. Examine raw data in `data/raw/`
3. Run Python scripts to understand data pipeline
4. Study the Jupyter notebook for analysis methodology
5. Explore Power BI dashboard for visualization best practices

### **For Portfolio/Resume**
1. Include project link in GitHub profile
2. Add to portfolio website with dashboard screenshots
3. Use Resume Bullet Points (see below)
4. Share Jupyter notebook as evidence of technical skills
5. Link to Power BI dashboard in portfolio

### **For Interviews**
1. Be ready to explain financial ratios and their significance
2. Discuss trade-offs between Walmart and Target
3. Walk through data pipeline methodology
4. Demonstrate Power BI dashboard and key insights

---

## 💼 Resume Bullet Points

**Financial Performance & Risk Analysis Dashboard | Python, Power BI, Excel, SEC EDGAR**

- Built an interactive financial analysis dashboard comparing Walmart and Target using 5 years of public financial statement data from SEC EDGAR.
- Designed and implemented Python data pipeline to extract, clean, and transform income statement, balance sheet, and cash flow data for analysis.
- Calculated 15+ financial ratios including profitability (gross/net margin, ROA, ROE), liquidity (current ratio), solvency (debt-to-equity), and efficiency metrics (inventory/asset turnover).
- Created Power BI dashboard with 4 interactive pages for profitability, liquidity/risk, efficiency, and executive summary analysis.
- Analyzed 5-year financial trends and presented data-driven recommendation that Walmart demonstrates stronger financial health based on scale, profitability, and cash generation.
- Cleaned and standardized $2+ trillion in combined financial data, handling missing values and creating calculated fields for ratio analysis.

---

## 🔍 Key Insights for Stakeholders

### **For Investors**
- Walmart offers lower risk with superior scale and cash generation
- Target provides growth opportunity in mid-market segment
- Both are financially stable with manageable debt

### **For Business Analysts**
- Retail efficiency (inventory turnover) critical for profitability
- Scale enables lower operating costs (Walmart advantage)
- Market positioning allows Target to maintain margin premiums

### **For Finance Professionals**
- Comparative ratio analysis reveals operational differences
- Cash flow strength indicates ability to fund growth
- Leverage levels appropriate for retail industry

---

## 📞 Contact & Questions

For questions about this analysis:
- Review the Jupyter notebook for detailed methodology
- Check the Power BI dashboard for interactive exploration
- Refer to financial ratio definitions in scripts

---

## 📄 License

This project uses publicly available financial data from SEC EDGAR and Yahoo Finance. 
Data is used for educational and analytical purposes.

---

**Project Completion Date**: FY 2024  
**Data Period**: Fiscal Years 2020-2024  
**Last Updated**: May 2026

---

*This project demonstrates the intersection of accounting, finance, data analytics, and business intelligence—essential skills for modern finance professionals.*
