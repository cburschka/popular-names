import json

data = json.load(open('data.json'))
data = {int(year): names for year, names in data.items()}

for year, names in data.items():
    if year + 30 in data:
        names2 = data[year + 30]
        common = (set(names['f']) & set(names2['f'])) | (set(names['m']) & set(names2['m']))
        print(year, year+30, len(common), *common)