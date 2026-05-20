"""
Financial Ratio Calculation Script
Calculates 12+ financial ratios for analysis
"""

import pandas as pd
import numpy as np
import os

class FinancialRatioCalculator:
    """Calculate financial ratios for analysis"""
    
    def __init__(self):
        self.cleaned_data_path = 'data/cleaned'
    
    def load_combined_data(self):
        """Load combined cleaned dataset"""
        try:
            filepath = f"{self.cleaned_data_path}/walmart_target_combined.csv"
            df = pd.read_csv(filepath)
            print(f"✓ Loaded combined dataset: {filepath}")
            return df
        except Exception as e:
            print(f"✗ Error loading combined data: {str(e)}")
            return None
    
    # PROFITABILITY RATIOS
    def calculate_gross_margin(self, df):
        """Gross Profit Margin = Gross Profit / Revenue"""
        return (df['gross_profit'] / df['revenue'] * 100).round(2)
    
    def calculate_operating_margin(self, df):
        """Operating Profit Margin = Operating Income / Revenue"""
        return (df['operating_income'] / df['revenue'] * 100).round(2)
    
    def calculate_net_margin(self, df):
        """Net Profit Margin = Net Income / Revenue"""
        return (df['net_income'] / df['revenue'] * 100).round(2)
    
    def calculate_roa(self, df):
        """Return on Assets (ROA) = Net Income / Average Total Assets"""
        return (df['net_income'] / df['avg_total_assets'] * 100).round(2)
    
    def calculate_roe(self, df):
        """Return on Equity (ROE) = Net Income / Average Shareholders' Equity"""
        return (df['net_income'] / df['avg_equity'] * 100).round(2)
    
    # LIQUIDITY RATIOS
    def calculate_current_ratio(self, df):
        """Current Ratio = Current Assets / Current Liabilities"""
        return (df['current_assets'] / df['current_liabilities']).round(2)
    
    def calculate_quick_ratio(self, df):
        """Quick Ratio = (Current Assets - Inventory) / Current Liabilities"""
        quick_assets = df['current_assets'] - df['inventory']
        return (quick_assets / df['current_liabilities']).round(2)
    
    # SOLVENCY RATIOS
    def calculate_debt_to_equity(self, df):
        """Debt-to-Equity Ratio = Total Liabilities / Shareholders' Equity"""
        return (df['total_liabilities'] / df['total_equity']).round(2)
    
    def calculate_debt_ratio(self, df):
        """Debt Ratio = Total Liabilities / Total Assets"""
        return (df['total_liabilities'] / df['total_assets'] * 100).round(2)
    
    def calculate_equity_ratio(self, df):
        """Equity Ratio = Shareholders' Equity / Total Assets"""
        return (df['total_equity'] / df['total_assets'] * 100).round(2)
    
    # EFFICIENCY RATIOS
    def calculate_inventory_turnover(self, df):
        """Inventory Turnover = COGS / Average Inventory"""
        return (df['cost_of_sales'] / df['avg_inventory']).round(2)
    
    def calculate_asset_turnover(self, df):
        """Asset Turnover = Revenue / Average Total Assets"""
        return (df['revenue'] / df['avg_total_assets']).round(2)
    
    def calculate_receivables_turnover(self, df):
        """Receivables Turnover = Revenue / Average Accounts Receivable"""
        return (df['revenue'] / df['avg_receivables']).round(2)
    
    # CASH FLOW RATIOS
    def calculate_ocf_margin(self, df):
        """Operating Cash Flow Margin = Operating Cash Flow / Revenue"""
        return (df['operating_cash_flow'] / df['revenue'] * 100).round(2)
    
    def calculate_free_cash_flow_margin(self, df):
        """Free Cash Flow Margin = Free Cash Flow / Revenue"""
        return (df['free_cash_flow'] / df['revenue'] * 100).round(2)
    
    def calculate_ratios(self, df):
        """Calculate all financial ratios"""
        print("\nCalculating financial ratios...")
        
        # Profitability Ratios
        df['Gross_Margin_%'] = self.calculate_gross_margin(df)
        df['Operating_Margin_%'] = self.calculate_operating_margin(df)
        df['Net_Margin_%'] = self.calculate_net_margin(df)
        df['ROA_%'] = self.calculate_roa(df)
        df['ROE_%'] = self.calculate_roe(df)
        
        # Liquidity Ratios
        df['Current_Ratio'] = self.calculate_current_ratio(df)
        df['Quick_Ratio'] = self.calculate_quick_ratio(df)
        
        # Solvency Ratios
        df['Debt_to_Equity'] = self.calculate_debt_to_equity(df)
        df['Debt_Ratio_%'] = self.calculate_debt_ratio(df)
        df['Equity_Ratio_%'] = self.calculate_equity_ratio(df)
        
        # Efficiency Ratios
        df['Inventory_Turnover'] = self.calculate_inventory_turnover(df)
        df['Asset_Turnover'] = self.calculate_asset_turnover(df)
        df['Receivables_Turnover'] = self.calculate_receivables_turnover(df)
        
        # Cash Flow Ratios
        df['OCF_Margin_%'] = self.calculate_ocf_margin(df)
        df['FCF_Margin_%'] = self.calculate_free_cash_flow_margin(df)
        
        # Replace inf and nan with None for cleaner output
        df = df.replace([np.inf, -np.inf], np.nan)
        
        print(f"  ✓ Calculated 15 financial ratios")
        
        return df
    
    def save_ratios(self, df, filename='financial_ratios.csv'):
        """Save calculated ratios to CSV"""
        filepath = f"{self.cleaned_data_path}/{filename}"
        df.to_csv(filepath, index=False)
        print(f"✓ Saved ratios to {filepath}")
        return filepath


def main():
    """Main execution function"""
    print("=" * 60)
    print("Financial Ratio Calculation")
    print("=" * 60)
    
    calculator = FinancialRatioCalculator()
    
    # Load combined data
    df = calculator.load_combined_data()
    
    if df is not None:
        # Calculate all ratios
        df_with_ratios = calculator.calculate_ratios(df)
        
        # Save results
        calculator.save_ratios(df_with_ratios)
        
        # Display summary
        print("\n" + "=" * 60)
        print("Ratio Calculation Complete!")
        print("=" * 60)
        print("\nSample of calculated ratios:")
        
        # Select key ratio columns
        key_ratios = ['company', 'year', 'Gross_Margin_%', 'Net_Margin_%', 
                      'ROE_%', 'Current_Ratio', 'Debt_to_Equity', 'Inventory_Turnover']
        
        print(df_with_ratios[key_ratios].head(10).to_string())
        
    else:
        print("\n✗ Failed to load combined dataset")


if __name__ == "__main__":
    main()
