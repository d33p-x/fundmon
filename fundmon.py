HIGH_FUNDING_THRESHOLD = 0.20

MARKET_DATA = {
    "BTC": {"funding": 0.000069, "mark": 112450.0, "index": 112380.0, "sector": "L1"},
    "ETH": {"funding": 0.000016, "mark": 4120.5, "index": 4119.8, "sector": "L1"},
    "SOL": {"funding": 0.000063, "mark": 198.42, "index": 198.30, "sector": "L1"},
    "NEAR": {"funding": 0.000048, "mark": 2.874, "index": 2.871, "sector": "L1"},
    "HYPE": {"funding": -0.000025, "mark": 44.10, "index": 44.16, "sector": "exchange"},
    "BNB": {"funding": 0.001000, "mark": 1012.4, "index": 1006.9, "sector": "exchange"},
    "XRP": {"funding": -0.000091, "mark": 2.8410, "index": 2.8452, "sector": "payments"},
    "ZEC": {"funding": 0.000037, "mark": 61.25, "index": 61.20, "sector": "payments"},
    "DOGE": {"funding": -0.000023, "mark": 0.2385, "index": 0.2388, "sector": "meme"},
    "XAU": {"funding": 0.000000, "mark": 2650.4, "index": 2650.4, "sector": "commodity"},
}

sectors = {details["sector"] for symbol, details in MARKET_DATA.items()}


def annualized_funding(rate, hours=8):
    """calculate the annualized funding rate based on rate"""
    hours_per_year = 365 * 24
    periods_per_year = hours_per_year / hours
    return periods_per_year * rate


def basis(mark, index):
    """calculate the basis bsed on mark and index"""
    return mark / index - 1


def funding_label(rate):
    if rate == 0:
        label = "neutral"
    elif rate < 0:
        label = "shorts pay"
    else:
        label = "longs pay"
    return label


def top_n(n, data):
    """return top n symbols based on funding rate"""
    sorted_data = sorted(data.items(), key=lambda x: x[1]["funding"], reverse=True)
    top_rates = [symbol for symbol, details in sorted_data]
    return top_rates[:n]


def average_funding(data):
    """return average funding rate of all symbols in data combined"""
    rates = [details["funding"] for symbol, details in data.items()]
    avg = sum(rates) / len(rates)
    return avg


def average_funding_by_sector(data):
    """return average funding rate per sector in data"""
    sector_rates = {}
    sector_averages = {}
    for symbol, details in data.items():
        sector = details["sector"]
        rate = details["funding"]
        if sector not in sector_rates:
            sector_rates[sector] = []
        sector_rates[sector].append(rate)
    for sector, rates in sector_rates.items():
        sector_averages[sector] = sum(rates) / len(rates)
    return sector_averages


sorted_rates = sorted(MARKET_DATA.items(), key=lambda x: x[1]["funding"], reverse=True)

high_funding = [
    symbol
    for symbol, details in sorted_rates
    if annualized_funding(details["funding"]) > HIGH_FUNDING_THRESHOLD
]

print(f"{'Symbol':<8} {'Rate/8h':>10} {'Annual':>10} {'Basis':>10} {'Label':<12}")
for symbol, details in sorted_rates:
    rate = details["funding"]
    annual = annualized_funding(rate)
    basis_rate = basis(details["mark"], details["index"])
    print(
        f"{symbol:<8} {rate:>10.4%} {annual:>10.2%} {basis_rate:>10.2%} {funding_label(rate):<12}"
    )
for i in high_funding:
    print(f"High Funding over 20% annually: {i}")

print(average_funding_by_sector(MARKET_DATA))
print(average_funding(MARKET_DATA))
print(top_n(4, MARKET_DATA))
