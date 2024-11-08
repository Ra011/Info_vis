import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from openpyxl import load_workbook

base_file_path = "C:/Users/Student/OneDrive/Documents/Docs2/uni/year 3/semester 1/COMP3736 Information Visualization/cw/data/transposed_seasonal_absence_data_"
file_extension = ".xlsx"
existing_file_path = "C:/Users/Student/OneDrive/Documents/Docs2/uni/year 3/semester 1/COMP3736 Information Visualization/cw/data/response_data.xlsx"

response_data = []

# Function to display the graph
def display_graph(graph_data, graph_number):
    # Create the scatter plot for each graph
    semesters = ['Autumn', 'Spring', 'Summer']
    values = graph_data[semesters].values.flatten()
    semester_labels = [semester for semester in semesters for _ in range(len(graph_data))]

    # Plot the graph
    plt.figure(figsize=(8, 6))
    plt.scatter(semester_labels, values, color='blue')
    plt.xlabel("Semester")
    plt.ylabel("Attendance %")
    plt.title(f"Graph {graph_number}: Attendance by Semester")
    plt.show(block=False)  # Display graph and allow user input at same time

    start_time = time.time()
    
    # Get user input and validate
    while True:
        user_input = input("Enter your response (1, 2, or 3): ")
        if user_input in ["1", "2", "3"]:
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
    
    # Record response and time
    response_time = time.time() - start_time
    response_data.append([graph_number, user_input, response_time])

    plt.close()
    blank_screen()

def blank_screen():
    # Create a blank figure
    plt.figure(figsize=(8, 6))
    plt.axis('off')  
    plt.show(block=False)
    time.sleep(1)  # Display blank screen for 1 sec
    plt.close()

#intro message
print("""
Welcome to the experiment, and thank you for helping us out!

In this experiment, you will be shown a series of graphs. Each graph displays the average attendance in 10 different schools across the Autumn, Spring, and Summer semesters.

For each graph, you will be asked to identify which semester has the highest average attendance based on your observation. 

To enter your response, type:
- '1' for Autumn
- '2' for Spring
- '3' for Summer
""")


while True:
    user_confirmation = input("Please type '1' to confirm that you understand and are ready to begin:")
    if user_confirmation == "1":
        break
    else:
        print("Invalid input. Please enter 1 to confirm.")

#run experiment
for i in range(1, 11):
    file_path = f"{base_file_path}{i}{file_extension}"
    # Read the data from each Excel file
    df = pd.read_excel(file_path)
    display_graph(df, i)

try:
    # Open results excel file
    workbook = load_workbook(existing_file_path)
    sheet = workbook.active
    # Find next empty row 
    next_row = sheet.max_row + 1
    # Add an empty row
    sheet.append([])
    # Add data
    for entry in response_data:
        sheet.append(entry)

    workbook.save(existing_file_path)
    print("Responses saved")

except FileNotFoundError:
    # If the file does not exist, create it and write the headers and data
    response_df = pd.DataFrame(response_data, columns=["Graph", "Response", "Response Time"])
    response_df.to_excel(existing_file_path, index=False)
    print("File not found. A new file has been created")
