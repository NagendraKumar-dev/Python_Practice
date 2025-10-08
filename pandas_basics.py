import pandas as pd

# 1️⃣ Create a simple dataset
data = {
    'Name': ['Amit', 'Priya', 'John', 'Neha'],
    'Age': [25, 30, 22, 28],
    'City': ['Mumbai', 'Delhi', 'Chennai', 'Pune']
}

# 2️⃣ Convert dictionary to DataFrame
df = pd.DataFrame(data)
print("Full DataFrame:")
print(df)
print("\n")

# 3️⃣ Access specific columns
print("Names Column:")
print(df['Name'])
print("\n")

# 4️⃣ Filter rows where Age > 25
print("People older than 25:")
print(df[df['Age'] > 25])
print("\n")

# 5️⃣ Add a new column
df['Salary'] = [50000, 60000, 45000, 52000]
print("With new Salary column:")
print(df)
print("\n")

# 6️⃣ Basic statistics
print("Average age:", df['Age'].mean())
print("Maximum salary:", df['Salary'].max())