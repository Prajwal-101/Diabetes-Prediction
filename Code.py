# -*- coding: utf-8 -*-
"""diabetes(Short)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C1RndiZK5L3vaYmGUKnvaYJXLVd2uiPq
"""



# 1. Aim of the project-
    # The main objective of this project is to predict whether the (Female)patient has the diabetes or not based on various factors.
# 2. About data set-
    # This dataset is originally from the National Institute of Diabetes and Digestive and Kidney
    # Diseases. The objective of the dataset is to diagnostically predict whether a patient has diabetes,
    # based on certain diagnostic measurements included in the dataset. Several constraints were placed
    # on the selection of these instances from a larger database. In particular, all patients here are females
    # at least 21 years old of Pima Indian heritage.2
    # From the data set in the (.csv) File We can find several variables, some of them are independent
    # (several medical predictor variables) and only one target dependent variable (Outcome).

# 3. Information about dataset attributes
    # Pregnancies: To express the Number of pregnancies
    #
    # Glucose: To express the Glucose level in blood
    #
    # BloodPressure: To express the Blood pressure measurement
    #
    # SkinThickness: To express the thickness of the skin
    #
    # Insulin: To express the Insulin level in blood
    #
    # BMI: To express the Body mass index
    #
    # DiabetesPedigreeFunction: To express the Diabetes percentage
    #
    # Age: To express the age
    #
    # Outcome: To express the final result 1 is Yes and 0 is No

# 4. Flow of the project
    # load the dataset -> EDA -> Data visualization -> Analyzing relationship between variables -> Feature scaling -> Train test split
    # ->build classification algorithm -> Making prediction -> model ecaluation -> Confusion matrix -> precison -> ROC curve

"""# **IMPORTING LIBRARIES->**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import roc_curve, auc,accuracy_score,confusion_matrix
from sklearn import datasets
from sklearn.preprocessing import label_binarize, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler

"""**READING THE FILE**"""

df=pd.read_csv('diabetes (1).csv')

df.head()

df.tail()

df.rename(columns={"Outcome":"Diabetes"},inplace=True)

df.head()

df.info()

df.shape

df.describe()

# From the above table we can conclude that the the min values of pregnancies, Glucose, BP,
# SkinThickness and Insulin are 0. It is clear that this values cannnot be zero.
# so replace this 0 with mean.

"""# **DATA CLEANING**


"""

# Drop the duplicate
df.shape

df=df.drop_duplicates()

df.shape

# Hence it is observed that we have no duplicates in the dataset.

df.isnull().sum()

# There is no null value in the dataset

# Checking for missing numbers
import missingno as mn

mn.bar(df)
plt.show()

df.columns

# no of zeros in the different col
print('No of zeros in the Glucose',df[df['Glucose']==0].shape[0])

print('No of zeros in the bloodpressure',df[df['BloodPressure']==0].shape[0])

print('No of zeros in the SkinThickness',df[df['SkinThickness']==0].shape[0])

print('No of zeros in the Insulin',df[df['Insulin']==0].shape[0])

print('No of zeros in the BMI',df[df['BMI']==0].shape[0])

## replacing zeros with mean of that column.
df['Glucose']=df['Glucose'].replace(0,df['Glucose'].mean())
print('No of zeros in the Glucose',df[df['Glucose']==0].shape[0])

df['BloodPressure']=df['BloodPressure'].replace(0,df['BloodPressure'].mean())
df['SkinThickness']=df['SkinThickness'].replace(0,df['SkinThickness'].mean())
df['Insulin']=df['Insulin'].replace(0,df['Insulin'].mean())
df['BMI']=df['BMI'].replace(0,df['BMI'].mean())



"""# **DATA VISUALIZATION**"""

#Univariate analysis->exploring the data
for i in df.columns:
    if df[i].dtype!="object":
        sns.histplot(x=df[i]);
        plt.show();

# kde plot
for i in df.columns:
    if df[i].dtype != "object":
        sns.kdeplot(x=df[i])
        plt.show()

# box plot
for i in df.columns:
    if df[i].dtype != "object":
        sns.boxplot(y=df[i])
        plt.show()

#Here we can see that except Glucode and Diabetes column rest of the culumn have Outliars

"""## **Removing Outliars:**

1.   Pregnancies
"""

preg_Q1 = df.Pregnancies.quantile(0.25)
preg_Q3 = df.Pregnancies.quantile(0.75)
# preg_Q1, preg_Q3

preg_IQR = preg_Q3-preg_Q1

preg_ll = preg_Q1 - 1.5*preg_IQR
preg_ul = preg_Q3 + 1.5*preg_IQR

