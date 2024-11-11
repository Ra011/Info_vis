import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel file from the provided file path
file_path = "C:/Users/Student/OneDrive/Documents/Docs2/uni/year 3/semester 1/COMP3736 Information Visualization/cw/data/transposed_seasonal_absence_data_1.xlsx"
df = pd.read_excel(file_path)

# Extract columns for plotting
semesters = ['Autumn', 'Spring', 'Summer']
data = df[semesters].values  # This extracts the numeric values for attendance by semester

# Create heatmap
fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.imshow(data, cmap="YlGnBu", aspect="auto")  # Adjust aspect ratio for better fit

# Add color bar for reference
plt.colorbar(cax)

# Set axis labels and tick labels
ax.set_xticks(np.arange(len(semesters)))
ax.set_xticklabels(semesters, fontsize=11)
ax.set_yticks(np.arange(len(df)))
ax.set_yticklabels(df.index, fontsize=11)  # Assumes row labels are the index

# Add axis labels
plt.xlabel("Semester", fontsize=11)
plt.ylabel("School", fontsize=11)  # Customize label based on data

plt.title("Attendance by Semester", fontsize=13)

plt.show()
