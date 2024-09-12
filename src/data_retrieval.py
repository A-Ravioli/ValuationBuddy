# data_retrieval.py
import yfinance as yf
import pandas as pd


def get_full_stock_data(ticker):
    stock = yf.Ticker(ticker)

    # Retrieve stock price history, financial statements, and other data
    history = stock.history(period="5y")
    info = stock.info

    # Financial Statements
    income_statement = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow = stock.cashflow

    # Key ratios and metrics
    key_ratios = {
        "Price to Earnings (P/E)": info.get("trailingPE"),
        "Price to Sales (P/S)": info.get("priceToSalesTrailing12Months"),
        "Price to Book (P/B)": info.get("priceToBook"),
        "Enterprise Value/EBITDA (EV/EBITDA)": info.get("enterpriseToEbitda"),
        "Profit Margin": info.get("profitMargins"),
        "Operating Margin": info.get("operatingMargins"),
        "Return on Equity (ROE)": info.get("returnOnEquity"),
        "Return on Assets (ROA)": info.get("returnOnAssets"),
    }

    return {
        "history": history,
        "info": info,
        "income_statement": income_statement,
        "balance_sheet": balance_sheet,
        "cash_flow": cash_flow,
        "key_ratios": key_ratios,
    }
