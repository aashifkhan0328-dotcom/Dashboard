# Power BI Dashboard Structure Guide
## Financial Performance & Risk Analysis Dashboard

---

## Dashboard Overview

**Dashboard Name**: Walmart vs. Target Financial Analysis  
**Data Source**: `data/cleaned/dashboard_export.csv`  
**Pages**: 4 (Executive Summary, Profitability, Liquidity/Solvency, Efficiency)  
**Filters**: Company, Year  
**Target Audience**: Finance professionals, investors, business analysts  

---

## Page 1: Executive Summary

### Purpose
Quick overview of financial health for both companies, ideal for executive presentations.

### Layout
```
┌─────────────────────────────────────────────────────────────┐
│  FINANCIAL PERFORMANCE DASHBOARD: WALMART VS. TARGET       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Company Filter: [Walmart ▼] [Target ▼]                   │
│  Year Slicer: [2020] [2021] [2022] [2023] [2024]          │
│                                                             │
├──────────────────┬──────────────────┬──────────────────────┤
│   Revenue        │   Net Income     │   Total Assets       │
│   $648.1B        │   $15.5B         │   $252.5B            │
│   (Walmart)      │   (Walmart)      │   (Walmart)          │
├──────────────────┼──────────────────┼──────────────────────┤
│  Operating CF    │  Current Ratio   │  Debt-to-Equity     │
│   $26.8B         │   0.76           │   1.83              │
│   (Walmart)      │   (Walmart)      │   (Walmart)         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Revenue Comparison (Bar Chart)                            │
│  ┌────────────────────────────────────────────────────┐   │
│  │  Walmart: ████████████████████████████ $648.1B   │   │
│  │  Target:  ████ $109.1B                            │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
│  Net Income Comparison (Bar Chart)                         │
│  ┌────────────────────────────────────────────────────┐   │
│  │  Walmart: ███████████████ $15.5B                 │   │
│  │  Target:  ███ $4.1B                              │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
│  Overall Financial Strength:                               │
│  ✓ Walmart demonstrates stronger financial position       │
│    based on revenue scale, profitability, and cash flow   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Visualizations

1. **KPI Cards** (4 large cards, top)
   - Revenue (millions)
   - Net Income (millions)
   - Total Assets (millions)
   - Operating Cash Flow (millions)

2. **Company Comparison Bar Charts** (6 cards, 2 rows × 3 columns)
   - Revenue: Walmart vs Target
   - Net Income: Walmart vs Target
   - Total Assets: Walmart vs Target
   - Total Equity: Walmart vs Target
   - Operating Cash Flow: Walmart vs Target
   - Inventory: Walmart vs Target

3. **Filters**
   - Company Filter (multi-select): Walmart, Target
   - Year Slicer: 2020-2024

4. **Summary Text Box**
   - "Overall, Walmart shows stronger revenue scale and cash flow strength, while Target maintains competitive profit margins..."

### Color Scheme
- Walmart: Blue (#0071ce)
- Target: Red (#cc0000)
- Background: Light gray (#f5f5f5)

---

## Page 2: Profitability Analysis

### Purpose
Deep dive into company profitability, margins, and returns.

### Layout
```
┌─────────────────────────────────────────────────────────────┐
│  PROFITABILITY ANALYSIS: WALMART VS. TARGET                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Revenue Growth Trend (Line Chart)                         │
│  ┌────────────────────────────────────────────────────┐   │
│  │    $700B ┼                                         │   │
│  │    $600B ┼   Walmart ───────────────               │   │
│  │    $500B ┼─ /                                      │   │
│  │    $100B ┼  ─── Target                             │   │
│  │  2020 2021 2022 2023 2024                          │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
│  Net Income Trend (Line Chart)                             │
│  ┌────────────────────────────────────────────────────┐   │
│  │    $16B ┼   Walmart ─────────────                  │   │
│  │    $12B ┼─ /                                       │   │
│  │     $8B ┼─                                         │   │
│  │     $4B ┼  ─── Target                              │   │
│  │  2020 2021 2022 2023 2024                          │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Profitability Ratio Comparison (Clustered Bar)            │
│  ┌────────────────────────────────────────────────────┐   │
│  │         Gross    Net      Operating                │   │
│  │         Margin   Margin   Margin                   │   │
│  │ Walmart  25.3%   2.4%     3.2%                     │   │
│  │ Target   33.7%   3.8%     5.0%                     │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
│  Return Metrics: ROA & ROE (Comparison)                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │         ROA      ROE                               │   │
│  │ Walmart 6.2%    17.4%                              │   │
│  │ Target  6.6%    16.9%                              │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Visualizations

