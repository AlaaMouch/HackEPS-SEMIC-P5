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
            #unit_price -= float(row['discount1'])
            #unit_price -= float(row['discount2'])
            unit_price *= (1 - (np.double(row['discount1']) / 100.0))
            unit_price *= (1 - (np.double(row['discount2']) / 100.0))
            #unit_price *= (1 - max(np.double(row['discount1']), np.double(row['discount2'])) / 100.0)
            #unit_price *= (1 - (np.double(row['discount1']) + np.double(row['discount2'])) / 100.0)

            cum_price += unit_price * np.double(row['units'])

        #cum_price *= (1 - (- np.double(value['shippingamount']) + np.double(value['discount']) + np.double(value['soonpayment'])) / 100.0)
        #cum_price *= (1 + np.double(value['shippingamount']) / 100.0)
        cum_price *= (1 - np.double(value['soonpayment']) / 100.0)
        #cum_price *= (1 - (np.double(value['discount']) + np.double(value['soonpayment'])) / 100.0)
        cum_price *= (1 - np.double(value['discount']) / 100.0)
        #cum_price -= float(value['discount'])
        #cum_price -= float(value['soonpayment'])


        #cum_price *= (1 - (np.double(value['discount']) + np.double(value['soonpayment'])) / 100.0)
        cum_price += (np.double(value['shippingamount']))
        #cum_price *= (1 + (np.double(value['shippingamount'])) / 100.0)

        floor_price += np.double('%.1f'%(cum_price))
        price += cum_price

    print(price)
    print(floor_price)
    print(price - floor_price)