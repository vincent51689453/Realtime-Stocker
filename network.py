import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, concatenate
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

epoches = 1500
batch_size = 64
initial_learning_rate = 0.001
decay_step = 100
decay_factor = 0.96

def Neural_Network():
    model = Sequential()
    neurons = 500

    #Input layer
    model.add(Dense(neurons, input_dim=1, activation='relu', kernel_initializer='normal'))
    
    #Hidden layer
    model.add(Dense(int(neurons-50*1),input_dim = neurons,activation='relu', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-50*2),input_dim = int(neurons-50*1),activation='relu', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-50*3),input_dim = int(neurons-50*2),activation='relu', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-50*4),input_dim = int(neurons-50*3),activation='relu', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-50*5),input_dim = int(neurons-50*4),activation='relu', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-50*6),input_dim = int(neurons-50*5),activation='relu', kernel_initializer='normal'))
    model.add(Dropout(0.15))

    #Output layer
    model.add(Dense(1, activation='sigmoid'))

    return model

def model_training(training_x,training_y,testing_x,testing_y,raw_index,raw_price):
    #Start AI Analysis
    loss_function = tf.keras.losses.MeanSquaredError()    

    #Create Network, remember to change the network with different dataset
    model = Neural_Network()

    # fit the model on the training dataset
    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate,
        decay_steps=decay_step ,
        decay_rate=decay_factor,
        staircase=True)

    #opt = keras.optimizers.Adam(learning_rate=lr_schedule)
    #opt = keras.optimizers.SGD(learning_rate=lr_schedule,momentum=0.9)
    opt = keras.optimizers.SGD(learning_rate=lr_schedule,momentum=0.9)
    model.compile(loss=loss_function, optimizer=opt)
    history = model.fit(training_x, training_y, epochs=epoches, batch_size=batch_size, validation_data=(testing_x, testing_y), verbose=2)

    print()
    print("History keys are following: ")
    print(history.history.keys())
    print()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['loss', 'validation loss'], loc='upper left')
    plt.grid()
    plt.show()


    #Prediction
    y_pred = model.predict(raw_index)
    fig = plt.figure(figsize=(15,8))
    plt.title('AI Prediction of EURUSD')
    plt.scatter(raw_index, raw_price, c='green', label='Market',s=5)
    plt.scatter(raw_index, y_pred, c='red', label='AI-Prediction',s=5)
    plt.legend()
    plt.grid()
    plt.show()