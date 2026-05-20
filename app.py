import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Financial Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .header {
        color: #0071ce;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subheader {
        color: #333;
        font-size: 1.2em;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/cleaned/walmart_target_combined.csv')
    df_ratios = pd.read_csv('data/cleaned/financial_ratios.csv')
    return df, df_ratios

df, df_ratios = load_data()

# Title and Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p class="header">📊 Financial Analysis Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Walmart vs. Target: Comprehensive Financial Comparison (FY 2020-2024)</p>', unsafe_allow_html=True)

# Sidebar filters
st.sidebar.markdown("## 🎯 Filters")
companies = st.sidebar.multiselect(
    "Select Companies:",
    options=['Walmart', 'Target'],
    default=['Walmart', 'Target']
)

years = st.sidebar.slider(
    "Select Year Range:",
    min_value=2020,
    max_value=2024,
    value=(2020, 2024)
)

# Filter data
df_filtered = df[(df['company'].isin(companies)) & (df['year'].between(years[0], years[1]))]
df_ratios_filtered = df_ratios[(df_ratios['company'].isin(companies)) & (df_ratios['year'].between(years[0], years[1]))]

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Executive Summary",
    "💰 Profitability Analysis",
    "🔒 Liquidity & Solvency",
    "⚡ Efficiency & Performance"
])

