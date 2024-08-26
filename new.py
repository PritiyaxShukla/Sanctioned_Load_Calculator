import streamlit as st
import numpy as np

user_type = st.selectbox("For what type of load you are calculating",('Home','Industry'))

st.image('Electricity Bill Demand.jpg')
    

option = np.arange(1,10000)




def appliance(appliances):

    names = []
    quantities = []
    wattages =[]

    for i in appliances:
        col1,col2,col3 =st.columns(3)
        
        with col1:
            st.write(f"{i}")
            names.append(i)
        with col2:
            quantity = st.number_input(f"no. of {i}",step=1)
            quantities.append(quantity)
        with col3:
            wattage = st.selectbox(f"please fill the no. watt per {i}",option,key=(f"{i}"))
            wattages.append(wattage)
    return names,quantities,wattages

def calculation(quantities,wattages):

    total = 0
    for i in range(len(quantities)):
        
        cal = (quantities[i]*wattages[i])+(total)
        total = cal
    
    sanctioned_load = (0.8*total)/1000
    return total,sanctioned_load


appliances = ['bulbs', 'tubelights', 'coolers', 'air_conditioners', 'fans', 'refrigerators', 'washing_machines', 'wifi_routers', 'water_purifiers','Motor', 'other_appliances']



if user_type == 'Home':
    names,quantities,wattages = appliance(appliances)

else:
    appliances += ['Machine 1','Machine 2','Machine 3','Machine 4','Other Appliances']
    name,quantities,wattages = appliance(appliances)


if st.button("Calculate Total Load"):
    total,sanctioned_load = calculation(quantities,wattages)
    st.write("Total Load=",total)
    st.write("Sanction Load Should Be Approx. = ",sanctioned_load)