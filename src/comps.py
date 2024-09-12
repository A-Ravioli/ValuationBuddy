import pandas as pd
from data_retrieval import get_full_stock_data


def get_comparative_analysis(tickers):
    """Perform comparative analysis for a list of peer companies."""
    comparisons = []

    for ticker in tickers:
        stock_data = get_full_stock_data(ticker)
        info = stock_data["info"]

        # Collect key metrics
        comparisons.append(
            {
                "Ticker": ticker,
                "P/E Ratio": info.get("trailingPE"),
                "Price/Sales": info.get("priceToSalesTrailing12Months"),
                "EV/EBITDA": info.get("enterpriseToEbitda"),
                "ROE": info.get("returnOnEquity"),
                "Profit Margin": info.get("profitMargins"),
            }
        )

    return pd.DataFrame(comparisons)
