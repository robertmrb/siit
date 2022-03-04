import csv
import os
from csv import DictReader

def read_car_from_csv(file_name):
    with open(file_name, 'r') as data:
        dict_data = DictReader(data)
        list_data = list(dict_data)
        print(list_data)
        for row in list_data:
            print(id(row), row)

read_car_from_csv('input.csv')