from DataProcessing import ExtPdDataFrame
from skimage.util import view_as_windows
import numpy as np

X_features=['feature1', 'feature2']
Y_features=['feature3']
data=np.array([[1,1,1],
               [2,2,2],
               [3,3,3],
               [4,4,4],
               [5,5,5],
               [6,6,6],
               [7,7,7],
               [8,8,8],
               [9,9,9]])
           
columns=['feature1', 'feature2', 'feature3']
data=ExtPdDataFrame(data, columns=columns)
X_data, Y_data=data.X_Y_split(X_features, Y_features)
window_length=2
X_data.ViewAsWindows(window_length)
dims=X_data.shape
LSTM_X_data=np.reshape(X_data.values, (int(dims[0]/window_length), window_length, dims[1]))
LSTM_Y_data=Y_data[window_length-1:]



