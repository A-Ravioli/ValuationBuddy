import yfinance as yf
from data.stock_data import fetch_stock_data
from data.financial_statements import fetch_financial_statements
from data.economic_data import fetch_economic_data
from analysis.dcf_model import perform_dcf_analysis
from analysis.comparable_analysis import fetch_comp_data, calculate_valuation_ratios
from excel.report_generator import create_excel_report


def main():
    ticker = input("Enter the stock ticker: ")
    comp_tickers = input("Enter competitor tickers (comma-separated): ").split(",")

    # Fetch all necessary data
    stock_data = fetch_stock_data(ticker)
    financial_statements = fetch_financial_statements(ticker)
    economic_data = fetch_economic_data()
    comp_data = fetch_comp_data(comp_tickers)

    # Perform analyses
    dcf_results = perform_dcf_analysis(financial_statements)
    comp_ratios = calculate_valuation_ratios(comp_data)

    # Create Excel report
    create_excel_report(
        ticker,
        stock_data,
        financial_statements,
        economic_data,
        dcf_results,
        comp_data,
        comp_ratios,
    )

    print(f"Excel report for {ticker} has been generated.")


if __name__ == "__main__":
    main()
