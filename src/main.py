# main.py
from data_retrieval import get_full_stock_data
from comps import get_comparative_analysis
from excel_export import export_advanced_excel

if __name__ == "__main__":
    # Input: stock ticker and competitors
    ticker = input("Enter the stock ticker: ")
    peers = input("Enter competitor tickers (comma-separated): ").split(",")

    # Get stock data for the main stock
    stock_data = get_full_stock_data(ticker)

    # Perform comparative analysis on competitors
    comp_df = get_comparative_analysis(peers)

    # Export the full analysis to Excel
    export_advanced_excel(stock_data, comp_df)
