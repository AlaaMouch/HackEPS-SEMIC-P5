import numpy as np
from classes import *

def read_bill_items(path):
    file_txt = open(path, "r")

    for line in [line.replace("\|", " - ") for line in file_txt.readlines() if line != ""]:
        values = line.split("|")

        billitem_id = values[0]
        bill_id = values[1]
        product_id = values[2]
        units = np.float64(values[3])
        price = np.float64(values[4])
        discount_1 = np.float64(values[5])
        discount_2 = np.float64(values[6])

        BillItem(billitem_id, bill_id, product_id, units, price, discount_1, discount_2)


def read_customers(path):
    file_txt = open(path, "r")

    for line in [line.replace("\|", " - ") for line in file_txt.readlines() if line != ""]:
        values = line.split("|")
        customer_id = values[0]
        company = values[1]
        national_id = values[2]
        customer_name = values[3]
        street_address = values[4]
        city = values[5]
        state = values[6]
        zipcode = values[7]
        country_id = values[8]
        email_address = values[9]
        telephone_number = values[10]

        Customer(customer_id, company, national_id, customer_name, street_address, city, state, zipcode, country_id, email_address, telephone_number)


def read_bills(path):
    file_txt = open(path, "r")

    for line in [line.replace("\|", " - ") for line in file_txt.readlines() if line != ""]:
        values = line.split("|")

        bill_id = values[0]
        bill_number = values[1]
        bill_date = values[2]
        customer_id = values[3]
        discount = np.float64(values[4])
        soon_payment = np.float64(values[5])
        shipping_amount = np.float64(values[6])

        Bill(bill_id, bill_number, bill_date, customer_id, discount, soon_payment, shipping_amount)


def read_countries(path):
    file_txt = open(path, "r")

    for line in [line.replace("\|", " - ") for line in file_txt.readlines() if line != ""]:
        values = line.split("|")

        country_id = values[0]
        country_full = values[1]
        telephone_country_code = int(values[2])

        Country(country_id, country_full, telephone_country_code)


def read_products(path):
    file_txt = open(path, "r")

    file_txt_raw = ''.join(file_txt.readlines()).replace("\\\n", " ")
    file_lines = [line.replace("\|", " - ") for line in file_txt_raw.split("\n") if line != ""]

    for line in file_lines:
        values = line.split("|")
        product_id = values[0]
        sku = values[1]
        product_description = values[2]
        price_cost = np.float64(values[3])
        price_sale = np.float64(values[4])

        Product(product_id, sku, product_description, price_cost, price_sale)


def read_dataset(path):
    read_products(path + "/products.txt")
    read_countries(path + "/countries.txt")
    read_customers(path + "/customers.txt")
    read_bills(path + "/bills.txt")
    read_bill_items(path + "/billitems.txt")

