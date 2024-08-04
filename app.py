from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import sqlite3

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
st.header("GenQuery")
st.subheader("It genrates the SQL queries on the STUDENT Database")
st.subheader("")



question=st.text_input("Input:",key="input")

submit=st.button("Get Query")
# st.header("Gemini App To Retrive SQL Data")

if submit:
    response=get_gemini_response(question,promt)
    # print(response)
    st.text(f"The Query is : {response}")
    # st.markdown(response)


    data=read_sql_query(response,"new_cms.db")
    st.subheader("The response Is : ")
    for row in data:
        # print(row)
        # st.markdown(row)
        st.markdown(row)



st.markdown("""
<style>
.custom-text{
    color: black;
    font-size: 20px;
    font-family:Garamond;
}
st.text{
    color: red;
    font-size: 20px;
    font-family:Garamond;
}
</style>
""", unsafe_allow_html=True)