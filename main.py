"""
    in this following code the tabulate and term colour python librb ary is not installerd by default 
    so we have to insatll them by running them by running the following commands in the terminal or cmd 
    for tabulate : pip install tabulate
    for term color : pip install termcolor
     
"""


import datetime
from tabulate import tabulate
import getpass
import termcolor


#ya batw customer buy sessoin start hunxa ani hami laptop ko bill print garxam

def customer_buy():
    # Read the contents of the "Stocks.txt" file
    with open("Stocks.txt", "r") as stocks_file:
        existing_stocks = stocks_file.readlines()

    # Print the list of available laptops
    
    print("")
    print("------------------")
    print("Available laptops:")
    
    laptops = []
    for stock_item in existing_stocks:
        item_parts = stock_item.strip().split(", ")
        laptops.append(item_parts[0])
    
    stocks()

    # Prompt the user to select a laptop and quantity to buy
    
    print("")
    while True:
        selected_laptop = input("Enter the name of the laptop you want to buy: ")
        if selected_laptop not in laptops:
            print("Invalid laptop name. Please try again.")
            
        else:
            break
        
    while True:
        selected_quantity = input("Enter the quantity you want to buy: ")
        try:
            if not selected_quantity.isdigit():
                raise ValueError("Invalid quantity! Please enter a number.")

            elif int(selected_quantity) <= 0:
                raise ValueError("Quantity must be greater than zero.")

            break

        except ValueError as e:
            print(str(e))


    # Update the stock in the "Stocks.txt" file
    
    for i, stock_item in enumerate(existing_stocks):
        item_parts = stock_item.strip().split(", ")
        if item_parts[0] == selected_laptop:
            current_stock = int(item_parts[3])
            
            if current_stock < int(selected_quantity):
                print(f"Sorry, we only have {current_stock} {selected_laptop}(s) in stock.")
                return
            
            new_stock = current_stock - int(selected_quantity)
            existing_stocks[i] = f"{item_parts[0]}, {item_parts[1]}, {item_parts[2]}, {new_stock}, {item_parts[4]}, {item_parts[5]}\n"
            
            #Notify user that purchase was successful
            
            print(f"Purchase of {selected_quantity} {selected_laptop}(s) was successful!")
            print("Generating invoices please wait................")
            break

    # Write the updated file contents back to the "Stocks.txt" file
    
    with open("Stocks.txt", "w") as stocks_file:
        stocks_file.writelines(existing_stocks)
         
        # Bill start from here
        customer_name = input("Please enter your name: ")
        with open(customer_name+".txt", "w") as bill_txt:
              
            current_datetime = datetime.datetime.now()
            
        #Format date and time as a string

            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            price_per_unit = int(item_parts[2].strip("$"))
            bill_txt.write("\n")
            vat_amount = 13 / 100
            shipping_cost = 250
        
            # Calculate total price
            total_price = int(selected_quantity) * price_per_unit
            without_vat = int(total_price) + int(shipping_cost)
            semi_final_anount = int(total_price) * (1+float(vat_amount))
            final_amount =  semi_final_anount + shipping_cost
            
            bill_txt.write("**************************************************************\n")
            bill_txt.write("Micro Star Pvt.ltd\n")
            bill_txt.write("**************************************************************\n")
            bill_txt.write("\n")
            bill_txt.write("**************************************************************\n")
            bill_txt.write("\n")
            bill_txt.write("Details.........\n")
            bill_txt.write("Date and Time: {}\n".format(formatted_datetime))
            bill_txt.write("\n")
            bill_txt.write("Name: {}\n".format(customer_name))
            bill_txt.write("Product Name: {}\n".format(selected_laptop))
            bill_txt.write("Quantity: {}\n".format(selected_quantity))
            bill_txt.write("Price of 1 product: ${}\n".format(price_per_unit))
            bill_txt.write("\n")
            bill_txt.write("----------------------------------------------------------------\n")
            bill_txt.write("VAT = 0.13 of total price.\n")
            bill_txt.write("Amount Without Shipping: ${}\n".format(total_price))
            bill_txt.write("Shipping Charge: ${}\n".format(shipping_cost))
            bill_txt.write("Total without vat : ${}\n".format(without_vat))
            bill_txt.write("----------------------------------------------------------------\n")
            bill_txt.write("----------------------------------------------------------------\n")
            bill_txt.write("Total including vat : ${}\n".format(final_amount))
            bill_txt.write("--------------------------------------------------------------\n")
            print("")
            print("invoice generated sucessfully.....")
            

 
