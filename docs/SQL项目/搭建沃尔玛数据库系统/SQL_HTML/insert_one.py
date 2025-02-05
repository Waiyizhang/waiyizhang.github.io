import sqlite3

def insert_users(user_id, gender, age, occupation, city_category, stay_in_current_city_years, marital_status):
    conn = sqlite3.connect('walmart.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM users WHERE User_ID = ?', (user_id,))
        if cursor.fetchone():
#             print("user already exists")

            return
        
        # Execute the insert statement
        sql = '''INSERT INTO users (User_ID, Gender, Age, Occupation, City_Category, Stay_In_Current_City_Years, Marital_Status)
                 VALUES (?, ?, ?, ?, ?, ?, ?)'''
        params = (user_id, gender, age, occupation, city_category, stay_in_current_city_years, marital_status)
        cursor.execute(sql, params)
        conn.commit()
        # Returns the current insertion data
        print("Data inserted successfully")
        return cursor.lastrowid
    except sqlite3.Error as e:
        # If an error occurs,roll back the transaction and print the error message
        conn.rollback()
        print("Data insertion failure:", e)
    finally:
        # Close the database connection
        conn.close()

def insert_products(product_id, product_category):
    conn = sqlite3.connect("walmart.db")
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM products WHERE Product_ID = ?', (product_id,))
        if cursor.fetchone():
#             print("Product already exists")
            return
        
        sql = '''INSERT INTO products (Product_ID, Product_Category)
                 VALUES (?, ?)'''
        params = (product_id, product_category)
        cursor.execute(sql, params)
        conn.commit()
    except sqlite3.Error as e:
        # If an error occurs, roll back the transaction and print the error message
        conn.rollback()
        print("Data insertion failure:", e)
    finally:
        # Close the database connection
        conn.close()

def insert_relevance(user_id, product_id, purchase):
    conn = sqlite3.connect("walmart.db")
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT 1 FROM relevance WHERE User_ID = ? AND Product_ID = ?', (user_id, product_id))
        if cursor.fetchone():
#             print("relevance exist")
            return
        sql = '''INSERT INTO relevance (User_ID, Product_ID, Purchase)
                 VALUES (?, ?, ?)'''
        params = (user_id, product_id, purchase)
        cursor.execute(sql, params)
        conn.commit()
    except sqlite3.Error as e:
        # If an error occurs, roll back the transaction and print the error message
        conn.rollback()
        print("Data insertion failure:", e)
    finally:
        # Close the database connection
        conn.close()

def insert():
    user_id = input("user id: ")
    product_id = input("product id: ")
    gender = input("gender: ")
    age = input("age: ")
    occupation = input("occupation: ")
    city_category = input("city category: ")
    stay_in_current_city_years = input("Stay_In_Current_City_years: ")
    product_category = input("Product_Category: ")
    marital_status = input("marital status: ")
    purchase = input("Purchase: ")
    insert_users(user_id, gender, age, occupation, city_category, stay_in_current_city_years, marital_status)
    insert_products(product_id, product_category)
    insert_relevance(user_id, product_id, purchase)

if __name__=="__main__":
    insert()

