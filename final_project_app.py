##########################
# SYSEN5160 Final Project 
# Jamie Donahue (jmd543)
# May 13 2022
##########################
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time


# USER INPUT SECTION
with st.sidebar:
    st.title("*Happy, Heathly & You*")
    st.subheader('Hello beautiful! Congratulations on starting your journey to be the best version of you! Lets get started!')
    
    # Q1: Please input your height (cms)
    height = float(st.slider('How tall are you, in centimeters?', 0, 250, 125)) # Question, Min, Max, Default Value
    # Q2: Please input your weight (kgs)
    weight = float(st.slider('How much do you weigh, in kilograms?', 0, 250, 125)) # Question, Min, Max, Default Value
    # Q3: Please input your age (yrs)
    age = float(st.slider('How old are you, in years?', 0, 100, 50)) # Question, Min, Max, Default Value
    # Q4: Please input your gender (male or female)
    gender = st.radio(
     "What's your biological gender?",
     ('Male', 'Female'))

# If gender equals male
if gender == 'Male':
    BMR_calories = 88.362 + (13.397*weight) + (4.799*height) - (5.677*age)
# If gender equals female
else:
    BMR_calories = 447.593 + (9.247*weight) + (3.098*height) - (4.330*age)

# Calculate avg_workout_cals_1hr
weight_in = [20.0,   59.1,  70.5,  81.8,  93.2, 250.0]
cals_in = [139.0, 325.0, 387.0, 449.0, 512.0, 853.0]
avg_workout_cals = np.interp(weight, weight_in, cals_in)

with st.sidebar:
    # Please select your health goal
    goal = st.radio(
     "Please select your health goal",
     ('Maintain Weight', 'Lose Weight', 'Gain Weight'))

if goal == 'Maintain Weight':
     goal_weight = weight
else:
     goal_weight = weight - 1.0
   
# MAINTAIN WEIGHT SECTION
if goal == 'Maintain Weight':
    st.title('You are already awesome, keep doing what your doing!')
  
    body_specific_vids = st.selectbox(
     'If you would like some specific body part workouts though, please click any of the options below',
     ('Arms', 'Legs', 'Back', 'Abs', 'Glutes', 'Posture'))
    # Output Weekly Fitness Plan (Calories to Burn, Workout days, Exercise Duration, Fitness Videos)
    if body_specific_vids == 'Arms':
       st.video('https://www.youtube.com/watch?v=hAGfBjvIRFI&list=LL&index=8')  
    if body_specific_vids == 'Legs':
       st.video('https://www.youtube.com/watch?v=xpzMr3nSOIE&list=LL&index=10') 
    if body_specific_vids == 'Back':
       st.video('https://www.youtube.com/watch?v=5hVAUMZkJq4&list=LL&index=7&t=127s') 
    if body_specific_vids == 'Abs':
       st.video('https://www.youtube.com/watch?v=hxjKZcOT17E&list=LL&index=9') 
    if body_specific_vids == 'Glutes':
       st.video('https://www.youtube.com/watch?v=i1ZzdBgLtZg') 
    if body_specific_vids == 'Posture':
       st.video('https://www.youtube.com/watch?v=5R54QoUbbow')
      
