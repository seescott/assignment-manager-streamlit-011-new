import streamlit as st

# Step 1: Header first (text elements)
st.title("Course Manager")
st.header("Course Assignments Manager")
st.subheader("Course Assignments Manager")
st.divider()

# Step 2: Define assignments list (data continuity)

assignments = [
    {
    "id" : "HW1",
    "title" : "Intro to Database",
    "description" : "basics of database design",
    "points" : 100,
    "type" : "homework"
    },
    {
    "id" : "HW2",
    "title" : "Normalization",
    "description" : "normalizing",
    "points" : 100,
    "type" : "homework"
    }
]

# Step 3: Add New Assignment Section


#col1, col2 = st.columns(2) --> This will give you 50%/50%
st.subheader("Add New Assignment")

with st.container(border=True):
    col1, col2 = st.columns([2,1])

    with col1:
        with st.container(border=True):
            st.markdown("### Assignment Details")
            title = st.text_input("Assignment Title",placeholder="homework1", help="enter a short name")
            description  = st.text_area("Assignment Description",placeholder="ex. details...")

    with col2:
        st.markdown("**Due Date Selection**")
        due_date = st.date_input("Due Date")