import argparse
import json
from pickle import NONE

DATA_SET_FILE = "converter.json"




class Converter:
    def __init__(self, data_set_file=DATA_SET_FILE):
        with open(data_set_file, "r") as data_set_file:
            self.dataset = json.load(data_set_file)
    
    def find_category(self, to_convert, convert_to):
        for category in iter(self.dataset):
            if to_convert in self.dataset[category]:
                if convert_to in self.dataset[category]:
                    return category
                raise ValueError("Units do not belong to the same physical quantity!")
        raise ValueError("Unit could not be found!")
    
    def convert(self, value, to_convert, convert_to):
        category = self.find_category(to_convert, convert_to)
        
        conversion_val = value / float(self.dataset[category][to_convert])
        conversion_factor = float(self.dataset[category][convert_to])
        return conversion_val * conversion_factor
        
parser = argparse.ArgumentParser()
parser.add_argument("value", type=float)
parser.add_argument("to_convert", type=str)
parser.add_argument("convert_to", type=str)
args = parser.parse_args()
converter = Converter()
try:
    result = converter.convert(args.value, args.to_convert, args.convert_to)
    print(f"{args.value} {args.to_convert} are {result} {args.convert_to}")
except ValueError as error:
    print(error)