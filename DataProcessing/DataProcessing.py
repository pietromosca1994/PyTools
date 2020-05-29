import pandas as pd
import os
import missingno as msno
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing    

class ExtPdDataFrame(object):
    
    def __init__(self, *args, **kwargs):  
        '''
        Initialisation method
        '''
        
        if 'path' in kwargs:
            self.path=kwargs['path']
            self.load_data(kwargs['path'])
        if 'dataframe' in kwargs:
            self.dataframe=kwargs['dataframe']
        if 'scaler' in kwargs:
            self.scaler=kwargs['scaler']        
        
    def info(self):
        '''
        Displays information on the loaded dataframe

        Returns
        -------
        None.

        '''
        self.dataframe.info()
        self.miss_vis()
        
        return None
    
    def load_data(self, path):
        '''
        Load data from a file 
        
        Returns
        -------
        None

        '''
        self.path=path
        # get file name and file extension from path
        filename, file_extension=os.path.splitext(self.path)
        
        # load data based on format
        if file_extension=='.csv':
            self.dataframe=pd.read_csv(self.path)            
            print('[INFO] Loaded', self.path)
        #elif file_extension== 
        else:
            raise NameError('Not a valid file path') 
            
        return None
    
    
    def miss_vis(self, *args, **kwargs):
        '''
        Visualise Missing Data statistics

        Returns
        -------
        None.

        '''
        start_sample=kwargs.get('start_sample', 0)
        end_sample=kwargs.get('end_sample', self.dataframe.shape[0])
        
        plt.figure()
        msno.matrix(self.dataframe[start_sample:end_sample])
        plt.show()
        #msno.bar(self.dataframe[start_sample:end_sample])
        
        return None
        
    def corrMatrix_vis(self):
        '''
        Visualise Correlation Matrix

        Returns
        -------
        None.
            
        '''
        plt.figure()
        self.corrMatrix=self.dataframe.corr()
        sn.heatmap(self.corrMatrix, annot=True)
        plt.show
        
        return None
      
    def X_Y_split(self, X_labels, Y_labels):
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
        None.

        '''
        
        self.X=self.dataframe.get(X_labels)
        self.Y=self.dataframe.get(Y_labels)
        
        print('[INFO] Dataset splitted into X and Y sets')
        
        return None
    
    def train_test_split(self, *args, **kwargs):
        '''
        Function to split train and test datasets
        '''
        
        self.X_train, self.X_test, self.Y_train, self.Y_test=train_test_split(self.X, self.Y, **kwargs)
         
        print('[INFO] Dataset splitted into Train (X_train, Y_train) and Test (X_test, Y_test) datasets')
        
        return None 

    def plot_2D(self, x_label, y_label, interval):
        '''
        Plots a 2D representation of 2 coloumns of self.dataframe
        '''
        
        x=self.dataframe.get(x_label)
        y=self.dataframe.get(y_label)
        self.x_test=x
        self.y_test=y
        
        x=x[interval[0]: interval[1]]
        y=y[interval[0]: interval[1]]
                
        plt.scatter(x,y)
        plt.xlabel(x_label)
        plt.ylabel(y_label)  
        plt.show()
        
        return None
         
    def preprocess(self, transformation, *args, **kwargs):
        '''
        Function to preprocess the data.
        sklearn.preprocessing wrapper
        '''
        
        if transformation=='StandardScaler': 
            self.scaler=preprocessing.StandardScaler()
            self.dataframe=pd.DataFrame(self.scaler.fit_transform(self.dataframe), columns=self.dataframe.columns)
            print('[INFO] Executed StandardScaler on the dataset')
        
        elif transformation=='Normalizer':
            self.scaler=preprocessing.Normalizer()
            self.dataframe=pd.DataFrame(self.scaler.fit_transform(self.dataframe), columns=self.dataframe.columns)
            print('[INFO] Executed Normalisation on the dataset')
        
        elif transformation=='MinMaxScaler':
            self.scaler=preprocessing.MinMaxScaler(*args, **kwargs)  
            self.dataframe=pd.DataFrame(self.scaler.fit_transform(self.dataframe), columns=self.dataframe.columns)
            print('[INFO] Executed MinMaxScaler on the dataset')
        
        elif transformation=='RobustScaler':
            self.scaler=preprocessing.RobustScaler(*args, **kwargs)
            self.dataframe=pd.DataFrame(self.scaler.fit_transform(self.dataframe), columns=self.dataframe)
            print('[INFO] Executed RobustScaler on the dataset')
             
        else:
            raise NameError('Transformation not implemented')     
        
        return self.scaler
        
    def inverse_transform(self, *args, **kwargs):
        '''
        Method to inverse the transformation applied to the data
        '''
        if 'scaler' in kwargs:
            self.scaler=kwargs['scaler']
        
        self.dataframe=pd.DataFrame(self.scaler.inverse_transform(self.dataframe), columns=self.dataframe.columns)
        print('[INFO] Executed Inverse Transform on the dataset')
        
        return None
         
        
        
        
        
        
    
        
        
        

