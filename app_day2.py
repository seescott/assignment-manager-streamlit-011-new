import streamlit as st

st.title("Course Management App")
st.header("Assignments")
st.subheader("Assignment Manager")

next_assignment_id_number = 3

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

points = st.number_input("Points")
#assignments_type2 = st.selectbox("Type",["homework", "lab", "other"])

#if assignments_type2 == "other":
    #assignments_type2 = st.text_input("Assignment Type")

#lab = st.checkbox("Lab")

with st.expander("Assignment Preview",expanded=True):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")
    st.markdown(f"Description: {description}")
    st.markdown(f"Due Date: {due_date}")
    st.markdown(f"Type: {assignments_type}")

btn_save = st.button("Save", use_container_width=True, disabled=False)
import time

if btn_save:
    with st.spinner("Saving Assignment..."):
        time.sleep(5)
        if title == "":
            st.warning("Enter Assignment Title")
        new_assignment_id = "HW_" + str(next_assignment_id_number)
        next_assignment_id_number += 1
        assignments.append({
            "id" : new_assignment_id,
            "title" : title,
            "description" : description,
            "points" : points,
            "type" : assignments_type
        }
        )

        st.success("Assignment is recorded!!")
        st.dataframe(assignments)


