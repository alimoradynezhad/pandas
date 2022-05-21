import pandas as pd
path = "deta.xlsx"
df = pd.read_excel(path)
#print(df)
for index, row in enumerate(df.values[:50]):
    if row[2] == 26:
        print(row)
        sumation = row[2] + 5
        print(sumation)

