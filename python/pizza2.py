class Session():
	def __init__(self):
		self.total_pizza=0
		self.total_pasta=0
		
	def add(self,pizza_price,pasta_price):
		self.total_pizza += pizza_price
		self.total_pasta += pasta_price
		
	def display(self):
		print("total pizza sale:" ,self.total_pizza)
		print("total pasta sale:" ,self.total_pasta)
		print("total sale today:" ,self.total_pasta+self.total_pizza)
			
class Pizza():
	def __init__(self,quantity):
		self.quantity = quantity
		self.price=0
		
	def get_price(self ):
		if self.quantity ==1:
			return 12
		if self.quantity ==2:
			return 22
		else:
			return self.quantity*10
			
	def show(self):
		print(self.quantity ," large pizza worth of ",self.price)
    
class Pasta():
	def __init__(self,quantity):
		self.quantity = quantity
		self.price= 0
		
	def get_price(self):
		if self.quantity ==1:
			return 8
		if self.quantity ==2:
			return 15
		else:
			return self.quantity*7
			
	def show(self):
		print(self.quantity ," large pasta worth of ",self.price)
				


class Customer():
    def __init__(self,name,phone,address):
        self.name = name
        self.phone = phone
		
class Order():
    def __init__(self,item_name,quantity,price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

class OrderLine():
	def __init__(self,item_name,quantity,price):
		self.pizza = pizza
		self.customer = customer
		self.delivary = delivary
	
def welcome(s):
	if s:
		s.display()

def buy_option():
	print("1) Buy a large pizza:")
	print("2) Buy a large pasta:")
	c=input("Please choose option: ")
	if c=='1':
		buy_pizza()
	elif c=='2':
		buy_pasta()
	else:
		buy_option()
		
def buy_pizza():
	q = input("Please enter quantiy: ")
	try:
		q = int(q)
		if q==0:
			buy_pizza()
	except:
		buy_pizza()
	p = Pizza(q)
	order = Order('large Pizza',q ,p.get_price())
	pizza_list.append(order)
	return order

def buy_pasta():
	q = input("Please enter quantiy: ")
	try:
		q = int(q)
		if q==0:
			buy_pasta()
	except:
		buy_pasta()
	p = Pasta(q)
	order = Order('large Pasta',q ,p.get_price())
	pasta_list.append(order)
	return order

def main(pizza_price,pasta_price):
	global pizza_list ,pasta_list
	pizza_list=[]
	pasta_list=[]
	sess = Session()
	welcome(sess)
	buy_option()	
	print(pizza_price,pasta_price)
	for pasta in pasta_list:
		pasta_price += pasta.price
		print(pasta.item_name ,pasta.quantity,pasta.price)
		
	for pizza in pizza_list:
		pizza_price += pizza.price
		print(pizza.item_name ,pizza.quantity,pizza.price)
		
	print('checkout: ')
	x= input("press 1 to continue with another purchase..")
	if x=='1':
		main(pizza_price,pasta_price)
	#print(pizza_list ,pasta_list)
global pizza_price,pasta_price
pizza_price=0
pasta_price=0	
main(pizza_price,pasta_price)