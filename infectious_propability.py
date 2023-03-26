"""
infectious_propability.py
2023-03-26, J. Köppern

Streamlit, 
determine the propability of meeting somesone infectious  dependent on the incidence 
"""
import streamlit as st

# Set page title and subtitle
st.title("Probability of Meeting Someone Infectious")
st.subheader("2023-03-26, J. Köppern")

incidence = st.text_input("Incidence (infections per 100.000)")
n_people = st.text_input("Number of people met")
unreported_min = st.text_input("Minimum number of unreported cases", value="1")
unreported_max = st.text_input("Maximum number of unreported cases", value="10")


# Create a button to calculate probability
if st.button("Calculate Probability"):
    def p(unreported):
        this_p = 1 - ((1 - incidence / 100000 * unreported)**n_people)

        return this_p
    
    # Convert input strings to numbers
    incidence = float(incidence)
    n_people = int(n_people)
    unreported_min = int(unreported_min)
    unreported_max = int(unreported_max)

    p_min = round(p(unreported_min), 3)
    p_max = round(p(unreported_max), 3)

    st.write(f"{p_min * 100} % <= p < {p_max * 100} %")
