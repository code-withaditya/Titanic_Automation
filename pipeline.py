import os
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
print("📡 Step 1: Fetching live data...")
df = pd.read_csv(url)
df = df.iloc[350:] 

print("🧼 Step 2: Running data cleaning algorithms...")
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
df['Cabin'] = df['Cabin'].fillna('Unknown')
df = df.dropna(subset=['Embarked'])
df['Sex'] = df['Sex'].str.strip().str.lower()
df['Embarked'] = df['Embarked'].str.strip().str.upper()

current_folder = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
output_path = os.path.join(current_folder, "cleaned_titanic_data.csv")

df.to_csv(output_path, index=False)
print(f"💾 Step 3: Pristine data saved locally to:\n   --> {output_path}")