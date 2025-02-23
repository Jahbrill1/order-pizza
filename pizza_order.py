import tkinter as tk
from tkinter import messagebox

class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
         return f"{self.name} (${self.price}): {', '.join(self.ingredients)}"


class Order:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, pizza, quantity, size):
        self.items.append({"pizza": pizza, "quantity": quantity, "size": size})
        size_multiplier = {"Small": 1, "Medium": 1.5, "Large": 2}
        self.total += pizza.price * quantity * size_multiplier[size]

def display_menu():
    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Display pizzas in the main window
    for i, pizza in enumerate(menu):
        pizza_label = tk.Label(root, text=f"{i+1}. {pizza}")
        pizza_label.pack(anchor="w")

    # Add a back button to return to the main interface
    back_button = tk.Button(root, text="Back", command=setup_main_interface)
    back_button.pack()

def add_to_order():
    # Get pizza choice, size, and quantity from the user using entry fields
    def add_pizza():
        try:
            pizza_choice = int(pizza_index.get()) - 1
            quantity = int(quantity_entry.get())
            size = size_var.get()
            order.add_item(menu[pizza_choice], quantity, size)
            messagebox.showinfo("Order Updated", "Pizza added to order!")
            add_pizza_window.destroy()  # Close the add pizza window
        except (ValueError, IndexError):
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")

    # Create a new window for adding pizza
    add_pizza_window = tk.Toplevel(root)
    add_pizza_window.title("Add Pizza to Order")

    # Pizza index entry
    pizza_index_label = tk.Label(add_pizza_window, text="Enter pizza number:")
    pizza_index_label.pack()
    pizza_index = tk.Entry(add_pizza_window)
    pizza_index.pack()

    # Size selection
    size_label = tk.Label(add_pizza_window, text="Select size:")
    size_label.pack()
    size_var = tk.StringVar(value="Medium")
    sizes = ["Small", "Medium", "Large"]
    for size in sizes:
        size_radio = tk.Radiobutton(add_pizza_window, text=size, variable=size_var, value=size)
        size_radio.pack(anchor="w")

    # Quantity entry
    quantity_label = tk.Label(add_pizza_window, text="Enter quantity:")
    quantity_label.pack()
    quantity_entry = tk.Entry(add_pizza_window)
    quantity_entry.pack()

    # Add button
    add_button = tk.Button(add_pizza_window, text="Add", command=add_pizza)
    add_button.pack()

def remove_from_order():
    #... (Similar to add_to_order, but with remove_item)
    pass  # Implement remove functionality

def view_order():
    # Create a new window for the order
    order_window = tk.Toplevel(root)
    order_window.title("Your Order")

    # Display order items in the order window
    if not order.items:
        order_label = tk.Label(order_window, text="Your order is empty.")
        order_label.pack()
    else:
        for item in order.items:
            item_label = tk.Label(order_window, text=f"{item['pizza'].name} x {item['quantity']} ({item['size']})")
            item_label.pack(anchor="w")
        total_label = tk.Label(order_window, text=f"Total: ${order.total:.2f}")
        total_label.pack()

def checkout():
    #... (Similar to the console version, but use messagebox for output)
    pass  # Implement checkout functionality

def setup_main_interface():
    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()

    # --- Buttons ---
    view_menu_button = tk.Button(root, text="View Menu", command=display_menu)
    view_menu_button.pack()

    add_to_order_button = tk.Button(root, text="Add to Order", command=add_to_order)
    add_to_order_button.pack()

    remove_from_order_button = tk.Button(root, text="Remove from Order", command=remove_from_order)
    remove_from_order_button.pack()

    view_order_button = tk.Button(root, text="View Order", command=view_order)
    view_order_button.pack()

    checkout_button = tk.Button(root, text="Checkout", command=checkout)
    checkout_button.pack()

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack()

# --- Main GUI Setup ---
root = tk.Tk()
root.title("Pizza Ordering System")

# --- Menu ---
menu = [
    Pizza("Margherita", ["Tomato sauce", "Mozzarella", "Basil"], 10.00),
    Pizza("Pepperoni", ["Tomato sauce", "Mozzarella", "Pepperoni"], 12.00),
    Pizza("Vegetarian", ["Tomato sauce", "Mozzarella", "Vegetables"], 11.50),
    Pizza("Meat Lovers", ["Tomato sauce", "Mozzarella", "Various meats"], 13.50)
]

order = Order()

setup_main_interface()

root.mainloop()