# ============ TAB 1: EXECUTIVE SUMMARY ============
with tab1:
    st.markdown("## 📊 Key Performance Indicators (Latest Year)")
    
    # Get latest data for selected companies
    latest_data = df_filtered.sort_values('year').groupby('company').tail(1)
    latest_ratios = df_ratios_filtered.sort_values('year').groupby('company').tail(1)
    
    # Create KPI cards
    if len(latest_data) > 0:
        cols = st.columns(len(companies))
        
        for idx, company in enumerate(companies):
            with cols[idx]:
                company_data = latest_data[latest_data['company'] == company]
                if not company_data.empty:
                    company_data = company_data.iloc[0]
                    
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, {'#0071ce' if company == 'Walmart' else '#cc0000'} 0%, {'#0091ff' if company == 'Walmart' else '#ff3333'} 100%); 
                                 padding: 20px; border-radius: 10px; color: white; text-align: center;">
                        <h3 style="margin: 0; color: white;">{company}</h3>
                        <p style="font-size: 0.9em; margin: 10px 0; opacity: 0.9;">FY {int(company_data['year'])}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.metric("Revenue", f"${company_data['revenue']/1000:.1f}B")
                    st.metric("Net Income", f"${company_data['net_income']:.0f}M")
                    st.metric("Total Assets", f"${company_data['total_assets']/1000:.1f}B")
                    st.metric("Operating Cash Flow", f"${company_data['operating_cash_flow']:.0f}M")
    
    # Revenue Comparison
    st.markdown("---")
    st.markdown("## 📊 Revenue & Profitability Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        df_sorted = df_filtered.sort_values('year')
        fig_revenue = px.line(df_sorted, x='year', y='revenue', color='company',
                            markers=True, title='Revenue Trend',
                            color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'})
        fig_revenue.update_layout(height=400, hovermode='x unified', template='plotly_white')
        fig_revenue.update_yaxes(title_text="Revenue ($M)")
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        fig_income = px.line(df_sorted, x='year', y='net_income', color='company',
                            markers=True, title='Net Income Trend',
                            color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'})
        fig_income.update_layout(height=400, hovermode='x unified', template='plotly_white')
        fig_income.update_yaxes(title_text="Net Income ($M)")
        st.plotly_chart(fig_income, use_container_width=True)
    
    # Summary insights
    st.markdown("### 🔍 Key Insights")
    
    col1, col2 = st.columns(2)
    with col1:
        walmart_data = latest_data[latest_data['company'] == 'Walmart']
        if not walmart_data.empty:
            wmt = walmart_data.iloc[0]
            st.info(f"""
            **Walmart - FY {int(wmt['year'])}**
            - Revenue: ${wmt['revenue']/1000:.1f}B
            - Net Income: ${wmt['net_income']:.0f}M
            - Total Assets: ${wmt['total_assets']/1000:.1f}B
            - 📈 Strong revenue scale and operational efficiency
            """)
    
    with col2:
        target_data = latest_data[latest_data['company'] == 'Target']
        if not target_data.empty:
            tgt = target_data.iloc[0]
            st.info(f"""
            **Target - FY {int(tgt['year'])}**
            - Revenue: ${tgt['revenue']/1000:.1f}B
            - Net Income: ${tgt['net_income']:.0f}M
            - Total Assets: ${tgt['total_assets']/1000:.1f}B
            - 💪 Solid financial position with sustainable growth
            """)


# ============ TAB 2: PROFITABILITY ANALYSIS ============
with tab2:
    st.markdown("## 💰 Profitability Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Profit Margins Comparison
        latest_ratios_sorted = df_ratios_filtered.sort_values('year')
        fig_margins = make_subplots(specs=[[{"secondary_y": False}]])
        
        for company in companies:
            company_data = latest_ratios_sorted[latest_ratios_sorted['company'] == company]
            fig_margins.add_trace(
                go.Scatter(x=company_data['year'], 
                          y=company_data['Gross_Margin_%'],
                          name=f'{company} (Gross)',
                          line=dict(color='#0071ce' if company == 'Walmart' else '#cc0000', dash='solid'))
            )
        
        fig_margins.update_layout(title='Gross Profit Margin Trend', height=400, template='plotly_white')
        fig_margins.update_yaxes(title_text="Margin (%)")
        st.plotly_chart(fig_margins, use_container_width=True)
    
    with col2:
        fig_net_margin = px.line(latest_ratios_sorted, x='year', y='Net_Margin_%', 
                                 color='company', markers=True,
                                 title='Net Profit Margin Trend',
                                 color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'})
        fig_net_margin.update_layout(height=400, template='plotly_white')
        fig_net_margin.update_yaxes(title_text="Net Margin (%)")
        st.plotly_chart(fig_net_margin, use_container_width=True)
    
    # ROA and ROE
    col1, col2 = st.columns(2)
    
    with col1:
        fig_roa = px.bar(latest_ratios_sorted, x='year', y='ROA_%', color='company',
                        title='Return on Assets (ROA)',
                        color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'},
                        barmode='group')
        fig_roa.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_roa, use_container_width=True)
    
    with col2:
        fig_roe = px.bar(latest_ratios_sorted, x='year', y='ROE_%', color='company',
                        title='Return on Equity (ROE)',
                        color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'},
                        barmode='group')
        fig_roe.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_roe, use_container_width=True)
    
    # Profitability Summary Table
    st.markdown("### 📊 Profitability Metrics Summary (Latest Year)")
    summary_data = latest_ratios_sorted.groupby('company')[['Gross_Margin_%', 'Operating_Margin_%', 'Net_Margin_%', 'ROA_%', 'ROE_%']].mean()
    summary_data = summary_data.round(2)
    st.dataframe(summary_data, use_container_width=True)


# ============ TAB 3: LIQUIDITY & SOLVENCY ============
with tab3:
    st.markdown("## 🔒 Financial Health & Risk Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        latest_ratios_sorted = df_ratios_filtered.sort_values('year')
        fig_current = px.line(latest_ratios_sorted, x='year', y='Current_Ratio', 
                             color='company', markers=True,
                             title='Current Ratio (Liquidity)',
                             color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'})
        fig_current.add_hline(y=1.0, line_dash="dash", line_color="gray", annotation_text="Industry Benchmark")
        fig_current.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_current, use_container_width=True)
    
    with col2:
        fig_dte = px.line(latest_ratios_sorted, x='year', y='Debt_to_Equity', 
                         color='company', markers=True,
                         title='Debt-to-Equity Ratio (Solvency)',
                         color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'})
        fig_dte.add_hline(y=1.5, line_dash="dash", line_color="green", annotation_text="Healthy Range")
        fig_dte.add_hline(y=2.0, line_dash="dash", line_color="orange", annotation_text="Upper Range")
        fig_dte.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_dte, use_container_width=True)
    
    # Debt Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        latest_data_sorted = df_filtered.sort_values('year')
        fig_debt = px.bar(latest_data_sorted, x='year', y='total_liabilities', 
                         color='company', title='Total Liabilities',
                         color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'},
                         barmode='group')
        fig_debt.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_debt, use_container_width=True)
    
    with col2:
        fig_equity = px.bar(latest_data_sorted, x='year', y='total_equity', 
                           color='company', title='Total Equity',
                           color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'},
                           barmode='group')
        fig_equity.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_equity, use_container_width=True)
    
    # Risk Assessment
    st.markdown("### 📋 Solvency Metrics Summary")
    solvency_data = latest_ratios_sorted.groupby('company')[['Current_Ratio', 'Quick_Ratio', 'Debt_to_Equity', 'Debt_Ratio_%', 'Equity_Ratio_%']].mean()
    solvency_data = solvency_data.round(2)
    st.dataframe(solvency_data, use_container_width=True)
    
    # Risk Assessment
    st.markdown("### ⚠️ Financial Risk Assessment")
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        **Walmart**
        - Liquidity Risk: ✅ LOW
        - Solvency Risk: ✅ LOW
        - Overall Risk: ✅ LOW
        """)
    with col2:
        st.success("""
        **Target**
        - Liquidity Risk: ✅ LOW
        - Solvency Risk: ✅ LOW
        - Overall Risk: ✅ LOW
        """)


# ============ TAB 4: EFFICIENCY & PERFORMANCE ============
with tab4:
    st.markdown("## ⚡ Operational Efficiency & Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        latest_ratios_sorted = df_ratios_filtered.sort_values('year')
        fig_inventory = px.line(latest_ratios_sorted, x='year', y='Inventory_Turnover', 
                               color='company', markers=True,
                               title='Inventory Turnover (⭐ Key Metric)',
                               color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'})
        fig_inventory.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_inventory, use_container_width=True)
    
    with col2:
        fig_asset = px.line(latest_ratios_sorted, x='year', y='Asset_Turnover', 
                           color='company', markers=True,
                           title='Asset Turnover Ratio',
                           color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'})
        fig_asset.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_asset, use_container_width=True)
    
    # Cash Flow Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        latest_data_sorted = df_filtered.sort_values('year')
        fig_ocf = px.bar(latest_data_sorted, x='year', y='operating_cash_flow', 
                        color='company', title='Operating Cash Flow',
                        color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'},
                        barmode='group')
        fig_ocf.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_ocf, use_container_width=True)
    
    with col2:
        fig_fcf = px.bar(latest_data_sorted, x='year', y='free_cash_flow', 
                        color='company', title='Free Cash Flow',
                        color_discrete_map={'Walmart': '#0071ce', 'Target': '#cc0000'},
                        barmode='group')
        fig_fcf.update_layout(height=400, template='plotly_white')
        st.plotly_chart(fig_fcf, use_container_width=True)
    
    # Efficiency Metrics Table
    st.markdown("### 📊 Efficiency Metrics Summary")
    efficiency_data = latest_ratios_sorted.groupby('company')[['Inventory_Turnover', 'Asset_Turnover', 'Receivables_Turnover', 'OCF_Margin_%', 'FCF_Margin_%']].mean()
    efficiency_data = efficiency_data.round(2)
    st.dataframe(efficiency_data, use_container_width=True)
    
    # Efficiency Analysis
    st.markdown("### 🎯 Key Performance Indicators")
    col1, col2 = st.columns(2)
    with col1:
        st.warning("""
        **Walmart - Operational Excellence**
        - Inventory Turnover: 8.4x (Every 43 days)
        - Asset Turnover: 2.57x
        - Strong cash generation capability
        - ⭐ Superior retail efficiency
        """)
    with col2:
        st.info("""
        **Target - Solid Operations**
        - Inventory Turnover: 5.8x (Every 63 days)
        - Asset Turnover: 1.79x
        - Healthy cash flow margins
        - ✅ Efficient business model
        """)


# ============ FOOTER ============
st.markdown("---")
st.markdown("""
### 📊 Dashboard Summary

**Overall Finding:** Walmart demonstrates superior financial strength across most metrics (revenue scale, profitability, cash generation, operational efficiency), while Target remains financially sound with sustainable profit margins and manageable debt levels.

**Data Source:** SEC EDGAR 10-K Filings | **Period:** FY 2020-2024 | **Currency:** USD (Millions)

**Created by:** Financial Analysis Project | **Project Link:** https://github.com/aashifkhan0328-dotcom/Dashboard
""")
