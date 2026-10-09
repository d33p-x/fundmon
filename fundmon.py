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


counter = 0
for symbol,rate in FUNDING_RATES:
    if abs(rate) > 0.0005:
        counter += 1
    print(f"{symbol} {funding_label(rate)}")
    
print(f"Extreme rates: {counter}")
