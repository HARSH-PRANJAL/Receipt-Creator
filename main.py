from db_connector import db_connector
from gui import GUI
import os
from dotenv import load_dotenv
import tkinter as tk

if __name__ == "__main__":

    load_dotenv()
    
    root = tk.Tk()

    connection = db_connector(
        user_name=os.getenv("user_name"),
        password=os.getenv("password"),
        db_name=os.getenv("db_name"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )

    gui = GUI(root,connection)
    root.mainloop()