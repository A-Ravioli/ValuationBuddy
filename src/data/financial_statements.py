import yfinance as yf


def fetch_financial_statements(ticker):
    stock = yf.Ticker(ticker)

    return {
        "income_statement": {
            "annual": stock.financials,
            "quarterly": stock.quarterly_financials,
        },
        "balance_sheet": {
            "annual": stock.balance_sheet,
            "quarterly": stock.quarterly_balance_sheet,
        },
        "cash_flow": {"annual": stock.cashflow, "quarterly": stock.quarterly_cashflow},
    }
