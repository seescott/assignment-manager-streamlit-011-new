import streamlit as st
import json
from pathlib import Path
import datetime
import uuid
import time

st.set_page_config(page_title = "Course Manager",
                  layout = "centered")


users =  [ 
    {
 "id": "1",
 "email": "admin@school.edu",
 "full_name": "System Admin",
 "password": "123ssag@43AE",
 "role": "Admin",
 "registered_at": "..."
}
]

json_path = Path("users.json")

if json_path.exists():
    with json_path.open("r", encoding = "utf-8") as f:
        users = json.load(f)

tab1, tab2 = st.tabs(["Register", "Login"])
with tab1:
    st.title("Register")
    st.header("New Instructor Account")

    email = st.text_input("Email Address",placeholder="ex. myemailadress@school.edu")

    name = st.text_area("First and Last Name",placeholder="ex. John Doe")

    password = st.text_input("Password", type="password")

    role = st.radio("Role",["Instructor"])


    btn_save = st.button("Create Account", use_container_width=True, disabled=False)
    if email and name and password and role:
        new_user = {
            "id": str(uuid.uuid4()),
            "email": email,
            "full_name": name,
            "password": password,
            "role": role,
            "registered_at": datetime.datetime.now().isoformat()
        }

        with st.spinner("Creating your account..."):
            time.sleep(4)
        users.append(new_user)
        with json_path.open("w", encoding="utf-8") as f:
            json.dump(users, f, indent=4)
        st.success("Account created successfully!")
    else:
        st.error("Please fill in all the fields.")

with tab2:
    with st.container(border = True):
        st.markdown("#Log in")
        user_name = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login", type = "primary", key = "login_button", use_container_width=True):
            with st.spinner("Checking the login...."):
                time.sleep(4)



