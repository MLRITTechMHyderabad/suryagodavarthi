import numpy as np

np.random.seed(42)  # For reproducibility
stock_prices = np.random.randint(100, 501, size=(30, 5))

average_prices = np.mean(stock_prices, axis=0)

max_price = np.max(stock_prices)
max_day, max_company = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)

min_price = np.min(stock_prices)
max_price_all = np.max(stock_prices)
normalized_prices = (stock_prices - min_price) / (max_price_all - min_price)

risky_days = {}
for i, day_prices in enumerate(stock_prices):
    risky = day_prices[day_prices < 200]
    if risky.size > 0:
        risky_days[i + 1] = risky.tolist()

print("Average stock prices:", average_prices)
print(f"Highest price recorded: ${max_price_all} at Day {max_day + 1}, Company {max_company + 1}")
print("\nNormalized Prices (first 5 rows):")
print(np.round(normalized_prices[:5], 2))

print("\n⚠️ Risky Investment Days:")
for day, prices in risky_days.items():
    print(f"Day {day}: {prices}")
