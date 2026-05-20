# Quick Start Guide
## Financial Performance & Risk Analysis Dashboard

---

## ⚡ 5-Minute Quick Start

### Option 1: View Pre-Generated Results (Fastest - 2 minutes)

1. **Look at cleaned data**:
   - Open `data/cleaned/walmart_target_combined.csv` in Excel
   - See financial statements for both companies, 5 years

2. **View calculated ratios**:
   - Open `data/cleaned/financial_ratios.csv` in Excel
   - See all 15 financial ratios already calculated

3. **Read the business insights**:
   - Open `reports/financial_analysis_report.md`
   - Get complete analysis and recommendations

4. **View the Jupyter analysis** (if Jupyter installed):
   - Open `notebooks/financial_analysis.ipynb`
   - See interactive charts and detailed analysis

### Option 2: Run the Complete Pipeline (15-20 minutes)

**Step 1: Install Python Dependencies**
```bash
# Navigate to project directory
cd financial-statement-analysis-dashboard

# Install required packages
pip install -r requirements.txt
```

**Step 2: Run Data Pipeline**
```bash
# Extract financial data
python scripts/extract_sec_data.py

# Clean and prepare data
python scripts/clean_data.py

# Calculate financial ratios
python scripts/calculate_ratios.py
```

**Step 3: View Results**
```bash
# Open Jupyter notebook for interactive analysis
jupyter notebook notebooks/financial_analysis.ipynb
```

---

## 📊 Project Files Overview

### Data Files
| File | Purpose | Format |
|------|---------|--------|
| `data/cleaned/walmart_target_combined.csv` | Cleaned financial statements | CSV |
| `data/cleaned/financial_ratios.csv` | Calculated financial ratios | CSV |
| `data/cleaned/dashboard_export.csv` | Data for Power BI | CSV |

### Analysis Files
| File | Purpose | Format |
|------|---------|--------|
| `notebooks/financial_analysis.ipynb` | Interactive analysis & charts | Jupyter |
| `reports/financial_analysis_report.md` | Detailed business report | Markdown |

### Code Files
| File | Purpose |
|------|---------|
| `scripts/extract_sec_data.py` | Extract data from SEC EDGAR |
| `scripts/clean_data.py` | Data cleaning & standardization |
| `scripts/calculate_ratios.py` | Calculate financial ratios |

### Documentation
| File | Purpose |
|------|---------|
| `README.md` | Complete project documentation |
| `RESUME_PORTFOLIO.md` | Resume bullets & portfolio info |

---

## 🎯 What Each Script Does

### extract_sec_data.py
**Purpose**: Extract financial data from SEC EDGAR

**What it does**:
- Connects to SEC EDGAR API (or uses pre-loaded data)
- Extracts financial statements for Walmart and Target
- Gets stock price data from Yahoo Finance
- Saves raw data to `data/raw/` folder

**Run it**: `python scripts/extract_sec_data.py`

**Output**: 
- `data/raw/walmart_financial_statements.csv`
- `data/raw/target_financial_statements.csv`

---

### clean_data.py
**Purpose**: Standardize and prepare data for analysis

**What it does**:
- Removes duplicates
- Standardizes company names
- Converts to consistent units (millions USD)
- Handles missing values
- Creates calculated columns (free cash flow, averages)
- Combines both companies into single dataset

**Run it**: `python scripts/clean_data.py`

**Output**:
- `data/cleaned/walmart_cleaned.csv`
- `data/cleaned/target_cleaned.csv`
- `data/cleaned/walmart_target_combined.csv`

---

### calculate_ratios.py
**Purpose**: Calculate 15+ financial ratios

**What it does**:
- Profitability ratios (gross margin, net margin, ROA, ROE)
- Liquidity ratios (current ratio, quick ratio)
- Solvency ratios (debt-to-equity, debt ratio)
- Efficiency ratios (inventory turnover, asset turnover)
- Cash flow ratios (OCF margin, FCF margin)
- Exports results to CSV for Power BI

