import pandas as pd
import matplotlib.pyplot as plt

# Load the tracking data from the CSV file
tracking_data = pd.read_csv('tracking_data.csv')

# Convert the 'Timestamp' column to datetime objects
tracking_data['Timestamp'] = pd.to_datetime(tracking_data['Timestamp'])

# Group by 15-minute intervals and count entries and exits
interval_data = tracking_data.resample('15T', on='Timestamp').agg({'Direction': 'count'})
interval_data.rename(columns={'Direction': 'Count'}, inplace=True)
# Maximum demand during each interval
max_demand = interval_data['Count'].max()

# Desired employee-to-customer ratio
employee_ratio = 1 / 3  # 1 employee for every 10 customers

# Estimate the required number of employees
required_employees = max_demand * employee_ratio
# Plot customer flow and staffing levels
plt.figure(figsize=(12, 6))
plt.plot(interval_data.index, interval_data['Count'], label='Customer Flow', marker='o')
plt.axhline(y=required_employees, color='r', linestyle='--', label='Required Employees')
plt.title('Customer Flow and Staffing Levels')
plt.xlabel('Time Interval')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.show()
