import matplotlib.pyplot as plt

#Hyperparameters
epoches = 700
batch_size = 64
initial_learning_rate = 0.001
decay_step = 100
decay_factor = 0.96

#Predictions
future_points = 200

#Dataset parameters
file_path = 'stock.csv'
training_fraction = 0.75
write_to_csv = False

#Stock parameters
target_stock = '2342.HK'
interval_seconds = 60
plot_delay = 10
sample_max = 10

