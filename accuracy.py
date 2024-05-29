import numpy as np

def calculate_accuracy(actual, forecast):
    # Mean Absolute Error (MAE)
    mae = np.mean(np.abs(actual - forecast))

    # Mean Squared Error (MSE)
    mse = np.mean((actual - forecast) ** 2)

    # Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mse)

    # Mean Absolute Percentage Error (MAPE)
    mape = np.mean(np.abs((actual - forecast) / actual)) * 100

    return mae, mse, rmse, mape

# Example usage:
actual_values = np.array([2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830])  # Corrected example actual values
forecast_values = np.array([2779, 2777, 2914, 3075, 3021, 3256, 3195, 3302, 3125, 2825, 2606, 2430])  # Example forecast values

mae, mse, rmse, mape = calculate_accuracy(actual_values, forecast_values)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Mean Absolute Percentage Error (MAPE):", mape)

accuracy_percentage = 100 - mape

print("Accuracy:", accuracy_percentage, "%")

#nifty act- 22326, 22326, 22326, 22326, 22326, 22326, 22326, 22326, 22326, 22326, 22326, 22326
# nifty pred- 20800, 20251, 20042, 19650, 19459, 19235, 18834, 18353, 17826, 17929, 17492, 17627

# reliance act - 2931, 2931, 2931, 2931, 2931, 2931, 2931, 2931, 2931, 2931, 2931, 2931
# reliance pred- 2719, 2547, 2400, 2211, 2199, 2344, 2413, 2382, 2185, 2045, 2053, 1951


# tcs act- 3872, 3872, 3872, 3872, 3872, 3872, 3872, 3872, 3872, 3872, 3872, 3872
# tcs pred- 3151, 3081, 2975, 3620, 3601, 3632, 3660, 3598, 3451, 3267, 3110, 2832

# hdfc act- 1509, 1509, 1509, 1509, 1509, 1509, 1509, 1509, 1509, 1509, 1509, 1509
# hdfc pred- 1544, 1537, 1508, 1608, 1647, 1764, 1853, 1885, 1898, 1900, 1948, 1835

# icici act- 1067, 1067, 1067, 1067, 1067, 1067, 1067, 1067, 1067, 1067, 1067, 1067
# icici pred- 839, 835, 891, 976, 982, 1019, 1034, 1024, 1064, 1061, 1038, 991

# hindulivr act- 2220, 2220, 2220, 2220, 2220, 2220, 2220, 2220, 2220, 2220, 2220, 2220
# hindulvr pred- 2724, 2926, 2868, 2506, 2509, 2544, 2620, 2892, 2838, 2874, 2891, 3028

# infy act- 1414, 1414, 1414, 1414, 1414, 1414, 1414, 1414, 1414, 1414, 1414, 1414,
# infy pred- 1424, 1279, 1304, 1298, 1299, 1296, 1260, 1147, 1238, 1177, 1172, 1176

# ITC.NS act- 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425, 425
# ITC.NS pred- 396, 389, 376, 488, 500, 549, 562, 567, 578, 567, 551, 534

# SBIN.NS act- 751, 751, 751, 751, 751, 751, 751, 751, 751, 751, 751, 751
# SBIN.NS pred- 556, 565, 616, 581, 567, 581, 613, 589, 628, 632, 626, 605

# BHARTIARTL.NS act- 1216, 1216, 1216, 1216, 1216, 1216, 1216, 1216, 1216, 1216, 1216, 1216
# BHARTIARTL.NS pred- 783, 803, 831, 963, 924, 930, 940, 918, 919, 878, 851, 826

# BAJFINANCE.NS act- 6945, 6945, 6945, 6945, 6945, 6945, 6945, 6945, 6945, 6945, 6945, 6945
# BAJFINANCE.NS pred- 5437, 5500, 5880, 7424, 7510, 7272, 6997, 6854, 6509, 5883, 5251, 4519

# LT.NS act- 3543, 3543, 3543, 3543, 3543, 3543, 3543, 3543, 3543, 3543, 3543, 3543
# LT.NS pred- 2058, 1991, 1915, 3365, 3244, 3345, 3189, 3099, 2954, 2878, 2919, 2749

# KOTAKBANK.NS act- 1792, 1792, 1792, 1792, 1792, 1792, 1792, 1792, 1792, 1792, 1792, 1792
# KOTAKBANK.NS pred- 1559, 1612, 1680, 1727, 1800, 1763, 1838, 1824, 1853, 1794, 1728, 1592

# ASIANPAINT.NS act- 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830, 2830
# ASIANPAINT.NS pred- 2779, 2777, 2914, 3075, 3021, 3256, 3195, 3302, 3125, 2825, 2606, 2430