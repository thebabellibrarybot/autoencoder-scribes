from tensorflow import keras

# Encoder Class
class encoder(keras.Model):
    def __init__(self):
        super(encoder, self).__init__()
        self.cnn1 = keras.layers.Conv2D(32, 3, strides=2, activation='relu', padding='same')
        self.cnn2 = keras.layers.Conv2D(64, 3, strides=2, activation='relu', padding='same')
        self.cnn3 = keras.layers.Conv2D(128, 3, strides=2, activation='relu')
    
    def call(self, x):
        x = self.cnn1(x)
        x = self.cnn2(x)     
        x = self.cnn3(x)        
        return x
# Decoder Class
class decoder(keras.Model):
    def __init__(self):
        super(decoder, self).__init__()
        self.cnnT1 = keras.layers.Conv2DTranspose(64, 3, strides=2, activation='relu')
        self.cnnT2 = keras.layers.Conv2DTranspose(32, 3, strides=2, activation='relu', padding='same')
        self.cnnT3 = keras.layers.Conv2DTranspose(1, 3, strides=2, activation='relu', padding='same')
    
    def call(self, x):
        x = self.cnnT1(x)
        x = self.cnnT2(x)     
        x = self.cnnT3(x)          
        return x
  #Autoencoder Class
class autoEncoder(keras.Model):
    def __init__(self):
        super(autoEncoder, self).__init__()
        self.encoder = encoder()
        self.decoder = decoder()
    
    def call(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