# LOSE WEIGHT SECTION
if goal == 'Lose Weight':
    with st.sidebar:
        # Please input your goal weight if nesscary
        weight_goal = float(st.slider('Input goal weight, if appicable', 0, 250, int(goal_weight))) # Question, Min, Max, Default Value

    # Calculate variable delta_weight & calculate time_restriction (max +/-0.909 kgs/wk)
    delta_weight = weight_goal - weight
    time_restriction = abs(delta_weight) / 0.909 * 7.0
    time_restriction = datetime.timedelta(days=time_restriction)
    
    # Please input your timeline for achieving your health goals
    # Q1: Start Date (units days)
    # Q2: End Date (units days), minimum end date based on time_restriction
    with st.sidebar:
        st.subheader('That is a fabulous health goal! When would you like to achieve that by?')
        time_start = st.date_input('Start Date', value=datetime.datetime.now(), min_value=datetime.datetime.now(), max_value=datetime.date(2022, 12, 31))
        st.write('*To keep you safe during your journey, the earliest end date is limited too a max weight change of +/-0.909 kg per week ^u^*')
        time_end = st.date_input('End Date', value=datetime.datetime.now()+time_restriction, min_value=datetime.datetime.now()+time_restriction, max_value=datetime.date(2025, 12, 31))

    # Calculate time delta
    time_2_goal_d = float((time_end - time_start).days)
    # Convert to weeks
    time_2_goal_w = time_2_goal_d / 7.0
    # Calculate Weight Change Rate
    weight_change_rate = delta_weight / time_2_goal_w
    # Calculate Calorie Change Rate
    cal_change_rate = abs(weight_change_rate) * 7700.0
    # Calculate Daily Calorie Loss from Food Percentage
    food_cals_loss = cal_change_rate * 0.50 / 7.0
    # Calculate Weekly Calorie Loss from Workout Percentage
    workout_cals_loss = cal_change_rate * 0.50
        
    # Q1: How many days a week would you like to workout?
    with st.sidebar:
        st.subheader('Great! Now lets talk fitness')
        workout_days = st.selectbox(
         'How many days a week would you like to workout?',
          ('1', '2', '3', '4', '5', '6', '7'))

    # Calculate exercise_duration
    exercise_duration = ( workout_cals_loss / avg_workout_cals ) * (1.0 / float(workout_days) ) * 60.0

    # Options: Arms, Legs, Back, Abs, Glutes, Posture
    with st.sidebar:
        body_specific_vids = st.selectbox(
         'Do you have a specific body part that you would really like to tone? Select it below',
         ('Arms', 'Legs', 'Back', 'Abs', 'Glutes', 'Posture'))

    st.title('*You did it! Here is your personalized nutrtion and fitness plan! Good luck!*')
    # Calculate Alloted Daily Calories 
    daily_cals = BMR_calories - food_cals_loss
    # Calculate Macros from DB based on daily_cals (using recommendend 30% carbs, 40% protein, 30% fats balance)
    # Grams per calories calculated based on https://drbillsukala.com/macronutrient-calorie-gram-calculator/
    mac_cals_in = [500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0, 3500.0, 4000.0]
    macro_pro_in = [38.0,	75.0,	113.0,	150.0,	188.0,	225.0,	263.0,	300.0]
    macro_carb_in = [50.0,	100.0,	150.0,	200.0,	250.0,	300.0,	350.0,	400.0]
    macro_fat_in = [17.0,	33.0,	50.0,	67.0,	83.0,	100.0,	117.0,	133.0]

    daily_proteins = np.interp(daily_cals, mac_cals_in, macro_pro_in)
    daily_carbs = np.interp(daily_cals, mac_cals_in, macro_carb_in)
    daily_fats = np.interp(daily_cals, mac_cals_in, macro_fat_in)

    # Output Daily Nutrition Plan (Daily Calories, Macros, Food Database)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Daily Calories", np.round(daily_cals,0))
    col2.metric("Daily Proteins (g)", np.round(daily_proteins,0))
    col3.metric("Daily Carbs (g)", np.round(daily_carbs,0))
    col4.metric("Daily Fats (g)", np.round(daily_fats,0))

    # Output Weekly Fitness Plan (Calories to Burn, Workout days, Exercise Duration, Fitness Videos)
    col1, col2, col3 = st.columns(3)
    col1.metric("Calories to Burn (per week)", np.round(workout_cals_loss,0))
    col2.metric("Workout Days", workout_days)
    col3.metric("Exercise Duration (in minutes)", np.round(exercise_duration,0))
   
    st.subheader('Helpful Food Calorie / Macro Database', 'https://www.calorieking.com/us/en/foods/')
    
    if body_specific_vids == 'Arms':
        st.video('https://www.youtube.com/watch?v=hAGfBjvIRFI&list=LL&index=8')  
    if body_specific_vids == 'Legs':
        st.video('https://www.youtube.com/watch?v=xpzMr3nSOIE&list=LL&index=10') 
    if body_specific_vids == 'Back':
        st.video('https://www.youtube.com/watch?v=5hVAUMZkJq4&list=LL&index=7&t=127s') 
    if body_specific_vids == 'Abs':
        st.video('https://www.youtube.com/watch?v=hxjKZcOT17E&list=LL&index=9') 
    if body_specific_vids == 'Glutes':
        st.video('https://www.youtube.com/watch?v=i1ZzdBgLtZg') 
    if body_specific_vids == 'Posture':
        st.video('https://www.youtube.com/watch?v=5R54QoUbbow') 

