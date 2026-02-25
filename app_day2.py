import streamlit as st

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignment Manager")

st.divider()

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

#Add New Assignment
st.markdown("# Add New Assignment")

#Input
st.markdown("### Title")

title = st.text_input("Assignment Title",placeholder="ex. homework1", help="This is the name of the assignment")

description = st.text_area("Description",placeholder="ex. database design...")

due_date = st.date_input("Due Date")

assignments_type = st.radio("Type",["homework", "lab"])

#assignments_type2 = st.selectbox("Type",["homework", "lab", "other"])

#if assignments_type2 == "other":
    #assignments_type2 = st.text_input("Assignment Type")

#lab = st.checkbox("Lab")

with st.expander("Assignment Preview",expanded=True):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")

btn_save = st.button("Save", width="stretch")

if btn_save:
    st.warning("Working on it!")