def customer_login():
    while True:
        print("")
        print("Dear customer wlecome to our shop.")
        print("what would u like to do today.")
        print("please choose from the option below")
        print("")
        print("1 Show available pcs in stock")
        print("2 Buy laptops.")
        print("3 Rollback to previous state")
        print("4 Exit from our shop")
        print("")
        customer_choice = int(input("-->> "))
        
        if customer_choice == 1:
            print("")
            print("the list of all the available stocks.")
            print("")
            stocks()
            print("")
            
        elif customer_choice == 2:
            print("")
            customer_buy()
            print("")
            
        elif customer_choice == 3:
            print("")
            print("rolling back to the previous state..............")
            break
                
        elif customer_choice == 4:
            print("")
            print("are u sure u want to exit?")
            print("confirmation needed : ")
            print("y or n ")
            print("")
            
            customer_exit_confirmation = input("-->>")
            
            if customer_exit_confirmation == "y":
                print("")
                print("byee have a good day")
                exit()
                
            elif customer_exit_confirmation == "n":
                
                print("")
                print("erors can be a pain in the buttt ")
                print("")
                break
                
            else:
                print("please enter a valid input : ")
                customer_login()
                               
def update_stocks():

    print("")
    print("Welcome to the update stock panel")
    print("")
    product = input("Enter product name: ")
    brand = input("Enter brand: ")
    price = input("Enter price: ")
    stock = input("Enter stock: ")
    processor = input("Enter processor: ")
    graphics = input("Enter graphics: ")

    # Read the contents of the "Stocks.txt" file
    with open("Stocks.txt", "r") as stocks_file:
        existing_stocks = stocks_file.readlines()

    # Check if the item already exists in the "Stocks.txt" file
    
    item_exists = False
    for i, stock_item in enumerate(existing_stocks):
        item_parts = stock_item.strip().split(", ")
        if item_parts[0] == product and item_parts[1] == brand and item_parts[4] == processor and item_parts[5] == graphics:
            existing_stock = int(item_parts[3])
            new_stock = int(stock)
            total_stock = existing_stock + new_stock
            existing_stocks[i] = f"{product}, {brand}, {price}, {total_stock}, {processor}, {graphics}\n"
            item_exists = True
            break
        
        else:
            print("")

    # If the item doesn't exist, add it to the end of the file
    
    if not item_exists:
        existing_stocks.append(f"{product}, {brand}, {price}, {stock}, {processor}, {graphics}\n")
        
    else:
        print("")

    # Write the updated file contents back to the "Stocks.txt" file
    
    with open("Stocks.txt", "w") as stocks_file:
        stocks_file.writelines(existing_stocks)

    print("")
    print("Stocks updated successfully")
    
    with open("FromManufacture.txt", "a") as our_updates:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        our_updates.write("\n")
        manufacurer_name = str(input("enter the name of manufacturer : " ))
        retailer_total = int(price) * int(stock)
        our_updates.write("**************************************************************\n")
        our_updates.write("Micro Star Pvt.ltd\n")
        our_updates.write("**************************************************************\n")
        our_updates.write("\n")
        our_updates.write("**************************************************************\n")
        our_updates.write("\n")
        our_updates.write("Details.........\n")
        our_updates.write("Date and Time: {}\n".format(formatted_datetime))
        our_updates.write("\n")
        our_updates.write("Seller Name: {}\n".format(manufacurer_name))
        our_updates.write("Product Name: {}\n".format(product))
        our_updates.write("Quantity: {}\n".format(stock))
        our_updates.write("Price of 1 product: ${}\n".format(price))
        our_updates.write("\n")
        our_updates.write("----------------------------------------------------------------\n")
        our_updates.write("Total including vat : ${}\n".format(retailer_total))
        our_updates.write("----------------------------------------------------------------\n")
        our_updates.write("--------------------------------------------------------------\n")
        
        
