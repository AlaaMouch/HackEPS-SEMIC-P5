import math
import sys
from decimal import Decimal as dec, ROUND_DOWN

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
	return val.quantize(dec('.01'), rounding=ROUND_DOWN)

def apply_percentage(val, percentage):
	return val*percentage

num_dec = 2
reverse_sort = False
sum = dec(0.0)
sum_s = dec(0.0)

values = []
values_s = []
for bill_id in BillDict.keys():
	bill_instance = BillDict[bill_id]

	values_p = []
	values_p_s = []
	for bill_item_instance in bill_instance.bill_items:
		cost = bill_item_instance.units
		cost *= bill_item_instance.price
		cost = apply_percentage(cost, bill_item_instance.discount_2)
		cost = apply_percentage(cost, bill_item_instance.discount_1)

		cost_s = bill_item_instance.units
		cost_s *= bill_item_instance.price
		cost_s = round_dec(apply_percentage(cost_s, bill_item_instance.discount_1), num_dec)
		cost_s = round_dec(apply_percentage(cost_s, bill_item_instance.discount_2), num_dec)

		values_p.append(cost)
		values_p_s.append(cost_s)

	partial = dec(0.0)
	partial_s = dec(0.0)

	values_p.sort(reverse=reverse_sort)
	values_p_s.sort(reverse=reverse_sort)
	for cost in values_p:     partial += cost
	for cost_s in values_p_s: partial_s += cost_s

	partial = apply_percentage(partial, bill_instance.soon_payment)
	partial = apply_percentage(partial, bill_instance.discount)

	partial_s = round_dec(apply_percentage(partial_s, bill_instance.discount), num_dec)
	partial_s = round_dec(apply_percentage(partial_s, bill_instance.soon_payment), num_dec)

	values.append(partial)
	values_s.append(partial_s)

values.sort(reverse=reverse_sort)
values_s.sort(reverse=reverse_sort)
for cost in values:     sum += cost
for cost_s in values_s: sum_s += cost_s

print("       sum: {}".format(float(sum)))
print("    sliced: {}".format(float(sum_s)))
print("      diff: {}".format(float(abs(sum_s - sum))))
print()

expected_sum = dec(1392964.84)
print("  expected: {}".format(expected_sum))
print("      diff: {}".format(expected_sum - sum))
print()

expected_sum_s = dec(1392960.00)
print("expected_s: {}".format(expected_sum_s))
print("    diff_s: {}".format(expected_sum_s - sum_s))
