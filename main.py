import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import log

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from model import autoencoder

#data import
#preprocessing
#plotting
#error calculation
#anything not model or train

#run

def preprocessing(df):
    #onehot encoding
    for col in df:
        if col != 'ID':
            df = pd.get_dummies(df, columns = [col], drop_first = True)

    #isolate the errors
    df_1 = df[df['ID']==1]
    df = df[df.ID != 1]

    #train-test-valid-split & drop ID columns
    df_train, df_test = train_test_split(df, test_size = 0.2)
    df_train, df_valid = train_test_split(df_train, test_size = 0.2)
    df_train = df_train.drop(['ID'], axis = 1)
    df_valid = df_valid.drop(['ID'], axis = 1)
    df_test = df_test.append(df_1)
    df_test_y = pd.DataFrame(df_test['ID'])
    df_test = df_test.drop(['ID'], axis = 1)

    print(df_train.shape, df_valid.shape, df_test.shape, df_test_y.shape)

    return df_train, df_valid, df_test, df_test_y

def train_plot(training_data):
    #plot the loss vs. training epoch
    plt.plot(history['loss'], linewidth=2, label='Train')
    plt.plot(history['val_loss'], linewidth=2, label='Valid')
    plt.legend(loc='upper right')
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.show()

def binary_cross_entropy(actual, predicted):
    #calculate binary cross entropy between actual and predicted
    sum_score = 0.0
    for i in range(len(actual)):
        sum_score += actual[i] * log(1e-15 + predicted[i])
    mean_sum_score = 1.0 / len(actual) * sum_score

    return -mean_sum_score

def reconstruction_loss(x, x_pred, label):
    #calculate the reconstruction loss for each journal
    reconstruction_loss_transaction = np.zeros(x.shape[0])
    for i in range(0, x.shape[0]):
        reconstruction_loss_transaction[i] = binary_cross_entropy(x.iloc[i], x_pred.iloc[i])

    error_df_test = pd.DataFrame({'Reconstruction_error': reconstruction_loss_transaction,
                                'True_class': label['ID']})
    error_df_test = error_df_test.reset_index()

    return error_df_test

def error_plot(df_error):
    #plot the reconstruction loss for each journal - highlighting the errors
    groups = error_df_test.groupby('True_class')
    fig, ax = plt.subplots()

    for name, group in groups:
        ax.plot(group.index, group.Reconstruction_error, marker='o', ms=3.5, linestyle='',
                label= "Error" if name == 1 else "Normal")
    ax.legend()
    plt.title("Reconstruction error for different classes")
    plt.ylabel("Reconstruction error")
    plt.xlabel("Data point index")
    plt.show();



if __name__ == '__main__':

    #data import
    filename = 'Book1.csv'
    df = pd.read_csv(filename)
    df_train, df_valid, df_test, df_test_y = preprocessing(df)

    #create the model
    model = autoencoder(df_train.shape[1])
    model.summary()

    #train the model
    output = model.fit(df_train, df_valid)
    train_plot(output)
