def calculate_dcf(
    cash_flows, growth_rate, discount_rate, terminal_growth_rate=0.02, years=5
):
    """Calculate the DCF value."""
    dcf_value = 0
    terminal_value = (
        cash_flows[-1]
        * (1 + terminal_growth_rate)
        / (discount_rate - terminal_growth_rate)
    )

    # Calculate the discounted cash flows
    for t in range(1, years + 1):
        dcf_value += cash_flows[t - 1] / (1 + discount_rate) ** t

    # Add terminal value
    dcf_value += terminal_value / (1 + discount_rate) ** years

    return dcf_value
