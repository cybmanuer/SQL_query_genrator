from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import sqlite3
import pandas as pd

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#loading google model to give question and prompt as input
# 
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


def read_sql_query(sql,db):
    conn=sqlite3.connect(db) 
    qry=conn.cursor()
    qry.execute(sql)
    rows=qry.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows


promt=["""
       
you are expert in converting English question to SQL Query.The code should not have ''' in the beginning and end and "sql" word in output \n
if empty question is asked just show all data in database
You are an expert in managing databases using SQL commands. The SQL database named 'cms' consists of several tables, including 'student', 'admin', 'contact', 'notification', 'tblfiles', and 'teacher', each with specific columns. 
Here's an example of the 'student' table contains:
1. student Table:
   - `s_name`: Student name
   - `s_reg`: Registration number
   - `s_phno`: Phone number
   - `s_sem`: Semester
   - `s_comb`: Combination/course
   - `s_pass`: Password
   - `s_fees`: Fees
   - `s_balance`: Balance

Here's an example of the 'admin' table contains:
2. admin Table:
   - `a_name`: Admin username
   - `a_pass`: Admin password


Here's an example of the 'contact' table contains:
3. contact Table:
   - `c_name`: Name of the person who contacted
   - `c_mail`: Email of the person who contacted
   - `c_msg`: Message content

Here's an example of the 'notification' table contains:
4. notification Table:
   - `msg`: Notification message
   - `t_name`: Teacher name

Here's an example of the 'tblfiles' table contains:
5. tblfiles Table:
   - `FileName`: Name of the file
   - `Location`: File location

Here's an example of the 'teacher' table contains:
6. teacher Table:
   - `t_name`: Teacher name
   - `t_phno`: Teacher phone number
   - `t_address`: Teacher address
   - `t_dept`: Department/Subject taught
   - `t_pass`: Teacher password

    Example 1: How many records are present in the 'student' table?
    The SQL command would look like this: "SELECT COUNT(*) FROM student;"

    Example 2: Show all the records in the 'notification' table.
    The SQL command would be something like: "SELECT * FROM notification;"

    Example 3: Retrieve the details of the 'teacher' whose name is 'Bhaskar'.
    The SQL command could be: "SELECT * FROM teacher WHERE t_name='Bhaskar';"

    Example 4: List all the unique messages in the 'notification' table.
    The SQL query might look like: "SELECT DISTINCT msg FROM notification;"

    Example 5: Display the filenames and their locations from the 'tblfiles' table.
    The SQL query would be: "SELECT FileName, Location FROM tblfiles;"

    Example 6: Find the total number of entries in the 'contact' table.
    The SQL query could be: "SELECT COUNT(*) FROM contact;"


"""]

# front end



st.set_page_config(page_title="GenQuery-cybmanuer")
# st.header("GenQuery")
# st.subheader("It genrates the SQL queries on the STUDENT Database")
# st.subheader("")

# Header and subheaders
st.markdown('<h1 class="main-header">GenQuery</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">It generates SQL queries on the STUDENT Database</h2>', unsafe_allow_html=True)


show_tables = st.button("Show Tables")

if show_tables:
    # Database Structure
    st.markdown('<h2 class="sub-header">Database Structure</h2>', unsafe_allow_html=True)

    # Example data for each table
    tables = {
        "student": [
            {"Column Name": "s_name", "Description": "Student name"},
            {"Column Name": "s_reg", "Description": "Registration number"},
            {"Column Name": "s_phno", "Description": "Phone number"},
            {"Column Name": "s_sem", "Description": "Semester"},
            {"Column Name": "s_comb", "Description": "Combination/course"},
            {"Column Name": "s_pass", "Description": "Password"},
            {"Column Name": "s_fees", "Description": "Fees"},
            {"Column Name": "s_balance", "Description": "Balance"},
        ],
        "admin": [
            {"Column Name": "a_name", "Description": "Admin username"},
            {"Column Name": "a_pass", "Description": "Admin password"},
        ],
        "contact": [
            {"Column Name": "c_name", "Description": "Name of the person who contacted"},
            {"Column Name": "c_mail", "Description": "Email of the person who contacted"},
            {"Column Name": "c_msg", "Description": "Message content"},
        ],
        "notification": [
            {"Column Name": "msg", "Description": "Notification message"},
            {"Column Name": "t_name", "Description": "Teacher name"},
        ],
        "tblfiles": [
            {"Column Name": "FileName", "Description": "Name of the file"},
            {"Column Name": "Location", "Description": "File location"},
        ],
        "teacher": [
            {"Column Name": "t_name", "Description": "Teacher name"},
            {"Column Name": "t_phno", "Description": "Teacher phone number"},
            {"Column Name": "t_address", "Description": "Teacher address"},
            {"Column Name": "t_dept", "Description": "Department/Subject taught"},
            {"Column Name": "t_pass", "Description": "Teacher password"},
        ],
    }

    # Display tables side by side
    columns = st.columns(3)  # Adjust the number of columns as needed

    for i, (table_name, columns_data) in enumerate(tables.items()):
        col = columns[i % 3]  # Distribute tables across the columns
        col.markdown(f'<h3 class="sub-header">{table_name} Table</h3>', unsafe_allow_html=True)
        df = pd.DataFrame(columns_data)
        col.dataframe(df.style.set_properties(**{'font-size': '12px'}))




























question = st.text_input("Input:", key="input",placeholder="Enter your question here")

submit=st.button("Get Query")
# st.header("Gemini App To Retrive SQL Data")

if submit:
    response=get_gemini_response(question,promt)
    # print(response)
    # st.text(f"The Query is : {response}")
    st.markdown(f'<p class="response-text">The Query is: {response}</p>', unsafe_allow_html=True)

    # st.markdown(response)


    data=read_sql_query(response,"new_cms.db")
    st.subheader("The response Is : ")
    for row in data:
        # print(row)
        # st.markdown(row)
        st.markdown(row)



st.markdown("""
<style>

.main-header {
        font-size: 30px;
        color: white;
    }
    .sub-header {
        font-size: 10px;
        color: white;
    }
    .input-label {
        font-size: 10px;
        color: #0000FF;
    }
    .response-text {
        font-size: 18px;
        color: #000;
        font-family: Arial, sans-serif;
    }        

            



.main-header {
        font-size: 36px;
        color: #4CAF50;
    }
    .sub-header {
        font-size: 24px;
        color: #FF5733;
    }
    .input-label {
        font-size: 20px;
        color: #0000FF;
    }
    .response-text {
        font-size: 18px;
        color: #000;
        font-family: Arial, sans-serif;
    }
    .small-font {
        font-size: 12px;
    }

</style>
""", unsafe_allow_html=True)