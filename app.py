import streamlit as st
import plotly.graph_objects as go

if "scenario_count" not in st.session_state:
    st.session_state.scenario_count = 1

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

scenarios = []

if st.button("Add Scenario"):
    st.session_state.scenario_count += 1
    
for i in range(2, st.session_state.scenario_count + 1):
    with st.expander(f"Scenario {i}"):
        scenario_price = st.number_input(f"Scenario {i} Selling Price ($)", min_value=0.0, value=0.0, key=f"scenario_{i}_price")
        scenario_units_sold = st.number_input(f"Scenario {i} Units Sold", min_value=0, value=0, step=1, key=f"scenario_{i}_units_sold")
        scenario_cost_per_unit = st.number_input(f"Scenario {i} Cost per Unit ($)", min_value=0.0, value=0.0, key=f"scenario_{i}_cost_per_unit")
        scenario_fixed_costs = st.number_input(f"Scenario {i} Fixed Costs ($)", min_value=0.0, value=0.0, key=f"scenario_{i}_fixed_costs")
        scenario_marketing_costs = st.number_input(f"Scenario {i} Marketing Costs ($)", min_value=0.0, value=0.0, key=f"scenario_{i}_marketing_costs")

        scenario_revenue = scenario_price * scenario_units_sold
        scenario_variable_costs = scenario_cost_per_unit * scenario_units_sold
        scenario_total_costs = scenario_variable_costs + scenario_fixed_costs + scenario_marketing_costs
        scenario_profit = scenario_revenue - scenario_total_costs

        if scenario_revenue > 0:
            scenario_profit_margin = (scenario_profit / scenario_revenue) * 100

        else:
            scenario_profit_margin = 0.0

        scenarios.append({
            "name": f"Scenario {i}",
            "profit": scenario_profit,
            "profit_margin": scenario_profit_margin
        })

        profit_difference = scenario_profit - profit

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"### Scenario {i}")
            st.metric("Profit", f"${scenario_profit:.2f}")
            st.metric("Profit Margin", f"{scenario_profit_margin:.2f}%")

        with col2:
            st.metric("Profit Difference", f"${profit_difference:.2f}")

        if profit_difference > 0:
            st.success(f"Scenario {i} is more profitable by ${profit_difference:.2f}")
        elif profit_difference < 0:
            st.error(f"Scenario {i} is less profitable by ${-profit_difference:.2f}") 
        else:
            st.info(f"Scenario {i} has the same profit as the current scenario.")

scenarios.append({
    "name": "Current Scenario",
    "profit": profit,
    "profit_margin": profit_margin})

if scenarios:
    highest_profit = max(scenario["profit"] for scenario in scenarios)

    best_scenarios = [
        scenario for scenario in scenarios
        if scenario["profit"] == highest_profit
    ]

    if len(best_scenarios) > 1:
        names = ", ".join(scenario["name"] for scenario in best_scenarios)
        st.info(
            f"Best Scenarios are tied: {names} "
            f"with a profit of ${highest_profit:.2f}"
        )
    else:
        best_scenario = best_scenarios[0]
        st.success(
            f'Best Scenario: {best_scenario["name"]} '
            f'with Profit: ${best_scenario["profit"]:.2f} '
            f'and Profit Margin: {best_scenario["profit_margin"]:.2f}%'
        )

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

st.subheader("Export Results")

import pandas as pd

data = {
    "Metric": [
        "Revenue",
        "Total Costs",
        "Profit",
        "Profit Margin",
        "Break-even Units",
        "Break-even Revenue"
    ],
    "Current Scenario": [
        revenue,
        total_costs,
        profit,
        profit_margin,
        break_even_units,
        break_even_revenue
    ],
    "Scenario 2": [
        scenario2_revenue,
        scenario2_total_costs,
        scenario2_profit,
        scenario2_profit_margin,
        None,
        None
    ]
}

df = pd.DataFrame(data)
csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="business_metrics.csv",
    mime="text/csv"
)