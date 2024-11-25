import pyttsx3
import mysql.connector as myconn
import time
import os

engine = pyttsx3.init() # Creating instance of pyttsx3

conn = myconn.connect(host="localhost",
                      user="root",
                      password="152021DS",
                      database="robocafe")      # Creating instance of mysql.connector

cur = conn.cursor()     #Creating cursor method instance to use

def clr_scr(t):         #Function for clearing screen & timesleep
    time.sleep(t)
    os.system('cls')

def call_robo(command):    #RoboCalling Function
    engine.say(command)
    engine.runAndWait()

def cafe_menu():    #Function to print cafe menu
    call_robo("WELCOME TO THE ROBO CAFE. THANKS FOR GIVING US OPPURTUNITY TO SERVE YOU")

    print("--------Here is your menu--------")
    menu = {
        "Coffee": 3.50,
        "Tea": 2.50,
        "Sandwich": 5.00,
        "Cake": 4.00,
        "Pasta": 6.50,
        "Juice": 2.00,
        "Salad": 4.50
    }
    
    for items,price in menu.items():
        print(f"{items} : ${price}")
    
    call_robo("Here is your menu")

    return menu

def take_order(menu):   #Function to take orders
    order = []
    total_cost = 0
    count = 0

    print("\nPlease select items from the menu. Type 'done' when you're finished.")

    while True:
        count += 1
        if(count <= 7):
            choice = input("Enter an item name to add to your order (or 'done' to finish): ").capitalize()
        else:
            choice = input("Can't order more than 7 items. Enter 'done' to complete order : ").capitalize()
            if choice.lower() == 'done':
                pass
            else:
                continue

        if choice.lower() == 'done':
            clr_scr(0)
            break
        elif choice in menu:
            order.append(choice)
            total_cost += menu[choice]
            print(f"{choice} has been added to your order.")
        else:
            print("Sorry, that's not on the menu. Please try again.")

    return order, total_cost,menu

def print_order_summary(order, total_cost, menu):   #Function to print order summary
    print("\nYour order summary:")
    if order:
        for item in order:
            price = menu[item]
            print(f"{item} : ${price:.2f}")
        
        print(f"Total cost: ${total_cost:.2f}")
        call_robo("YOUR ORDERED LIST IS HERE, PRESS Y TO GO AHEAD AND N TO EXIT")
    else:
        print("You did not order anything.")
        exit()

def user_details(): #Function to Input User details
    approval = input("\nDo You Want To Approve Your Order, Enter Y/N : ").capitalize()
    clr_scr(0)

    if approval == 'Y':
        call_robo("YOUR ORDER IS APPROVED, KINDLY FILL YOUR BASIC INFORMATION.")
    
        name = input("Enter your name : ")
        mob = int(input("Enter your mobile number : "))
        adrs = input("Enter your address : ")

        submit = input("\nEnter Y to submit details or N to cancel : ")
        clr_scr(0)

        if submit.lower() == 'y':
            for i in range(3,0,-1):
                print(f"Submitting details in {i} seconds")
                clr_scr(1)
        else:
            print("Order canceled")
            call_robo("Order canceled")
            exit()
    else:
        print("Permission Denied, Order Cancelled")
        call_robo("Permission Denied, Order Cancelled")
        exit()
    
    return name,mob,adrs

def create_table(): #Creating table in SQL database
    """Create the orders table if it doesn't exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        mobile VARCHAR(20) NOT NULL,
        address TEXT NOT NULL,
        item1 VARCHAR(255),
        item2 VARCHAR(255),
        item3 VARCHAR(255),
        item4 VARCHAR(255),
        item5 VARCHAR(255),
        item6 VARCHAR(255),
        item7 VARCHAR(255),
        total_cost DECIMAL(10, 2) NOT NULL
    );
    """
    try:
        cur.execute(create_table_query)
        conn.commit()  # Commit the transaction to the database
    except myconn.Error as err:
        print(f"Error creating table: {err}")
        conn.rollback()

    clr_scr(0)

def sql_record(user,order,total_cost):  #Inserting data in Table in SQL.
    items = order + [None] * (7 - len(order))  # Fill remaining items with None if less than 7
    
    query = """INSERT INTO orders (name, mobile, address, item1, item2, item3, item4, item5, item6, item7, total_cost)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    try:
        cur.execute(query, (user[0], user[1], user[2], *items, total_cost)) # *item is unpacking items of list
        conn.commit()  # Commit the transaction to the database
        
        print("------Record inserted successfully.------")
    except conn.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()  # Rollback in case of error  
    finally:
        cur.close()  # Close the cursor
        conn.close()  # Close the connection    

def main(): #Main function
    order,total_cost,menu = take_order(cafe_menu())
    print_order_summary(order, total_cost, menu)
    name,mob,adrs = user_details()
    user = (name,str(mob),adrs)
    create_table()  # Create the table before processing the order
    sql_record(user,order,total_cost)
    print("Thank you for visiting our café! Have a great day!")
    call_robo("Record inserted successfully. Thank you for visiting our café! Have a great day!")

if __name__ == "__main__":
    main()