# GAIN WEIGHT SECTION
if goal == 'Gain Weight':
    with st.sidebar:
        # Please input your goal weight if nesscary
        weight_goal = float(st.slider('Input goal weight, if appicable', 0, 250, int(goal_weight))) # Question, Min, Max, Default Value
    # Calculate variable delta_weight & calculate time_restriction (max +/-0.909 kgs/wk)
    delta_weight = weight_goal - weight
    time_restriction = abs(delta_weight) / 0.909 * 7.0
    time_restriction = datetime.timedelta(days=time_restriction)
    
    # Please input your timeline for achieving your health goals
    # Q1: Start Date (units days)
    # Q2: End Date (units days), minimum end date based on time_restriction
    with st.sidebar:
        st.subheader('That is a fabulous health goal! When would you like to achieve that by?')
        time_start = st.date_input('Start Date', value=datetime.datetime.now(), min_value=datetime.datetime.now(), max_value=datetime.date(2022, 12, 31))
        st.write('Because we want you to achieve your health goals in a safe and sustainable manner the timeline is limited to a max weight change on +/-0.909 kg per week ^u^')
        time_end = st.date_input('End Date', value=datetime.datetime.now()+time_restriction, min_value=datetime.datetime.now()+time_restriction, max_value=datetime.date(2025, 12, 31))
    
    # Calculate time delta
    time_2_goal_d = float((time_end - time_start).days)
    # Convert to weeks
    time_2_goal_w = time_2_goal_d / 7.0
    # Calculate Weight Change Rate
    weight_change_rate = delta_weight / time_2_goal_w
    # Calculate Calorie Change Rate
    cal_change_rate = weight_change_rate * 7700.0
    # Calculate Daily Calorie Loss from Food Percentage
    food_cals_loss = cal_change_rate * 0.75 / 7.0

    # Options: Arms, Legs, Back, Abs, Glutes, Posture
    with st.sidebar:
        body_specific_vids = st.selectbox(
         'Do you have a specific body part that you would really like to tone? Select it below',
         ('Arms', 'Legs', 'Back', 'Abs', 'Glutes', 'Posture'))

    st.title('*You did it! Here is your personalized nutrtion and fitness plan! Good luck!*')
    
    # Calculate Alloted Daily Calories 
    daily_cals = BMR_calories + food_cals_loss
    # Calculate Macros from DB based on daily_cals (using recommendend 30% carbs, 40% protein, 30% fats balance)
    # Grams per calories calculated based on https://drbillsukala.com/macronutrient-calorie-gram-calculator/
    mac_cals_in = [500.0, 1000.0, 1500.0, 2000.0, 2500.0, 3000.0, 3500.0, 4000.0]
    macro_pro_in = [38.0,	75.0,	113.0,	150.0,	188.0,	225.0,	263.0,	300.0]
    macro_carb_in = [50.0,	100.0,	150.0,	200.0,	250.0,	300.0,	350.0,	400.0]
    macro_fat_in = [17.0,	33.0,	50.0,	67.0,	83.0,	100.0,	117.0,	133.0]

    daily_proteins = np.interp(daily_cals, mac_cals_in, macro_pro_in)
    daily_carbs = np.interp(daily_cals, mac_cals_in, macro_carb_in)
    daily_fats = np.interp(daily_cals, mac_cals_in, macro_fat_in)

    # Output Daily Nutrition Plan (Daily Calories, Macros, Food Database)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Daily Calories", np.round(daily_cals,0))
    col2.metric("Daily Proteins (g)", np.round(daily_proteins,0))
    col3.metric("Daily Carbs (g)", np.round(daily_carbs,0))
    col4.metric("Daily Fats (g)", np.round(daily_fats,0))
    
    st.write('Helpful Food Calorie / Macro Database', 'https://www.calorieking.com/us/en/foods/')

    # Output Weekly Fitness Plan (Calories to Burn, Workout days, Exercise Duration, Fitness Videos)
    if body_specific_vids == 'Arms':
        st.video('https://www.youtube.com/watch?v=hAGfBjvIRFI&list=LL&index=8')  
    if body_specific_vids == 'Legs':
        st.video('https://www.youtube.com/watch?v=xpzMr3nSOIE&list=LL&index=10') 
    if body_specific_vids == 'Back':
        st.video('https://www.youtube.com/watch?v=5hVAUMZkJq4&list=LL&index=7&t=127s') 
    if body_specific_vids == 'Abs':
        st.video('https://www.youtube.com/watch?v=hxjKZcOT17E&list=LL&index=9') 
    if body_specific_vids == 'Glutes':
        st.video('https://www.youtube.com/watch?v=i1ZzdBgLtZg') 
    if body_specific_vids == 'Posture':
        st.video('https://www.youtube.com/watch?v=5R54QoUbbow') 
