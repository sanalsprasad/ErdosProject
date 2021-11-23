import streamlit as st
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier

#model = DecisionTreeClassifier(max_depth=8)

model = pickle.load(open('model.pickle','rb'))


st.write("""
# CoverMyMeds - PA Approval Chances
""")

st.header("User Information")

st.write("Please fill in the following information." )

bin = st.radio("Select the BIN of Insurance payer: ", ("417380","417614","417740","999001"))

drug = st.radio("Select the drug that you want covered: ", ("A","B","C"))

tried_failed = st.radio("Have you tried and failed the generic alternative?", ("Yes","No"))

contraindication = st.radio("Contraindication?",("Yes","No"));

correct_diagnosis = st.radio("Correct diagnosis?",("Yes","No"));


# Find reject code:
reject_code = 0;
if bin == "417380":
    if drug == "A":
        reject_code = 75;
    elif drug == "B":
        reject_code = 76;
    elif drug == "C":
        reject_code = 70;
elif bin == "417614":
    if drug == "A":
        reject_code = 70;
    elif drug == "B":
        reject_code = 75;
    elif drug == "C":
        reject_code = 76;
elif bin == "417740":
    if drug == "A":
        reject_code = 76;
    elif drug == "B":
        reject_code = 70;
    elif drug == "C":
        reject_code = 75;
elif bin == "999001":
    reject_code = 76;

#Set features
d = {"Yes":1, "No":0} #Dictionary for Yes = 1, No  = 0

cd = d[correct_diagnosis]
tf = d[tried_failed]
contra = d[contraindication]
drug_B = int(drug == "B")
drug_C = int(drug == "C")
bin_417614 = int(bin == "417614")
bin_417740 = int(bin == "417740")
bin_999001 = int(bin == "999001")
reject_code_75 = int(reject_code == 75)
reject_code_76 = int(reject_code == 76)

#Predict
pred = model.predict_proba([[cd,tf,contra,drug_B,drug_C,bin_417614,bin_417740,bin_999001, reject_code_75, reject_code_76]])

st.header("Result")
st.write("The chances of your PA being approved are: {}".format(100*np.round(pred[0,1],5)), "%.")


