import pandas as pd
import numpy as np
import streamlit as st
import joblib
 
# URL mentah dari file CSV di GitHub
url = 'https://raw.githubusercontent.com/rhisadkaptri/Dicoding/main/data.csv'
 
# Membaca data dari URL mentah ke dalam DataFrame dengan separator ;
data_ori = pd.read_csv(url, sep=';')
 
data_ori = data_ori[data_ori['Status'] != 'Enrolled']
 
df = data_ori.copy(deep=True)
 
# Mengubah Keterangan Kolom
df['Marital_status'] = df['Marital_status'].replace({1: 'single', 2: 'married', 3: 'widower', 4: 'divorced', 5: 'facto union', 6: 'legally separated'})
df['Gender'] = df['Gender'].replace({0: 'Female', 1: 'Male'})
df['Tuition_fees_up_to_date'] = df['Tuition_fees_up_to_date'].replace({0: 'No', 1: 'Yes'})
df['Debtor'] = df['Debtor'].replace({0: 'No', 1: 'Yes'})
df['Daytime_evening_attendance'] = df['Daytime_evening_attendance'].replace({0: 'Evening', 1: 'Daytime'})
df['Scholarship_holder'] = df['Scholarship_holder'].replace({0: 'No', 1: 'Yes'})
 
df['Application_mode'] = df['Application_mode'].replace({1: '1st-GeneralContingent', 2: 'Ordinance No.612/93', 5: '1st-SpecialContingent(AzoresIsland)',
                                                         7: 'HoldersOfOtherHigher', 10: 'Ordinance No.854-B/99', 15: 'InterStudent(Bachelor)',
                                                         16: '1st-SpecialContingent(MadeiraIsland)', 17: '2nd-GeneralContingent', 18: '3rd-GeneralContingent',
                                                         26: 'Ordinance No.533-A/99(B2)', 27: 'Ordinance No. 533-A/99(B3)',
                                                         39: 'Over 23 years old', 42: 'Transfer', 43: 'ChangeOfCourse', 44: 'TechnologicalSpecializationD.H',
                                                         51: 'ChangeOfInstitution', 53: 'ShortCycleD.H', 57: 'ChangeOfInstitution(Inter))'})
 
# Convertin the predictor variable in a binary numeric variable
data_ori['Status'].replace(to_replace='Graduate', value=1, inplace=True)
data_ori['Status'].replace(to_replace='Dropout', value=0, inplace=True)
 
df = data_ori[['Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_approved',
                     'Tuition_fees_up_to_date', 'Scholarship_holder', 'Age_at_enrollment', 'Debtor', 'Gender', 'Application_mode', 'Status']]
 
# Fungsi untuk memuat model dan membuat prediksi
def load_model():
    model = joblib.load('model\model_random_forest.pkl')
    return model
 
def get_user_input():
    st.title('Status Prediction App')
 
    p1 = st.number_input('Curricular_units_1st_sem_grade', min_value=0.0, max_value=20.0, step=0.1)
    p2 = st.number_input('Curricular_units_1st_sem_approved', min_value=0, max_value=10, step=1)
    p3 = st.number_input('Curricular_units_2nd_sem_grade', min_value=0.0, max_value=20.0, step=0.1)
    p4 = st.number_input('Curricular_units_2nd_sem_approved', min_value=0, max_value=10, step=1)
    p5 = st.selectbox('Tuition_fees_up_to_date', options=[('Yes', 1), ('No', 0)], format_func=lambda x: x[0])
    p6 = st.selectbox('Scholarship_holder', options=[('Yes', 1), ('No', 0)], format_func=lambda x: x[0])
    p7 = st.number_input('Age_at_enrollment', min_value=17, max_value=100, step=1)
    p8 = st.selectbox('Debtor', options=[('Yes', 1), ('No', 0)], format_func=lambda x: x[0])
    p9 = st.selectbox('Gender', options=[('Male', 1), ('Female', 0)], format_func=lambda x: x[0])
    p10 = st.selectbox('Application_mode', options=list(df['Application_mode'].unique()))
 
    # Mengambil nilai numerik dari tuple
    p5 = p5[1]
    p6 = p6[1]
    p8 = p8[1]
    p9 = p9[1]
 
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
 
def main():
    user_input = get_user_input()
    model = load_model()
 
    if st.button('Predict'):
        result = model.predict([user_input])
        st.write('Status Prediction:', 'Graduate' if result[0] == 1 else 'Dropout')
 
        # # Menyimpan data input pengguna ke dalam file CSV
        # with open('data_dashboard2.csv', mode='a', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerow(user_input + [result[0]])
 
if __name__ == "__main__":
    main()