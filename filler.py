
from classes import *

BillBillItems = {}
for bill_item in BillItemDict:
	if bill_item.bill_id not in BillBillItems:
		BillBillItems[bill_item.bill_id] = []
	BillBillItems[bill_item.bill_id].append(bill_item)