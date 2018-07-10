#!/usr/bin/env python3

import ssa_names
import json
import argparse
import datetime
import sys

parser = argparse.ArgumentParser()

parser.add_argument("start", type=int, default=1880, help="First year to acquire")
parser.add_argument("end", type=int, default=datetime.datetime.now().year - 1, help="Last year to load")
parser.add_argument("--output", "-o", default=sys.stdout, help="Where to write the JSON data.")

args = parser.parse_args()

def main(args):
    data = {}
    for year in range(args.start, args.end + 1):
        data[year] = ssa_names.get_year(year)
    if type(args.output) is str:
        args.output = open(args.output, 'w')
    json.dump(data, args.output, indent=4)

main(args)
