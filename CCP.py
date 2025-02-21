# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"D:\Dhivya Programs\Credit Card Prediction\archive (1)\Application_Data.csv"
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}. Please check the path.")
    exit()

# Display the dataset in an organized tabular format
print("\n--- Displaying First 20 Rows ---")
print(data.head(20))  # Display the first 10 rows for clarity

# Display basic dataset information
print("\n--- Dataset Information ---")
print(data.info())

# Display a summary of the dataset
print("\n--- Dataset Summary ---")
print(data.describe())

# Visualize a heatmap of correlations
print("\n--- Generating Heatmap ---")
plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
correlation_matrix = data.corr()  # Calculate correlations
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Heatmap")
plt.show()

# Save the organized data into a CSV file
output_file = "organized_data_with_heatmap.csv"
data.to_csv(output_file, index=False)
print(f"\nOrganized data saved to '{output_file}'. You can open this file in Excel or any text editor.")
