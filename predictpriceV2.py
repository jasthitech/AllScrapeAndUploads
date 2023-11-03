import numpy as np
import pandas as pd

# Historical prices
prices = [
    1942.24, 1937.12, 1919.66, 1914.53, 1916.60,
    1914.31, 1897.00, 1893.94, 1888.19, 1888.89,
    1891.76, 1901.56, 1907.90, 1913.32, 1912.06,
    1914.59, 1924.82, 1936.39, 1941.62, 1933.74,
    1933.56, 1944.08, 1964.19, 1959.20, 1944.99,
    1972.10, 1964.58, 1954.51, 1960.23, 1969.62,
    1976.74, 1978.71, 1954.74, 1954.93, 1960.19,
    1957.09, 1931.99, 1924.99, 1924.28, 1910.80,
    1917.32, 1925.09, 1921.43, 1919.57, 1919.57,
    1908.15, 1907.42, 1913.35, 1922.85, 1921.36,
    1913.52, 1932.26, 1935.91, 1950.12, 1957.36,
    1957.65, 1942.99, 1943.33, 1956.92, 1960.60,
    1967.76, 1939.63, 1962.85, 1961.45, 1947.63,
    1977.88, 1962.30, 1959.14
]

# Create a DataFrame
df = pd.DataFrame({'Price': prices})

# Calculate average daily change and standard deviation
average_daily_change = np.mean(df['Price'].pct_change().dropna())
std_dev_daily_change = np.std(df['Price'].pct_change().dropna())

# Simulate future daily changes
num_days = 30
simulated_changes = np.random.normal(average_daily_change, std_dev_daily_change * 50, num_days)

# Construct future price path
future_prices = [df['Price'].iloc[-1]]

for change in simulated_changes:
    future_prices.append(future_prices[-1] * (1 + change / 100))

# Display the simulated future prices
print(future_prices)
