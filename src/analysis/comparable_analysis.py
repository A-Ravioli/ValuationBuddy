import yfinance as yf
import pandas as pd


def fetch_comp_data(comp_tickers):
    comp_data = {}
    for ticker in comp_tickers:
        stock = yf.Ticker(ticker)
        comp_data[ticker] = {"info": stock.info, "financials": stock.financials}
    return comp_data


def calculate_valuation_ratios(comp_data):
    ratios = {}
    for ticker, data in comp_data.items():
        info = data["info"]
        financials = data["financials"]

        market_cap = info.get("marketCap", None)
        enterprise_value = info.get("enterpriseValue", None)

        if market_cap and enterprise_value:
            ratios[ticker] = {
                "P/E": info.get("trailingPE", None),
                "Price/Book": info.get("priceToBook", None),
                "P/FCF": (
                    market_cap / financials.loc["Free Cash Flow", financials.columns[0]]
                    if "Free Cash Flow" in financials.index
                    else None
                ),
                "EV/EBITDA": info.get("enterpriseToEbitda", None),
                "EV/Interest": (
                    enterprise_value
                    / financials.loc["Interest Expense", financials.columns[0]]
                    if "Interest Expense" in financials.index
                    else None
                ),
            }

    return pd.DataFrame(ratios).T
