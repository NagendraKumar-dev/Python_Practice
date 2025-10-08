import pandas as pd

# Read a sample dataset (you can download 'sample.csv' or create one manually)
data = {
    'Name': ['Amit', 'Priya', 'Ravi', 'Kiran', 'Tara', 'John'],
    'Age': [25, 30, 28, 22, 35, None],
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [40000, 55000, None, 48000, 60000, 45000]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# 1️⃣ Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# 2️⃣ Filter employees earning more than 50k
high_salary = df[df['Salary'] > 50000]
print("\nEmployees earning more than 50,000:")
print(high_salary)

# 3️⃣ Group by Department
print("\nAverage Salary by Department:")
print(df.groupby('Department')['Salary'].mean())

# 4️⃣ Save cleaned data
df.to_csv("cleaned_employees.csv", index=False)
print("\nCleaned data saved to cleaned_employees.csv ✅")
