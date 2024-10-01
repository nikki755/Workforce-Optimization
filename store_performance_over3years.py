import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
import matplotlib.dates as mdates

# Generate synthetic data for three years (approximately 36 months)
start_date = pd.to_datetime('2023-11-01 00:00:00')
end_date = start_date + pd.DateOffset(years=3)
date_range = pd.date_range(start_date, end_date, freq='15T')

# Generate synthetic customer influx and outflow data
customer_influx = np.random.randint(5, 15, size=len(date_range))
customer_outflow = np.random.randint(3, 12, size=len(date_range))

# Create a DataFrame for the synthetic data
data = pd.DataFrame({'Timestamp': date_range, 'Customer Influx': customer_influx, 'Customer Outflow': customer_outflow})

# Calculate Net Customer Traffic and Conversion Rate
data['Net Customer Traffic'] = data['Customer Influx'] - data['Customer Outflow']
data['Conversion Rate'] = data['Customer Outflow'] / data['Customer Influx']

# Create a cleaner and more presentable plot
plt.figure(figsize=(12, 6))
plt.plot(data['Timestamp'], data['Customer Influx'], label='Customer Influx', marker='o', linewidth=2)
plt.plot(data['Timestamp'], data['Customer Outflow'], label='Customer Outflow', marker='o', linewidth=2)
plt.plot(data['Timestamp'], data['Net Customer Traffic'], label='Net Customer Traffic', marker='o', linewidth=2)
plt.plot(data['Timestamp'], data['Conversion Rate'], label='Conversion Rate', marker='o', linewidth=2)

# Format date axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.xticks(rotation=45)
plt.title('Store Performance Metrics Over Three Years', fontsize=16)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Count / Rate', fontsize=12)
plt.legend()
plt.grid(True)

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()
