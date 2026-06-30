# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:31:26 2026

@author: Welcome
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('C:/Users/Welcome/Desktop/multiple disease pred/saved models/diabetic_model.sav','rb'))

heart_model=pickle.load(open('C:/Users/Welcome/Desktop/multiple disease pred/saved models/heart_model.sav','rb'))

parkinson_model=pickle.load(open('C:/Users/Welcome/Desktop/multiple disease pred/saved models/parkinson_model.sav','rb'))



#side bar for navigation
with st.sidebar:
    
    selected=option_menu('multiple disease prediction system',
                         
                         ['Diabetes_prediction',
                          'Heart Disease prediction',
                          'parkinsons prediction'],
                         
                         icons=['activity','heart','person'],
                         
                         default_index=0)

#diabetes prediction page
if(selected=="Diabetes_prediction"):
    
    #page title
    st.title('diabetes prediction using ml')
    
    
    #getting the input data f the user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        BloodPressure=st.text_input('Bloodpressure value')
    with col1:
        SkinThickness=st.text_input('Skin thickness value')
    with col2:
        Insulin=st.text_input('Insulin value')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetis pedigree function value')
    with col2:
        Age=st.text_input('age value')
        
    
    ##code for prediction
    diab_diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis='diabetic'
        else:
            diab_diagnosis='non diabetic'
            
    st.success(diab_diagnosis)
    
    
#heart prediction page
if(selected=="Heart Disease prediction"):
    
    #page title
    st.title('heart prediction using ml') 
    
    #getting the input data f the user
    #columns for input fields
    col1,col2,col3,col4=st.columns(4)
    
    with col1:
        age=st.text_input('age value')
    with col2:
        sex=st.text_input('sex')
    with col3:
        cp=st.text_input('cp')
    with col4:
        trestbps=st.text_input('trestbps')
    with col1:
        chol=st.text_input('chol')
    with col2:
        fbs=st.text_input('fbs')
    with col3:
        restecg=st.text_input('restecg')
    with col4:
        thalach=st.text_input('thalach')
    with col1:
        exang=st.text_input('exang')
    with col2:
        oldpeak=st.text_input('oldpeak')
    with col3:
        slope=st.text_input('slope')
    with col4:
        ca=st.text_input('ca') 
    with col1:
        thal=st.text_input('thal')
        
        
    ##code for prediction
    heart_diagnosis=''
    
    #creating a button for prediction
    if st.button('Heart Test Result'):
        heart_prediction=heart_model.predict([[float(age) ,float(sex), float(cp), float(trestbps),float( chol), float(fbs) ,float(restecg), float(thalach), float(exang),float(oldpeak), float(slope),float( ca),float( thal)]])
        
        if(heart_prediction[0]==1):
            heart_diagnosis='Defective heart'
        else:
            heart_diagnosis='healthy heart'
            
    st.success(heart_diagnosis)
    
        

#parkinson prediction page
if(selected=="parkinsons prediction"):
    
    #page title
    st.title('parkinson prediction using ml') 
    
    
    #getting the input data f the user
    #columns for input fields
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        Fo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        Fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        Flo=st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter=st.text_input('MDVP:Jitter(%)')
    with col5:
        JitterAbs=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP=st.text_input('MDVP:RAP')
    with col2:
        PPQ=st.text_input('MDVP:PPQ')
    with col3:
        DDP=st.text_input('Jitter:DDP')
    with col4:
        Shimmer=st.text_input('MDVP:Shimmer')
    with col5:
        ShimmerDB=st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3=st.text_input('Shimmer:APQ3')
    with col2:
        APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        APQ=st.text_input('MDVP:APQ')
    with col4:
        DDA=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input(' HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input(' DFA')
    with col4:
        spread1=st.text_input('spread1')
    with col5:
        spread2=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2') 
    with col2:
        PPE=st.text_input('PPE')
        
    
        
    if st.button('Parkinsons Test Result'):

        inputs = [
            Fo, Fhi, Flo, Jitter, JitterAbs, RAP, PPQ, DDP,
            Shimmer, ShimmerDB, APQ3, APQ5, APQ, DDA,
            NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ]

        if "" in inputs:
            st.error("Please fill all the input fields.")
        else:
            parkinson_prediction = parkinson_model.predict([[float(x) for x in inputs]])

            if parkinson_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease."
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease."

    st.success(parkinsons_diagnosis)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

