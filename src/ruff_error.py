from re import X
import sys
import os

def process_data(  data, options = {}  ):
    target = data["value"]

    if target == None:
        return []

    if options.get("verbose") == True:
        print(f"Processing data: {target}")

    result_list = [ "apple", "banana", "orange", "grape",
                    "peach", "melon"]

    unused_var = 100
    
    x = 10