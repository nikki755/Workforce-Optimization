import pandas as pd
import matplotlib.pyplot as plt
# Load the tracking data from the CSV file
tracking_data = pd.read_csv('tracking_data.csv')

# Convert the 'Timestamp' column to datetime objects
tracking_data['Timestamp'] = pd.to_datetime(tracking_data['Timestamp'])

# Group the data by direction (Up or Down) and resample by 15-minute intervals
data_up = tracking_data[tracking_data['Direction'] == 'Up']
data_down = tracking_data[tracking_data['Direction'] == 'Down']

data_up = data_up.set_index('Timestamp').resample('15T').count()
data_down = data_down.set_index('Timestamp').resample('15T').count()

# Fill missing time intervals with 0 counts
data_up = data_up.fillna(0)
data_down = data_down.fillna(0)

# Calculate KPIs
data_up['Customer Influx'] = data_up['Direction']
data_down['Customer Outflow'] = data_down['Direction']
data_up['Customer Outflow'] = data_down['Customer Outflow']

# Calculate Net Customer Traffic and Conversion Rate
data_up['Net Customer Traffic'] = data_up['Customer Influx'] - data_up['Customer Outflow']
data_up['Conversion Rate'] = data_up['Customer Outflow'] / data_up['Customer Influx']

# Create line plots to visualize KPIs
plt.figure(figsize=(12, 6))
plt.plot(data_up.index, data_up['Customer Influx'], label='Customer Influx', marker='o')
plt.plot(data_up.index, data_up['Customer Outflow'], label='Customer Outflow', marker='o')
plt.plot(data_up.index, data_up['Net Customer Traffic'], label='Net Customer Traffic', marker='o')
plt.plot(data_up.index, data_up['Conversion Rate'], label='Conversion Rate', marker='o')
plt.title('Store Performance Metrics')
plt.xlabel('Time')
plt.ylabel('Count / Rate')
plt.legend()
plt.grid(True)
plt.show()