preg_ll, preg_ul

#Showing outliars below Lower limit nad above upper limit
df[(df.Pregnancies < preg_ll) | (df.Pregnancies > preg_ul)]

df = df[(df.Pregnancies > preg_ll) & (df.Pregnancies < preg_ul)]

# Checking if Outliars are removed
sns.boxplot(y=df['Pregnancies'])
plt.show()

"""2.   Blood Pressure


"""

bp_Q1 = df.BloodPressure.quantile(0.25)
bp_Q3 = df.BloodPressure.quantile(0.75)
# bp_Q1, bp_Q3

bp_IQR = bp_Q3-bp_Q1

bp_ll = bp_Q1 - 1.5*bp_IQR
bp_ul = bp_Q3 + 1.5*bp_IQR

bp_ll, bp_ul

#Showing outliars below Lower limit nad above upper limit
df[(df.BloodPressure < bp_ll) | (df.BloodPressure > bp_ul)]

df = df[(df.BloodPressure > bp_ll) & (df.BloodPressure < bp_ul)]

# Checking if Outliars are removed
sns.boxplot(y=df['BloodPressure'])
plt.show()

"""3. Skin Thickness"""

st_Q1 = df.SkinThickness.quantile(0.25)
st_Q3 = df.SkinThickness.quantile(0.75)
# st_Q1, st_Q3

st_IQR = st_Q3-st_Q1

st_ll = st_Q1 - 1.5*st_IQR
st_ul = st_Q3 + 1.5*st_IQR

st_ll, st_ul

#Showing outliars below Lower limit nad above upper limit
df[(df.SkinThickness < st_ll) | (df.SkinThickness > st_ul)]

df = df[(df.SkinThickness > st_ll) & (df.SkinThickness < st_ul)]

# Checking if Outliars are removed
sns.boxplot(y=df['SkinThickness'])
plt.show()

"""4. Insulin"""

in_Q1 = df.Insulin.quantile(0.25)
in_Q3 = df.Insulin.quantile(0.75)

in_IQR = in_Q3-in_Q1

in_ll = in_Q1 - 1.5*in_IQR
in_ul = in_Q3 + 1.5*in_IQR

in_ll, in_ul

#Showing outliars below Lower limit nad above upper limit
df[(df.Insulin < in_ll) | (df.Insulin > in_ul)]

df = df[(df['Insulin'] > in_ll) & (df['Insulin'] < in_ul)]
df.shape

# Checking if Outliars are removed
sns.boxplot(y=df['Insulin'])
plt.show()

"""5. BMI"""

bmi_Q1 = df.BMI.quantile(0.25)
bmi_Q3 = df.BMI.quantile(0.75)

bmi_IQR = bmi_Q3-bmi_Q1

bmi_ll = bmi_Q1 - 1.5*bmi_IQR
bmi_ul = bmi_Q3 + 1.5*bmi_IQR

bmi_ll, bmi_ul

#Showing outliars below Lower limit nad above upper limit
df[(df.BMI < bmi_ll) | (df.BMI > bmi_ul)]

df = df[(df['BMI'] > bmi_ll) & (df['BMI'] < bmi_ul)]
df.shape

# Checking if Outliars are removed
sns.boxplot(y=df['BMI'])
plt.show()

"""6. DiabetesPedigreeFunction"""

dpf_Q1 = df.DiabetesPedigreeFunction.quantile(0.25)
dpf_Q3 = df.DiabetesPedigreeFunction.quantile(0.75)

dpf_IQR = dpf_Q3-dpf_Q1

dpf_ll = dpf_Q1 - 1.5*dpf_IQR
dpf_ul = dpf_Q3 + 1.5*dpf_IQR

dpf_ll, dpf_ul

#Showing outliars below Lower limit nad above upper limit
df[(df.DiabetesPedigreeFunction < dpf_ll) | (df.DiabetesPedigreeFunction > dpf_ul)]

df = df[(df['DiabetesPedigreeFunction'] > dpf_ll) & (df['DiabetesPedigreeFunction'] < dpf_ul)]
df.shape

# Checking if Outliars are removed
sns.boxplot(y=df['DiabetesPedigreeFunction'])
plt.show()

"""7. Age"""

age_Q1 = df.Age.quantile(0.25)
age_Q3 = df.Age.quantile(0.75)

age_IQR = age_Q3-age_Q1

age_ll = age_Q1 - 1.5*age_IQR
age_ul = age_Q3 + 1.5*age_IQR

age_ll, age_ul

#Showing outliars below Lower limit nad above upper limit
df[(df.Age < age_ll) | (df.Age > age_ul)]

