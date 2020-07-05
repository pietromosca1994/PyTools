from DataProcessing import ExtPdDataFrame
from skimage.util import view_as_windows
import numpy as np

# Create ExtPdDataFrame
columns=['feature1', 'feature2', 'feature3', 'feature4']
data=np.array([[1,1,1,1],
               [2,2,2,2],
               [3,3,3,3],
               [4,4,4,4],
               [5,5,5,5],
               [6,6,6,6],
               [7,7,7,7],
               [8,8,8,8],
               [9,9,9,9]])
df=ExtPdDataFrame(data, columns=columns)
print('Dataframe')
print(df)

# split in X and Y dataframes
X_features=['feature1', 'feature2', 'feature3']
Y_features=['feature4']
X_data, Y_data=df.X_Y_split(X_features, Y_features)

#apply transformation
df_trans=df
df_trans.Transform(transformation='StandardScaler')
print('Transformed Dataframe')
print(df_trans)


# view as windows for RNN training
window_length=2 
X_data.ViewAsWindows(window_length)
dims=X_data.shape
RNN_X_data=np.reshape(X_data.values, (int(dims[0]/window_length), window_length, dims[1]))
RNN_Y_data=Y_data[window_length-1:]
print('RNN X shape: ', RNN_X_data.shape)
print('RNN Y shape: ', RNN_Y_data.shape)


