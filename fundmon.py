def annualized_funding(rate, hours=8):
    hours_year = 365 * 24
    fundings_year = hours_year / hours
    return fundings_year * rate

def basis_pct(mark, index):
    return mark / index - 1
