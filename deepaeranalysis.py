import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# Extract month and year for deeper analysis
data['Month'] = data['Timestamp'].dt.month
data['Year'] = data['Timestamp'].dt.year

# Calculate monthly averages
monthly_avg = data.groupby(['Year', 'Month']).agg({
    'Customer Influx': 'mean',
    'Customer Outflow': 'mean',
    'Net Customer Traffic': 'mean',
    'Conversion Rate': 'mean'
}).reset_index()

# Visualize the data
plt.figure(figsize=(16, 10))
sns.set(style="whitegrid")

plt.subplot(2, 2, 1)
sns.lineplot(data=monthly_avg, x='Year', y='Customer Influx', hue='Month', marker='o')
plt.title('Monthly Customer Influx Over Time')

plt.subplot(2, 2, 2)
sns.lineplot(data=monthly_avg, x='Year', y='Customer Outflow', hue='Month', marker='o')
plt.title('Monthly Customer Outflow Over Time')

plt.subplot(2, 2, 3)
sns.lineplot(data=monthly_avg, x='Year', y='Net Customer Traffic', hue='Month', marker='o')
plt.title('Monthly Net Customer Traffic Over Time')

plt.subplot(2, 2, 4)
sns.lineplot(data=monthly_avg, x='Year', y='Conversion Rate', hue='Month', marker='o')
plt.title('Monthly Conversion Rate Over Time')

plt.tight_layout()
plt.show()
