
import streamlit as st
import pandas as pd

# Display the main image and header
st.image('logomain.jpg')
st.header('*Check the SideBar on the left for interesting features of BlackBus*')

# Sidebar layout
with st.sidebar:
    c1, c2 = st.columns(2)
    with c1:
        st.header("*Welcome to BlackBus*")
        st.subheader("*Find the Best Suitable Bus for your comfort!*")
    with c2:
        st.image('logo.jpg')
    st.subheader('Choose your Bus preference', divider="gray")
    
    # Load data
    gov_data = pd.read_csv('Government_Bus.csv')
    prv_data = pd.read_csv('Private_Bus.csv')

    # Checkboxes for user input
    Government_Bus_Details = st.checkbox('Government_Bus_Details')
    Private_Bus_Details = st.checkbox('Private_Bus_Details')

# Government Bus Details
if Government_Bus_Details:
    c3, c4 = st.columns([4, 3])
    with c4:
        gov_search_box = st.text_input('Search for Government Bus Route:')
    with c3:
        st.subheader('To begin your Search, enter partial Route Name & press enter')

    gov_route_names = gov_data['Route_Name'].unique()
    filtered_gov_route_names = [gov_route_name for gov_route_name in gov_route_names if gov_search_box.lower() in gov_route_name.lower()]

    if filtered_gov_route_names:
        st.subheader('Choose your exact Route')
        selected_gov_route_name = st.selectbox('Select Route', filtered_gov_route_names)
        if selected_gov_route_name:
            # Filter data by selected route
            filtered_gov_route_name = gov_data[gov_data['Route_Name'] == selected_gov_route_name]

            # Dropdown for Bus_Type
            bus_types = filtered_gov_route_name['Bus_Type'].unique()
            selected_bus_type = st.selectbox('Select Bus Type', ['All'] + list(bus_types))

            if selected_bus_type != 'All':
                filtered_gov_route_name = filtered_gov_route_name[filtered_gov_route_name['Bus_Type'] == selected_bus_type]

            # Ensure columns are numeric
            filtered_gov_route_name['Price'] = pd.to_numeric(filtered_gov_route_name['Price'], errors='coerce')
            filtered_gov_route_name['Rating'] = pd.to_numeric(filtered_gov_route_name['Rating'], errors='coerce')

            # Check if there are multiple values for Price and Rating
            if gov_data['Price'].nunique() > 1:
                gov_min_price = float(gov_data['Price'].min())
                gov_max_price = float(gov_data['Price'].max())
            else:
                gov_min_price = gov_max_price = float(gov_data['Price'].iloc[0])
                
            if gov_data['Rating'].nunique() > 1:
                gov_min_rating = float(gov_data['Rating'].min())
                gov_max_rating = float(gov_data['Rating'].max())
            else:
                gov_min_rating = gov_max_rating = float(gov_data['Rating'].iloc[0])

            c7, c8 = st.columns(2)

            with c7:
                Gov_Price_Range = st.slider(
                    'Choose your Preferred Government Bus by Price:',
                    min_value=gov_min_price,
                    max_value=gov_max_price,
                    value=(gov_min_price, gov_max_price)
                )
            with c8:
                Gov_Rating_Range = st.slider(
                    'Choose your Preferred Government Bus by Rating:',
                    min_value=gov_min_rating,
                    max_value=gov_max_rating,
                    value=(gov_min_rating, gov_max_rating)
                )

            # Apply the price and rating filters
            filtered_gov_route_name = filtered_gov_route_name[
                (filtered_gov_route_name['Price'] >= Gov_Price_Range[0]) &
                (filtered_gov_route_name['Price'] <= Gov_Price_Range[1]) &
                (filtered_gov_route_name['Rating'] >= Gov_Rating_Range[0]) &
                (filtered_gov_route_name['Rating'] <= Gov_Rating_Range[1])
            ]

            st.write(filtered_gov_route_name)

    else:
        st.header('Oops!! No search results found')

# Private Bus Details
if Private_Bus_Details:
    c5, c6 = st.columns([4, 3])
    with c6:
        prv_search_box = st.text_input('Search for Private Bus Route:')
    with c5:
        st.subheader('To begin your Search, enter partial Route Name & press enter')

    prv_route_names = prv_data['Route_Name'].unique()
    filtered_prv_route_names = [prv_route_name for prv_route_name in prv_route_names if prv_search_box.lower() in prv_route_name.lower()]

    if filtered_prv_route_names:
        st.subheader('Choose your exact Route')
        selected_prv_route_name = st.selectbox('Select Route', filtered_prv_route_names)
        if selected_prv_route_name:
            # Filter data by selected route
            filtered_prv_route_name = prv_data[prv_data['Route_Name'] == selected_prv_route_name]

            # Dropdown for Bus_Type
            bus_types = filtered_prv_route_name['Bus_Type'].unique()
            selected_bus_type = st.selectbox('Select Bus Type', ['All'] + list(bus_types))

            if selected_bus_type != 'All':
                filtered_prv_route_name = filtered_prv_route_name[filtered_prv_route_name['Bus_Type'] == selected_bus_type]

            # Ensure columns are numeric
            filtered_prv_route_name['Price'] = pd.to_numeric(filtered_prv_route_name['Price'], errors='coerce')
            filtered_prv_route_name['Rating'] = pd.to_numeric(filtered_prv_route_name['Rating'], errors='coerce')

            # Check if there are multiple values for Price and Rating
            if prv_data['Price'].nunique() > 1:
                prv_min_price = float(prv_data['Price'].min())
                prv_max_price = float(prv_data['Price'].max())
            else:
                prv_min_price = prv_max_price = float(prv_data['Price'].iloc[0])
                
            if prv_data['Rating'].nunique() > 1:
                prv_min_rating = float(prv_data['Rating'].min())
                prv_max_rating = float(prv_data['Rating'].max())
            else:
                prv_min_rating = prv_max_rating = float(prv_data['Rating'].iloc[0])

            c9, c10 = st.columns(2)

            with c9:
                Prv_Price_Range = st.slider(
                    'Choose your Preferred Private Bus by Price:',
                    min_value=prv_min_price,
                    max_value=prv_max_price,
                    value=(prv_min_price, prv_max_price)
                )
            with c10:
                Prv_Rating_Range = st.slider(
                    'Choose your Preferred Private Bus by Rating:',
                    min_value=prv_min_rating,
                    max_value=prv_max_rating,
                    value=(prv_min_rating, prv_max_rating)
                )

            # Apply the price and rating filters
            filtered_prv_route_name = filtered_prv_route_name[
                (filtered_prv_route_name['Price'] >= Prv_Price_Range[0]) &
                (filtered_prv_route_name['Price'] <= Prv_Price_Range[1]) &
                (filtered_prv_route_name['Rating'] >= Prv_Rating_Range[0]) &
                (filtered_prv_route_name['Rating'] <= Prv_Rating_Range[1])
            ]

            st.write(filtered_prv_route_name)

    else:
        st.header('Oops!! No search results found')

# Feedback Section
st.write('Rate us from the count of 1 to 5 based on your experience with BlackBus.')
ratings = ['1','2','3','4','5']
selected = st.feedback("stars")
if st.button('Rate Us'):
    st.balloons()
    st.write(f'Thanks for your valuable feedback! You have rated us {selected+1} out of 5.')
st.markdown('**Want to share your thoughts? Share it with us**')
user_feedback = st.text_area('')
if st.button('Submit your Respose here'): 
    st.write("Thanks for your Feedback! It will help us Improve our Services!")
    st.balloons()






