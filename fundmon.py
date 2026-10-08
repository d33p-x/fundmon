def annualized_funding(rate, hours=8):
    hours_per_year = 365 * 24
    periods_per_year = hours_per_year / hours
    return periods_per_year * rate


def basis(mark, index):
    return mark / index - 1


print(f'annualized funding 0.00034 = {annualized_funding(0.00034):.4f}')
print(f'annualized funding -0.00014 = {annualized_funding(-0.00014):.4f}')
print(f'annualized funding 0.00004 = {annualized_funding(0.00004):.4f}')

print(f"basis 101/100 = {basis(101, 100):.4f}")
print(f"basis 99.5/100 = {basis(99.5, 100):.4f}")
print(f"basis 64320/64000 = {basis(64320, 64000):.4f}")