df = df[(df['Age'] > age_ll) & (df['Age'] < age_ul)]
df.shape

# Checking if Outliars are removed
sns.boxplot(y=df['Age'])
plt.show()

## multivarite analysis
a=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
    'BMI', 'DiabetesPedigreeFunction', 'Age']
for i in a:
    sns.barplot(x="Diabetes",y=df[i],data=df)
    plt.show()

# Plotting a pie chart before Balancing the dataset
df['Diabetes'].value_counts()

balanced_counts = df['Diabetes'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(balanced_counts, labels=balanced_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Balanced Class Distribution')
plt.show()

# Out of total 578 people, 168 are diabetice. The countplot tell us that dataset is imbalanced.

"""# **Data Blancing**"""

x=df.iloc[:,:-1]
y=df.iloc[:,-1]

# Balancing the data

over_sampler = RandomOverSampler(random_state=42)
x_resampled, y_resampled = over_sampler.fit_resample(x,y)

# from imblearn.over_sampling import SMOTE

# smote = SMOTE(random_state=0)

# x_resampled, y_resampled = smote.fit_resample(x,y)

y_resampled.value_counts()

y_resampled.shape

# Plotting a pie chart after balancing the data
balanced_counts = y_resampled.value_counts()

plt.figure(figsize=(6, 6))
plt.pie(balanced_counts, labels=balanced_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Balanced Class Distribution')
plt.show()

# Here we can see that after balancing our data set is of size 820 (where 410->1 & 410->0)

# X_train, X_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.2, stratify=y_resampled, random_state=2)

import seaborn as sns

corrmat=df.corr()
top_corr_features=corrmat.index
plt.figure(figsize=(10,10))

# plot heatmap
g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")

# #observation-From correlation heatmap->
# we can see that there is a high correlation between outcome and
#  ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI',
#   'DiabetesPedigreeFunction', 'Age', 'Diabetes']

"""# **TRAIN TEST SPLIT**


"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.2, stratify=y_resampled, random_state=2)

X_train.shape,y_train.shape,X_test.shape,y_test.shape

# When you call the train_test_split function with a specific random_state value,
# it ensures that the data is split in the same way every time you run the code with the same random_state value.
# This allows for reproducibility of results, meaning that if you or someone else runs the code with the same random_state value,
# you will obtain the same train-test split.

"""# **STANDARDIZATION USING STANDARD SCALING**"""

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)

# Apply the same scaling to the testing set
X_test_scaled = scaler.transform(X_test)

# ## standardization and normalization are different thing
# ## Normalization
# Normalization is a rescaling of the data from the original range so that all values are within the new range of 0 and 1.
# Normalization requires that you know or are able to accurately estimate the minimum and maximum observable values.
# You may be able to estimate these values from your available data.

# A value is normalized as follows:
#
#     y = (x – min) / (max – min)
#
# Where the minimum and maximum values pertain to the value x being normalized.
#
# For example, for a dataset, we could guesstimate the min and max observable values as 30 and -10. We can then normalize any value, like 18.8, as follows:
#
#     y = (x – min) / (max – min)
#     y = (18.8 – (-10)) / (30 – (-10))
#     y = 28.8 / 40
#     y = 0.72
#
# You can see that if an x value is provided that is outside the bounds of the minimum and maximum values, the resulting value will not be in the range of 0 and 1.
# ## standardization
# Standardizing a dataset involves rescaling the distribution of values so that the mean of observed values is 0 and the standard deviation is 1.This can be thought of as subtracting the mean value or centering the data.
# A value is standardized as follows:
#
#     y = (x – mean) / standard_deviation
#
# Where the mean is calculated as:
#
#     mean = sum(x) / count(x)
#
# And the standard_deviation is calculated as:
#
#     standard_deviation = sqrt( sum( (x – mean)^2 ) / count(x))
#
# We can guesstimate a mean of 10.0 and a standard deviation of about 5.0. Using these values, we can standardize the first value of 20.7 as follows:
#
#     y = (x – mean) / standard_deviation
#     y = (20.7 – 10) / 5
#     y = (10.7) / 5
#     y = 2.14

#inplace of standard scaler we can also use data scaling technique
# like normalizer, minmax scaler and binarizer

"""# **BUILD THE CLASSIFICATION ALGORITHM -**

1. SVM
"""

from sklearn.svm import SVC
sv=SVC(kernel='rbf', random_state=42)
sv.fit(X_train,y_train)

train_pred=sv.predict(X_train)
test_pred=sv.predict(X_test)

# Train score and test score of logistic regression
from sklearn.metrics import accuracy_score

print("Accuracy (Train) of SVM", sv.score(X_train,y_train)*100)
print(" Accuracy (Test) of SVM", sv.score(X_test,y_test)*100)
print("Accuracy Score of SVM", accuracy_score(y_test,test_pred)*100)

# MAking the Confusion Matrix
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test, test_pred)

print("Confusion Matrix:")
print(conf_matrix)

# Calculate precision
from sklearn.metrics import precision_score

precision = precision_score(y_test, test_pred)
print("Precision: ",precision*100)

# Calculate F1 score
from sklearn.metrics import f1_score

f1 = f1_score(y_test, test_pred)
print("F1 Score: ", f1*100)

# Calculate Recall
from sklearn.metrics import recall_score
recall = recall_score(y_test, test_pred)
print("Recall :", recall*100)

"""2. Random Forest"""

from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier(criterion='entropy')
rf.fit(X_train,y_train)

rf_pred=rf.predict(X_test)

print("Accuracy (Train) of Random Forest",rf.score(X_train,y_train)*100)
print(" Accuracy (Test) of Random Forest",rf.score(X_test,y_test)*100)
print("Accuracy Score of Random forest", accuracy_score(y_test,rf_pred)*100)

# MAking the Confusion Matrix
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test, rf_pred)

