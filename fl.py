#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import streamlit as st
# import pickle
# import numpy as np
# import datetime
# model=pickle.load(open(r"C:\MPSTME\Projects\Streamlit\Log.pkl",'rb'))

# def predict(sepal_length,sepal_width,petal_length,petal_width):
#     input=np.array([[sepal_length,sepal_width,petal_length,petal_width]]).astype(np.float64)
#     prediction=model.predict(input)
#     return prediction

# def main():
#     st.title("Iris")
#     html_temp = """
#     <div style="background-color:#025246 ;padding:10px">
#     <h2 style="color:white;text-align:center;">Iris Prediction ML App </h2>
#     </div>
#     """
#     st.markdown(html_temp, unsafe_allow_html=True)
    
#     d = st.date_input('Date Of Journey', datetime.date.today())
    
#     sepal_length = st.selectbox('Sepal Length', (1, 1.5, 2, 2.5, 3, 3.5, 4))
#     sepal_width = st.text_input("sepal_width","Type Here")
#     petal_length = st.text_input("petal_length","Type Here")
#     petal_width = st.text_input("petal_width","Type Here")
#     output=""
#     if st.button("Predict"):
#         output=predict(sepal_length,sepal_width,petal_length,petal_width)
#         st.success('The output is {}'.format(output))

# if __name__=='__main__':
#      main()


# In[17]:

import streamlit as st
import pickle
import numpy as np
import datetime
import pandas as pd
from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='19bAjDx6a1SQN8B3lvCqgspq2GTHA_2x-',
                                    dest_path='./n.pkl',
                                    unzip=False)

model=pickle.load(open("n.pkl",'rb'))

def predict(Total_Stops, Journey_day, Journey_month, Dep_hour,Dep_min, Arrival_hour, Arrival_min, Air_Asia, Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
            Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara, Vistara_Premium_economy,
            s_Banglore, s_Chennai, s_Delhi, s_Kolkata, s_Mumbai,
            d_Banglore, d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata):
     input=np.array([[Total_Stops, Journey_day, Journey_month, Dep_hour,Dep_min, Arrival_hour, Arrival_min, Air_Asia, Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business,
            Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara, Vistara_Premium_economy,
            s_Banglore, s_Chennai, s_Delhi, s_Kolkata, s_Mumbai,
            d_Banglore, d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata]])
     prediction=model.predict(input)
     return prediction
    
def main():
    st.subheader('Author: Maaz Ansari')
    st.title("Flight Price Prediction")
    
#     html_temp = """
#     <div style="background-color:#025246 ;padding:10px">
#     <h2 style="color:white;text-align:center;">Author: Maaz Ansari </h2>
#     </div>
#     """
#     st.markdown(html_temp, unsafe_allow_html=True)
    
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    #Date_of_Journey = st.text_input("Date of Your Journey","24/04/2019")
    Date_of_Journey = st.date_input("Date of Your Journey", today)
    
    Journey_day = pd.to_datetime(Date_of_Journey, format="%Y/%m/%d").day
    Journey_month = pd.to_datetime(Date_of_Journey, format = "%Y/%m/%d").month

    #Journey_day = pd.to_datetime(Date_of_Journey, format="%d/%m/%Y").day
    #Journey_month = pd.to_datetime(Date_of_Journey, format = "%d/%m/%Y").month
    
    Dep_Time = st.time_input("Departure Time", datetime.time(8, 45))
    Dep_hour = Dep_Time.hour
    Dep_min = Dep_Time.minute
    

    not_needed = st.date_input("Return Date", tomorrow)
    
    if Date_of_Journey > not_needed:
        st.error('Error: Return Date must fall after Date of your Journey.')
    
    Arr_Time = st.time_input("Arrival Time", datetime.time(10, 40))
    Arrival_hour = Arr_Time.hour
    Arrival_min = Arr_Time.minute

#     Dep_Time = st.text_input("Dep_Time","01:10")
#     Dep_hour = pd.to_datetime(Dep_Time).hour
#     Dep_min = pd.to_datetime(Dep_Time).minute

#     Arr_Time = st.text_input("Arr_Time","06:20")
#     Arrival_hour = pd.to_datetime(Arr_Time).hour
#     Arrival_min = pd.to_datetime(Arr_Time).minute
    
    

    airline = st.selectbox('Airline', ('Jet Airways', "IndiGo", "Air India", "Multiple carriers", "SpiceJet", "Vistara","Air Asia","GoAir","Multiple carriers Premium economy","Jet Airways Business","Vistara Premium economy","Trujet", "Air_Asia"))
    if (airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0

    elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0

    elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0
            
    elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0
            
    elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            Air_Asia = 0
            
    elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0

    elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0

    elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0

    elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0

    elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            Air_Asia = 0
            
    elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
            Air_Asia = 0

    elif (airline=='Air Asia'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 1
    else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
            Air_Asia = 0
     
    
        
    Source = st.selectbox('Source', ("Mumbai", "Chennai", "Delhi", "Kolkata", "Banglore"))

    if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 0

    elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 0

    elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
            s_Banglore = 0

    elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            s_Banglore = 0

    elif (Source == 'Banglore'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 1

    else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Banglore = 0
    
    
    Destination = st.selectbox('Destination', ("Cochin", "Delhi", "Hyderabad", "Kolkata","Banglore"))
    if (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_Banglore = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
    elif (Destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_Banglore = 0
            d_Hyderabad = 0
            d_Kolkata = 0

    elif (Destination == 'Banglore'):
            d_Cochin = 0
            d_Delhi = 0
            d_Banglore = 1
            d_Hyderabad = 0
            d_Kolkata = 0

    elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_Banglore = 0
            d_Hyderabad = 1
            d_Kolkata = 0

    elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_Banglore = 0
            d_Hyderabad = 0
            d_Kolkata = 1
    else:
            d_Cochin = 0
            d_Delhi = 0
            d_Banglore = 0
            d_Hyderabad = 0
            d_Kolkata = 0
    

    Total_Stops = st.selectbox('Total Stops', (0, 1, 2, 3, 4, 5))        
    
    output=""
    if st.button("Predict"):
        output=predict(Total_Stops, Journey_day, Journey_month, Dep_hour,Dep_min, Arrival_hour, Arrival_min, Air_Asia, Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business, Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara, Vistara_Premium_economy, s_Banglore, s_Chennai, s_Delhi, s_Kolkata, s_Mumbai, d_Banglore, d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata)
        output=round(output[0],2)
        st.success('The Price is {}'.format(output))
        st.success('Bon Voyage!')
        st.balloons()


if __name__=='__main__':
     main()


# In[ ]:




