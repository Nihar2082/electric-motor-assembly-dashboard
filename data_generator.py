import os
import pandas as pd
import random
from datetime import datetime, timedelta

# Ensure the data directory exists
output_path = "../data/Electric_Motor_Production_Data.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Simulate the data
data = {
    "Motor Type": [random.choice(["A", "B", "C"]) for _ in range(100)],
    "Assembly Time (min)": [random.randint(10, 50) for _ in range(100)],
    "Efficiency Rating (%)": [random.randint(70, 95) for _ in range(100)],
    "Defect Rate (%)": [round(random.uniform(0, 10), 2) for _ in range(100)],
    "Production Date": [
        (datetime.today() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        for _ in range(100)
    ],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the file
df.to_csv(output_path, index=False)
print(f"File saved as {output_path}")