1. **Revenue Trend Line Chart**
   - X-axis: Year (2020-2024)
   - Y-axis: Revenue (millions)
   - Two lines: Walmart (blue), Target (red)
   - Show growth trajectory

2. **Net Income Trend Line Chart**
   - Same structure as revenue
   - Y-axis: Net Income (millions)

3. **Profit Margin Comparison**
   - Clustered bar chart
   - Categories: Gross Margin, Operating Margin, Net Margin
   - Series: Walmart, Target

4. **ROA vs. ROE Comparison**
   - Side-by-side bar chart
   - Show Walmart's higher ROE
   - Show Target's slightly higher ROA

5. **Trend Analysis Cards**
   - 5-Year Revenue CAGR: Walmart 5.3%, Target 3.8%
   - Average Gross Margin: Walmart 25.3%, Target 33.7%
   - Average Net Margin: Walmart 2.3%, Target 3.7%
   - Average ROE: Walmart 16.6%, Target 16.8%

### Key Insights Displayed
- "Walmart shows stronger absolute profitability..."
- "Target maintains higher percentage margins..."
- "Both companies show stable profitability over time..."

---

## Page 3: Liquidity, Solvency & Risk

### Purpose
Assess financial stability, debt management, and risk profile.

### Layout
```
┌─────────────────────────────────────────────────────────────┐
│  LIQUIDITY, SOLVENCY & RISK: WALMART VS. TARGET            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Current Ratio Trend (Line Chart)                          │
│  ┌────────────────────────────────────────────────────┐   │
│  │   1.0 ┼─────────────                               │   │
│  │   0.8 ┼   Walmart ────── Target ────               │   │
│  │   0.6 ┼─                                           │   │
│  │   0.4 ┼────────────────────────                    │   │
│  │ 2020 2021 2022 2023 2024                           │   │
│  │ (Below 1.0 is normal for retail)                  │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
│  Debt-to-Equity Ratio Trend (Line Chart)                   │
│  ┌────────────────────────────────────────────────────┐   │
│  │   2.0 ┼                                            │   │
│  │   1.8 ┼   Walmart ────────────                     │   │
│  │   1.6 ┼─ ─── Target ──────────                     │   │
│  │   1.4 ┼────────────────────────                    │   │
│  │ 2020 2021 2022 2023 2024                           │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Solvency Metrics Comparison (Table)                       │
│  ┌──────────────────────────────────────────────────┐     │
│  │ Metric              Walmart    Target            │     │
│  │ Debt Ratio          64.7%      61.0%             │     │
│  │ Equity Ratio        35.3%      39.0%             │     │
│  │ Debt-to-Equity      1.83       1.58              │     │
│  │ Total Liabilities   $163.3B    $38.5B            │     │
│  │ Total Equity        $89.2B     $24.4B            │     │
│  └──────────────────────────────────────────────────┘     │
│                                                             │
│  Operating Cash Flow vs. Liabilities                       │
│  ┌────────────────────────────────────────────────────┐   │
│  │ Walmart: $163.3B Debt / $26.8B OCF = 6.1x coverage   │   │
│  │ Target:  $38.5B Debt / $6.2B OCF = 6.2x coverage     │   │
│  │                                                     │   │
│  │ Both companies can service debt ~6x over with OCF    │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
│  Financial Risk Assessment:                                │
│  ✓ Both companies: Low financial distress risk            │
│  ✓ Both maintain investment-grade credit ratings          │
│  ✓ Stable debt service capability                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Visualizations

1. **Current Ratio Trend**
   - Line chart, years on X-axis
   - Add horizontal reference line at 1.0
   - Show both companies

2. **Debt-to-Equity Trend**
   - Line chart with industry benchmark (1.5-2.0)
   - Show both companies

3. **Liquidity Ratio Comparison**
   - Clustered bar: Current Ratio, Quick Ratio
   - For both companies

4. **Debt Composition (Pie Chart)**
   - Liabilities vs. Equity split
   - Separate for Walmart and Target

5. **Debt Service Coverage (Card)**
   - Total Liabilities ÷ Operating Cash Flow
   - Show in multiples (6.1x for Walmart, 6.2x for Target)

6. **Risk Assessment Matrix**
   - Text box with risk rating
   - Liquidity Risk: LOW
   - Solvency Risk: LOW
   - Overall Financial Risk: LOW

### Key Insights
- "Both companies maintain adequate liquidity for retail operations..."
- "Walmart carries more absolute debt due to larger size..."
- "Target has slightly lower leverage relative to equity..."

---

## Page 4: Efficiency & Market Performance

### Purpose
Analyze operational efficiency, asset utilization, and business performance.

### Layout
```
┌─────────────────────────────────────────────────────────────┐
│  OPERATIONAL EFFICIENCY & PERFORMANCE: WALMART VS. TARGET  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Inventory Turnover Comparison (Bar Chart)                 │
│  ┌────────────────────────────────────────────────────┐   │
│  │   10x ┼                                            │   │
│  │    8x ┼   Walmart ██████████                       │   │
│  │    6x ┼─  Target ██████                            │   │
│  │    4x ┼────────────────                            │   │
│  │    2x ┼────────────────                            │   │
│  │    0x ┼────────────────                            │   │
│  │  2020 2021 2022 2023 2024                          │   │
│  │                                                     │   │
│  │ Walmart: 8.4x (every 43 days)                     │   │
│  │ Target:  5.8x (every 63 days)                     │   │
│  │ ★ Critical advantage for Walmart                  │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
│  Asset Turnover Ratio (Line Chart)                         │
│  ┌────────────────────────────────────────────────────┐   │
│  │   3.0x ┼   Walmart ──────────                      │   │
│  │   2.5x ┼─ /                                        │   │
│  │   2.0x ┼─  ─── Target                              │   │
│  │   1.5x ┼──                                         │   │
│  │   1.0x ┼──────────────────                         │   │
│  │ 2020 2021 2022 2023 2024                           │   │
│  │                                                     │   │
│  │ Walmart: 2.57x | Target: 1.79x                    │   │
│  │ Shows Walmart generates more revenue per asset    │   │
│  └────────────────────────────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Efficiency Metrics Summary (KPI Cards)                    │
│  ┌──────────────────┬──────────────────┬─────────────┐   │
│  │ Receivables      │ OCF Margin       │ FCF Margin  │   │
│  │ Turnover         │ %                │ %           │   │
│  │ WMT: 49.2x       │ WMT: 4.1%        │ WMT: 2.5%   │   │
│  │ TGT: 46.5x       │ TGT: 5.7%        │ TGT: 2.5%   │   │
│  └──────────────────┴──────────────────┴─────────────┘   │
│                                                             │
│  Business Performance Summary:                              │
│  ✓ Walmart: Superior inventory & asset efficiency         │
│  ✓ Target: Strong cash flow margins                        │
│  ✓ Both: Effective working capital management              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Visualizations

