import math
import numpy as np

if __name__ == '__main__':
    bill_data = {}
    f = open('codes1.txt', 'r')
    for line in f:
        s_line = line.split('|')
        if s_line[1] not in bill_data:
            bill_data[s_line[1]] = {'bill_items': []}
        bill_data[s_line[1]]['bill_items'].append({'units': s_line[3], 'price': s_line[4], 'discount1': s_line[5], 'discount2': s_line[6]})

    f2 = open('bills.txt', 'r')
    for line in f2:
        s_line = line.split('|')
        if s_line[0] in bill_data:
            bill_data[s_line[0]]['discount'] = s_line[4]
            bill_data[s_line[0]]['soonpayment'] = s_line[5]
            bill_data[s_line[0]]['shippingamount'] = s_line[6]

    price = 0.0
    floor_price = 0.0
    for key, value in bill_data.items():
        cum_price = 0.0
        for row in value['bill_items']:
            unit_price = np.double(row['price'])

            unit_price = (int(unit_price * 100) / 100.0) * (1 - (np.double(row['discount1']) / 100.0))
            unit_price = (int(unit_price * 100) / 100.0) * (1 - (np.double(row['discount2']) / 100.0))

            cum_price += (int(unit_price * 100) / 100.0) * np.double(row['units'])

        cum_price = (int(cum_price * 100) / 100.0) * (1 - np.double(value['discount']) / 100.0)
        cum_price = (int(cum_price * 100) / 100.0) * (1 - np.double(value['soonpayment']) / 100.0)
        cum_price = (int(cum_price * 100) / 100.0) + np.double(value['shippingamount'])

        price += int(cum_price * 100) / 100.0

    print(price)
    print(floor_price)
    print(price - floor_price)