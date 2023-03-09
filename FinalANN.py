import numpy as np
import tensorflow as tf
import pandas as pd
from keras import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from ann_visualizer.visualize import ann_viz

np.random.seed(7)
dataset = pd.read_csv("DiabetesDataset.csv")
medicines = ["Metaformin", "SGLT-2", "GLP-1", "DPP-4", "Thiazolidinediones", "Sulfonylureas", "A-Glucosesidase"]
med_array = [1,2,3,4,5,6,7]

X = dataset.iloc[:, 0:25].values
Y = dataset.iloc[:, 25:].values

train_X = X[:int(0.8*len(X))]
test_X = X[int(0.8*len(X)):]

train_Y = Y[:int(0.8*len(Y))]
test_Y = Y[int(0.8*len(Y)):]

model = Sequential()
model.add(Dense(32, input_dim=25, activation='relu')),
model.add(Dense(15, activation='relu')),
model.add(Dense(8, activation='relu')),
model.add(Dense(10, activation='relu')),
model.add(Dense(8, activation='relu')),
model.add(Dense(15, activation='relu')),
model.add(Dense(7, activation='softmax'));

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_X, train_Y, epochs=67)
model.save("final_ann_model.h5")
def sigmoidfunc(X):
    return 1/(1+np.exp(-X))

def funcpredict():
    print("Enter the Patient ID number: ")       #Row number is the Patient ID
    rn = input()
    a = int(rn)
    #a = 193
    predict = dataset.iloc[int(a), 0:25].values
    predict = np.array([predict])
    print(predict)
    res1 = model.predict(predict)
    
    finalres1 = sigmoidfunc(res1)
    fresult = finalres1.ravel().tolist()
    d1 = dict(enumerate(finalres1.flatten(),1))
    print(d1)
    d2 = dict(enumerate(medicines, 1))
    print(d2)
    
    maxprob = np.amax(finalres1)
    print(maxprob)
    for key, value in d1.items():
        if(value == maxprob):
            finalmed = key
            print(finalmed)
    
    for key,value in d2.items():
        if(key == finalmed):
            medsuggestion = value
    print("Medicine Suggested is : ", medsuggestion)
    

    plt.title("Medicine-Probability Graph")
    plt.plot(medicines, fresult, 'o', linestyle='solid', markerfacecolor='blue', color='orange')
    plt.annotate('Medicine Suggested', (medsuggestion,maxprob))
    plt.xlabel('Medicines')
    plt.ylabel('Probabilities')
    plt.show()
    
    ann_viz(model, title="Neural Network", view=True)
    tf.keras.utils.plot_model(model, to_file='network.png', show_shapes=True, show_layer_names=True)

funcpredict()