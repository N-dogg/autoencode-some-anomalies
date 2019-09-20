from keras.layers import Input, Dense
from keras.models import Model, load_model
from keras.callbacks import ModelCheckpoint
from keras import regularizers

encoding_dim = 200
hidden_dim = int(encoding_dim/2)

class autoencoder(object):

    def __init__(self, input_dim, learning_rate = 1e-3):
        self.input_dim = input_dim
        self.save_path = "autoencoder_v4.h5"
        self.learning_rate = learning_rate
        self.input = Input(shape = (self.input_dim, ))
        self.encoder = Dense(encoding_dim, activation = 'relu', activity_regularizer= regularizers.l1(learning_rate))(self.input)
        self.encoder = Dense(hidden_dim, activation='relu')(self.encoder)
        self.encoder = Dense(int(hidden_dim/2), activation = 'relu')(self.encoder)
        self.decoder = Dense(hidden_dim, activation='relu')(self.encoder)
        self.decoder = Dense(encoding_dim, activation='relu')(self.decoder)
        self.decoder = Dense(self.input_dim, activation='sigmoid')(self.decoder)

        self.autoencoder = Model(inputs = self.input, outputs = self.decoder)

        self.autoencoder.compile(metrics = ['binary_accuracy'], loss = 'binary_crossentropy',
                    optimizer = 'adam')

    def summary(self):
        self.autoencoder.summary()

    def set_save_path(self, path):
        self.save_path = path

    def fit(self, train, valid, n_epochs = 100, batch_size = 500):
        cp = ModelCheckpoint(filepath=self.save_path,
                               save_best_only=True,
                               verbose=0)

        history = self.autoencoder.fit(train, train,
                            epochs=n_epochs,
                            batch_size=batch_size,
                            shuffle=True,
                            validation_data=(valid, valid),
                            verbose=1,
                            callbacks=[cp]).history

        return history

    def predict(self, x):
        return pd.DataFrame(autoencoder.predict(x))

    def load_model(self, path):
        self.autoencoder = load_model(path)
