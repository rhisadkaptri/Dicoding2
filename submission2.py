import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
 
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
 
df_final = data_ori[['Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_approved',
                     'Tuition_fees_up_to_date', 'Scholarship_holder', 'Age_at_enrollment', 'Debtor', 'Gender', 'Application_mode', 'Status']]
 
# One Hot Encoding semua features
df_dummies = pd.get_dummies(df_final)
 
## Modeling
 
# tentukan variabel X dan variabel y
X = df_dummies.loc[:, df_dummies.columns != 'Status']
y = df_dummies['Status']
 
X, y = SMOTE().fit_resample(X, y)
 
# split data menjadi training dan testing set dengan perbadingan 80:20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
 
# Inisialisasi model RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=0)
 
# Melatih Model
model.fit(X_train, y_train)
 
# Membuat prediksi
y_pred = model.predict(X_test)
 
## Evaluation
 
# tampilkan evaluasi
print("Train Score:", model.score(X_train, y_train))
print("Test Score:", model.score(X_test, y_test))
 
# Menampilkan classification report
print(classification_report(y_test, y_pred))
 
import joblib
 
joblib.dump(model, 'model\model_random_forest.pkl')