import streamlit as st

# Set the title of the app
st.title("Dynamic Page Content with Selectbox")

# Create a selectbox for navigation
page = st.selectbox(
    "Choose A Player Position",
    ("GoalKeeper", "Defender", "Midfield", "Attack")
)

# Display content based on the selected page
if page == "GoalKeeper":
    st.header("Welcome To The Checker")
    height = st.number_input("GoalKeeper Height : ")
    appearance = st.number_input("GoalKeeper Appearance : ", step=1)
    clean_sheets = st.number_input("GoalKeeper Clean Sheets : ")
    minutes_played = st.number_input("GoalKeeper Minutes Played : ", step=1)
    games_injured = st.number_input("GoalKeeper Games Injured : ", step=1)
    award = st.number_input("GoalKeeper award : ", step=1)
    highest_value = st.number_input("GoalKeeper Highest Value : ", step=1)

    # Prediction button
    if st.button("Predict Category"):
        # API request URL
        url = "https://the-penguin.onrender.com/predict"
        
        # Data for the POST request
        data = {
            "Year": year,
            "Engine_Size": engine_size,
            "Mileage": mileage,
            "Type": car_type,
            "Make": make,
            "Options": options
        }

        # Send the POST request
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Check for request errors
            prediction = response.json()  # Parse JSON response
            # {'Cheap_Price': 0, 'Good_Price': 1, 'High_Price': 2}

            if prediction['pred'] == 0:
                prediction = "Cheap Price"
            elif prediction['pred'] == 1:
                prediction = "Good Price"
            elif prediction['pred'] == 2:
                prediction = "High Price"
                
            st.write(f"Estimated Price: {prediction}")
        except requests.exceptions.RequestException as e:
            st.error("Error requesting prediction from API. Please try again.")
            st.write(e)
    
elif page == "Defender":
    st.header("Welcome To The Checker")
    st.write("This app demonstrates how to change content dynamically based on the selectbox.")
    
elif page == "Midfield":
    st.header("Welcome To The Checker")
    st.write("For inquiries, please reach out to contact@example.com.")

elif page == "Attack":
    st.header("Welcome To The Checker")
    st.write("For inquiries, please reach out to contact@example.com.")
