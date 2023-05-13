from tensorflow import keras

def encoder():
    inputs = keras.Input(shape=(28, 28, 1))
    x = keras.layers.Conv2D(32, 3, strides=2, activation='relu', padding='same')(inputs)
    x = keras.layers.Conv2D(64, 3, strides=2, activation='relu', padding='same')(x)
    x = keras.layers.Conv2D(128, 3, strides=2, activation='relu')(x)
    return keras.Model(inputs, x)

def decoder():
    inputs = keras.Input(shape=(4, 4, 128))
    x = keras.layers.Conv2DTranspose(64, 3, strides=2, activation='relu')(inputs)
    x = keras.layers.Conv2DTranspose(32, 3, strides=2, activation='relu', padding='same')(x)
    x = keras.layers.Conv2DTranspose(1, 3, strides=2, activation='sigmoid', padding='same')(x)
    return keras.Model(inputs, x)

def autoencoder():
    inputs = keras.Input(shape=(28, 28, 1))
    x = encoder()(inputs)
    x = decoder()(x)
    return keras.Model(inputs, x)

