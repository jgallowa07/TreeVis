from keras import models
from keras import layers
from ImageProcessing import *
from keras import backend as K
import numpy as np
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

data,targets = LoadImageData(	rootdir = "../Images/RecombRegressionData",
				labelPath = "../Images/Labels",
				numSamples = 2000,
				percentValidation=0.0,
				imagePostFix="_VR.png")

num_val_samples = 100
num_epochs = 20
batch_size = 3

data = data[:,850:,850:,:]
targets = targets * 1e9

val_data = data[:num_val_samples]
val_targets = targets[:num_val_samples]

train_data = data[num_val_samples:]
train_targets =targets[num_val_samples:]

if K.image_data_format() == 'channels_first':
    input_shape = (3, 150, 150)
else:
    input_shape = (150, 150, 3)

def build_model():
    # Because we will need to instantiate
    # the same model multiple times,
    # we use a function to construct it.
	model = models.Sequential()
	model.add(Conv2D(32, (3, 3), input_shape=input_shape))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Conv2D(32, (3, 3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

#	model.add(Conv2D(64, (3, 3)))
#	model.add(Activation('relu'))
#	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Flatten())
	model.add(Dense(64))
	model.add(Activation('relu'))
	model.add(Dropout(0.5))
	model.add(Dense(1))
	model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
	return model

'''
#K-fold cross validation
k = 5
num_val_samples = len(train_data) // k
num_epochs = 2
all_scores = []
for i in range(k):
    print('processing fold #', i)
    # Prepare the validation data: data from partition # k
    val_data = train_data[i * num_val_samples: (i + 1) * num_val_samples]
    val_targets = train_targets[i * num_val_samples: (i + 1) * num_val_samples]

    # Prepare the training data: data from all other partitions
    partial_train_data = np.concatenate(
        [train_data[:i * num_val_samples],
         train_data[(i + 1) * num_val_samples:]],
        axis=0)
    partial_train_targets = np.concatenate(
        [train_targets[:i * num_val_samples],
         train_targets[(i + 1) * num_val_samples:]],
        axis=0)

    # Build the Keras model (already compiled)
    model = build_model()
    # Train the model (in silent mode, verbose=0)
    model.fit(partial_train_data, partial_train_targets,
              epochs=num_epochs, batch_size=1, verbose=0)
    # Evaluate the model on the validation data
    val_mse, val_mae = model.evaluate(val_data, val_targets,verbose=0)
    all_scores.append(val_mae)

print(all_scores)
'''


#k = 5

    # Build the Keras model (already compiled)
model = build_model()
    # Train the model (in silent mode, verbose=0)
model.fit(train_data,train_targets,
              epochs=num_epochs, batch_size=batch_size)
    # Evaluate the model on the validation data
val_mse, val_mae = model.evaluate(val_data, val_targets)

print(val_mae)


