import pandas as pd
import numpy as np


def perform_dcf_analysis(financial_statements, assumptions):
    # This is a simplified DCF model. In practice, you'd want to make this more robust.
    income_statement = financial_statements["income_statement"]["annual"]

    # Extract and project free cash flows
    revenue = income_statement.loc["Total Revenue"]
    ebit = income_statement.loc["EBIT"]

    # Project future cash flows (simplified)
    projection_years = 5
    growth_rate = assumptions["growth_rate"]
    projected_revenues = [
        revenue[-1] * (1 + growth_rate) ** i for i in range(1, projection_years + 1)
    ]
    projected_ebit = [ebit[-1] / revenue[-1] * rev for rev in projected_revenues]

    # Calculate free cash flow (simplified)
    tax_rate = assumptions["tax_rate"]
    capex_rate = assumptions["capex_rate"]
    fcf = [
        (1 - tax_rate) * ebit - capex_rate * rev
        for ebit, rev in zip(projected_ebit, projected_revenues)
    ]

    # Discount cash flows
    discount_rate = assumptions["discount_rate"]
    pvs = [cf / (1 + discount_rate) ** (i + 1) for i, cf in enumerate(fcf)]

    # Terminal value
    terminal_growth = assumptions["terminal_growth"]
    terminal_value = fcf[-1] * (1 + terminal_growth) / (discount_rate - terminal_growth)
    terminal_value_pv = terminal_value / (1 + discount_rate) ** projection_years

    # Sum up
    enterprise_value = sum(pvs) + terminal_value_pv

    return {
        "enterprise_value": enterprise_value,
        "projected_fcf": fcf,
        "present_values": pvs,
        "terminal_value": terminal_value,
    }