**Run it**: `python scripts/calculate_ratios.py`

**Output**:
- `data/cleaned/financial_ratios.csv`
- `data/cleaned/dashboard_export.csv`

---

## 📈 Power BI Dashboard Setup

### What the Dashboard Includes

**Page 1: Executive Summary**
- KPI cards (Revenue, Net Income, Assets, OCF)
- Company comparison charts
- Key metrics overview
- Recommendation statement

**Page 2: Profitability Analysis**
- Revenue trend line (5 years)
- Net income trend
- Profit margin comparison
- ROA and ROE comparison

**Page 3: Liquidity, Solvency & Risk**
- Current ratio trend
- Debt-to-equity ratio trend
- Debt ratio comparison
- Operating cash flow trend

**Page 4: Efficiency & Market Performance**
- Inventory turnover comparison
- Asset turnover comparison
- Receivables turnover
- Cash flow margin analysis

### How to Create Dashboard in Power BI

1. **Open Power BI Desktop**

2. **Connect to Data**
   - Click "Get Data" → "Text/CSV"
   - Select `data/cleaned/dashboard_export.csv`
   - Load the data

3. **Create KPI Cards (Page 1)**
   - Drag "Revenue" field to canvas
   - Change visualization to "Card"
   - Repeat for Net Income, Total Assets, Operating Cash Flow

4. **Create Company Filters**
   - Drag "Company" field to Filters area
   - Allow multiple selections

5. **Create Year Slicer**
   - Insert "Slicer" visualization
   - Add "Year" field
   - This enables filtering by year

6. **Create Charts (Pages 2-4)**
   - Line charts: Drag Year to X-axis, ratio to Y-axis
   - Bar charts: Compare Walmart vs Target
   - Add company filter to each visual

