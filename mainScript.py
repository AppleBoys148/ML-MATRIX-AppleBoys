# %% [markdown]
# #IMPORTS

# %%
#Basic
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Scaling
from imblearn.over_sampling import RandomOverSampler

#ML
    #metrics
from sklearn.metrics import classification_report

    #KNN
from sklearn.neighbors import KNeighborsClassifier

    #naive bayes
from sklearn.naive_bayes import GaussianNB

    #log ref
from sklearn.linear_model import LogisticRegression

    #SVM
from sklearn.svm import SVC

    #NeuralNetworks
from sklearn.neural_network import MLPClassifier


# %% [markdown]
# #DATASET

# %%
# DATASET
# - TAKEN FROM KAGGLE
# - https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset

datasePath = "dataset.csv"

# %%
diseaseDF = pd.read_csv(datasePath)
diseaseNames = list(set(diseaseDF["Disease"].values))
diseaseCount = len(diseaseNames)
diseaseNames = dict(zip(diseaseNames, range(diseaseCount)))

for name in diseaseNames:
    diseaseDF = diseaseDF.replace(name, diseaseNames[name])

symptNames = set()

for symptNo in diseaseDF.columns[1:]:
    symptNames.update(diseaseDF[symptNo].values)

symptNames = list(symptNames)
symptCount = len(symptNames)

symptNames = dict(zip(symptNames, range(symptCount)))

for name in symptNames:
    diseaseDF = diseaseDF.replace(name, symptNames[name])

NULLINDEX = symptNames[np.nan]


# %% [markdown]
# #TRAIN, VALID, TEST

# %%
def Scaler(df: pd.DataFrame, oversample = True):
    ros = RandomOverSampler()
    X = [x[1:] for x in df.values]
    Y = [x[0] for x in df.values]
    if oversample: 
        X, Y = ros.fit_resample(X, Y)
    data = np.hstack((np.reshape(Y, (-1, 1)), X))
    return data, X, Y
    
    
def PlotHist(data, index = 0, title = "Plot"):
    plotdata = [int(x[index]) for x in np.array(data)]
    plt.hist(plotdata, bins = 41, rwidth = 0.5)
    plt.ylim(0, 100)
    plt.xlim(0, 43)
    plt.xlabel("Diseases")
    plt.ylabel("Disease_Count")
    plt.title(title)
    plt.show()

# %%

dataCount = len(diseaseDF)

train, valid, test = np.split(diseaseDF.sample(frac = 1), (int(0.6 * dataCount), int(0.7 * dataCount)))

# PlotHist(train, title = "train")
# PlotHist(valid, title = "valid")
# PlotHist(test, title = "test")

train, Xtrain, Ytrain = Scaler(train)
valid, Xvalid, Yvalid = Scaler(valid, False)
test, Xtest, Ytest = Scaler(test, False)

# print("AFTER OVERSAMPLING")

# PlotHist(train, title = "train_resampled")
# PlotHist(valid, title = "valid")
# PlotHist(test, title = "test")

# %% [markdown]
# #KNN

# %%

# print()
# print("KNN")
# print()

knn_model = KNeighborsClassifier()
knn_model = knn_model.fit(Xtrain, Ytrain)

Ypred = knn_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %% [markdown]
# #Naive Bayes

# %%
# print()
# print("NAIVE BAYES")
# print()

nb_model = GaussianNB()
nb_model = nb_model.fit(Xtrain, Ytrain)

Ypred = nb_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %% [markdown]
# #Logistic Regression

# %%
# print()
# print("LOGISTIC REGRESSION")
# print()

lg_model = LogisticRegression()
lg_model = lg_model.fit(Xtrain, Ytrain)

Ypred = lg_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %% [markdown]
# #SVM

# %%
# print()
# print("SVM")
# print()

svm_model = SVC()
svm_model = svm_model.fit(Xtrain, Ytrain)

Ypred = svm_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %% [markdown]
# #NEURAL NETWORKS

# %%
# print()
# print("NEURAL NETWORKS")
# print()

nn_model = MLPClassifier(hidden_layer_sizes = 10,
                         activation = "logistic",
                         solver = "adam")
nn_model = nn_model.fit(Xtrain, Ytrain)

Ypred = nn_model.predict(Xtest)

# print(classification_report(Ytest, Ypred))

# %%

def Diagnose(symptoms, model):
    symptoms = [symptNames[name] for name in symptoms]
    diagnosis = int(model.predict(np.reshape(symptoms, (1, -1)))[0])
    for disease in diseaseNames:
        if diseaseNames[disease] == diagnosis:
            print(disease)
            return disease
 

