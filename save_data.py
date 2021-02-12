from yahoo_fin import stock_info as si
from datetime import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from network import *
from random import shuffle
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import csv


#Company
target_stock = 'wkhs'
#Sampling interval
intervals_seconds = 1
#Buffers
price_buffer = []
time_buffer = []
index_buffer = []
#Plot
marker_color = 'b'
marker_size = 20
marker_shape = 'x'
#CSV data
file_path = 'stock.csv'
csv_index = 0



def get_stockprice_now(company):
    price = si.get_live_price(company)
    return price

def get_systime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def realtime_plot(time_x,price_y):
    plt.autoscale(enable=True, axis='both')
    y = np.array(price_y)
    x = np.array(time_x)
    plt.title('Stock Price :'+target_stock)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.scatter(x,y,s=marker_size,c=marker_color,marker=marker_shape)
    plt.pause(intervals_seconds)

    

def main():
    global price_buffer,window_size,csv_index,index_buffer
    counter = 0
    while True:
        #Read stock prices
        systime = get_systime()
        price = get_stockprice_now(target_stock)
        csv_list = [systime,price,csv_index]
        csv_index += 1


        #Save to csv for dataset
        with open(file_path, 'a',newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_list)
        
        #Realtime plot
        price_buffer.append(price)
        time_buffer.append(systime)
        index_buffer.append(csv_index)
        print("Time: "+systime+"| Price: "+str(price)+"|  Buffer_index: "+str(counter))
        realtime_plot(index_buffer,price_buffer)
        
    plt.show()



if __name__ == '__main__':
    main()