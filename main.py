import math
import numpy as np
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

def apply_percentage(val, percentage):
	return val*((np.float64(100.0) - np.float64(percentage))/np.float64(100.0))

sum = np.float64(0.0)
sum_s = np.float64(0.0)
for bill_id in BillDict.keys():
	bill_instance = BillDict[bill_id]
	partial = np.float64(0.0)
	partial_s = np.float64(0.0)
	for bill_item_instance in bill_instance.bill_items:
#		product_item = ProductDict[bill_item_instance.product_id]
		cost = bill_item_instance.units
#		cost *= product_item.price_sale
		cost *= bill_item_instance.price
		cost = apply_percentage(cost, bill_item_instance.discount_1)
		cost = apply_percentage(cost, bill_item_instance.discount_2)
		partial += cost

		cost_s = bill_item_instance.units
#		cost_s *= product_item.price_sale
		cost_s *= bill_item_instance.price
		cost_s = round2dec(apply_percentage(cost_s, bill_item_instance.discount_1))
		cost_s = round2dec(apply_percentage(cost_s, bill_item_instance.discount_2))
		partial_s += cost_s
	partial = apply_percentage(partial, bill_instance.discount)
	partial = apply_percentage(partial, bill_instance.soon_payment)
	partial += bill_instance.shipping_amount
	sum += partial

	partial_s = round2dec(apply_percentage(partial_s, bill_instance.discount))
	partial_s = round2dec(apply_percentage(partial_s, bill_instance.soon_payment))
	partial_s += bill_instance.shipping_amount
	sum_s += partial_s

print("     sum: {}".format(sum))
print("  sliced: {}".format(sum_s))
print("    diff: {}".format(abs(sum_s - sum)))
print()

expected_sum = 1392964.84
print("expected: {}".format(expected_sum))
