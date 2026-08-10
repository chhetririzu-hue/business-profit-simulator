import streamlit as st

st.title("Business Profit Simulator")
st.write("Test different business scenarios and see how they affect profit.")

selling_price = st.number_input("selling Price ($)", min_value=0.0, value=0.0)
unit_sold = st.number_input("Units Sold", min_value=0, value=0, step=1)
cost_per_unit = st.number_input("Cost per Unit ($)", min_value=0.0, value=0.0)
fixed_costs = st.number_input("Fixed Costs ($)", min_value=0.0, value=0.0)
marketing_costs = st.number_input("Marketing Costs ($)", min_value=0.0, value=0.0)

revenue = selling_price * unit_sold
variable_costs = cost_per_unit * unit_sold
total_costs = variable_costs + fixed_costs + marketing_costs
profit = revenue - total_costs

if revenue > 0:
    profit_margin = (profit / revenue) * 100
else:
    profit_margin = 0.0

st.write(f"Revenue: ${revenue:.2f}")
st.write(f"Variable Costs: ${variable_costs:.2f}")
st.write(f"Total Costs: ${total_costs:.2f}")
st.write(f"Profit: ${profit:.2f}")
st.write(f"Profit Margin: {profit_margin:.2f}%")

if selling_price > cost_per_unit:
    break_even_units = (fixed_costs + marketing_costs) / (selling_price - cost_per_unit)
else:
    break_even_units = 0

st.write(f"Break-even Units: {break_even_units:.2f}")