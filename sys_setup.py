import matplotlib.pyplot as plt

#Hyperparameters
epoches = 700
batch_size = 64
initial_learning_rate = 0.001
decay_step = 100
decay_factor = 0.96

#Dataset parameters
file_path = 'stock.csv'
training_fraction = 0.75

#Stock parameters
target_stock = 'wkhs'
interval_seconds = 1

