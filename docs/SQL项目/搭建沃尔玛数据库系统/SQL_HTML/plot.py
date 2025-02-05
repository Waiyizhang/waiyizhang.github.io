import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob
def plot():
    # Define the folder path
    folder_path = './images'

    # Get a list of all files in the folder
    files = glob.glob(os.path.join(folder_path, '*'))

    # Iterate over the list of files and remove each file
    for file in files:
        try:
            os.remove(file)
            print(f"Removed file: {file}")
        except Exception as e:
            print(f"Error deleting file {file}: {e}")

    print("All files in the './images' folder have been cleared.")

    # Connect to the SQLite database
    conn = sqlite3.connect('walmart.db')

    # Load the tables into pandas DataFrames
    users_df = pd.read_sql_query("SELECT * FROM users", conn)
    products_df = pd.read_sql_query("SELECT * FROM products", conn)
    relevance_df = pd.read_sql_query("SELECT * FROM relevance", conn)

    # Close the connection
    conn.close()

    # Perform the join operations
    # Join users with relevance
    users_relevance_df = pd.merge(users_df, relevance_df, on='User_ID')

    # Join the result with products
    df = pd.merge(users_relevance_df, products_df, on='Product_ID')

    # Display the resulting DataFrame
    # print(df)
    import matplotlib.patches as mpatches

    # Assuming df is already defined and contains your data

    # Create a table to see the Gender Distribution
    plt.figure(figsize=(8,6))
    ax = sns.countplot(x='Gender', data=df, palette=['pink','skyblue'])

    # Calculate percentages
    total = len(df['Gender'])
    for p in ax.patches:
        percentage = f'{100 * p.get_height() / total:.1f}%'
        x = p.get_x() + p.get_width() / 2
        y = p.get_height()
        ax.annotate(percentage, (x, y), ha='center', va='bottom')

    # Setting title and labels
    ax.set_title('Gender Distribution')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')

    # To illustrate the series or types of data represented by different colors or patterns in the chart.
    colors = [p.get_facecolor() for p in ax.patches]
    gender_groups = df['Gender'].unique()
    gender_groups.sort()
    patches = [mpatches.Patch(color=colors[i], label=age_group) for i, age_group in enumerate(gender_groups)]
    ax.legend(handles=patches, title='Age Groups')

    # Save the plot instead of showing it
    plt.tight_layout()
    plt.savefig('./images/gender_distribution.png')  # You can specify any file format you prefer (e.g., .pdf, .jpg)

    # # Age Distribution
    plt.figure(figsize=(10, 8))

    # Draws a bar chart and displays A, B, C in sequence
    ax = sns.countplot(x='Age', data=df, palette=['darkred','lightcoral','lightgrey','violet','lightpink','purple','darkviolet'])

    # Calculate percentages
    total = len(df['Age'])
    for p in ax.patches:
        percentage = f'{100 * p.get_height() / total:.1f}%'
        x = p.get_x() + p.get_width() / 2
        y = p.get_height()
        ax.annotate(percentage, (x, y), ha='center', va='bottom')

    # Setting title and labels
    ax.set_title('Age Distribution')
    ax.set_xlabel('Age Group')
    ax.set_ylabel('Count')

    # Creating legend
    colors = [p.get_facecolor() for p in ax.patches]
    age_groups = df['Age'].unique()
    age_groups.sort()
    patches = [mpatches.Patch(color=colors[i], label=age_group) for i, age_group in enumerate(age_groups)]
    ax.legend(handles=patches, title='Age Groups')

    plt.tight_layout()
    plt.savefig('./images/age_distribution.png')  # You can specify any file format you prefer (e.g., .pdf, .jpg)

    plt.figure(figsize=(8, 5))

    custom_colors = ['red', 'green', 'yellow'] 

    # Draws a bar chart and displays A, B, C in sequence
    sns.countplot(x='City_Category', data=df, order=['A', 'B', 'C'], palette=custom_colors)

    # Calculate the percentage of each category
    total = len(df)
    for p in plt.gca().patches:
        height = p.get_height()
        plt.gca().text(p.get_x() + p.get_width() / 2., height + 3,
                    '{:1.1f}%'.format(height / total * 100),
                    ha="center")

    #set Title & Label
    plt.title('Distribution of Purchases by City Category')
    plt.xlabel('City Category')
    plt.ylabel('Percentage')

    plt.savefig("./images/city_distribution.png")

    plt.figure(figsize=(12, 6))

    sns.countplot(x='Occupation', data=df, palette='Spectral')

    # percentage: every occupation
    total = len(df)
    for p in plt.gca().patches:
        height = p.get_height()
        plt.gca().text(p.get_x() + p.get_width() / 2., height + 3,
                    '{:1.1f}%'.format(height / total * 100),
                    ha="center")

    plt.title('Distribution of Purchases by Occupation')
    plt.xlabel('Occupation')
    plt.ylabel('Percentage')

    plt.savefig("./images/occupation_distribution.png")

    plt.figure(figsize=(10, 6))

    sns.countplot(x='Stay_In_Current_City_Years', data=df, order=df['Stay_In_Current_City_Years'].value_counts().index, palette='viridis')

    total = len(df)
    for p in plt.gca().patches:
        height = p.get_height()
        plt.gca().text(p.get_x() + p.get_width() / 2., height + 3,
                    '{:1.1f}%'.format(height / total * 100),
                    ha="center")

    plt.title('Distribution of Purchases by Stay in Current City Years')
    plt.xlabel('Years Stay in Current City')
    plt.ylabel('Percentage')

    plt.savefig("./images/stay_years_distribution.png")
    plt.figure(figsize=(8, 5))

    sns.countplot(x='Marital_Status', data=df, palette='plasma')

    total = len(df)
    for p in plt.gca().patches:
        height = p.get_height()
        plt.gca().text(p.get_x() + p.get_width() / 2., height + 3,
                    '{:1.1f}%'.format(height / total * 100),
                    ha="center")

    plt.title('Distribution of Purchases by Marital Status')
    plt.xlabel('Marital Status')
    plt.ylabel('Percentage')

    plt.savefig("./images/marital_distribution.png")

    plt.figure(figsize=(12, 6))

    sns.countplot(x='Product_Category', data=df)

    total = len(df)
    for p in plt.gca().patches:
        height = p.get_height()
        plt.gca().text(p.get_x() + p.get_width() / 2., height + 3,
                    '{:1.1f}%'.format(height / total * 100),
                    ha="center")

    plt.title('Distribution of Purchases by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Percentage')

    plt.savefig("./images/category_purchase.png")

    # Top 10 products
    top_product_ids = df['Product_ID'].value_counts().head(10).index
    df_top_products = df[df['Product_ID'].isin(top_product_ids)]

    # Plotting with seaborn
    plt.figure(figsize=(12, 8))
    ax = sns.countplot(x='Product_ID', data=df_top_products, palette='Spectral', order=top_product_ids)

    # Calculate percentages
    total = len(df_top_products)
    for p in ax.patches:
        percentage = f'{100 * p.get_height() / total:.1f}%'
        x = p.get_x() + p.get_width() / 2
        y = p.get_height()
        ax.annotate(percentage, (x, y), ha='center', va='bottom')

    # Setting title and labels
    ax.set_title('Top 10 Products')
    ax.set_xlabel('Product ID')
    ax.set_ylabel('Count')

    # Creating legend
    colors = [p.get_facecolor() for p in ax.patches]
    patches = [mpatches.Patch(color=colors[i], label=product_id) for i, product_id in enumerate(top_product_ids)]
    ax.legend(handles=patches, title='Product IDs')

    plt.tight_layout()
    plt.savefig("./images/top_ten.png")

if __name__=="__main__":
    plot()