SYMBOLS = [
    ("BTC", 0.0069),
    ("ETH", 0.0016),
    ("SOL", 0.0063),
    ("HYPE", -0.0025),
    ("XRP", -0.0091),
    ("ZEC", 0.0037),
    ("XAU", 0.0000),
    ("NEAR", 0.0048),
    ("DOGE", -0.0023),
    ("BNB", 0),
]


def annualized_funding(rate, hours=8):
    hours_per_year = 365 * 24
    periods_per_year = hours_per_year / hours
    return periods_per_year * rate


def basis(mark, index):
    return mark / index - 1


def funding_label(rate):
    if rate[1] == 0:
        print(f"{rate[0]} neutral")
    if rate[1] < 0:
        print(f"{rate[0]} shorts pay")
    if rate[1] > 0:
        print(f"{rate[0]} longs pay")


for i in SYMBOLS:
    counter = 0
    funding_label(i)
    if abs(i[1]) > 0.05:
        counter += 1
print(f"Extreme rates: {counter}")

