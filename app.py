import streamlit as st
from joblib import load
import numpy as np
import pandas as pd

# Model load
model = load('loan_model_logistic.joblib')

# Main app with data fields
def main():
    st.title('Loan application prediction')

    amount = st.number_input('Amount (USD)', min_value=0, value=1000)
    loan_type = st.selectbox('Loan type', ['Refinancing', 'Business loan', 'Real estate',
                                           'Relocation/travel/other', 'Car purchase', 'Repairs',
                                           'Medical expenses'])
    risk_score = st.number_input('Risk/FICO score', min_value=0, max_value=2000, value=650)
    risk_score_uncertainty = st.selectbox('Risk score certainty (1 if yes)', [0, 1])
    dti = st.number_input('DTI (pct.)', min_value=0.0, max_value=100.0, value=15.0)
    employment_length = st.number_input('Employment length in years', min_value=0, value=5)
    
    # with 'Predict' clicked make the prediction in the model and display
    if st.button('Predict'):
        input_df = pd.DataFrame([[amount, loan_type, risk_score, risk_score_uncertainty, dti, employment_length]],
                                columns=['Amount (USD)', 'Loan type', 'Risk/FICO score', 
                                         'Risk score uncertain', 'DTI (pct.)', 'Employment length (years)'])

        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)[:, 1]
        
        if prediction[0] == 1:
            st.success(f'The application is likely to be accepted with a probability of {probability[0]:.1f}')
        else:
            st.error(f'The application is likely to be rejected with a probability of {1 - probability[0]:.1f}')

# object
if __name__ == '__main__':
    main()
