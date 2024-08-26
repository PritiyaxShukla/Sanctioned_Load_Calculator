import streamlit as st

# Header and Image
st.header("Load Survey and Sanction Load Calculator by Pritiyax Shukla")
st.image('Electricity Bill Demand.jpg')

# Selectbox for Usage Type
usage_type = st.selectbox("Select the type of connection:", ('Home', 'Industry'))

# Initialize session state for dynamic rows
if 'industry_rows' not in st.session_state:
    st.session_state.industry_rows = [{'id': 1}]

# Function to calculate load
def calculate_load(appliances):
    total_load = sum(appliances[appliance]['quantity'] * appliances[appliance]['wattage'] for appliance in appliances)
    sanctioned_load = (0.8 * total_load) / 1000
    return total_load, sanctioned_load

# Function to add a new row for industry mode
def add_row():
    new_id = len(st.session_state.industry_rows) + 1
    st.session_state.industry_rows.append({'id': new_id})

# User Inputs for Home
if usage_type == 'Home':
    st.write("Please fill in the necessary fields to calculate your Home Load")

    appliances = {
        'bulbs': {
            'quantity': st.number_input("Number of Bulbs", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Bulb", (1, 9, 14, 20, 40, 60, 70, 100))
        },
        'tubelights': {
            'quantity': st.number_input("Number of Tubelights", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Tubelight", (20, 40, 50, 60, 70, 100))
        },
        'tvs': {
            'quantity': st.number_input("Number of Televisions", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Television", (50, 60, 70, 100, 150, 170, 190, 200))
        },
        'coolers': {
            'quantity': st.number_input("Number of Coolers", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Cooler", (70, 90, 100, 120, 130, 150, 190, 200, 220, 250, 300))
        },
        'air_conditioners': {
            'quantity': st.number_input("Number of Air Conditioners", min_value=0, step=1),
            'wattage': st.selectbox("Tonnage per Air Conditioner", (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5))
        },
        'fans': {
            'quantity': st.number_input("Number of Fans", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Fan", (20, 40, 50, 60, 70, 100))
        },
        'refrigerators': {
            'quantity': st.number_input("Number of Refrigerators", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Refrigerator", (300, 350, 400, 450, 550, 650, 700, 800))
        },
        'washing_machines': {
            'quantity': st.number_input("Number of Washing Machines", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Washing Machine", (400, 500, 700, 800, 900, 1200, 1500, 1600, 1700, 2000, 2200, 2500))
        },
        'wifi_routers': {
            'quantity': st.number_input("Number of Wifi Routers", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Wifi Router", (4, 5, 6, 9, 10, 12, 15, 20))
        },
        'water_purifiers': {
            'quantity': st.number_input("Number of Water Purifiers", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Water Purifier", (60, 70, 80, 90, 100, 110, 120, 150))
        },
        'other_appliances': {
            'quantity': st.number_input("Number of Other Appliances", min_value=0, step=1),
            'wattage': st.selectbox("Wattage per Other Appliance", (60, 70, 80, 90, 100, 110, 120, 150))
        }
    }

# User Inputs for Industry
elif usage_type == 'Industry':
    st.write("Please fill in the necessary fields to calculate your Industry Load")

    appliances = {}
    
    for row in st.session_state.industry_rows:
        row_id = row['id']
        st.write(f"Appliance Set {row_id}")

        appliances[f'bulbs_{row_id}'] = {
            'quantity': st.number_input(f"Number of Bulbs {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Bulb {row_id}", (1, 9, 14, 20, 40, 60, 70, 100))
        }

        appliances[f'tubelights_{row_id}'] = {
            'quantity': st.number_input(f"Number of Tubelights {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Tubelight {row_id}", (20, 40, 50, 60, 70, 100))
        }

        appliances[f'computers_{row_id}'] = {
            'quantity': st.number_input(f"Number of Computers {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Computer {row_id}", (200, 250, 300, 350, 400, 450, 500))
        }

        appliances[f'coolers_{row_id}'] = {
            'quantity': st.number_input(f"Number of Coolers {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Cooler {row_id}", (70, 90, 100, 120, 130, 150, 190, 200, 220, 250, 300))
        }

        appliances[f'air_conditioners_{row_id}'] = {
            'quantity': st.number_input(f"Number of Air Conditioners {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Tonnage per Air Conditioner {row_id}", (1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5))
        }

        appliances[f'fans_{row_id}'] = {
            'quantity': st.number_input(f"Number of Fans {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Fan {row_id}", (20, 40, 50, 60, 70, 100))
        }

        appliances[f'refrigerators_{row_id}'] = {
            'quantity': st.number_input(f"Number of Refrigerators {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Refrigerator {row_id}", (300, 350, 400, 450, 550, 650, 700, 800))
        }

        appliances[f'wifi_routers_{row_id}'] = {
            'quantity': st.number_input(f"Number of Wifi Routers {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Wifi Router {row_id}", (4, 5, 6, 9, 10, 12, 15, 20))
        }

        appliances[f'water_purifiers_{row_id}'] = {
            'quantity': st.number_input(f"Number of Water Purifiers {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Water Purifier {row_id}", (60, 70, 80, 90, 100, 110, 120, 150))
        }

        appliances[f'other_appliances_{row_id}'] = {
            'quantity': st.number_input(f"Number of Other Appliances {row_id}", min_value=0, step=1),
            'wattage': st.selectbox(f"Wattage per Other Appliance {row_id}", (60, 70, 80, 90, 100, 110, 120, 150))
        }

    # Button to add a new row
    if st.button("Add New Row"):
        add_row()

# Calculation button
if st.button("Calculate Load"):
    total_load, sanctioned_load = calculate_load(appliances)
    st.write(f"The Total Load is {total_load} Watt")
    st.write(f"The Sanctioned Load should be {sanctioned_load} KW")
