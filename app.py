import streamlit as st
import plotly.graph_objects as go

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

break_even_revenue = break_even_units * selling_price
unts_difference = unit_sold - break_even_units

if selling_price <= cost_per_unit:
    break_even_message = "Break-even is not possible."
elif unts_difference > 0:
    break_even_message = f"You are above the break-even point by {unts_difference:.2f} units."
elif unts_difference < 0:
    break_even_message = f"You are below the break-even point by {-unts_difference:.2f} units."
else:
    break_even_message = "You are at the break-even point."



st.subheader("Business Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Revenue", f"${revenue:.2f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")
col2.metric("Profit", f"${profit:.2f}")

col4, col5 = st.columns(2)
col4.metric("Toal Costs", f"${total_costs:.2f}")
col5.metric("Break-even Units", f"{break_even_units:.2f}")
col5.metric("Break-even Revenue", f"${break_even_revenue:.2f}")
col5.write(break_even_message)

if profit > 0:
    st.success(f"Profit: ${profit:.2f}")
elif profit < 0:
    st.error(f"Loss: ${-profit:.2f}")   
else:
    st.info("Break-even: No profit or loss.")

st. subheader("Business Performance")
fig = go.Figure()
fig.add_trace(go.Bar(
    x=["Revenue", "Total Costs", "Profit"],
    y=[revenue, total_costs, profit],
))

st.plotly_chart(fig, use_container_width=True)

st.subheader("Scenario Comparison")
st.write("Enter a second set of business assumptions to compare against the current scenario.")

senario2_price = st.number_input("Scenario 2 Selling Price ($)", min_value=0.0, value=0.0)
senario2_units_sold = st.number_input("Scenario 2 Units Sold", min_value=0, value=0, step=1)

senario2_cost_per_unit = st.number_input("Scenario 2 Cost per Unit ($)", min_value=0.0, value=0.0)
senario2_fixed_costs = st.number_input("Scenario 2 Fixed Costs ($)", min_value=0.0, value=0.0)
senario2_marketing_costs = st.number_input("Scenario 2 Marketing Costs ($)", min_value=0.0, value=0.0)

senario2_revenue = senario2_price * senario2_units_sold
senario2_variable_costs = senario2_cost_per_unit * senario2_units_sold
senario2_total_costs = senario2_variable_costs + senario2_fixed_costs + senario2_marketing_costs
senario2_profit = senario2_revenue - senario2_total_costs

if senario2_revenue > 0:
    senario2_profit_margin = (senario2_profit / senario2_revenue) * 100
else:
    senario2_profit_margin = 0.0

profit_difference = senario2_profit - profit

col1, col2 = st.columns(2)

with col1:
    st.write("### Current Scenario")
    st.metric("Profit", f"${profit:.2f}")
    st.metric("Profit Margin", f"{profit_margin:.2f}%")

with col2:
    st.write("### Scenario 2")
    st.metric("Profit", f"${senario2_profit:.2f}")
    st.metric("Profit Margin", f"{senario2_profit_margin:.2f}%")
    st.metric("Profit Difference", f"${profit_difference:.2f}")

if profit_difference > 0:
    st.success(f"Scenario 2 is more profitable by ${profit_difference:.2f}")
elif profit_difference < 0:
    st.error(f"Scenario 2 is less profitable by ${-profit_difference:.2f}") 
else:
    st.info("Both scenarios have the same profit.")

st.subheader("Monthly Profit Projection")
projection_months = st.number_input("Number of Months", min_value=1, value=12, step=1)
months = list(range(1, projection_months + 1))
monthly_growth_rate = st.number_input("Monthly Growth Rate (%)", value=0.0, step=1.0)
projected_profit = []
current_profit = profit
for month in months:
    projected_profit.append(current_profit)
    current_profit = current_profit * (1 + monthly_growth_rate / 100)
projection_fig = go.Figure()

projection_fig.add_trace(go.Scatter(
    x=months,
    y=projected_profit,
    mode='lines+markers',
    name='Projected Profit',
))

st.plotly_chart(projection_fig, use_container_width=True)



projection_fig.update_layout(
    title="Projected Profit Over Time",
    xaxis_title="Month",
    yaxis_title="Profit ($)"
)