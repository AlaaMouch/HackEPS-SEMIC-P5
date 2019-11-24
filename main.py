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

def round_dec(val, num_decimals):
	power_ten = np.power(np.float64(10.0), num_decimals)
	return np.floor(power_ten*val)/power_ten

def apply_percentage(val, percentage):
	hundred = np.float64(100.0)
	return val*((hundred - percentage)/hundred)

num_dec = 2
reverse_sort = True
sum = np.float64(0.0)
sum_s = np.float64(0.0)

values = []
values_s = []
for bill_id in BillDict.keys():
	bill_instance = BillDict[bill_id]

	values_p = [bill_instance.shipping_amount]
	values_p_s = [bill_instance.shipping_amount]
	for bill_item_instance in bill_instance.bill_items:
		cost = bill_item_instance.units * bill_item_instance.price
		cost = apply_percentage(cost, bill_item_instance.discount_1)
		cost = apply_percentage(cost, bill_item_instance.discount_2)

		cost_s = bill_item_instance.units * bill_item_instance.price
		cost_s = round_dec(apply_percentage(cost_s, bill_item_instance.discount_1), num_dec)
		cost_s = round_dec(apply_percentage(cost_s, bill_item_instance.discount_2), num_dec)

		values_p.append(cost)
		values_p_s.append(cost_s)

	partial = np.float64(0.0)
	partial_s = np.float64(0.0)

	values_p.sort(reverse=reverse_sort)
	values_p_s.sort(reverse=reverse_sort)
	for cost in values_p:     partial += cost
	for cost_s in values_p_s: partial_s += cost_s

	partial = apply_percentage(partial, bill_instance.discount)
	partial = apply_percentage(partial, bill_instance.soon_payment)

	partial_s = round_dec(apply_percentage(partial_s, bill_instance.discount), num_dec)
	partial_s = round_dec(apply_percentage(partial_s, bill_instance.soon_payment), num_dec)

	if len(values_p) > 1:   values.append(partial)
	if len(values_p_s) > 1: values_s.append(partial_s)

values.sort(reverse=reverse_sort)
values_s.sort(reverse=reverse_sort)
for cost in values:     sum += cost
for cost_s in values_s: sum_s += cost_s

print("     sum: {}".format(sum))
print("  sliced: {}".format(sum_s))
print("    diff: {}".format(abs(sum_s - sum)))
print()

expected_sum = 1392964.84
print("expected: {}".format(expected_sum))
print("    diff: {}".format(abs(expected_sum - sum)))
print("  diff_s: {}".format(abs(expected_sum - sum_s)))
