import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the Excel file from the provided file path
file_path = 'C:/Users/Student/OneDrive/Documents/Docs2/uni/year 3/semester 1/COMP3736 Information Visualization/cw/data/transposed_seasonal_absence_data_1.xlsx'
df = pd.read_excel(file_path)

# Extract columns for plotting
seasons = ['Autumn', 'Spring', 'Summer']
values = df[seasons].values.flatten()
season_labels = [season for season in seasons for _ in range(len(df))]
# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(season_labels, values, color='blue')
plt.xlabel("Season")
plt.ylabel("Value")
plt.title("Values by Season")
plt.show()