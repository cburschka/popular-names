#!/usr/bin/env python3

import json
import argparse
import sys

parser = argparse.ArgumentParser(description="Check for overlap in names over a given interval.")

parser.add_argument("--input", default=sys.stdin, help="Input file (default STDIN)")
parser.add_argument("--interval", type=int, default=30, help="Interval length")
parser.add_argument("--all", action="store_const", const=True, help="Check all years in interval, not just ends.")

def main(args):
    if type(args.input) is str:
        args.input = open(args.input, "r")
    data = json.load(args.input)
    data = {int(year): names for year, names in data.items()}
    interval = args.interval
    for year, names in data.items():
        if year + interval in data:
            x = range(year, year+interval+1) if args.all else (year, year+interval)
            c = lambda g: set.intersection(*(set(data[i][g]) for i in x))
            common = c('m') | c('f')
            print(year, year+interval, len(common), *common)

main(parser.parse_args())