#this stocks function helps us to format our stocks in  a well foramtted manner using the tabulate python library
      
def stocks():
    with open("Stocks.txt", "r") as file:
        data = [line.strip().split(", ") for line in file]
    headers = ["Product", "Brand", "Price", "Stock", "Processor", "Graphics"]
    our_stocks = tabulate(data, headers, tablefmt="grid")
    print(our_stocks)


def admin_session():
    while True:
        print("")
        print("welcome admin what would u like to do")
        print("below are the list of things admin has access to: ")
        print("")
        print("1 show current items in stock.")
        print("2 update stocks.")
        print("3 show invoices.")
        print("4 Logout")
        print("5 exit the program")
        print("")
        
        admin_option = int(input("-->> "))
        
        if admin_option == 1:
            print("")
            print("the list of all the available stocks.")
            print("")
            stocks()
            print("")
            
        elif admin_option == 2:
            print("")
            print("update stocks pannel")
            update_stocks()
            print("")
            
        elif admin_option == 3:
            print("")
            print("Do you want to see our purchase history?")
            print("'y' to confirm, 'n' to reject")
            look_bill = input("-->> ")

            if look_bill == "y":
                try:
                    print("Getting purchase history...")
                    history = open("FromManufacturer.txt", "r")
                    print(history.read())
                    history.close()
                    
                except FileNotFoundError:
                    
                    print("⚠️  Sorry, the file does not exist.")
                    
            elif look_bill == "n":
                print("Okay, no problem.")
                admin_session()
                
            else:
                print("Invalid input.")
    
        elif admin_option == 4:
            print("")
            break
        
        elif admin_option == 5:
            print("")
            print("are u sure u want to exit?")
            print("confirmation needed : ")
            print("y or n ")
            print("")
            
            admin_exit_confirmation = input("-->>")
            
            if admin_exit_confirmation == "y":
                
                print("")
                print("byee have a good day")
                print("")
                exit()
                
            elif admin_exit_confirmation == "n":
                print("")
                admin_session()
            else:
                print("")
                print("invalid input entered!!!!!")
                print("")

def admin_login():
    print("")
    print("Welcome to the admin console")
    print("please verify your account to login.")
    
    print("credentials = uname = admin and pw = admin")
    username = input("username : ")
    password = getpass.getpass("password : ")
    if username == "admin" and password == "admin":
        print("")
        print("login sucessfull!!!!!")
        admin_session()
        
    else:
        print("")
        print("Login Details failed ")
        print("please check and try again!!!!!")
        
        
def start():
        while True:

            print("")
            print("Hello!! Welcome to Micro Computers Pvt.LTD")
            print("Your very own place to buy computers at cheap\n")
            print("Which mode do you want to select?")
            print("1 = Customer Mode")
            print(termcolor.colored(("2 = Retailer Mode"),'green'))
            print("3 = Exit")

            mode_selection = int(input("Enter 1 or 2 or 3 : "))

            if mode_selection == 1:
                print("\n----------------------------------------------------------------------------")
                print("Hello!! Welcome to Micro Computers Pvt.LTD")
                print("Contact us: 9800000011, 025-12345")
                print("Email: microsmart.pcs@shop.np")
                print("Address: Dharan-16, Sunsari, Nepal")
                print("----------------------------------------------------------------------------\n")
                print("")
                customer_login()
                
            elif mode_selection == 2:
                admin_login()

            elif mode_selection == 3:
                print("")
                print("are u sure u want to exit?")
                print("please enter either y or n ")
                print("")

                exit_choice = input("-->> ")
                if exit_choice == "y":
                    print("")
                    print("exiting program")
                    print("")
                    exit()

                else:
                    print("")
                    print("invalid input")
                    print("please enter either y or n ")

            else:
                print("")
                print(mode_selection, "is an invalid input!!!....."," please enter either 1 or 2 or 3 :")
                continue
start()