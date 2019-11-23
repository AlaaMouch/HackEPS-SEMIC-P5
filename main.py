import sys

if len(sys.argv) <= 1:
	print("Not enough arguments! Please input the folder name of the dataset!")
	quit()

dataset_name = sys.argv[1]

from classes import *
from read import read_dataset

read_dataset(dataset_name)

print(ProductDict)
print(CountryDict)
print(CustomerDict)
print(BillDict)
print(BillItemDict)

