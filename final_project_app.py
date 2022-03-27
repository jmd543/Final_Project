##########################
# SYSEN5160 Final Project 
# Jamie Donahue (jmd543)
# May 13 2022
##########################
# Make Databases
    # Macros Database
    # Exercise Video Database
    # Food Database
    # Exercise Calorie Burned Database

import streamlit as st
import pandas as pd
import numpy as np
from scipy import interpolate
import datetime

st.title("Happy, Heathly & You")

# User Input Section on Streamlit
st.write('Hello beautiful! Congratulations on starting your journey to be the best version of you! Lets get started!')

st.write('In order to make your personalized nutrition & fitness planner we will need just a litte information about yourself.')
# Q1: Please input your height (cms)
height = st.slider('How tall are you, in centimeters?', 0, 250, 125) # Question, Min, Max, Default Value
st.write("Your height is", height, 'centimeters')

# Q2: Please input your weight (kgs)
weight = st.slider('How much do you weigh, in kilograms?', 0, 250, 125) # Question, Min, Max, Default Value
st.write("Your weight is", weight, 'kilograms')

# Q3: Please input your gender (male or female)
gender = st.radio(
 "What's your biological gender?",
 ('Male', 'Female'))

if gender == 'Male':
     st.write('You selected Male')
else:
     st.write('You selected Female')

# Q4: Please input your age (yrs)
age = st.slider('How old are you, in years?', 0, 100, 50) # Question, Min, Max, Default Value
st.write("Your age is", age, 'years')

# If gender equals male
if gender == 'Male':
    BMR_calories = 88.362 + (13.397*weight) + (4.799*height) - (5.677*age)
# If gender equals female
else:
    BMR_calories = 447.593 + (9.247*weight) + (3.098*height) - (4.330*age)

# Lookup avg_workout_cals_1hr from DB
avg_workout_cals_1hr = pd.read_csv('Average_calories_burned_1hr_v2.csv')
activity = 'General'
activity_interpolator = interpolate.interp1d([59.1, 70.5, 81.8, 93.2],avg_workout_cals_1hr.loc[avg_workout_cals_1hr.Activity == activity,['59.1', '70.5', '81.8', '93.2']], fill_value = 'extrapolate')
avg_workout_cals = activity_interpolator(weight)

st.write('Awesome! Now tell us what are your health goals?')
# Please select your health goal
# Option 1: Maintain weight
# Option 2: Change weight
goal = st.radio(
 "Please select your health goal",
 ('Maintain Weight', 'Change Weight'))

if goal == 'Maintain Weight':
     st.write('You selected Maintain Weight!')
else:
     st.write('You selected Change Weight! Please input your goal weight below in kilograms')
   
# Please input your goal weight
weight_goal = st.slider('Input goal weight', 0, 250, 125) # Question, Min, Max, Default Value
st.write("Your weight goal is", weight_goal, 'kilograms')

# Calculate variable delta_weight & calculate time_restriction (max +/-0.909 kgs/wk) = abs(delta_weight) / 0.909 * 7 (covert to days for time selection)
if goal == 'Change Weight':
    delta_weight = weight_goal - weight
    time_restriction = abs(delta_weight) / 0.909 * 7
    time_restriction = datetime.timedelta(days=time_restriction)
    
# Please input your timeline for achieving your health goals
# Q1: Start Date (units days)
# Q2: End Date (units days), minimum end date based on time_restriction
st.write('Your doing amazing! That is a fabulous health goal! When would you like to achieve that by? (please click the date box below)')
time_start = st.date_input('Start Date', value=datetime.datetime.now(), min_value=datetime.datetime.now(), max_value=datetime.date(2022, 12, 31))
st.write('Because we want you to achieve your health goals in a safe and sustainable manner the timeline is limited to a max weight change on +/-0.909 kg per week ^u^')
time_end = st.date_input('End Date', value=datetime.datetime.now()+time_restriction, min_value=datetime.datetime.now()+time_restriction, max_value=datetime.date(2025, 12, 31))

# Calculate time delta
time_2_goal_d = (time_end - time_start).days
# Convert to weeks
time_2_goal_w = time_2_goal_d / 7
# Calculate Weight Change Rate
weight_change_rate = delta_weight / time_2_goal_w
# Calculate Calorie Change Rate
cal_change_rate = weight_change_rate * 3500
# Calculate Daily Calorie Loss from Food Percentage
food_cals_loss = cal_change_rate * 0.25 / 7
# Calculate Weekly Calorie Loss from Workout Percentage
workout_cals_loss = cal_change_rate * 0.75

st.write('Great! Now lets talk fitness')
# Q1: How many days a week would you like to workout?
workout_days = st.selectbox(
 'How many days a week would you like to workout?',
 ('1', '2', '3', '4', '5', '6', '7'))
st.write('You selected:', workout_days)
# Calculate exercise_duration
exercise_duration = ( workout_cals_loss / workout_days / 7 ) / avg_workout_cals

st.write('Alright last question! Do you have any specific body part that you would really like to tone?')
# Options: Arms, Legs, Back, Abs, Butt, Posture
body_specific_vids = st.selectbox(
 'Select what area you would like to focus on',
 ('Arms', 'Legs', 'Back', 'Abs', 'Butt', 'Posture'))
st.write('You selected:', body_specific_vids)
    
st.write('You did it! Now sit back, relax, and wait a few seconds while we create your personalized nutrtion and fitness plan.')
#with st.spinner('Results cooking...'):
#    time.sleep(5)
#st.success('Done!')
# Output Daily Nutrition Plan
    # --> Calculate Alloted Daily Calories = BMR_calories - food_cals_loss and store daily_cals
    # --> Lookup Macros from DB based on daily_cals (percentage & grams of fats, proteins, and carbs)
    # --> Output daily_cals and Macros
    # --> Output Helpful Food Database with Calories and Macros

# Output Weekly Fitness Plan
    # --> Output Calories to Burn per week = workout_cals_loss (cals/wk)
    # --> type('Based on your preferences that means you'll need to workout this much')
            # --> Output workout_days (days) and approximate exercise_duration (hrs)
    # --> Lookup and output fitness videos based on body_specific_vids variable
    # --> Output Helpful Exercise Database with Calories burned / hour based on weight, height, gender

#st.ballons()
