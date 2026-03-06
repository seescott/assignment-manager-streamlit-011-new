
import streamlit as st
import time
import json
from pathlib import Path

st.set_page_config(page_title = "Course Management",
                   page_icon = "🎓",
                   layout = "centered",
                   initial_sidebar_state = "collapsed")

json_path = Path("assignments.json")

if json_path.exists:
    with json_path.open("r", encoding = "utf-8") as f:
        assignments = json.load(f)

tab1, tab2, tab3 = st.tabs(["View Assignments", "Add new assignment", "Update an assignment"])

with tab1:
    tab_options = st.radio("View/Search", ["View", "Search"], horizontal = True)
    if tab_options == "View":
        st.dataframe(assignments)
    else: 
        titles = []
        for assignment in assignments:
            titles.append(assignment["title"])

        selected_title = st.selectbox("Select a title", titles, key = "selected_title")

        selected_assignment = {}

        for assignment in assignments:
            if assignment["title"] == selected_title:
                selected_assignment = assignment
                break

        st.divider()

        selected_assignment = st.selectbox("Select Title", options=assignments, format_func=lambda x:f"{x['title']}({x['type']})")

        if selected_assignment:
            with st.expander("Assignment Details", expanded=True):
                st.markdown(f"### Title: {selected_assignment['title']}")
                st.markdown(f"### Description: {selected_assignment['description']}")
                st.markdown(f"Type: **{selected_assignment['type']}**")

                
with tab2:

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

    ##Recording the data into an actual file 
            with json_path.open("w", encoding = "utf-8") as f:
                json.dump(assignments,f)

    st.success("Assignment is Recorded!")
    st.info("This is a new assignment")
    time.sleep(4)
    #st.dataframe(assignments)
    st.rerun()

with tab3:
    st.markdown("### Update an Assignment")
    titles = []

    for assignment in assignments:
        titles.append(assignment["title"])


    selected_title = st.selectbox("Select a title", titles, key = "selected_title_edit")


    assignment_edit = {}
    for assignment in assignments:
        if assignment["title"] == selected_title:
            assignment_edit = assignment
            break

    if assignment_edit:
        edit_title = st.text_input("Title", key=f"edit_title_{assignment_edit['id']}", 
                                   value=assignment_edit["title"])
        edit_description = st.text_area("Description", key=f"edit_description_{assignment_edit['id']}", 
                                        value=assignment_edit["description"])
        
        type_options = ["homework", "lab"]
        selected_index = type_options.index(assignment_edit["type"])

        edit_type = st.radio("Type", [type_options], key=f"edit_type_{assignment_edit['id']}", index=selected_index)

    btn_update = st.button("Update", key="update_button", type="secondary", use_container_width=True)
    if btn_update:
        with st.spinner("Updating Assignment..."):
            time.sleep(5)
            assignment_edit["title"] = edit_title
            assignment_edit["description"] = edit_description
            assignment_edit["type"] = edit_type

        with json_path.open("w", encoding = "utf-8") as f:
            json.dump(assignments,f)
       
        st.success("Asssignment is udpated!")
        time.sleep(5)
        st.rerun()

with st.sidebar:
    st.markdown("Sidebar")
