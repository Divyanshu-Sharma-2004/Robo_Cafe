# Robo Cafe Ordering System

This is a **Robo Cafe Ordering System** that integrates voice commands and MySQL database to automate the process of ordering food and beverages. The system allows customers to order from a menu, enter their details, and have their order saved in a MySQL database, all with the help of voice feedback from a robotic assistant.

## Features:
- **Voice Interaction**: Uses the `pyttsx3` library to provide voice feedback and guidance during the ordering process.
- **Cafe Menu**: Customers can view the menu and order items (up to 7 items).
- **Order Summary**: Displays a summary of the customer's order with the total cost.
- **User Details Collection**: Prompts users for their name, mobile number, and address.
- **Database Integration**: Stores the order details (including customer information and ordered items) in a MySQL database.
- **SQL Table Creation**: Automatically creates an orders table in the database if it doesn't exist.
  
## How To Use:
1. **Start the system**: The robot will greet you and provide the menu.
2. **Place your order**: Enter the items you want from the menu. You can order up to 7 items.
3. **Confirm your order**: Once you're done, the system will display your order summary and ask for approval.
4. **Provide user details**: If you approve, the system will ask for your name, mobile number, and address.
5. **Data Submission**: The system will save your order and personal information into the MySQL database.

## How It Works:
- **Voice Interaction**: The robot uses text-to-speech (TTS) to interact with the user.
- **Menu Display**: The menu is printed in the terminal, and users can select items by typing their choices.
- **Database Interaction**: The program connects to a MySQL database (`robocafe`) to save user orders and details.
- **Order Summary**: After order confirmation, the details are stored in an SQL table named `orders`.

## Code Explanation:

### Key Functions:
1. **`cafe_menu()`**: Displays the menu with available items and their prices. It also uses voice to announce the menu.
2. **`take_order(menu)`**: Allows users to order items from the menu. It handles user input and adds items to the order.
3. **`print_order_summary(order, total_cost, menu)`**: Displays the summary of the ordered items along with the total cost.
4. **`user_details()`**: Collects user details like name, mobile number, and address, and handles order approval.
5. **`create_table()`**: Creates the SQL table for storing orders if it does not already exist.
6. **`sql_record(user, order, total_cost)`**: Inserts the user order and details into the SQL database.

### Example:

1. **Menu**:
   - Coffee: $3.50
   - Tea: $2.50
   - Sandwich: $5.00
   - Cake: $4.00
   - Pasta: $6.50
   - Juice: $2.00
   - Salad: $4.50

2. **Order**:
   - User orders "Coffee" and "Cake".
   - The system asks for confirmation, then collects the user's details (name, phone, address).
   - The order is stored in the database with a total cost.

3. **Database Schema** (`orders` table):
   - `order_id`: Primary key (auto-incremented)
   - `name`: Customer's name
   - `mobile`: Customer's mobile number
   - `address`: Customer's address
   - `item1`, `item2`, ... `item7`: Ordered items (up to 7 items)
   - `total_cost`: Total cost of the order
