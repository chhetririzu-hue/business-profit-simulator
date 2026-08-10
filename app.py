import streamlit as st

st.title("Business Profit Simulator")
st.write("Test different business scenarios and see how they affect profit.")

selling_price = st.number_input("selling Price ($)", min_value=0.0, value=0.0)
unit_sold = st.number_input("Units Sold", min_value=0, value=0, step=1)
cost_per_unit = st.number_input("Cost per Unit ($)", min_value=0.0, value=0.0)
fixed_costs = st.number_input("Fixed Costs ($)", min_value=0.0, value=0.0)
marketing_costs = st.number_input("Marketing Costs ($)", min_value=0.0, value=0.0)