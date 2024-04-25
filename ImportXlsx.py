import tablib

with open('data.xlsx', 'rb') as f:
    data = tablib.Dataset().load(f, format='xlsx')

print("First few lines of data:")
print(data[:5])
