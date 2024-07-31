import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pypickle

loaded_model = pypickle.load('model.pkl')

def prediction(data):

    df = pd.DataFrame(data)

    label = LabelEncoder()

    num_columns = [0, 1, 2, 14, 16]

    for i in num_columns:
         df.iloc[i] = label.fit_transform(df.iloc[i])


    num_data = df.drop([0, 10, 11, 12, 13]).values.reshape(1,-1)

    scaler = StandardScaler()
    num_data = scaler.fit_transform(num_data)  

    pred = loaded_model.predict(num_data)

    if  pred[0] == 0:
        return "The client will not churn"
    else:
        return "The client will churn"

def main ():
     st.title("Expresso Churn Prediction Model")
     user_id = st.text_input("Please enter ID Number: ")
     REGION = st.radio('Please enter client Region: ', ('FATICK', 'DAKAR', 'LOUGA', 'TAMBACOUNDA', 'KAOLACK', 'THIES', 'SAINT-LOUIS', 'KOLDA', 'KAFFRINE', 'DIOURBEL', 'ZIGUINCHOR','MATAM', 'SEDHIOU', 'KEDOUGOU'))
     TENURE = st.radio("Please select your tenure: ", ('9-12 months', '12-15 months', '15-18 months', '18-21 months', '21 -24 months', '> 24 months'))
     MONTANT = st.number_input('Please enter Montant: ')
     FREQUENCE_RECH = st.number_input('Please enter Frequency Reach: ')
     REVENUE = st.number_input('Please enter Revenue: ')
     ARPU_SEGMENT = st.number_input('Please specify APRU: ')
     FREQUENCE = st.number_input('Enter Frequency Input: ')
     DATA_VOLUME = st.number_input('Enter Data Volume: ')
     ON_NET = st.number_input('Enter On-Net: ')
     ORANGE = st.number_input('Enter Orange: ')
     TIGO = st.number_input('Enter Tigo: ')
     ZONE1 = st.number_input('Enter Zone1: ')
     ZONE2 = st.number_input('Enter Zone2: ')
     MRG = st.radio("Are you going? select yes or no ", ("yes" , "no"))
     REGULARITY = st.number_input('Specify Regularity: ')
     TOP_PACK = st.text_input('Enter Top Pack: ')
     FREQ_TOP_PACK = st.number_input('Enter Top Pack: ')

     CHURN = ""

     if st.button("Result"):
        CHURN = prediction([user_id, REGION, TENURE, MONTANT, FREQUENCE_RECH, 
        REVENUE,ARPU_SEGMENT, FREQUENCE, DATA_VOLUME, ON_NET, ORANGE, TIGO, 
        ZONE1, ZONE2, MRG, REGULARITY, TOP_PACK, FREQ_TOP_PACK])

        st.success(CHURN)

if  __name__ == "__main__":
            main()
