from model import BRC
from generator import Generator
import glob
import os
from keras.optimizers import Adam
from random import shuffle
from keras.callbacks import ModelCheckpoint, TensorBoard,EarlyStopping
import matplotlib.pyplot as plt

def process(paths):

	# Get the model
	model = BRC()
	model.model.summary()

	# Get the generator
	img_list = glob.glob(os.path.join(paths,'*.jpg'))
	shuffle(img_list)
	split = int(0.8*len(img_list))
	print("split value",split)
	train = Generator(img_list[0:split],8)
	valid = Generator(img_list[split:],8).__getitem__(5)

	# Compile model then run
	optimizer = Adam(lr = 0.002)
	model.model.compile(loss = 'mean_squared_error',optimizer = optimizer)


	# Define Callbacks (save model, validation etc)
	ckpt = ModelCheckpoint('model.h5',save_best_only=True,mode = 'min')
	tsb = TensorBoard(log_dir=os.path.join( os.getcwd(),'logs' ),write_graph=True,histogram_freq=1)
	early_stop_cb = EarlyStopping(monitor='val_loss',min_delta=0.001,patience=3,mode='min',verbose=1)
	callback = [ckpt,tsb,early_stop_cb]

	# Train the model
	run_hist_2=model.model.fit_generator(generator = train,steps_per_epoch = 5,epochs = 5,verbose = 1,validation_data = valid,callbacks = callback)

	fig = plt.figure()
	plt.plot(run_hist_2.history["loss"],'r', marker='.', label="Train Loss")
	plt.plot(run_hist_2.history["val_loss"],'b', marker='.', label="Validation Loss")
	plt.title("Train loss and validation error with dropouts")
	plt.legend()
	plt.grid()
	fig.savefig('TrainLoss.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	