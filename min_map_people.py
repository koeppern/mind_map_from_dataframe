import pandas as pd
import graphviz
import streamlit as st
import pandas as pd
import graphviz


def create_mind_map(df, group_by):

    
    # Define the criteria for grouping the data
    grouped = df.groupby(group_by)

    # Create a Graphviz dot object
    dot = graphviz.Digraph()

    # Add the root node
    dot.node(group_by.capitalize(), shape="ellipse")

    # Loop through the groups and add child nodes for each group
    for name, group in grouped:
        group_node = str(name)

        dot.node(group_node, shape="ellipse")
        dot.edge(group_by.capitalize(), group_node)
        
        for index, row in group.iterrows():
            dot.node(row["name"], shape="box")
            dot.edge(group_node, row["name"])
    
    # Render the mind map
    dot.render(f"mind_map", format="png", view=False)

df = df = pd.DataFrame({"name":["anton", "berta", "claudia", "daniela"], 
                        "sex":["male","female","female","female"], 
                        "adult":["yes","yes","no","no"]})




st.title("Create minmaps.")

st.write("2023-03-11, Johannes Köppern")

st.header("Date (interactive)")

edited_df = st.experimental_data_editor(df,
                                        num_rows="dynamic")

st.header("Mind map")

group_by_selection= st.selectbox("Select a column:", options=df.columns)

create_mind_map(edited_df, group_by_selection)

st.image("mind_map.png")
