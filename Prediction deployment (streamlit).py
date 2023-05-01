# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:52:29 2023

@author: omole
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/omole/Downloads/Machine learning/Car price prediction (From Modelling to deployment)/Cartrained_model.sav', 'rb'))

#creating a function for the data
def price_prediction(input):

    # changing the input_data to numpy array
    input_as_numpy_array = np.asarray(input)

    # reshape the array as we are predicting for one instance
    input_reshaped = input_as_numpy_array.reshape(1,-1)

    #prediction = loaded_model.predict(input_data_reshaped)
    prediction = -14915 + (5*input_reshaped[0][0]) + (78*input_reshaped[0][1]) + (53*input_reshaped[0][2])
    return prediction
    if prediction <= 3000:
        return 'This car has a low price'
        
    elif prediction <= 15000:
        return 'This is a mid-range car'  
        
    else:
        return 'This car has a high price'
    
    
    
def main():
    
    #create a title
    st.title('Car Price Prediction')
    
    
    curb_weight = st.number_input('curb weight of the car')
    engine_size = st.number_input('size of the engine')
    Horsepower = st.number_input('Horsepower of the car')
    
    car_price_prediction = ''
    
    if st.button('Price prediction'):
        car_price_prediction = price_prediction([curb_weight, engine_size, Horsepower])
        
    st.success(car_price_prediction)
    
    
if __name__=='__main__':
    main()
    
    