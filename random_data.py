import numpy as np
import pandas as pd
import statistics

autumn_data_original = [5.8, 8.0, 7.6]
spring_data_original = [3.3, 7.9, 7.0]
summer_data_original = [5.8, 8.0, 7.6]
# Define the seasonal averages across all years
autumn_mean = np.mean(autumn_data_original)  # Average for Autumn
spring_mean = np.mean(spring_data_original)  # Average for Spring
summer_mean = np.mean(summer_data_original)  # Average for Summer

autumn_sd= statistics.stdev(autumn_data_original)
spring_sd= statistics.stdev(spring_data_original)
summer_sd= statistics.stdev(summer_data_original)
# Define standard deviation for random variation

for i in range(1, 11):  # Loop 10 times
    # Generate 10 random absence rates around each seasonal mean
    autumn_data = np.random.normal(autumn_mean, autumn_sd, 10).clip(0, 12)
    spring_data = np.random.normal(spring_mean, spring_sd, 10).clip(0, 12)
    summer_data = np.random.normal(summer_mean, summer_sd, 10).clip(0, 12)

    # Arrange data in the desired layout
    transposed_data = pd.DataFrame({
        "Autumn": autumn_data,
        "Spring": spring_data,
        "Summer": summer_data
    }, index=[f"Value{i+1}" for i in range(10)])

    # Export to Excel
    file_path = f"C:/Users/Student/OneDrive/Documents/Docs2/uni/year 3/semester 1/COMP3736 Information Visualization/cw/data/transposed_seasonal_absence_data_{i}.xlsx"
    transposed_data.to_excel(file_path)

    print(f"Data saved to {file_path}")
