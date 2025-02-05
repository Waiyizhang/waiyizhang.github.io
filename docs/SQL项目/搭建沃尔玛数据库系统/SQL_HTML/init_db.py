import pandas as pd

df = pd.read_csv("walmart.csv")
import pandas as pd
import sqlite3

# Define users table
sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                    user_id integer PRIMARY KEY,
                                    gender tinyint NOT NULL,
                                    age text NOT NULL,
                                    occupation text NOT NULL,
                                    city_category text NOT NULL,
                                    stay_in_current_city_years text NOT NULL,
                                    marital_status text NOT NULL
                                ); """
# Define Product table
sql_create_products_table = """ CREATE TABLE IF NOT EXISTS products (
                                        product_id text PRIMARY KEY,
                                        product_category text NOT NULL
                                  ); """
# Define a table of user-product associations
sql_create_relevance_table = """CREATE TABLE IF NOT EXISTS relevance (
                                user_id integer NOT NULL,
                                product_id text NOT NULL,
                                purchase integer,
                                PRIMARY KEY (user_id, product_id, purchase),
                                FOREIGN KEY (user_id) REFERENCES users(user_id),
                                FOREIGN KEY (product_id) REFERENCES products(product_id)
                            );"""

db_file = 'walmart.db'

def dbInit():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    conn.commit()
    # Clear the table
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")

    df = pd.read_csv('walmart.csv')

    # Remove duplicates
    user_columns = df[['User_ID', 'Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status']].drop_duplicates()
    product_columns = df[['Product_ID', 'Product_Category']].drop_duplicates()
    sales_columns = df[['User_ID', 'Product_ID', 'Purchase']].drop_duplicates()

    cursor.execute(sql_create_users_table)
    user_columns.to_sql('users', conn, if_exists='replace', index=False)

    cursor.execute(sql_create_products_table)
    product_columns.to_sql('products', conn, if_exists='replace', index=False)

    cursor.execute(sql_create_relevance_table)
    sales_columns.to_sql('relevance', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

    print(user_columns)
    print(product_columns)
    print(sales_columns)
if __name__=="__main__":
    dbInit()
