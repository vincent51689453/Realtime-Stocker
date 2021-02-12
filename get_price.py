from yahoo_fin import stock_info as si
from datetime import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Get price template

while True:
    price = si.get_live_price('wkhs')
    print(price)