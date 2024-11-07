import matplotlib.pyplot as plt
import time
import numpy as np

# Function to display graph and record response time
def display_graph(graph_data, correct_answer):
    # Create the graph
    plt.plot(graph_data)
    plt.title("Graph - Type 1, 2, or 3")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.show(block=False)  # Display graph without blocking the program

    # Start timing the response
    start_time = time.time()
    
    # Prompt user for input
    user_input = input("Enter your response (1, 2, or 3): ")
    
    # Record time taken for response
    response_time = time.time() - start_time

    # Show a blank screen for a few seconds before the next graph
    plt.close()  # Close the previous graph
    print("Blank screen...wait for the next graph.")
    time.sleep(2)  # Display a blank screen for 2 seconds

# List of graphs and corresponding correct answers (for example)
graphs = [
    (np.sin(np.linspace(0, 10, 100)), '1'),
    (np.cos(np.linspace(0, 10, 100)), '2'),
    (np.tan(np.linspace(0, 10, 100)), '3')
]

# Loop through the graphs and display each one
for graph_data, correct_answer in graphs:
    display_graph(graph_data, correct_answer)
