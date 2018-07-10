import json

data = json.load(open('data.json'))
data = {int(year): names for year, names in data.items()}
interval = 30
for year, names in data.items():
    if year + interval in data:
        names2 = data[year + interval]
        common = (set(names['f']) & set(names2['f'])) | (set(names['m']) & set(names2['m']))
        print(year, year+interval, len(common), *common)
