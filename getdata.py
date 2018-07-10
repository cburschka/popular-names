import names
import json

data = {}

def main():
    for year in range(1880, 2018):
        data[year] = names.get_year(year)
    print(json.dumps(data, indent=4))

main()
