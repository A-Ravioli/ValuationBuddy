def calculate_balance_sheet_ratios(balance_sheet):
    """Extract key balance sheet ratios from the data."""
    current_assets = balance_sheet.loc["Total Current Assets"].iloc[0]
    current_liabilities = balance_sheet.loc["Total Current Liabilities"].iloc[0]
    total_debt = balance_sheet.loc["Total Liabilities Net Minority Interest"].iloc[0]
    equity = balance_sheet.loc["Total Stockholder Equity"].iloc[0]

    # Key ratios
    current_ratio = current_assets / current_liabilities
    debt_to_equity = total_debt / equity

    return {"Current Ratio": current_ratio, "Debt/Equity": debt_to_equity}
