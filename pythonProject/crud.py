import psycopg2
import streamlit as st
import pandas as pd


connection = psycopg2.connect(database="crud_streamlit",
                              user="postgres",
                              password="reload14",
                              host="localhost",
                              port="5432")

mycursor = connection.cursor()
#print(connection.info)
#print(connection.status)

def main():
    st.title("CRUD Operations With Postgres")
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))

    match option:
        case "Create":
            st.subheader("Create a Record")
            name = st.text_input("Name")
            email = st.text_input("Email")
            if st.button("Create"):
                sql = "insert into users (name, email) values (%s, %s)"
                val = (name, email)
                mycursor.execute(sql, val)
                connection.commit()
                st.success("Record Created Succesfully")
        case "Read":
            st.subheader("Read a Record")
            mycursor.execute("select * from users")
            rows = mycursor.fetchall()
            df = pd.DataFrame(rows)
            st.dataframe(df, width=1000, height=1200)
        case "Update":
            st.subheader("Update a Record")
            id = st.number_input("ID", min_value=1)
            name = st.text_input("New Name")
            email = st.text_input("New Email")
            if st.button("Update"):
                sql = "update users set name=%s, email=%s where id=%s"
                val = (name, email, id)
                mycursor.execute(sql, val)
                connection.commit()
                st.success("Record Updated Succesfully")
        case "Delete":
            st.subheader("Delete a Record")
            id = st.number_input("ID", min_value=1)
            if st.button("Delete"):
                sql = "delete from users where id=%s"
                val = (id,)
                mycursor.execute(sql, val)
                connection.commit()
                st.success("Record Updated Succesfully")


if __name__ == '__main__':
    main()