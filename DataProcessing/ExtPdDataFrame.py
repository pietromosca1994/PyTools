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
        self.scaler=None

    @property
    def _constructor(self):
        return type(self)
    
    def load(self, path):
        '''
        Function to load data into a DataFrame from a file
        '''
        # get file name and file extension from path
        filename, file_extension=os.path.splitext(path)
        
        # load data based on format
        if file_extension=='.csv':
            dataframe=self.__init__(pd.read_csv(path))            
            print('[INFO] Loaded', path)
        #elif file_extension== 
        else:
            raise NameError('Not a valid file path')
        
        return dataframe
    
    def X_Y_split(self, X_columns, Y_columns):
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
        
        X_dataframe=self.get(X_columns)
        Y_dataframe=self.get(Y_columns)
        
        return X_dataframe, Y_dataframe
    
    def train_test_split(self, *args, **kwargs):
        '''
        Wrpper for sklearn.model_selection.train_test_split
        
        '''
        
        training_dataframe, test_dataframe=train_test_split(self, *args, **kwargs)
        
        return training_dataframe, test_dataframe 
    
    def transform(self, transformation, *args, **kwargs):
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
        
        if transformation=='StandardScaler': 
            scaler=preprocessing.StandardScaler()
        
        elif transformation=='Normalizer':
            scaler=preprocessing.Normalizer()
        
        elif transformation=='MinMaxScaler':
            scaler=preprocessing.MinMaxScaler(*args, **kwargs)  
        
        elif transformation=='RobustScaler':
            scaler=preprocessing.RobustScaler(*args, **kwargs)
        
        
        self.__init__(scaler.fit_transform(self.values), columns=self.columns)
        self.scaler=scaler
        
        return self.scaler
        
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
        self.scaler=kwargs.get('scaler', self.scaler)
        self.__init__(self.scaler.inverse_transform(self.values), columns=self.columns)
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
        
        plt.figure()
        msno.matrix(self.dataframe[start_sample:end_sample])
        plt.show()
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
    
    def view_as_windows(self, *args, **kwargs):
        self.__init__(view_as_windows(np.array(self.values), *args, **kwargs), columns=self.columns)
        
        return None