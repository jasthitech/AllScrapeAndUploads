# import numpy as np
# import pandas as pd

# # Historical data
# data = {
#     'Date': [
#         '09/29/2023', '09/28/2023', '09/27/2023', '09/26/2023', '09/25/2023',
#         '09/22/2023', '09/21/2023', '09/20/2023', '09/19/2023', '09/18/2023',
#         '09/15/2023', '09/14/2023', '09/13/2023', '09/12/2023', '09/11/2023',
#         '09/08/2023', '09/07/2023', '09/06/2023', '09/05/2023', '09/04/2023',
#         '09/01/2023', '08/31/2023', '08/30/2023'
#     ],
#     'Price': [
#         1848.31, 1864.56, 1874.70, 1900.49, 1915.66,
#         1924.99, 1919.57, 1929.68, 1930.94, 1933.14,
#         1923.57, 1910.32, 1906.30, 1913.26, 1921.66,
#         1917.81, 1919.19, 1916.28, 1925.81, 1938.19,
#         1938.80, 1939.74, 1942.24
#     ]
# }

# df = pd.DataFrame(data)
# df['Date'] = pd.to_datetime(df['Date'])
# df.set_index('Date', inplace=True)

# # Calculate average daily change and standard deviation
# average_daily_change = np.mean(df['Price'].pct_change().dropna())
# std_dev_daily_change = np.std(df['Price'].pct_change().dropna())

# # Simulate future daily changes
# num_days = 30
# simulated_changes = np.random.normal(average_daily_change, std_dev_daily_change, num_days)

# # Construct future price path
# future_prices = [df['Price'].iloc[-1]]

# for change in simulated_changes:
#     future_prices.append(future_prices[-1] * (1 + change))

# # Display the simulated future prices
# print(future_prices)
#****************************************************************

import numpy as np
import pandas as pd

