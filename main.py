from yahoo_fin import stock_info as si
from datetime import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Company
target_stock = 'wkhs'
#Sampling interval
intervals_seconds = 1
#Analyze window size
window_size = 100
#Buffers
price_buffer = []
time_buffer = []
#Plot
marker_color = 'b'
marker_size = 20
marker_shape = 'x'



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
    plt.title('AI Estimator:'+target_stock)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.scatter(x,y,s=marker_size,c=marker_color,marker=marker_shape)
    plt.pause(intervals_seconds)
    

def main():
    global price_buffer,window_size
    counter = 0
    while True:
        systime = get_systime()
        price = get_stockprice_now(target_stock)

        if(counter<window_size):
            price_buffer.append(price)
            time_buffer.append(systime)
            print("Time: "+systime+"| Price: "+str(price)+"|  Buffer_index: "+str(counter))
            if(counter>0):
                realtime_plot(time_buffer,price_buffer)
            counter += 1
        else:
            price_buffer = []
            counter = 0


        #time.sleep(intervals_seconds)
    plt.show()



if __name__ == '__main__':
    main()