1. **Inventory Turnover Trend**
   - Line chart, both companies
   - Highlight that Walmart is faster

2. **Asset Turnover Trend**
   - Line chart, showing Walmart's advantage
   - Y-axis: Turnover multiplier (0-3.5)

3. **Efficiency Ratios Summary**
   - Clustered bar chart
   - Categories: Inventory Turnover, Asset Turnover, Receivables Turnover
   - Walmart vs. Target

4. **Cash Flow Margin Comparison**
   - Pie chart or bar: Operating Cash Flow Margin vs. FCF Margin
   - Show both companies side-by-side

5. **Operational Efficiency Score Card**
   - Inventory Management: Walmart ★★★★★ | Target ★★★★☆
   - Asset Utilization: Walmart ★★★★★ | Target ★★★★☆
   - Cash Generation: Walmart ★★★★☆ | Target ★★★★☆

6. **Summary Text Box**
   - "Walmart's superior inventory management (8.4x turnover) 
     demonstrates operational excellence critical for retail success.
     Target's strong cash flow margins indicate effective cost management."

---

## Dashboard Interactivity

### Filters & Slicers

**1. Company Filter (Page 1)**
```
[✓ Walmart] [✓ Target]  ← Allow both selected
```
- Multi-select enabled
- Allows user to compare or view individual company

