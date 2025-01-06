import streamlit as st 
import sqlite3

def show_create():
    if st.button("Back to Log-in page"):
        st.session_state.logged_in = False
        st.session_state.create_account = False
        st.rerun()
    st.header("Let's start with some basic details about you")

    name_input = st.text_input("Name")
    email_input = st.text_input("Email")
    user_input = st.text_input("Username")
    pass_input = st.text_input("Password", type="password")
    submit = st.button("Submit")
    
    if submit:
        make_data()
        records = check_data(email_input, user_input)
        if records:
            st.error("Username or Email already exists")
        else:
            st.write("Account created successfully")
            try:
                insert_user(name_input, email_input, user_input, pass_input)
            except KeyError as e:
                st.error(f"Error: {e}")
                
        
        
        
        
    


def make_data():
    conn = sqlite3.connect("user_info.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_info (
        id integer PRIMARY KEY AUTOINCREMENT,
        name TEXT, 
        email TEXT, 
        username TEXT, 
        password TEXT,
        created_on DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
    conn.commit()
    conn.close()


def insert_user(name, email, username, password):
    """Insert a user into the system"""
    conn = sqlite3.connect("user_info.db")
    c = conn.cursor()
    c.execute('''INSERT INTO user_info (name, email, username, password)
              VALUES (?, ?, ?, ?)''', (name, email, username, password))
    conn.commit()
    conn.close()
    
def check_data(email, username):
    conn = sqlite3.connect("user_info.db")
    c = conn.cursor()
    c.execute("""
              SELECT id 
              FROM  user_info
              WHERE email = ?
              OR username = ?
            """, (email, username))
    records = c.fetchall()
    conn.close()
    return records

def check_user(username, password):
    conn = sqlite3.connect("user_info.db")
    c = conn.cursor()
    c.execute("""
              SELECT * FROM user_info
              WHERE username = ?
              AND password = ?
            """, (username, password))
    records = c.fetchall()
    conn.close()
    return records


if __name__ == '__main__':
    make_data()
    