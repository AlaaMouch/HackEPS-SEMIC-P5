class Product:
	def __init__(self, product_id, sku, product_description, price_cost, price_sale):
		self.product_id = product_id
		self.product_description = product_description
		self.price_cost = price_cost
		self.price_sale = price_sale

class Country:
	def __init__(self, country_id, country_full, telephone_countrycode):
		self.country_id = country_id
		self.country_full = country_full
		self.telephone_countrycode = telephone_countrycode

class Customer:
	def __init__(self, customer_id, company, national_id, customer_name, street_address, city, state, zipcode, country_id, email_address, telephone_number):
		self.customer_id = customer_id
		self.company = company
		self.national_id = national_id
		self.customer_name = customer_name
		self.street_address = street_address
		self.city = city
		self.state = state
		self.zipcode = zipcode
		self.country_id = country_id
		self.email_address = email_address
		self.telephone_number = telephone_number

class Bill:
	def __init__(self, bill_id, bill_number, bill_date, customer_id, discount, soon_payment, shipping_amount)
		self.bill_id = bill_id
		self.bill_number = bill_number
		self.bill_date = bill_date
		self.customer_id = customer_id
		self.discount = discount
		self.soon_payment = soon_payment
		self.shipping_amount = shipping_amount

class BillItem:
	def __init__(self, bill_item_id, bill_id, product_id, units, price, discount_1, discount_2):
		self.bill_item_id = bill_item_id
		self.bill_id = bill_id
		self.product_id = product_id
		self.units = units
		self.price = price
		self.discount_1 = discount_1
		self.discount_2 = discount_2



