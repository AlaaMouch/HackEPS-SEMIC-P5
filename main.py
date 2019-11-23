import math
import sys

if len(sys.argv) <= 1:
	print("Not enough arguments! Please input the folder name of the dataset!")
	quit()

from classes import *
from read import read_dataset

dataset_name = sys.argv[1]
read_dataset(dataset_name)

for bill_item_id in BillItemDict.keys():
	bill_item_instance = BillItemDict[bill_item_id]
	BillDict[bill_item_instance.bill_id].bill_items.append(bill_item_instance)

def round2dec(val):
#	return val
	return math.floor(100.0*val)/100.0

sum = 0.0
for bill_id in BillDict.keys():
	bill_instance = BillDict[bill_id]
	partial_sum = 0.0
	for bill_item_instance in bill_instance.bill_items:
#		product_item = ProductDict[bill_item_instance.product_id]
		product_final_cost = 0.0
		product_final_cost += bill_item_instance.units
#		product_final_cost *= product_item.price_sale
		product_final_cost *= bill_item_instance.price
		product_final_cost = round2dec(product_final_cost)
		product_final_cost *= (100.0 - bill_item_instance.discount_1)/100.0
		product_final_cost = round2dec(product_final_cost)
		product_final_cost *= (100.0 - bill_item_instance.discount_2)/100.0
		product_final_cost = round2dec(product_final_cost)
		partial_sum += product_final_cost
	partial_sum *= (100.0 - bill_instance.discount)/100.0
	partial_sum = round2dec(partial_sum)
	partial_sum *= (100.0 - bill_instance.soon_payment)/100.0
	partial_sum = round2dec(partial_sum)
	partial_sum += bill_instance.shipping_amount
	partial_sum = round2dec(partial_sum)
	sum += partial_sum

print(sum)
