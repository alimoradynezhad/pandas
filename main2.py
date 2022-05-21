import pandas as pd
import xlsxwriter
path = 'deta.xlsx'
df = pd.read_excel(path)

for index, row in enumerate(df.values[:50]):
    if row[3] == "sim":
        print(row)
        print()
print("---------------------------------------------------")
for col in df.columns:
    print(col)
print("---------------------------------------------------")
for row in df.values[:]:
    if row[0] == 'بهروز':
        print(row)

print("---------------------------------------------------")
for col in df.columns:
    if col == "name":
        print(col)
print("-------------------------------------------------------")
count = 0
for row in df.values[:]:
    if row[0] == 'ali':
        count +=1
        print(row)
print(count)