**2. Year Slicer (All Pages)**
```
[2020] [2021] [2022] [2023] [2024]
```
- Single or multi-select
- Allows time-period analysis

**3. Metric Selector (Optional)**
```
View by: [Absolute Dollars] [Percentages] [Ratios]
```
- Changes visualization format
- Alternative: Create separate pages instead

### Drill-Through Capabilities

**Executive Summary → Profitability Page**
- Click revenue bar → Shows profitability details for selected company

**Profitability → Detailed Analysis**
- Click margin bar → Shows year-by-year breakdown

---

## Data Refresh Strategy

### Manual Refresh (Quarterly)
1. Download latest 10-Q/10-K from SEC EDGAR
2. Update `data/cleaned/dashboard_export.csv`
3. Refresh Power BI dataset
4. Dashboard automatically updates

### Automated Refresh (Advanced)
1. Create Python script to pull SEC API quarterly
2. Update CSV automatically
3. Configure Power BI to refresh on schedule
4. New data flows to dashboard automatically

---

## Visual Design Best Practices

### Color Scheme
- **Primary Colors**:
  - Walmart: #0071ce (Blue)
  - Target: #cc0000 (Red)
  
- **Supporting Colors**:
  - Positive: #4CAF50 (Green)
  - Negative: #f44336 (Red)
  - Neutral: #757575 (Gray)
  - Background: #f5f5f5 (Light Gray)

### Typography
- **Title**: 24pt, Bold
- **Subtitle**: 16pt, Bold
- **Labels**: 12pt, Regular
- **Values**: 14pt, Bold

### Chart Standards
- Always include title and axis labels
- Use consistent scales for same metric across pages
- Include data source reference
- Use sparklines for quick trend identification

### Page Structure
- **Top**: Title + Company/Year filters
- **Middle**: 2-4 main visualizations (rotate daily)
- **Bottom**: Summary insights or detailed table

---

## Exporting & Sharing

### Dashboard Screenshots
1. Capture Page 1 (Executive Summary) - use for presentations
2. Capture Page 2 (Profitability) - for investor materials
3. Capture Page 3 (Liquidity/Risk) - for credit analysis
4. Capture Page 4 (Efficiency) - for operational review

### PDF Export
1. File → Export
2. Include all 4 pages
3. High resolution (300 DPI)
4. Save as `financial_analysis_dashboard.pdf`

### Web Publishing (Premium Power BI)
1. Publish to Power BI Service
2. Share report link
3. Enable automatic refresh
4. Allow stakeholder comments

### Excel Export
1. Right-click visualization
2. Export underlying data
3. Create pivot tables for additional analysis
4. Share with stakeholders for auditing

---

## Dashboard Maintenance Checklist

- [ ] Data refreshed monthly with latest figures
- [ ] KPI calculations verified against source data
- [ ] Filters working correctly
- [ ] Charts readable and professional
- [ ] Colors consistent across pages
- [ ] Spelling/grammar checked
- [ ] Calculations cross-validated
- [ ] Dashboard performance optimized
- [ ] Users trained on how to use
- [ ] Feedback collected and incorporated

---

**Your Power BI dashboard is now ready to impress stakeholders!** 📊✨
