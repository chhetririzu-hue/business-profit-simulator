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


if selling_price > cost_per_unit:
    break_even_units = (fixed_costs + marketing_costs) / (selling_price - cost_per_unit)
else:
    break_even_units = 0



st.subheader("Business Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Revenue", f"${revenue:.2f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")
col2.metric("Profit", f"${profit:.2f}")

col4, col5 = st.columns(2)
col4.metric("Toal Costs", f"${total_costs:.2f}")
col5.metric("Break-even Units", f"{break_even_units:.2f}")

if profit > 0:
    st.success(f"Profit: ${profit:.2f}")
elif profit < 0:
    st.error(f"Loss: ${-profit:.2f}")   
else:
    st.info("Break-even: No profit or loss.")
    