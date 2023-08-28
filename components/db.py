import mysql.connector as cn
import streamlit as sl

# import pandas as pd
import duckdb as db

# ====================Connect to the MySQL Database============
# contosodb = cn.connect(
#     host="localhost", user="root", password="ekedie", database="contoso_store"
# )

# data = pd.read_sql_query("select * from factsale limit 200000", contosodb)

# ========= Fetch data from the database ===============
@sl.cache_data
def fetch_data():
    with db.connect("consoto.db") as con:
        data = con.sql("""select * from consoto_store limit 100000""").df()
        # data.to_csv(f"{cwd}\\query.csv", index=False)

    return data


data = fetch_data()

# create new date metadata columns
data["Year"] = data["DateKey"].dt.year
data["Month"] = data["DateKey"].dt.month_name()
data["Month_Number"] = data["DateKey"].dt.month
data["Day_Name"] = data["DateKey"].dt.day_name()
data["Day_Number"] = data["DateKey"].dt.day_name()

# create day number column.
data["Day_Number"].replace(
    ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    [1, 2, 3, 4, 5, 6, 7],
    inplace=True,
)
