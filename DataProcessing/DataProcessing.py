import pandas as pd
import numpy as np
import os
import missingno as msno
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from skimage.util import view_as_windows
from sklearn import preprocessing

class ExtPdDataFrame(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super(ExtPdDataFrame, self).__init__(*args, **kwargs)

    @property
    def _constructor(self):
        return type(self)
    
    def load(self, path, *args, **kwargs):
        '''
        Function to load data into a DataFrame from a file
        '''
        # get file name and file extension from path
        filename, file_extension=os.path.splitext(path)
        
        # load data based on format
        if file_extension=='.csv':
            self.__init__(pd.read_csv(path, *args, **kwargs))            
            print('[INFO] Loaded', path)
        #elif file_extension== 
        else:
            raise NameError('Not a valid file path')
        
        return None
    
    def X_Y_split(self, X_features, Y_features):
        ''' 
        Method to split dataset in X and Y datasets
        
        Parameters
        ----------
        X_labels : list
            X dataset labels
        Y_labels : list
            X dataset labels

        Returns
        -------
        X_dataframe
        Y_dataframe

        '''
        
        X_dataframe=self.get(X_features)
        Y_dataframe=self.get(Y_features)
        
        return X_dataframe, Y_dataframe
    
    def train_test_split(self, *args, **kwargs):
        '''
        Wrpper for sklearn.model_selection.train_test_split
        
        '''
        
        training_dataframe, test_dataframe=train_test_split(self, *args, **kwargs)
        
        return training_dataframe, test_dataframe 
    
    def transform(self, transformation, scaler=None, *args, **kwargs):
        '''
        Wrapper for sklearn.preprocessing
        
        Parameters
        ----------
        transformation : 'string'
            preprocessing transformation from sklearn.preprocessing
        
        Returns
        -------
        self.scaler : scaler(object)
            scaler
        '''
    
        if scaler==None:
            if transformation=='StandardScaler': 
                scaler=preprocessing.StandardScaler()
            
            elif transformation=='Normalizer':
                scaler=preprocessing.Normalizer()
            
            elif transformation=='MinMaxScaler':
                scaler=preprocessing.MinMaxScaler(*args, **kwargs)  
            
            elif transformation=='RobustScaler':
                scaler=preprocessing.RobustScaler(*args, **kwargs)
            
            self.scaler=scaler.fit(self.values)
        else:
            self.scaler=scaler

        self.__init__(scaler.transform(self.values), columns=self.columns)
        self.scaler=scaler
        
        return None
        
    def inverse_transform(self, *args, **kwargs):
        '''
        Method to inverse the transformation applied to the data
        
        Parameters
        ----------
        transformation : 'string'
            preprocessing transformation from sklearn.preprocessing
        
        Returns
        -------
        None      
        '''
        self.__init__(self.scaler.inverse_transform(self.values), columns=self.columns)
        
        return None
    
    def ViewAsWindows(self, window_length):
        '''
        window_length
        
        Parameters
        ----------
        window_length : 'int'
            length (in samples) of the window
        
        Returns
        -------
        None      
        '''   
        data_as_windows=np.squeeze(view_as_windows(self.values, (window_length, self.values.shape[1])))
        shape=data_as_windows.shape
        data_as_windows=np.reshape(data_as_windows, (shape[0]*shape[1], shape[2]))
        self.__init__(data_as_windows, columns=self.columns)
        
        return None
        
    def miss_plt(self, *args, **kwargs):
        '''
        Visualise Missing Data statistics

        Returns
        -------
        None.

        '''
        start_sample=kwargs.get('start_sample', 0)
        end_sample=kwargs.get('end_sample', self.shape[0])
        
        msno.matrix(self[start_sample:end_sample])
        #msno.bar(self.dataframe[start_sample:end_sample])
        
        return None
    
    def CorrMatrix_vis(self, *args, **kwargs):
        '''
        Visualise Correlation Matrix
        Wrapper for pandas.DataFrame.corr()

        Returns
        -------
        None.
            
        '''
        plt.figure()
        CorrMatrix=self.corr(*args, **kwargs)
        sn.heatmap(CorrMatrix, annot=True)
        plt.show
        
        return CorrMatrix