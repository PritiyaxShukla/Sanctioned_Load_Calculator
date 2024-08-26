import streamlit as st

st.header("Load Survey and Sanction Load Calculator by Pritiyax Shukla")
st.image('Electricity Bill Demand.jpg')

usage_type = st.selectbox("Select the type of connection:", ('Home', 'Industry'))

def calculate_load(appliances):
    total_load = sum(appliances[appliance]['quantity'] * appliances[appliance]['wattage'] for appliance in appliances)
    sanctioned_load = (0.8 * total_load) / 1000
    return total_load, sanctioned_load

def get_appliance_inputs(appliance_list):
    appliances = {}
    for appliance in appliance_list:
        appliances[appliance] = {
            'quantity': st.number_input(f"Number of {appliance.capitalize()}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per {appliance.capitalize()}", (1, 9, 14, 20, 40, 60, 70, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000))
        }
    return appliances

default_appliances = ['bulbs', 'tubelights', 'coolers', 'air_conditioners', 'fans', 'refrigerators', 'washing_machines', 'wifi_routers', 'water_purifiers', 'other_appliances']

if usage_type == 'Home':
    st.write("Please fill in the necessary fields to calculate your Home Load")
    appliances = get_appliance_inputs(default_appliances)
elif usage_type == 'Industry':
    st.write("Please fill in the necessary fields to calculate your Industry Load")
    default_appliances += ['computers', 'machines']  # Add industry-specific appliances
    appliances = get_appliance_inputs(default_appliances)

if st.button('add_row'):
    name = st.text_input("Enter the name of the New Appliance")
    if name:
            default_appliances +=[name]
            appliances = get_appliance_inputs(default_appliances)

if st.button("Calculate Load"):
    total_load, sanctioned_load = calculate_load(appliances)
    st.write(f"The Total Load is {total_load} Watt")
    st.write(f"The Sanctioned Load should be {sanctioned_load} KW")
