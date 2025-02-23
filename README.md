# Pizza Ordering System with GUI

This is a simple pizza ordering system built with Python and the `tkinter` library for the graphical user interface (GUI). It allows users to view the menu, add pizzas to their order, and proceed to checkout.

## Features

* **GUI:** User-friendly interface with buttons and windows for easy interaction.
* **Menu:** Displays the available pizzas with their ingredients and prices.
* **Order Management:** Add pizzas to the order with options for size and quantity.
* **Order Summary:** View the current order with a total price calculation.
* **Checkout:** (To be implemented) Collects customer details and confirms the order.

## Prerequisites

* Python 3.x
* tkinter (usually included with Python, otherwise install with `pip install tkinter`)

## How to Run

1. Save the code as a Python file (e.g., `pizza_gui.py`).
2. Run the file from your terminal: `python pizza_gui.py`

## Usage

1. **View Menu:** Click the "View Menu" button to see the available pizzas.
2. **Add to Order:**
   * Click "Add to Order."
   * Enter the pizza number, select the size, and enter the quantity.
   * Click "Add."
3. **View Order:** Click "View Order" to see the items in your order and the total price.
4. **Remove from Order:** (To be implemented)
5. **Checkout:** (To be implemented)

## Code Structure

* **`Pizza` Class:** Represents a pizza with name, ingredients, and price.
* **`Order` Class:** Manages the order, including adding items and calculating the total.
* **GUI Functions:**
    * `display_menu()`: Displays the pizza menu in a new window.
    * `add_to_order()`: Opens a window to add a pizza to the order.
    * `remove_from_order()`: (To be implemented) Removes a pizza from the order.
    * `view_order()`: Displays the order summary in a new window.
    * `checkout()`: (To be implemented) Handles the checkout process.
    * `setup_main_interface()`: Sets up the main window with buttons.

## Future Improvements

* **Implement Remove Functionality:** Add the ability to remove items from the order.
* **Complete Checkout:** Implement the checkout process, including collecting customer details and order confirmation.
* **Enhance GUI:**
    * Improve the visual layout and design.
    * Add input validation and error handling.
    * Consider using a more advanced GUI framework like PyQt or Kivy for more features and customization.
* **Add More Features:**
    * Display images of the pizzas.
    * Allow customization of toppings.
    * Implement different crust types.
    * Integrate with a payment system.

This project provides a basic framework for a GUI-based pizza ordering system. You can expand upon it to create a more comprehensive and feature-rich application.
