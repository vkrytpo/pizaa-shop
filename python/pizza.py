import tkinter as tk
from tkinter import messagebox
from tkinter import *
import re;
mobilePattern = re.compile("[0-9]{10}")

win = tk.Tk()
win.geometry('600x600')
win.winfo_toplevel().title("Pizza Shop")

class Pizza():
    def __init__(self,size,price,toppings):
        self.size = size
        self.price = price
        self.toppings = toppings

class Customer():
    def __init__(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address

class Order():
    def __init__(self,pizza,customer,delivary):
        self.pizza = pizza
        self.customer = customer
        self.delivary = delivary
        
global address_var
global toppings
toppings = []
global pasta_list
pasta_list = []
global pizza_list
pizza_list = []
global address_var 
address_var = tk.StringVar()
address_label = tk.Label(win, text='Address *', font=('Arial',16))
address_entry = tk.Entry(win, text='Address', textvariable=address_var)

       
def validate_phone(*args):
    global phone
    phone = phone_var.get()
    print ("Phone: " + phone)
    if (not mobilePattern.match(phone)):
        messagebox.showerror('Please enter valid phone number. ')
     
def remove_all_widgets():
    global win
    for widget in win.winfo_children():
        widget.grid_remove()

def create_order_screen():
    pizza_sizes = ["Large"]
    toppings = []
    tk.Label(win, text='Select pizza '+str(len(pizza_list)+1)+' size', font=('Arial',16)).grid(row=2, column=0)        
    global pizza_size_var
    pizza_size_var = tk.StringVar()
    pizza_size_var.set(pizza_sizes[0]) 
    OptionMenu(win, pizza_size_var, *pizza_sizes).grid(row=2, column=1, sticky="nw",pady=30)

    tk.Label(win, text='Select pizza '+str(len(pizza_list)+1)+' Toppings: ', font=('Arial',16)).grid(row=2, column=0)
    tk.Label(win, text='(Maximum 4 allowed)', font=('Arial',14)).grid(row=3, column=0)

    global bacon_var
    bacon_var = tk.StringVar()
    tk.Checkbutton(win, text = "Bacon", variable = bacon_var).grid(row=2,column=1,sticky="nw")

    global olives_var
    olives_var = tk.StringVar()
    tk.Checkbutton(win, text = "Olives", variable = olives_var).grid(row=3,column=1,sticky="nw")

    global ham_var
    ham_var = tk.StringVar()
    tk.Checkbutton(win, text = "Ham", variable = ham_var).grid(row=4,column=1,sticky="nw")

    global mushroom_var
    mushroom_var = tk.StringVar()
    tk.Checkbutton(win, text = "Mushrooms", variable = mushroom_var).grid(row=5,column=1,sticky="nw")

    global pineapple_var
    pineapple_var = tk.StringVar()
    tk.Checkbutton(win, text = "Pineapple", variable = pineapple_var).grid(row=6,column=1,sticky="nw")

    global salami_var
    salami_var = tk.StringVar()
    tk.Checkbutton(win, text = "Salami", variable = salami_var).grid(row=7,column=1,sticky="nw")

    global anchovies_var
    anchovies_var = tk.StringVar()
    tk.Checkbutton(win, text = "Anchovies", variable = anchovies_var).grid(row=8,column=1,sticky="nw")
    
    submitbtn = tk.Button(win, text='Proceed to checkout',font=('Arial',18),command=proceed_to_checkout)
    submitbtn.grid(row=9,column=0,padx=30,pady=50)

    submitbtn = tk.Button(win, text='Add more pizza',font=('Arial',18),command=new_pizza_order)
    submitbtn.grid(row=9,column=1,padx=30,pady=50)

def billing_details_screen():
    
    tk.Label(win, text='Add Personal details', font=('Arial',32)).grid(row=0,column=0, columnspan=2, sticky='nsew',padx=30,pady=30)
    delivery_type = ["Collected","Delivered"] 
    tk.Label(win, text='Select delivary type', font=('Arial',16)).grid(row=1, column=0, sticky="nw",padx=[30,10],pady=10)
    global delivery_type_var
    delivery_type_var = tk.StringVar()
    delivery_type_var.set(delivery_type[0]) 
    OptionMenu(win, delivery_type_var, *delivery_type).grid(row=1, column=1,sticky="nw",padx=[30,10],pady=10)
    delivery_type_var.trace('w', add_address_row)

    global name_var
    name_var = tk.StringVar()
    tk.Label(win, text='Name *', font=('Arial',16)).grid(row=2,column=0, sticky="nw",padx=[30,10],pady=10)
    name_entry = tk.Entry(win, textvariable=name_var)
    name_entry.grid(row=2,column=1,sticky="nw",padx=[30,10],pady=10)

    global phone_var
    phone_var = tk.StringVar()
    tk.Label(win, text='Phone *', font=('Arial',16)).grid(row=3,column=0, sticky="nw",padx=[30,10],pady=10)
    phone_entry = tk.Entry(win, textvariable=phone_var)
    phone_entry.grid(row=3,column=1,sticky="nw",padx=[30,10],pady=10)
    #phone_var.trace('w', validate_phone)
  
  
    submitbtn = tk.Button(win, text='Complete Order',font=('Arial',18),command=submit_order)
    submitbtn.grid(row=5,column=0, sticky="nw",padx=[30,10],pady=10)
    
def create_order_details():
    
    tk.Label(win, text='Your Order details', font=('Arial',32)).grid(row=0, column=0, columnspan=1 ,sticky="nsew",padx=30,pady=10)
    
    order_details_var = tk.StringVar()
    
    scrollbar = Scrollbar(win,orient='vertical')
    scrollbar.grid(row=1,column=1,sticky='nse')
    order_detail_text_widget = tk.Text(win, state='disabled', height=17, width=55, yscrollcommand = scrollbar.set)
    #order_detail_text_widget = tk.Text(win, state='disabled')
    order_detail_text_widget.grid(row=1,column=0,sticky='nsew')
    order_detail = ""
    personal_details = ""
    topping_price = 0
    pizza_price = 0
    print(pizza_list)
    count=len(pizza_list)
    for i, p in enumerate(pizza_list):
        print("i: ",i)
        topping_price += len(p.toppings)
		
        pizza_price += p.price
        
        order_detail += "\n\nPizza "+str(i+1)+" Details: \n\tSize: "+p.size+"\n\tPrice: "+str(p.price)
        if(len(p.toppings) > 0):
            order_detail += "\n\tToppings: "
            for j, t in enumerate(p.toppings):
                print("j: ",j)
                if j != 0:
                    order_detail += ", "
                order_detail += t
        else:
            order_detail += "\n\tToppings: No additional toppings."
    if count ==1:
        pizza_price =12
    elif count ==2:
        pizza_price = 22
    else:
        pizza_price = 10*count
    order_detail_text_widget.config(state='normal')
    order_detail_text_widget.delete(1.0,END)
    order_detail_text_widget.insert(INSERT, str(order_detail))            
    order_detail_text_widget.config(state='disabled')
    scrollbar.config( command = order_detail_text_widget.yview )
    row=3;
    font_size = 16
    tk.Label(win, text="Delivery type: "+delivarytype, font=('Arial',14)).grid(row=3, column=0, sticky="nw",padx=[10,5],pady=[5,1])
    tk.Label(win, text="Name: "+name, font=('Arial',14)).grid(row=4, column=0, sticky="nw",padx=[10,5],pady=3)
    tk.Label(win, text="Phone: "+phone, font=('Arial',14)).grid(row=5, column=0, sticky="nw",padx=[10,5],pady=1)
    if delivarytype == "Delivered":
        tk.Label(win, text="Address: "+address, font=('Arial',14)).grid(row=6, column=0, sticky="nw",padx=[10,10],pady=1)
    total_price = pizza_price+topping_price
    if total_price < 30 and delivarytype == "Delivered":
        total_price+=8
        font_size = 12
        personal_details += "\nTotal price is $"+str(pizza_price+topping_price)+",which is less than $30. \nAdditional $8 delivary fee will be added."
        tk.Label(win, text=personal_details, font=('Arial',14)).grid(row=7, column=0, sticky="nw",padx=[10,10],pady=1)
    tk.Label(win, text="\nTotal price: $"+str(total_price), font=('Arial',16)).grid(row=8, column=0, sticky="nw",padx=[10,10],pady=1)    
    tk.Label(win, text="\nTotal pizza sale: $"+str(pizza_price), font=('Arial',16)).grid(row=8, column=0, sticky="nw",padx=[10,10],pady=1)    
    tk.Label(win, text="\nTotal pasta sale: $0", font=('Arial',16)).grid(row=9, column=0, sticky="nw",padx=[10,1],pady=1)    
    tk.Button(win, text='New Order',font=('Arial',18),command=create_new_order_again).grid(row=10, column=1, sticky="nw",padx=[10,10],pady=1)
def save_pizza_details():
    pizza_size = pizza_size_var.get()
    print ("pizza size: " + pizza_size)

    if pizza_size == "Small":
        price = 5
    elif pizza_size == "Medium":
        price = 8
    else:
        price =12

    print("price: "+ str(price))
    global toppings
    toppings = []

    bacon = bacon_var.get()
    if bacon == '1':
        toppings.append("Bacon")
        print ("Bacon: " + bacon)
    
    olives = olives_var.get()
    if olives == '1':
        toppings.append("Olives")
        print ("Olives: " + olives)
    
    ham = ham_var.get()
    if ham == '1':
        toppings.append("Ham")
        print ("Ham: " + ham)
        
    
    mushroom = mushroom_var.get()
    if mushroom == '1':
        toppings.append("Mushroom")
        print ("Mushroom: " + mushroom)
    
    pineapple = pineapple_var.get()
    if pineapple == '1':
        toppings.append("pineapple")
        print ("pineapple: " + pineapple)
    
    salami = salami_var.get()
    if salami == '1':
        toppings.append("Salami")
        print ("Salami: " + salami)
    
    anchoive = anchovies_var.get()
    if anchoive == '1':
        toppings.append("Anchoives")
        print ("Anchoives: " + anchoive)
    

    if(len(toppings) > 4):
        messagebox.showerror('More topping selected',' Maximum 4 topping allowed!!!')
    else:
        p1 = Pizza(pizza_size,price,toppings)
        pizza_list.append(p1)
        

    print(toppings)
    

def new_pizza_order():
    save_pizza_details()
    print(toppings)
    if(len(toppings) < 5):
        remove_all_widgets()
        create_order_screen()
    
def proceed_to_checkout():
    save_pizza_details()
    print(toppings)
    if(len(toppings) < 5):
        remove_all_widgets()
        billing_details_screen()
    
def submit_order():
    
    delivary_type = delivery_type_var.get()
    print ("delivary_type: " + delivary_type)

    global name
    name = name_var.get()
    print ("Name: " + name)

    global phone
    phone = phone_var.get()
    print ("Phone: " + phone)


    global address
    address = address_var.get()
    print ("Address: " + address)

    global delivarytype
    delivarytype = delivery_type_var.get()

    if delivarytype == "Delivered":
        if(len(name) == 0 or len(phone) == 0 or len(address) == 0):
            messagebox.showerror('Please enter required field.',' Fields marked with * are required fields.')
        else:
            remove_all_widgets()
            create_order_details()
    else:
        if(len(name) == 0 or len(phone) == 0):
            messagebox.showerror('Please enter required field.',' Fields marked with * are required fields.')
        else:
            remove_all_widgets()
            create_order_details()
 
      
def add_address_row(*args):
    if delivery_type_var.get() == "Delivered":
        address_label.grid(row=4,column=0, sticky="nw",padx=[30,10],pady=10)
        address_entry.grid(row=4,column=1,sticky="nw",padx=[30,10],pady=10)
    else:
        #address_entry.destroy()
        address_label.grid_forget()
        address_entry.grid_forget()
        
        #address_label.destroy()
        #print("Deli")
        
def create_new_order_again():
    remove_all_widgets()
    create_order_screen()
        
create_order_screen()
win.mainloop()