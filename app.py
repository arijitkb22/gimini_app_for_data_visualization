from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt
 

# Configure our api key

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Function to load google Gimini Modle
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

#function to retrieve query from the sql database
def read_sql_quary(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    columns = cur.description
    result = [column[0] for column in columns]
    print(result)
    conn.commit()
    conn.close()
    return [result, rows]

#Define Prompt
prompt = [
    """
    You are an expart in converting English question to SQl query!
    The SQL database has the  name  EMP and has following columns - NAME,
    DESIGNATION, EXPERIANCE, PROFILE \n \nfor example, \nExample 1 - How many employees are present?,
    the SQL command will be something like this SELECT COUNT(*) from EMP;
    \nExample 2 - Tell me all the employees of designation SSE?, The SQL command will be something like this
    SELECT * FROM EMP where DESIGNATION = "SSE";
    also the sql code should not have ``` in begining or end and sql word in output
    """
]

#Streamlit App
st.set_page_config(page_title = "Lets ask sql!!")
st.header("Gimini App To Retrive SQL Data")
question = st.text_input("Input: ", key="imput")
submit = st.button("Ask Me.....")

#if submit is clicketed
if submit:
    res = get_gemini_response(question, prompt)
    print(res)
    data = read_sql_quary(res, "employee.db")
    st.subheader("Here is your result: ")
    print(type(data))
    columns_data = data[0]
    values = data[1]
    print(columns_data)
    head = []
    val = []
    for item in values:
        head.append(item[0])
        val.append(item[1])

    # Create dataframe for plotting
    # for items in values:
    #     val.append(list(items))
    # print(val)
    # dataframe = pd.DataFrame(val, columns=columns_data)
    # st.subheader(val)
    dic=zip(head,val)
    st.subheader(dict(dic))
    fig, ax = plt.subplots()
    ax.bar(head, val, width=1, edgecolor="white", linewidth=0.7)
    st.pyplot(fig)
