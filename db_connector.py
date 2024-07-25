import psycopg2


class db_connector:

    def __init__(self, user_name, password, db_name, host, port) -> None:
        """connecting to the database and creating cursor"""

        self.conn = psycopg2.connect(
            user=user_name, dbname=db_name, password=password, host=host, port=port
        )

        print("connection completed")

        self.cursor = self.conn.cursor()
        self.conn.autocommit = True

    def creating_user(self, name, mobile, gst_number, email=None):
        new_user_insert = """insert into Users (name,email,mobile,gst_number)
                                values(%s,%s,%s,%s)"""
        self.cursor.execute(new_user_insert, (name, email, mobile, gst_number))

    def creating_receipt(self, mobile, total_amount, items) -> bool:
        check_user_id = """select id from Users 
                                where mobile = %s"""
        self.cursor.execute(check_user_id, (mobile,))

        if check_user_id:
            user_id = self.cursor.fetchone()[0]
            new_receipt_insert = """insert into Receipts (total_amount,user_id)
                                        values (%s,%s) Returning id"""
            self.cursor.execute(new_receipt_insert, (total_amount, user_id))
            self.creating_items(self.cursor.fetchone()[0], items)
            return True

    def creating_items(self, receipt_id, items) -> bool:
        new_item_inserted = """insert into items (name,quantity,price,receipt_id)
                                    values (%s,%s,%s,%s)"""

        for item in items:
            self.cursor.execute(
                new_item_inserted,
                (
                    item["name"].get(),
                    item["quantity"].get(),
                    item["price"].get(),
                    receipt_id,
                ),
            )

    
    def search_receipts(self, mobile, date=None) -> list:
        if date:
            query = """ select * from items where receipt_id = (select id from receipts where receipt_date::date = %s
					and user_id=(select id from users where mobile=%s)) """
            self.cursor.execute(query, (date, mobile))
        else:
            query = """ select * from receipts where user_id = (select id from users where mobile=%s) """
            self.cursor.execute(query, (mobile,))
        
        return self.cursor.fetchall()
