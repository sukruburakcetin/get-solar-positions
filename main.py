from pvlib import solarposition
import pandas as pd

# Define the location and time for which we want to find the solar position
latitude = 41.01651532305031
longitude = 28.984844054094197
date_time = '2018-06-03'

# Create a range of times on this date (we'll assume the timezone is for Istanbul, Turkey)
times = pd.date_range(date_time, periods=24, freq='H', tz='Europe/Istanbul')

# Calculate the solar position
solar_positions = solarposition.get_solarposition(times, latitude, longitude)

# Output the results
print(solar_positions.head(24))  # Displaying the solar position data for the entire day

solar_positions.to_csv("solar_positions.csv")