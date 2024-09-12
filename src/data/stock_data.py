import yfinance as yf


def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    history = stock.history(period="1y")

    return {"info": info, "history": history}
