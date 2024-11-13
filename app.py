import requests
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
        url = "https://football-players-transfer.onrender.com/goalkeeper/predict"
        
        # Data for the POST request
        data = {
            "height": height,
            "appearance": appearance,
            "clean_sheets": clean_sheets,
            "minutes_played": minutes_played,
            "games_injured": games_injured,
            "award": award,
            "highest_value": highest_value,
        }

        # Send the POST request
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Check for request errors
            prediction = response.json()  # Parse JSON response

            if prediction['pred'] == 0:
                prediction = "High Value"
            elif prediction['pred'] == 1:
                prediction = "Normal Value"
                
            st.write(f"The Value Of The GoalKeeper : {prediction}")
        except requests.exceptions.RequestException as e:
            st.error("Error requesting prediction from API. Please try again.")
            st.write(e)
    
elif page == "Defender":
    st.header("Welcome To The Checker")
    height = st.number_input("Defender Height : ")
    appearance = st.number_input("Defender Appearance : ", step=1)
    minutes_played = st.number_input("Defender Minutes Played : ", step=1)
    games_injured = st.number_input("Defender Games Injured : ", step=1)
    award = st.number_input("Defender award : ", step=1)
    highest_value = st.number_input("Defender Highest Value : ", step=1)

    # Prediction button
    if st.button("Predict Category"):
        # API request URL
        url = "https://football-players-transfer.onrender.com/defender/predict"
        
        # Data for the POST request
        data = {
            "height": height,
            "appearance": appearance,
            "minutes_played": minutes_played,
            "games_injured": games_injured,
            "award": award,
            "highest_value": highest_value,
        }

        # Send the POST request
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Check for request errors
            prediction = response.json()  # Parse JSON response

            if prediction['pred'] == 0:
                prediction = "High Value"
            elif prediction['pred'] == 1:
                prediction = "Normal Value"
                
            st.write(f"The Value Of The Defender : {prediction}")
        except requests.exceptions.RequestException as e:
            st.error("Error requesting prediction from API. Please try again.")
            st.write(e)
    
elif page == "Midfield":
    st.header("Welcome To The Checker")
    height = st.number_input("Midfield Height : ")
    appearance = st.number_input("Midfield Appearance : ", step=1)
    goals = st.number_input("Midfield Goals : ")
    assists = st.number_input("Midfield Assists : ")
    minutes_played = st.number_input("Midfield Minutes Played : ", step=1)
    games_injured = st.number_input("Midfield Games Injured : ", step=1)
    award = st.number_input("Midfield award : ", step=1)
    highest_value = st.number_input("Midfield Highest Value : ", step=1)

    # Prediction button
    if st.button("Predict Category"):
        # API request URL
        url = "https://football-players-transfer.onrender.com/midfield/predict"
        
        # Data for the POST request
        data = {
            "height": height,
            "appearance": appearance,
            "goals": goals,
            "assists": assists,
            "minutes_played": minutes_played,
            "games_injured": games_injured,
            "award": award,
            "highest_value": highest_value,
        }

        # Send the POST request
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Check for request errors
            prediction = response.json()  # Parse JSON response

            if prediction['pred'] == 0:
                prediction = "High Value"
            elif prediction['pred'] == 1:
                prediction = "Normal Value"
                
            st.write(f"The Value Of The Midfield : {prediction}")
        except requests.exceptions.RequestException as e:
            st.error("Error requesting prediction from API. Please try again.")
            st.write(e)

elif page == "Attack":
    st.header("Welcome To The Checker")
    appearance = st.number_input("Attack Appearance : ", step=1)
    goals = st.number_input("Attack Goals : ")
    assists = st.number_input("Attack Assists : ")
    minutes_played = st.number_input("Attack Minutes Played : ", step=1)
    games_injured = st.number_input("Attack Games Injured : ", step=1)
    award = st.number_input("Attack award : ", step=1)
    highest_value = st.number_input("Attack Highest Value : ", step=1)

    # Prediction button
    if st.button("Predict Category"):
        # API request URL
        url = "https://football-players-transfer.onrender.com/attack/predict"
        
        # Data for the POST request
        data = {
            "appearance": appearance,
            "goals": goals,
            "assists": assists,
            "minutes_played": minutes_played,
            "games_injured": games_injured,
            "award": award,
            "highest_value": highest_value,
        }

        # Send the POST request
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Check for request errors
            prediction = response.json()  # Parse JSON response

            if prediction['pred'] == 0:
                prediction = "High Value"
            elif prediction['pred'] == 1:
                prediction = "Normal Value"
                
            st.write(f"The Value Of The Attack : {prediction}")
        except requests.exceptions.RequestException as e:
            st.error("Error requesting prediction from API. Please try again.")
            st.write(e)