7. **Format & Polish**
   - Use consistent color scheme (Walmart: blue #0071ce, Target: red #cc0000)
   - Add titles to each page
   - Create drill-through filters
   - Add background image

8. **Save**
   - Save as `dashboard/walmart_target_dashboard.pbix`

---

## 🔍 Interpreting Key Ratios

### Profitability Ratios

**Gross Margin %** = (Gross Profit / Revenue) × 100
- Higher = Better pricing power
- Walmart: 25.3% | Target: 33.7%
- Target has higher margins due to premium positioning

**Net Profit Margin %** = (Net Income / Revenue) × 100
- Shows how much profit from each sales dollar
- Walmart: 2.4% | Target: 3.8%
- Both healthy for retail industry

**ROE %** = (Net Income / Average Equity) × 100
- Shows return on shareholder investment
- Walmart: 17.4% | Target: 16.9%
- Both excellent returns (>15% is very good)

### Liquidity Ratios

**Current Ratio** = Current Assets / Current Liabilities
- Measures ability to pay short-term obligations
- Walmart: 0.76 | Target: 0.87
- Below 1.0 is normal for retail (inventory converts to cash quickly)

**Quick Ratio** = (Current Assets - Inventory) / Current Liabilities
- More conservative; excludes inventory
- Both around 0.39-0.40
- Normal for retail operations

### Solvency Ratios

**Debt-to-Equity** = Total Liabilities / Shareholders' Equity
- Shows leverage; how much debt relative to equity
- Walmart: 1.83 | Target: 1.58
- Both sustainable (1.5-2.0 is normal for retailers)

**Debt Ratio %** = (Total Liabilities / Total Assets) × 100
- Shows % of assets financed by debt
- Walmart: 64.7% | Target: 61.0%
- Both healthy (60-70% is normal)

### Efficiency Ratios

**Inventory Turnover** = COGS / Average Inventory
- How many times inventory sold per year
- Walmart: 8.4x (every 43 days) | Target: 5.8x (every 63 days)
- **Walmart is more efficient** (critical for retail)

**Asset Turnover** = Revenue / Average Total Assets
- How much revenue from each dollar of assets
- Walmart: 2.57x | Target: 1.79x
- Walmart generates more sales from assets

### Cash Flow Ratios

**OCF Margin %** = (Operating Cash Flow / Revenue) × 100
- Quality of earnings; cash generated per sales dollar
- Walmart: 4.1% | Target: 5.7%
- Target's higher OCF margin shows strong cash generation

**FCF Margin %** = (Free Cash Flow / Revenue) × 100
- Cash available after reinvestment
- Walmart: 2.5% | Target: 2.5%
- Both generate solid free cash flow

---

## 📊 Key Findings Summary

### Walmart Strengths
✓ 6x larger revenue ($648B vs $109B)  
✓ Superior profitability ($15.5B net income)  
✓ Better inventory management (8.4x turnover)  
✓ Stronger cash generation ($26.8B OCF)  
✓ Higher asset turnover (2.57x)  

### Target Strengths
✓ Higher profit margins (33.7% gross, 3.8% net)  
✓ Lower leverage (D/E: 1.58 vs 1.83)  
✓ Better OCF margin (5.7% vs 4.1%)  
✓ Stronger in premium market positioning  
✓ Solid financial health  

### Bottom Line
**Walmart is financially stronger** across most metrics due to scale and operational efficiency. **Target is financially sound** with sustainable profitability and manageable debt.

---

## 🎓 Learning Path

### Beginner Level (30 minutes)
1. Read this Quick Start Guide
2. Open `data/cleaned/walmart_target_combined.csv` in Excel
3. Review `reports/financial_analysis_report.md`
4. Done! You understand the analysis

### Intermediate Level (1-2 hours)
1. Install Python and run data cleaning scripts
2. Examine Python code to understand the approach
3. Create simple Power BI dashboard
4. Modify visualizations for your own preferences

### Advanced Level (4-6 hours)
1. Modify Python scripts to add new ratios
2. Create comprehensive Power BI dashboard (4+ pages)
3. Add your own analysis and insights
4. Export for presentation

### Expert Level (8+ hours)
1. Extend to more companies (add Nike, Adidas, etc.)
2. Implement automated data updates from SEC API
3. Add predictive modeling (future profitability)
4. Deploy as interactive web dashboard

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"
**Solution**: Run `pip install -r requirements.txt`

### "FileNotFoundError: data/raw/walmart_financial_statements.csv"
**Solution**: Run `python scripts/extract_sec_data.py` first, or use pre-generated data in `data/cleaned/`

### "No data in Power BI"
**Solution**: 
1. Check that `data/cleaned/dashboard_export.csv` exists
2. Refresh Power BI query
3. Verify file path in Power BI data source

### "Jupyter won't open"
**Solution**: Install Jupyter with `pip install jupyter` then run `jupyter notebook`

### Charts show #DIV/0! error
**Solution**: Ensure no division by zero in ratio calculations (check for null values)

---

## 📞 Quick Help

**Q: Can I use this data to predict future performance?**
A: Yes! This is foundation. Next step would be regression analysis or machine learning.

**Q: How often should I update the data?**
A: Quarterly (10-Q reports) or annually (10-K) when companies file with SEC.

**Q: Can I compare different companies?**
A: Absolutely! Modify scripts to extract data for any public company.

**Q: How do I present this to stakeholders?**
A: Use the Power BI dashboard + `financial_analysis_report.md` + your resume bullets.

---

## ✅ Success Checklist

- [ ] All Python dependencies installed
- [ ] Data extraction scripts run successfully
- [ ] Cleaned data files created in `data/cleaned/`
- [ ] Financial ratios calculated
- [ ] Jupyter notebook runs without errors
- [ ] Power BI dashboard created with 4 pages
- [ ] Business report reviewed and understood
- [ ] Resume bullets ready for applications
- [ ] Project pushed to GitHub

---

**You're now ready to present this project to prospective employers!** 🚀
