import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
DATA_FILE = 'data/Electric_Motor_Production_Data.csv'
DASHBOARD_FOLDER = r'F:\Projects\electric-motor-assembly-dashboard\dashboards'  # Updated path

# Ensure the dashboards/ directory exists
os.makedirs(DASHBOARD_FOLDER, exist_ok=True)

def load_data(file_path):
    """Loads production data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None

def plot_motor_type_distribution(data):
    """Plots the distribution of motor types."""
    motor_counts = data['Motor Type'].value_counts()
    motor_counts.plot(kind='bar', color=['skyblue', 'orange', 'green'], alpha=0.7)
    plt.title('Distribution of Motor Types')
    plt.xlabel('Motor Type')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    output_path = os.path.join(DASHBOARD_FOLDER, 'motor_type_distribution.png')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Motor type distribution saved at: {output_path}")

def plot_efficiency_distribution(data):
    """Plots the efficiency rating distribution."""
    data['Efficiency Rating (%)'].plot(kind='hist', bins=10, color='purple', alpha=0.7)
    plt.title('Efficiency Rating Distribution')
    plt.xlabel('Efficiency Rating (%)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    output_path = os.path.join(DASHBOARD_FOLDER, 'efficiency_distribution.png')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Efficiency distribution saved at: {output_path}")

def plot_defect_rate_trends(data):
    """Plots defect rate trends over time."""
    data['Production Date'] = pd.to_datetime(data['Production Date'])
    data.sort_values('Production Date', inplace=True)
    plt.plot(data['Production Date'], data['Defect Rate (%)'], marker='o', linestyle='-', color='red', alpha=0.8)
    plt.title('Defect Rate Trends Over Time')
    plt.xlabel('Production Date')
    plt.ylabel('Defect Rate (%)')
    plt.xticks(rotation=45)
    plt.grid(axis='both', linestyle='--', alpha=0.6)
    output_path = os.path.join(DASHBOARD_FOLDER, 'defect_rate_trends.png')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"Defect rate trends saved at: {output_path}")

def main():
    # Load data
    data = load_data(DATA_FILE)
    if data is None:
        return
    
    # Generate and save visualizations
    plot_motor_type_distribution(data)
    plot_efficiency_distribution(data)
    plot_defect_rate_trends(data)

if __name__ == "__main__":
    main()
