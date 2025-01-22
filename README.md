
# Electric Motor Assembly Dashboard

This project simulates and visualizes data for an electric motor assembly line. It generates simulated production data, analyzes key performance indicators (KPIs), and saves visualizations using Python libraries. The project also serves as a foundation for AWS Quicksight dashboards, providing deeper insights into the performance of the assembly line.

## Features

- **Simulated Data Generation**: Randomly generates data related to motor assembly operations.
- **Data Analysis**: Analyzes key metrics such as assembly time, efficiency, and defect rates.
- **Visualization**: Generates plots to visualize motor type distribution, efficiency ratings, and other production insights.
- **Output**: Saves the generated data and visualizations to CSV and PNG files.

## Requirements

- **Python 3.x**
- **Libraries**:
  - `pandas`: For data manipulation and storage.
  - `matplotlib`: For generating visualizations.
  
## Installation Instructions

Follow the steps below to set up the project on your local machine.

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd electric-motor-assembly-dashboard

### 2. Install dependencies

Use the requirements.txt file to install the necessary dependencies:

```bash
pip install -r requirements.txt


## Project Structure

electric-motor-assembly-dashboard/
│
├── data/               # Simulated data files
├── dashboards/         # Saved visualizations (e.g., screenshots)
├── scripts/            # Python scripts for data processing
├── notebooks/          # Jupyter notebooks (optional)
├── src/                # Code for backend simulation
│   ├── data_generator.py  # Script to generate simulated data
│   └── analysis.py       # Script for analysis and visualization
├── README.md           # Project overview and setup instructions
├── LICENSE             # Optional license for the project
└── requirements.txt    # List of dependencies

## How to Run

### 1. Generate Simulated Data
Run the data_generator.py script to generate simulated production data:

python src/data_generator.py

This script will create a CSV file called Electric_Motor_Production_Data.csv in the data/ folder, containing 100 rows of simulated data about motor assembly operations. It includes columns such as:

Motor Type: The type of motor (A, B, or C).
Assembly Time (min): Time taken to assemble each motor (in minutes).
Efficiency Rating (%): The efficiency rating of the motor (as a percentage).
Defect Rate (%): The defect rate for the assembly line (as a percentage).
Production Date: The date the motor was assembled.

### 2. Run the Data Analysis Script

Next, run the analysis.py script to analyze the data and create visualizations:

python src/analysis.py

This script will:

Load the generated data from Electric_Motor_Production_Data.csv.
Perform analysis, including calculating the distribution of motor types, average efficiency, etc.
Save the visualizations in the dashboards/ folder, including PNG images like motor_type_distribution.png.

### 3. Visualizations
After running the analysis script, you can find the generated visualizations in the dashboards/ folder. These images include:

- Distribution of motor types.
- Efficiency rating distribution.
- Defect rate trends.

You can modify the analysis.py script to include additional visualizations or adjust the existing ones based on your needs.

### Expected Outputs
- Generated Data: A CSV file Electric_Motor_Production_Data.csv in the data/ folder containing the simulated production data.
- Visualizations: PNG images saved in the dashboards/ folder, which can be used for insights and presentations.
- Analysis Reports: Visual insights about the assembly line performance, motor type distribution, defect rates, and efficiency.

### Example Outputs

Motor Type    Assembly Time (min)    Efficiency Rating (%)    Defect Rate (%)    Production Date
A             42                      85                       3.2                2024-01-15
B             36                      90                       1.4                2024-02-20
