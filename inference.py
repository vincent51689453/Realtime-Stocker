import matplotlib.pyplot as plt
from random import shuffle
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import csv
import network
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import sys_setup as ss

#Raw data
price_data = []
time_data = []
index = []

#AI input
price_ready = []

def load_dataset(csv_file):
    i = 0
    global price_data,time_data,index
    print("[INFO] Start loading dataset...")
    print("[INFO] It may take some time... Be patient")
    with open(csv_file) as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            price_data.append(float(row[1]))
            time_data.append(row[0])
            index.append(i)
            i += 1
    print("[INFO] Dataset is ready...")
    return i  

def split_data(num_data):
    #Prepare training and testing dataset
    np.random.seed(1000)

    #Zip two lists together so they can shuffle in the same order
    temp = list(zip(price_data,index)) 

    #Backup and normalized ordered data
    sc = MinMaxScaler()
    norm_price = np.array(price_data)
    norm_price_backup = sc.fit_transform(norm_price.reshape(-1,1))
    norm_price_backup = norm_price_backup.reshape(1,-1)    

    np.random.shuffle(temp)

    #Sepearte two lists
    y_data,x_data = zip(*temp)  


    #Normalize price within 0 - 1
    sc = MinMaxScaler()
    y_data = np.array(y_data)
    y_data_norm = sc.fit_transform(y_data.reshape(-1,1))
    y_data_norm = y_data_norm.reshape(1,-1)

    x_data = np.array(x_data)
    
    i = 0
    while(i<num_data):
        price_ready.append(y_data_norm[0][i])
        i+=1

    training_size = int(num_data*ss.training_fraction)

    x_train = x_data[:training_size]
    x_test = x_data[training_size:]
    y_train = price_ready[:training_size]
    y_test = price_ready[training_size:]  

    """
    plt.subplot(2,2,1)
    plt.title('Data Distribution')
    #plt.scatter(index, price_data, c='blue', label='Market',s=2)
    plt.scatter(x_train, y_train, c='red', label='train',s=5)
    plt.scatter(x_test, y_test, c='green', label='validation',s = 5)
    plt.legend()
    plt.grid()
    #plt.show()
    """   

    return x_train,x_test,y_train,y_test,norm_price_backup

def main():

    total_data = load_dataset(ss.file_path)
    x_train,x_test,y_train,y_test,y_backup = split_data(total_data)
    network.model_training(x_train,y_train,x_test,y_test,index,y_backup)



if __name__ == '__main__':
    main()