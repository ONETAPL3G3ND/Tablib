import tablib

data = tablib.Dataset()
data.headers = ['Name', 'Age', 'Country']
data.append(['John', 30, 'USA'])
data.append(['Alice', 25, 'Canada'])
data.append(['Bob', 35, 'UK'])

csv_data = data.export('csv')
print(csv_data)
