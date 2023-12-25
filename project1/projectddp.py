import tkinter as tk
from tkinter import messagebox

class PointOfSaleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Point of Sale App")

        self.product_label = tk.Label(master, text="Product:")
        self.product_label.grid(row=0, column=0, padx=10, pady=10)

        self.product_entry = tk.Entry(master)
        self.product_entry.grid(row=0, column=1, padx=10, pady=10)

        self.price_label = tk.Label(master, text="Price:")
        self.price_label.grid(row=1, column=0, padx=10, pady=10)

        self.price_entry = tk.Entry(master)
        self.price_entry.grid(row=1, column=1, padx=10, pady=10)

        self.quantity_label = tk.Label(master, text="Quantity:")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=10)

        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add to Cart", command=self.add_to_cart)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.cart_label = tk.Label(master, text="Cart:")
        self.cart_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.cart_text = tk.Text(master, height=10, width=40)
        self.cart_text.grid(row=5, column=0, columnspan=2, pady=10)

        self.total_label = tk.Label(master, text="Total:")
        self.total_label.grid(row=6, column=0, padx=10, pady=10)

        self.total_amount_label = tk.Label(master, text="")
        self.total_amount_label.grid(row=6, column=1, padx=10, pady=10)

        self.total_amount = 0
        self.cart_items = []

    def add_to_cart(self):
        product = self.product_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())

        total_price = price * quantity
        self.cart_items.append(f"{product} - {quantity} x {price} = {total_price}")

        self.cart_text.delete(1.0, tk.END)
        for item in self.cart_items:
            self.cart_text.insert(tk.END, item + "\n")

        self.total_amount += total_price
        self.total_amount_label.config(text=str(self.total_amount))

if __name__ == "__main__":
    root = tk.Tk()
    app = PointOfSaleApp(root)
    root.mainloop()
