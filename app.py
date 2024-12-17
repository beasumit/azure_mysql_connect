import streamlit as st
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
# Establish connection to Azure MySQL database
cnx = mysql.connector.connect(user=os.getenv("USERNAME"), 
                                  password=os.getenv("PASSWORD"), 
                                  host=os.getenv("SERVER"), 
                                  port=3306, 
                                  database=os.getenv("DATABASE"), 
                                  ssl_ca="azure_certificate/DigiCertGlobalRootCA.crt.pem")
# Query data
def get_data_from_db(query):
    db_connection = cnx
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db_connection.close()
    return result

# Streamlit UI
st.title('Azure MySQL with Streamlit')

query = "SELECT * from mytable LIMIT 10;"  # Change query as needed
data = get_data_from_db(query)

if data:
    st.write("Data from MySQL Database:")
    for row in data:
        st.write(f"{row['name']} has a :{row['pet']}:")
else:
    st.write("No data found.")