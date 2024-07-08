import streamlit as st
st.title("Drug Prediction system")
import streamlit as st
import pickle
import numpy as np

with open("drug.pkl","rb") as file:
    xgb_model= pickle.load(file)

def predict_function(age,Gender,BP,Chelosterol,Na_to_K):
    input_array= np.array([[age,Gender,BP,Chelosterol,Na_to_K]])
    drug_prediction= xgb_model.predict(input_array)
    return drug_prediction
    
    
st.title("Drug Prediction system")
age= st.slider("age",min_value=1, max_value=100)
Gender= st.selectbox("Gender",["Male","Female"])
BP= st.selectbox("BP",["Low","Normal","High"])
Chelosterol= st.selectbox("Chelosterol",["High","Normal"])
Na_to_K=st.slider("Na_to_K" ,min_value=1, max_value=100)

Gender= 1 if Gender =="Male" else 0
bp_mapping= {"High":0,"Low":1,"Normal":2}
BP= bp_mapping[BP]
Chelosterol_mapping= {"High":0,"Normal":1}
Chelosterol= Chelosterol_mapping[Chelosterol]
st.button("Predict")
st.write(f"user values are {age,Gender,BP,Chelosterol,Na_to_K}")
prediction= predict_function(age,Gender,BP,Chelosterol,Na_to_K)
drug_dct= {0:"DrugA",1:"DrugB",2:"DrugC",3:"DrugX",4:"DrugY"}
st.write(f"\n The prediction is {drug_dct[prediction[0]]}")