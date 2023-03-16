# Define the necessary input data
historic_flow_data = [list of historic flow data]
upstream_reservoirs_data = [list of upstream reservoirs data]
downstream_reservoirs_data = [list of downstream reservoirs data]
water_demand_data = [list of water demand data]

# Define the necessary parameters
evaporation_rate = 0.2
inflow_variability = 0.1
outflow_variability = 0.1
downstream_release_policy = "Lowest Upper Bound"
upstream_diversion_policy = "Proportional Sharing"
water_loss_factor = 0.05
power_production_efficiency = 0.8

# Define the initial conditions
upstream_reservoirs_level = [list of initial upstream reservoirs levels]
downstream_reservoirs_level = [list of initial downstream reservoirs levels]
current_month = 1
cumulative_water_demand = 0
cumulative_power_production = 0

# Define the probabilistic fan chart parameters
num_scenarios = 1000
num_months_forecast = 12
forecast_inflows = [list of forecast inflows for the next num_months_forecast months]

# Define the main loop for the 24-month study period
for month in range(1, 25):
    # Update the upstream reservoir levels based on inflows, evaporation, and diversions
    upstream_inflow = [calculate upstream inflow for current month]
    upstream_diversion = [calculate upstream diversion for current month]
    upstream_reservoirs_level = [calculate new upstream reservoirs levels]
    
    # Update the downstream reservoir levels based on inflows, outflows, and water losses
    downstream_inflow = [calculate downstream inflow for current month]
    downstream_release = [calculate downstream release for current month based on downstream release policy]
    downstream_reservoirs_level = [calculate new downstream reservoirs levels]
    
    # Calculate the total flow of the Colorado River for the current month
    colorado_river_flow = [calculate total flow of the Colorado River]
    
    # Calculate the water demand for the current month
    water_demand = [calculate water demand for current month based on water demand data]
    unmet_water_demand = max(water_demand - downstream_release, 0)
    cumulative_water_demand += water_demand
    
    # Calculate the power production for the current month
    power_production = [calculate power production for current month based on upstream reservoirs level and power production efficiency]
    cumulative_power_production += power_production
    
    # Save the current month's data to the output file
    [write current month's data to output file]
    
    # Update the current month
    current_month += 1

# Generate the probabilistic fan chart for the next num_months_forecast months
fan_chart_data = []
for i in range(num_scenarios):
    scenario_forecast = [list of forecast inflows for scenario i]
    scenario_upstream_reservoirs_level = upstream_reservoirs_level.copy()
    scenario_downstream_reservoirs_level = downstream_reservoirs_level.copy()
    fan_chart_data.append([])
    for j in range(num_months_forecast):
        # Update the upstream reservoir levels based on scenario inflows, evaporation, and diversions
        upstream_inflow = scenario_forecast[j]
        upstream_diversion = [calculate upstream diversion for current month based on upstream_diversion_policy]
        scenario_upstream_reservoirs_level = [calculate new upstream reservoirs levels based on scenario inflows, evaporation, diversions, and water losses]

        # Update the downstream reservoir levels based on scenario infl
