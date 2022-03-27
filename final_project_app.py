##########################
# SYSEN5160 Final Project 
# Jamie Donahue (jmd543)
# May 13 2022
##########################

import streamlit as st
import pandas as pd
import numpy as np

# Insert Databases
    # Average Calories burned in 1 hour
    # Macros Database
    # Exercise Video Database
    # Food Database
    # Exercise Calorie Burned Database

# User Input Section on Streamlit
type('Hello beautiful! Congratulations on starting your journey to be the best version of you! Lets get started!')

type('In order to make your personalized nutrition & fitness planner we will need just a litte information about yourself.')
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

    # --> Store variable height
    # --> Store variable weight_current
    # --> Store variable gender
    # --> Store variable age
    # --> If gender equals male
    #       BMR_calories = Insert EQ
    # --> If gender equals female
    #       BMR_calories = Insert EQ
    # Lookup avg_workout_cals_1hr from DB

type('Awesome! Now tell us what are your health goals?')
# Please select your health goal and input your goal weight if desired
# Option 1: Maintain weight
# Option 2: Lose weight --> Insert goal weight (units lbs)
# Option 3: Gain Weight --> Insert goal weight (units lbs)

    # --> Store variable weight_goal from OP1, OP2, or OP3
    # --> Calculate variable delta_weight = weight_goal - weight_current
    # --> Calculate time_restriction (max +/-2 lbs/wk) = abs(delta_weight) / 2 * 7 (covert to days for time selection)

type('Your doing amazing! That is a fabulous health goal! When would you like to achieve that by?')
# Please input your timeline for achieving your health goals
type('Because we want you to achieve your health goals in a safe and sustainable manner the timeline is limited to a max weight change on +/-2 lbs per week ^u^')
# Q1: Start Date (units days)
# Q2: End Date (units days), minimum end date based on time_restriction

    # --> Store variable time_start
    # --> Store variable time_end
    # --> Calculate variable time_2_goal_d = time_end - time_start
    # --> Convert to weeks, time_2_goal_w = time_2_goal_d / 7 
    # --> Calculate Weight Change Rate = delta_weight / time_2_goal_w and store variable weight_change_rate
    # --> Calculate Calorie Change Rate = weight_change_rate * 3500 and store variable cal_change_rate
    # --> Calculate Daily Calorie Loss from Food Percentage = cal_change_rate * 0.25 / 7 and store variable food_cals_loss
    # --> Calculate Weekly Calorie Loss from Workout Percentage = cal_change_rate * 0.75 and store variable workout_cals_loss

type('Great! Now lets talk fitness')
# Q1: How many days a week would you like to workout?
    # --> Store variable workout_days
    # --> Calculate exercise_duration = ( workout_cals_loss / workout_days / 7 ) / avg_workout_cals_1hr (average calories burned in 1hr workout based on height, weight, gender)

type('Alright last question! Do you have any specific body part that you would really like to tone?')
# Options: Arms, Legs, Back, Abs, Butt, Posture
    # --> Store selection body_specific_vids

type('You did it! Now sit back, relax, and wait a few seconds while we create your personalized nutrtion and fitness plan.')
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

# Visual Setup on Streamlit
