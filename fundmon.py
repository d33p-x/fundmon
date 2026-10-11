FUNDING_RATES = [
    ("BTC", 0.000069),
    ("ETH", 0.000016),
    ("SOL", 0.000063),
    ("HYPE", -0.000025),
    ("XRP", -0.000091),
    ("ZEC", 0.000037),
    ("XAU", 0.000000),
    ("NEAR", 0.000048),
    ("DOGE", -0.000023),
    ("BNB", 0.001000),
]


def annualized_funding(rate, hours=8):
    hours_per_year = 365 * 24
    periods_per_year = hours_per_year / hours
    return periods_per_year * rate


def basis(mark, index):
    return mark / index - 1


def funding_label(rate):
    if rate == 0:
        label = "neutral"
    elif rate < 0:
        label = "shorts pay"
    else:
        label = "longs pay"
    return label


sorted_rates = sorted(FUNDING_RATES, key=lambda pair: pair[1], reverse=True)

print(f"{'Symbol':<8}{"Rate/8h":>10}{"Annual":>10}{"Label":>10}")

high_funding = []
for symbol, rate in sorted_rates:
    if annualized_funding(rate) > 0.2:
        high_funding.append((symbol, rate))
    print(
        f"{symbol:<8} {rate:>10.4%} {annualized_funding(rate):>10.4} {funding_label(rate):>10}"
    )
for i in high_funding:
    print(f"High Funding over 20% annually: {i[0]:>10} {i[1]:>10}")
