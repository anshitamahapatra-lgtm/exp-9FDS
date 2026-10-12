
import pandas as pd

students = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Anu', 'Ravi', 'Sita'],
    'Course': ['CSE', 'ECE', 'CSE'],
    'Marks': [85, 90, 78]
})

students2 = pd.DataFrame({
    'ID': [4, 5],
    'Name': ['Rahul', 'Priya'],
    'Course': ['ECE', 'CSE'],
    'Marks': [88, 92]
})

print("Original DataFrame:")
print(students)

# 2. Hierarchical Indexing
print("\nHierarchical Indexing:")
hierarchy = students.set_index(['Course', 'ID'])
print(hierarchy)

# 3. Combining DataFrames using concat()
print("\nCombining DataFrames:")
combined = pd.concat([students, students2], ignore_index=True)
print(combined)

# 4. Merging DataFrames using merge()
courses = pd.DataFrame({
    'Course': ['CSE', 'ECE'],
    'Department': ['Computer Science', 'Electronics']
})

print("\nMerging DataFrames:")
merged = pd.merge(students, courses, on='Course')
print(merged)

# 5. Reshaping using stack()
print("\nStacking:")
stacked = students.set_index('ID').stack()
print(stacked)

# 6. Reshaping using unstack()
print("\nUnstacking:")
unstacked = students.set_index('ID').stack().unstack()
print(unstacked)

# 7. Pivoting
print("\nPivot Table:")
pivoted = students.pivot(
    index='Name', columns='Course', values='Marks'
)
print(pivoted)

# 8. Pivot Table with aggregation
print("\nPivot Table with Average Marks:")
pivot_table = students.pivot_table(
    index='Course', values='Marks', aggfunc='mean'
)
print(pivot_table)

# 9. Reshaping using melt()
print("\nMelting DataFrame:")
melted = students.melt(
    id_vars=['ID', 'Name'],
    value_vars=['Course', 'Marks'],
    var_name='Attribute',
    value_name='Value'
)
print(melted)
