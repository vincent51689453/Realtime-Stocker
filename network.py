import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, concatenate
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import sys_setup as ss


def Neural_Network():
    model = Sequential()
    neurons = 500

    #Input layer
    model.add(Dense(neurons, input_dim=1, activation='tanh', kernel_initializer='normal'))
    
    #Hidden layer
    model.add(Dense(int(neurons-20*1),input_dim = neurons,activation='tanh', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-20*2),input_dim = int(neurons-20*1),activation='tanh', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-20*3),input_dim = int(neurons-20*2),activation='tanh', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-20*4),input_dim = int(neurons-20*3),activation='tanh', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-20*5),input_dim = int(neurons-20*4),activation='tanh', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-20*6),input_dim = int(neurons-20*5),activation='tanh', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    model.add(Dense(int(neurons-20*7),input_dim = int(neurons-20*6),activation='tanh', kernel_initializer='normal'))
    model.add(Dropout(0.15))
    #Output layer
    model.add(Dense(1, activation='linear'))

    return model

def model_training(training_x,training_y,testing_x,testing_y,raw_index,raw_price):
    #Start AI Analysis
    loss_function = tf.keras.losses.MeanSquaredError()    

    #Create Network, remember to change the network with different dataset
    model = Neural_Network()

    # fit the model on the training dataset
    lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        ss.initial_learning_rate,
        decay_steps=ss.decay_step ,
        decay_rate=ss.decay_factor,
        staircase=True)

    opt = keras.optimizers.Adam(learning_rate=lr_schedule)
    #opt = keras.optimizers.SGD(learning_rate=lr_schedule,momentum=0.9)
    #opt = keras.optimizers.SGD(learning_rate=lr_schedule,momentum=0.9)
    model.compile(loss=loss_function, optimizer=opt)
    history = model.fit(training_x, training_y, epochs=ss.epoches, batch_size=ss.batch_size, validation_data=(testing_x, testing_y), verbose=2)
    model.save('Network_core.h5')
    print("Network saved!")

    print()
    print("History keys are following: ")
    print(history.history.keys())
    print()

    #Data Visualization
    fig = plt.figure(1,figsize=(15,8))
    plt.subplot(2,2,1)
    plt.title('Data Distribution')
    #plt.scatter(index, price_data, c='blue', label='Market',s=2)
    plt.scatter(training_x, training_y, c='red', label='train',s=5)
    plt.scatter(testing_x, testing_y, c='green', label='validation',s = 5)
    plt.legend()
    plt.grid()

    plt.subplot(2,2,2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['loss', 'validation loss'], loc='upper left')
    plt.grid()


    #Prediction
    y_pred = model.predict(raw_index)
    plt.subplot(2,2,3)
    plt.title('AI Stock Price Prediction')
    plt.scatter(raw_index, raw_price, c='green', label='Market',s=5)
    plt.scatter(raw_index, y_pred, c='red', label='AI-Prediction',s=5)
    plt.legend()
    plt.grid()
    plt.show()