print("Confusion Matrix:")
print(conf_matrix)

# Calculate precision
from sklearn.metrics import precision_score

precision = precision_score(y_test, rf_pred)
print("Precision: ",precision*100)

# Calculate F1 score
from sklearn.metrics import f1_score

f1 = f1_score(y_test, rf_pred)
print("F1 Score: ", f1*100)

# Calculate Recall
from sklearn.metrics import recall_score
recall = recall_score(y_test, rf_pred)
print("Recall :", recall*100)

"""3. Logistic Regression"""

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(solver='liblinear',multi_class='ovr')
lr.fit(X_train,y_train)

lr_pred=lr.predict(X_test)

print("Accuracy (Train)of Logistic Regression",lr.score(X_train,y_train)*100)
print(" Accuracy (Test) of Logistic Regression",lr.score(X_test,y_test)*100)
print("Accuracy Score of Logistic Regression", accuracy_score(y_test,lr_pred)*100)

# MAking the Confusion Matrix
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test, lr_pred)

print("Confusion Matrix:")
print(conf_matrix)

# Calculate precision
from sklearn.metrics import precision_score

precision = precision_score(y_test, lr_pred)
print("Precision: ",precision*100)

# Calculate F1 score
from sklearn.metrics import f1_score

f1 = f1_score(y_test, lr_pred)
print("F1 Score: ", f1*100)

# Calculate Recall
from sklearn.metrics import recall_score
recall = recall_score(y_test, lr_pred)
print("Recall :", recall*100)

"""4. Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(X_train,y_train)

dt_pred=dt.predict(X_test)

print("Accuracy (Train)of Decision Tree",dt.score(X_train,y_train)*100)
print(" Accuracy (Test) of Decision Tree",dt.score(X_test,y_test)*100)
print("Accuracy Score of Decision Tree", accuracy_score(y_test,dt_pred)*100)

# MAking the Confusion Matrix
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test, dt_pred)

print("Confusion Matrix:")
print(conf_matrix)

# Calculate precision
from sklearn.metrics import precision_score

precision = precision_score(y_test, dt_pred)
print("Precision: ",precision*100)

# Calculate F1 score
from sklearn.metrics import f1_score

f1 = f1_score(y_test, dt_pred)
print("F1 Score: ", f1*100)

# Calculate Recall
from sklearn.metrics import recall_score
recall = recall_score(y_test, dt_pred)
print("Recall :", recall*100)

"""5. KNN"""

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)

knn_pred=knn.predict(X_test)

print("Accuracy (Train)of KNN",knn.score(X_train,y_train)*100)
print(" Accuracy (Test) of KNN",knn.score(X_test,y_test)*100)
print("Accuracy Score of KNN", accuracy_score(y_test,knn_pred)*100)

# MAking the Confusion Matrix
from sklearn.metrics import confusion_matrix

conf_matrix = confusion_matrix(y_test, knn_pred)

print("Confusion Matrix:")
print(conf_matrix)

# Calculate precision
from sklearn.metrics import precision_score

precision = precision_score(y_test, knn_pred)
print("Precision: ",precision*100)

# Calculate F1 score
from sklearn.metrics import f1_score

f1 = f1_score(y_test, knn_pred)
print("F1 Score: ", f1*100)

# Calculate Recall
from sklearn.metrics import recall_score
recall = recall_score(y_test, knn_pred)
print("Recall :", recall*100)