# Historical data
data = {
    'Date': [
        '08/30/2023', '08/29/2023', '08/28/2023', '08/25/2023', '08/24/2023',
        '08/23/2023', '08/22/2023', '08/21/2023', '08/18/2023', '08/17/2023',
        '08/16/2023', '08/15/2023', '08/14/2023', '08/11/2023', '08/10/2023',
        '08/09/2023', '08/08/2023', '08/07/2023', '08/04/2023', '08/03/2023',
        '08/02/2023', '08/01/2023', '07/31/2023', '07/28/2023', '07/27/2023',
        '07/26/2023', '07/25/2023', '07/24/2023', '07/21/2023', '07/20/2023',
        '07/19/2023', '07/18/2023', '07/17/2023', '07/14/2023', '07/13/2023',
        '07/12/2023', '07/11/2023', '07/10/2023', '07/07/2023', '07/06/2023',
        '07/05/2023', '07/04/2023', '07/03/2023', '06/30/2023', '06/30/2023',
        '06/29/2023', '06/28/2023', '06/27/2023', '06/26/2023', '06/23/2023',
        '06/22/2023', '06/21/2023', '06/20/2023', '06/19/2023', '06/16/2023',
        '06/15/2023', '06/14/2023', '06/13/2023', '06/12/2023', '06/09/2023',
        '06/08/2023', '06/07/2023', '06/06/2023', '06/05/2023', '06/02/2023',
        '06/01/2023', '05/31/2023', '05/30/2023', '05/29/2023', '05/26/2023',
        '05/25/2023', '05/24/2023', '05/23/2023', '05/22/2023', '05/19/2023',
        '05/18/2023', '05/17/2023', '05/16/2023', '05/15/2023', '05/12/2023',
        '05/11/2023', '05/10/2023', '05/09/2023', '05/08/2023', '05/05/2023',
        '05/04/2023', '05/03/2023', '05/02/2023', '05/01/2023', '04/28/2023',
        '04/27/2023', '04/26/2023', '04/25/2023', '04/24/2023', '04/21/2023',
        '04/20/2023', '04/19/2023', '04/18/2023', '04/17/2023', '04/14/2023',
        '04/13/2023', '04/12/2023', '04/11/2023', '04/10/2023', '04/07/2023',
        '04/06/2023', '04/05/2023', '04/04/2023', '04/03/2023', '03/31/2023',
        '03/30/2023', '03/29/2023', '03/28/2023', '03/27/2023', '03/24/2023',
        '03/23/2023', '03/22/2023', '03/21/2023', '03/20/2023', '03/17/2023',
        '03/16/2023', '03/15/2023', '03/14/2023', '03/13/2023', '03/10/2023',
        '03/09/2023', '03/08/2023', '03/07/2023', '03/06/2023', '03/03/2023',
        '03/02/2023', '03/01/2023', '02/28/2023', '02/27/2023', '02/24/2023',
        '02/23/2023', '02/22/2023', '02/21/2023', '02/20/2023', '02/17/2023',
        '02/16/2023', '02/15/2023', '02/14/2023', '02/13/2023', '02/10/2023',
        '02/09/2023', '02/08/2023', '02/07/2023', '02/06/2023', '02/03/2023',
        '02/02/2023', '02/01/2023', '01/31/2023', '01/30/2023', '01/27/2023',
        '01/26/2023', '01/25/2023', '01/24/2023', '01/23/2023', '01/20/2023',
        '01/19/2023', '01/18/2023', '01/17/2023', '01/16/2023', '01/13/2023',
        '01/12/2023', '01/11/2023', '01/10/2023', '01/09/2023', '01/06/2023',
        '01/05/2023', '01/04/2023', '01/03/2023', '01/02/2023'
    ],
    'Price': [
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
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate average daily change and standard deviation
average_daily_change = np.mean(df['Price'].pct_change().dropna())
std_dev_daily_change = np.std(df['Price'].pct_change().dropna())

# Simulate future daily changes
num_days = 30
simulated_changes = np.random.normal(average_daily_change, std_dev_daily_change, num_days)

# Construct future price path
future_prices = [df['Price'].iloc[-1]]

for change in simulated_changes:
    future_prices.append(future_prices[-1] * (1 + change))

# Display the simulated future prices
print(future_prices)

#

#****************************************************

# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# # Historical prices
# prices = [
#         1942.24, 1937.12, 1919.66, 1914.53, 1916.60,
#         1914.31, 1897.00, 1893.94, 1888.19, 1888.89,
#         1891.76, 1901.56, 1907.90, 1913.32, 1912.06,
#         1914.59, 1924.82, 1936.39, 1941.62, 1933.74,
#         1933.56, 1944.08, 1964.19, 1959.20, 1944.99,
#         1972.10, 1964.58, 1954.51, 1960.23, 1969.62,
#         1976.74, 1978.71, 1954.74, 1954.93, 1960.19,
#         1957.09, 1931.99, 1924.99, 1924.28, 1910.80,
#         1917.32, 1925.09, 1921.43, 1919.57, 1919.57,
#         1908.15, 1907.42, 1913.35, 1922.85, 1921.36,
#         1913.52, 1932.26, 1935.91, 1950.12, 1957.36,
#         1957.65, 1942.99, 1943.33, 1956.92, 1960.60,
#         1967.76, 1939.63, 1962.85, 1961.45, 1947.63,
#         1977.88, 1962.30, 1959.14
#     ]

# # Check the length of 'Price' array
# print("Length of 'Price':", len(prices))

# # Create DataFrame
# df = pd.DataFrame({'Price': prices})

# # Add features for prediction (e.g., lagged prices)
# df['Price_Lag1'] = df['Price'].shift(1)
# df['Price_Lag2'] = df['Price'].shift(2)
# df['Price_Lag3'] = df['Price'].shift(3)

# # Drop missing values created by lagging
# df = df.dropna()

# # Separate features (X) and target (y)
# X = df[['Price_Lag1', 'Price_Lag2', 'Price_Lag3']]
# y = df['Price']

# # Create and train the model
# model = LinearRegression()
# model.fit(X, y)

# # Predict prices for the next 30 days
# next_days = 30
# last_prices = prices[-3:]  # Last three prices from the historical data

# predictions = []
# for _ in range(next_days):
#     next_price = model.predict([last_prices])[0]
#     predictions.append(next_price)
#     last_prices = [next_price] + last_prices[:-1]

# # Print predicted prices
# print("Predicted Prices for the Next 30 Days:")
# for i, price in enumerate(predictions, start=1):
#     print(f"Day {i}: {price:.2f}")
