from fredapi import Fred
from config import FRED_API_KEY


def fetch_economic_data():
    fred = Fred(api_key=FRED_API_KEY)

    gdp = fred.get_series("GDP")
    inflation = fred.get_series("CPIAUCSL")
    unemployment = fred.get_series("UNRATE")

    return {"gdp": gdp, "inflation": inflation, "unemployment": unemployment}
