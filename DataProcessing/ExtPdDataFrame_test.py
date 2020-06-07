from DataProcessing import ExtPdDataFrame
from skimage.util import view_as_windows

data_path="C:/Users/pietr/Desktop/repos/battery model/NN_OCV_vs_ROD_temp/battery_data.csv"
data=ExtPdDataFrame()
data.load(data_path)



