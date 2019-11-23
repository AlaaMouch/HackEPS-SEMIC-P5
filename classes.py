ProductDict = {}
class Product:
	container = ProductDict
	def __init__(self, product_id, sku, product_description, price_cost, price_sale):
		self.product_id = product_id
		self.sku = sku
		self.product_description = product_description
		self.price_cost = price_cost
		self.price_sale = price_sale
		if product_id not in self.container:
			self.container[product_id] = self
		else:
			print("Product with primary id {id} already in database!".format(id=product_id))


CountryDict = {}
class Country:
	container = CountryDict
	def __init__(self, country_id, country_full, telephone_countrycode):
		self.country_id = country_id
		self.country_full = country_full
		self.telephone_countrycode = telephone_countrycode
		if country_id not in self.container:
			self.container[country_id] = self
		else:
			print("Country with primary id {id} already in database!".format(id=country_id))


CustomerDict = {}
class Customer:
	container = CustomerDict
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
		if customer_id not in self.container:
			self.container[customer_id] = self
		else:
			print("Customer with primary id {id} already in database!".format(id=customer_id))

BillDict = {}
class Bill:
	container = BillDict
	def __init__(self, bill_id, bill_number, bill_date, customer_id, discount, soon_payment, shipping_amount):
		self.bill_id = bill_id
		self.bill_number = bill_number
		self.bill_date = bill_date
		self.customer_id = customer_id
		self.discount = discount
		self.soon_payment = soon_payment
		self.shipping_amount = shipping_amount
		if bill_id not in self.container:
			self.container[bill_id] = self
		else:
			print("Bill with primary id {id} already in database!".format(id=bill_id))

BillItemDict = {}
class BillItem:
	container = BillItemDict
	def __init__(self, bill_item_id, bill_id, product_id, units, price, discount_1, discount_2):
		self.bill_item_id = bill_item_id
		self.bill_id = bill_id
		self.product_id = product_id
		self.units = units
		self.price = price
		self.discount_1 = discount_1
		self.discount_2 = discount_2
		if bill_item_id not in self.container:
			self.container[bill_item_id] = self
		else:
			print("BillItem with primary id {id} already in database!".format(id=bill_item_id))
