"""
Data Cleaning and Preparation Script
Standardizes and cleans financial data for analysis
"""

import pandas as pd
import numpy as np
import os

class DataCleaner:
    """Clean and standardize financial data"""
    
    def __init__(self):
        self.raw_data_path = 'data/raw'
        self.cleaned_data_path = 'data/cleaned'
    
    def load_raw_data(self, company_name):
        """Load raw financial data for a company"""
        try:
            filename = f"{self.raw_data_path}/{company_name}_financial_statements.csv"
            df = pd.read_csv(filename, index_col='year')
            print(f"✓ Loaded raw data for {company_name}")
            return df
        except Exception as e:
            print(f"✗ Error loading {company_name}: {str(e)}")
            return None
    
    def standardize_company_name(self, df, company_name):
        """Add standardized company name column"""
        df['company'] = company_name.title()
        return df
    
    def convert_units(self, df, unit='millions'):
        """Ensure all numeric values are in consistent units (millions USD)"""
        # Already in millions from source data
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        df[numeric_columns] = df[numeric_columns].astype(float)
        return df
    
    def add_calculated_columns(self, df):
        """Add calculated financial metrics"""
        
        # Free Cash Flow
        if 'operating_cash_flow' in df.columns and 'capital_expenditures' in df.columns:
            df['free_cash_flow'] = df['operating_cash_flow'] - df['capital_expenditures']
        
        # Calculate average values for ratio calculations
        df['avg_total_assets'] = (df['total_assets'] + df['total_assets'].shift(1)) / 2
        df['avg_equity'] = (df['total_equity'] + df['total_equity'].shift(1)) / 2
        df['avg_inventory'] = (df['inventory'] + df['inventory'].shift(1)) / 2
        df['avg_receivables'] = (df['accounts_receivable'] + df['accounts_receivable'].shift(1)) / 2
        
        return df
    
    def handle_missing_values(self, df):
        """Handle missing or null values"""
        # Fill forward for missing values
        df = df.fillna(method='ffill')
        
        # Drop rows that are still mostly empty
        df = df.dropna(thresh=len(df.columns) * 0.7)
        
        print(f"  Missing values handled. Remaining rows: {len(df)}")
        return df
    
    def clean_company_data(self, company_name):
        """Execute full cleaning pipeline for a company"""
        print(f"\nCleaning data for {company_name}...")
        
        df = self.load_raw_data(company_name)
        if df is None:
            return None
        
        df = self.standardize_company_name(df, company_name)
        df = self.convert_units(df)
        df = self.add_calculated_columns(df)
        df = self.handle_missing_values(df)
        
        # Reorder columns logically
        column_order = [
            'company',
            'revenue', 'cost_of_sales', 'gross_profit',
            'operating_income', 'net_income',
            'total_assets', 'current_assets', 'inventory', 'accounts_receivable',
            'total_liabilities', 'current_liabilities', 'total_equity',
            'operating_cash_flow', 'capital_expenditures', 'free_cash_flow',
            'avg_total_assets', 'avg_equity', 'avg_inventory', 'avg_receivables'
        ]
        
        # Keep only existing columns
        df = df[[col for col in column_order if col in df.columns]]
        
        # Sort by year descending
        df = df.sort_index(ascending=False)
        
        print(f"  ✓ Cleaned data shape: {df.shape}")
        
        return df
    
    def combine_datasets(self, walmart_df, target_df):
        """Combine cleaned data from both companies"""
        combined_df = pd.concat([walmart_df, target_df], axis=0)
        combined_df = combined_df.reset_index().rename(columns={'index': 'year'})
        combined_df = combined_df.sort_values(['company', 'year'])
        return combined_df
    
    def save_cleaned_data(self, df, filename):
        """Save cleaned dataset to CSV"""
        filepath = f"{self.cleaned_data_path}/{filename}"
        df.to_csv(filepath, index=False)
        print(f"✓ Saved cleaned data to {filepath}")
        return filepath


def main():
    """Main execution function"""
    print("=" * 60)
    print("Data Cleaning and Preparation")
    print("=" * 60)
    
    # Create cleaned data directory if it doesn't exist
    os.makedirs('data/cleaned', exist_ok=True)
    
    cleaner = DataCleaner()
    
    # Clean individual company data
    walmart_df = cleaner.clean_company_data('walmart')
    target_df = cleaner.clean_company_data('target')
    
    if walmart_df is not None and target_df is not None:
        # Combine datasets
        print("\nCombining datasets...")
        combined_df = cleaner.combine_datasets(walmart_df, target_df)
        
        # Save cleaned datasets
        cleaner.save_cleaned_data(walmart_df, 'walmart_cleaned.csv')
        cleaner.save_cleaned_data(target_df, 'target_cleaned.csv')
        cleaner.save_cleaned_data(combined_df, 'walmart_target_combined.csv')
        
        print("\n" + "=" * 60)
        print("Data cleaning complete!")
        print("Combined dataset preview:")
        print(combined_df.head(10))
        print("=" * 60)
    else:
        print("\n✗ Failed to clean data for one or both companies")


if __name__ == "__main__":
    main()
