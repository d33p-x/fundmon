def annualized_funding(rate, hours=8):
    hours_per_year = 365 * 24
    periods_per_year = hours_per_year / hours
    return periods_per_year * rate


def basis(mark, index):
    return mark / index - 1


print(annualized_funding(0.002))
print(annualized_funding(-0.0032))
print(annualized_funding(0.01))

print("basis 101/100 = %0.4f" % basis(101, 100))
print("basis 99.5/100 = %0.4f" % basis(99.5, 100))
print("basis 64320/64000 = %0.4f" % basis(64320, 64000))
