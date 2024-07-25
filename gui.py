import tkinter as tk
from tkinter import messagebox


class GUI:

    def __init__(self, root, db_manager) -> None:
        self.db_manager = db_manager
        self.root = root
        self.root.title("Receipt Creation")
        self.root.geometry("600x600")

        self.main_menu()

    def main_menu(self) -> None:

        for widget in self.root.winfo_children():
            widget.destroy()

        self.main_menu_label = tk.Label(self.root, text="Main Menu")
        self.main_menu_label.pack(pady=20)

        self.create_user_button = tk.Button(
            self.root, text="Create User", command=self.add_user
        )
        self.create_user_button.pack(pady=20)

        self.create_receipt_button = tk.Button(
            self.root, text="Create Receipt", command=self.add_receipt
        )
        self.create_receipt_button.pack(pady=20)

        self.create_search_button = tk.Button(
            self.root, text="Search Receipt", command=self.search_receipt
        )
        self.create_search_button.pack(pady=20)

    def add_user(self) -> None:

        for widget in self.root.winfo_children():
            widget.destroy()

        self.user_name_lable = tk.Label(self.root, text="User Name")
        self.user_name_lable.grid(row=0, column=0, padx=10, pady=10)
        self.user_name_entry = tk.Entry(self.root)
        self.user_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.user_Email_lable = tk.Label(self.root, text="User Email")
        self.user_Email_lable.grid(row=1, column=0, padx=10, pady=10)
        self.user_Email_entry = tk.Entry(self.root)
        self.user_Email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.user_mobile_lable = tk.Label(self.root, text="User Mobile")
        self.user_mobile_lable.grid(row=2, column=0, padx=10, pady=10)
        self.user_mobile_entry = tk.Entry(self.root)
        self.user_mobile_entry.grid(row=2, column=1, padx=10, pady=10)

        self.user_gst_lable = tk.Label(self.root, text="User Gst number")
        self.user_gst_lable.grid(row=3, column=0, padx=10, pady=10)
        self.user_gst_entry = tk.Entry(self.root)
        self.user_gst_entry.grid(row=3, column=1, padx=10, pady=10)

        self.back_button = tk.Button(
            self.root, text="Main Menu", command=self.main_menu
        )
        self.back_button.grid(row=5, column=1, columnspan=3, padx=10, pady=10)

        self.submit_user_button = tk.Button(
            self.root, text="Save", command=self.submit_user
        )
        self.submit_user_button.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

    def submit_user(self) -> None:
        user_name = self.user_name_entry.get()
        email = self.user_Email_entry.get()
        mobile = self.user_mobile_entry.get()
        gst_number = self.user_gst_entry.get()

        try:
            if email:
                self.db_manager.creating_user(
                    name=user_name, mobile=mobile, gst_number=gst_number, email=email
                )
            else:
                self.db_manager.creating_user(
                    name=user_name, mobile=mobile, gst_number=gst_number
                )
            messagebox.showinfo("Success","User Created", parent=self.root)
            self.main_menu()

        except Exception as e:
            messagebox.showerror("Error in creating user", str(e), parent=self.root)

    def add_receipt(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

        self.user_mobile_lable = tk.Label(self.root, text="User Mobile")
        self.user_mobile_lable.grid(row=0, column=0, padx=10, pady=10)
        self.user_mobile_entry = tk.Entry(self.root)
        self.user_mobile_entry.grid(row=0, column=1, padx=10, pady=10)

        self.items = []

        self.item_name_lable = tk.Label(self.root, text="Item Name")
        self.item_name_lable.grid(row=1, column=0, padx=10, pady=10)
        self.item_quantity_lable = tk.Label(self.root, text="Quantity")
        self.item_quantity_lable.grid(row=1, column=1, padx=10, pady=10)
        self.item_price_lable = tk.Label(self.root, text="Price (Unit)")
        self.item_price_lable.grid(row=1, column=2, padx=10, pady=10)
        self.item_totalprice_lable = tk.Label(self.root, text="Total Price")
        self.item_totalprice_lable.grid(row=1, column=3, padx=20, pady=10)

        self.add_item_button = tk.Button(
            self.root, text="Add Items", command=self.add_items
        )
        self.add_item_button.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        self.save_receipt = tk.Button(self.root,text="Save",command=self.submit_receipt)
        self.save_receipt.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

        self.back_button = tk.Button(
            self.root, text="Main Menu", command=self.main_menu
        )
        self.back_button.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

    def add_items(self):
        row = len(self.items)+3
        item_name = tk.Entry(self.root)
        item_name.grid(row=row,column=0,padx=10,pady=10)
        item_quantity = tk.Entry(self.root)
        item_quantity.grid(row=row,column=1,padx=10,pady=10)
        item_price = tk.Entry(self.root)
        item_price.grid(row=row,column=2,padx=10,pady=10)
        item_total_price = tk.Entry(self.root, state="readonly")
        item_total_price.grid(row=row,column=3,padx=10,pady=10)

        self.items.append({'name':item_name,'quantity':item_quantity,'price':item_price,'total_price':item_total_price})

        self.add_item_button.grid(row=row+2, column=1, columnspan=2, padx=10, pady=10)
        self.save_receipt.grid(row=row+3, column=1, columnspan=2, padx=10, pady=10)
        self.back_button.grid(row=row+4, column=1, columnspan=2, padx=10, pady=10)

        item_quantity.bind("<KeyRelease>",lambda event,index = len(self.items)-1:self.calculate_total_price(index))
        item_price.bind("<KeyRelease>",lambda event,index = len(self.items)-1:self.calculate_total_price(index))        

    def calculate_total_price(self,index):
        try:
            q = int(self.items[index]['quantity'].get())
            price = float(self.items[index]['price'].get())

            total_price = f"{q*price:.2f}"
            self.items[index]["total_price"].config(state='normal')
            self.items[index]["total_price"].delete(0,tk.END)
            self.items[index]["total_price"].insert(0,str(total_price))
            self.items[index]["total_price"].config(state='readonly')
        except:
            pass
    
    def submit_receipt(self):
        try:
            total_amount = 0
            for item in self.items:
                total_amount += float(item['total_price'].get())
            
            items = []
            for item  in self.items:
                if item['name'] and item['price'] and item['quantity']:
                    items.append(item)

            self.db_manager.creating_receipt(mobile = self.user_mobile_entry.get(),total_amount=total_amount,items=items)
            messagebox.showinfo("Success","Reciept Saved",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error in Creating Receipt",str(e),parent=self.root)

    def search_receipt(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()

        self.user_mobile_lable = tk.Label(self.root, text="User Mobile")
        self.user_mobile_lable.grid(row=0, column=0, padx=10, pady=10)
        self.user_mobile_entry = tk.Entry(self.root)
        self.user_mobile_entry.grid(row=0, column=1, padx=10, pady=10)

        self.user_date_lable = tk.Label(self.root, text="Date (optional)")
        self.user_date_lable.grid(row=1, column=0, padx=10, pady=10)
        self.user_date_entry = tk.Entry(self.root)
        self.user_date_entry.grid(row=1, column=1, padx=10, pady=10)

        self.user_search_receipt = tk.Button(self.root,text="Search",command=self.search)
        self.user_search_receipt.grid(row=2, column=1, columnspan=3, padx=10, pady=10)
        self.back_button = tk.Button(
            self.root, text="Main Menu", command=self.main_menu
        )
        self.back_button.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    def search(self):
        try:
            date = self.user_date_entry.get()
            mobile = self.user_mobile_entry.get()
            result = self.db_manager.search_receipts(date=date,mobile=mobile)

            result_window = tk.Toplevel(self.root)
            result_window.title("Search Receipts")
            result_window.geometry("600x600")

            for i, receipt in enumerate(result):
                receipt_lable = tk.Label(result_window,text=f"Receipts {i+1}:{receipt}")
                receipt_lable.pack(pady=5)

            messagebox.showinfo("Success","Search Result",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",str(e),parent=self.root)