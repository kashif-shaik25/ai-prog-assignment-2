This program is a Simple Reflex Agent that processes air quality data. It reads PM 2.5 values from a CSV file, applies a set of "if-then" rules based on environmental safety standards, and outputs the corresponding AQI.




Agent Components
Sensors: Reads PM2.5 data from a CSV file.

Logic: Maps data to AQI categories using fixed thresholds.

Actuators: Prints the AQI status to the console.

Why it is a Reflex Agent?
This agent acts only on the current percept. It does not use historical data or internal state to make decisions. It follows a direct condition-action rule set.

Using Custom Data
To use a custom CSV file, we would need to modify these two lines in the script:

Header Name: Change 'pm25' to match the column name:
return [float(row['COLUMN_NAME']) for row in reader]

File Name: Change 'sensor_data.csv' to the filename:
agent.run('YOUR_FILE_NAME.csv')
