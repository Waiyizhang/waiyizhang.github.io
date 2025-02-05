import pandas as pd
import sqlite3
db_file = "walmart.db"
# 1 As for female consumer, they made {count }  purchases ，  as for male consumer , they made {count } purchases”-- Gender-specific and number of purchases
gender_purchase_count_sql = """SELECT gender, COUNT(*) AS purchase_count FROM users JOIN relevance ON users.user_id = relevance.user_id GROUP BY gender;"""
# 2 For customers age between {Age_group} made {count}purchases，occupied {percentage} of the total age group ” -- Different age groups and number of purchases
age_group_purchase_count_sql = """
    WITH age_group_purchases AS (SELECT age, COUNT(purchase) AS purchase_count FROM users JOIN relevance ON users.user_id = relevance.user_id GROUP BY age),
    total_purchases AS (SELECT SUM(purchase_count) AS total_count FROM age_group_purchases)
    SELECT
        age_group_purchases.age,
        age_group_purchases.purchase_count,
        (age_group_purchases.purchase_count * 1.0 / total_purchases.total_count) * 100 AS percentage
    FROM
        age_group_purchases,
        total_purchases;
    """

# For customers who live in{City_Category} made {count} purchases ” -- Distribution of consumer purchases in different cities
city_category_purchases_sql = """
    SELECT
        city_category,
        COUNT(purchase) AS purchase_count
    FROM
        users
    JOIN
        relevance ON users.user_id = relevance.user_id
    GROUP BY
        city_category;
    """

# For consumers is {Occupation}, people are bought {Product_Category} most .”-- Find out the Occupation and buying preference
occupation_preference_sql = """
    WITH ranked_purchases AS (
        SELECT
            users.occupation,
            products.product_category,
            COUNT(relevance.product_id) AS purchase_count,
            ROW_NUMBER() OVER (PARTITION BY users.occupation ORDER BY COUNT(relevance.product_id) DESC) AS rnk
        FROM
            users
        JOIN
            relevance ON users.user_id = relevance.user_id
        JOIN
            products ON relevance.product_id = products.product_id
        GROUP BY
            users.occupation, products.product_category
    )
    SELECT
        occupation,
        product_category,
        purchase_count
    FROM
        ranked_purchases
    WHERE
        rnk = 1;
    """

# The customers who live in current city for{Stay_In _Current_City_years} year(s) made {count}  purchases ” -- The relationship duration of staying in current city and purchase amount.
# Output: Output resident IDs by city, including years of residence and total purchases.
stay_duration_purchases_sql = """
    SELECT
        users.user_id,
        users.stay_in_current_city_years,
        COUNT(relevance.purchase) AS purchase_count
    FROM
        users
    LEFT JOIN
        relevance ON users.user_id = relevance.user_id
    WHERE
        users.city_category = ?
    GROUP BY
        users.user_id, users.stay_in_current_city_years;
    ORDER BY
        users.user_id;
    """


# For customers who are{Marital_Status} bought {Product_ID} most which belongs to {Product_category}.”--Find out the relationship between Marital Status and buying preference.
marital_status_preference_sql = """
    SELECT
        users.marital_status,
        relevance.product_id,
        products.product_category,
        COUNT(relevance.product_id) AS purchase_count
    FROM
        users
    JOIN
        relevance ON users.user_id = relevance.user_id
    JOIN
        products ON relevance.product_id = products.product_id
    GROUP BY
        users.marital_status, relevance.product_id, products.product_category
    ORDER BY
        users.marital_status, purchase_count DESC;
    """


# For the product belong to{Product_catagory}was purchased{count}times” -- Product category and purchases amount .
product_category_purchases_sql = """
    SELECT
        products.product_category,
        COUNT(relevance.product_id) AS purchase_count
    FROM
        products
    JOIN
        relevance ON products.product_id = relevance.product_id
    GROUP BY
        products.product_category;
    """


# {Product_ID}was purchased in {count},which is NO.{Rank}in the best selling products. ” -- The best selling products Top 10
top_selling_products_sql = """
    WITH ranked_products AS (
        SELECT
            products.product_id,
            COUNT(relevance.product_id) AS purchase_count,
            ROW_NUMBER() OVER (ORDER BY COUNT(relevance.product_id) DESC) AS rank
        FROM
            products
        JOIN
            relevance ON products.product_id = relevance.product_id
        GROUP BY
            products.product_id
    )
    SELECT
        product_id,
        purchase_count,
        rank
    FROM
        ranked_products
    WHERE
        rank <= 10;
    """

def queryFn(sqlTemp):
  conn = sqlite3.connect(db_file)
  cur = conn.cursor()
  cur.execute(sqlTemp)
  rows = cur.fetchall()
  conn.close()
  return rows

# 1. gender_purchase_count_sql, retuen [(gender， amount)]
def fetch_gender_purchase_count():
    return queryFn(gender_purchase_count_sql)

# 2. age_group_purchase_count_sql, return [(Age group, total purchases, percentage)]
def fetch_age_group_purchase_count():
    return queryFn(age_group_purchase_count_sql)

# 3. city_category_purchases_sql, return [(Cities， Overall proportion)]
def get_city_category_purchases():
    return queryFn(city_category_purchases_sql)

# 4. occupation_preference_sql, return [(Occupation, Products, Total amount)]
def get_occupation_preference():
    return queryFn(occupation_preference_sql)

# 5. stay_duration_purchases_sql, return
def get_stay_duration_purchases(city_category):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(stay_duration_purchases_sql, (city_category,))
    rows = cur.fetchall()
    conn.close()
    return rows

# 6. marital_status_preference_sql, return [(Marital status, Product, Category， Purchase Frequency)]
# Maximum not found
def get_marital_status_preference():
   return queryFn(marital_status_preference_sql)

# 7. product_category_purchases_sql, return [(Product categories， Total Purchases)]
def get_product_category_purchases():
   return queryFn(product_category_purchases_sql)

# 8. top_selling_products_sql, return [(Product， Total Purchases， Ranking)]
def get_top_selling_products():
   return queryFn(top_selling_products_sql)

if __name__=="__main__":
    fetch_gender_purchase_count()
    # fetch_age_group_purchase_count()
    # get_city_category_purchases()
    # get_occupation_preference()
    # get_stay_duration_purchases('A')
    # get_marital_status_preference()

    # get_product_category_purchases()
    # get_top_selling_products()