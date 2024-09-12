import pandas as pd


def export_advanced_excel(stock_data, comp_df, file_name="stock_analysis.xlsx"):
    """Export financial data, ratios, and peer comparison to an Excel file."""
    with pd.ExcelWriter(file_name, engine="openpyxl") as writer:

        # Write financial statements to separate sheets
        stock_data["income_statement"].to_excel(writer, sheet_name="Income Statement")
        stock_data["balance_sheet"].to_excel(writer, sheet_name="Balance Sheet")
        stock_data["cash_flow"].to_excel(writer, sheet_name="Cash Flow Statement")

        # Write key financial ratios to a sheet
        pd.DataFrame(stock_data["key_ratios"], index=[0]).to_excel(
            writer, sheet_name="Key Ratios"
        )

        # Write comparative analysis to a separate sheet
        comp_df.to_excel(writer, sheet_name="Comparative Analysis")

    print(f"Advanced financial data exported to {file_name}")
