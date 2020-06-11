import pickle

def SaveData(obj, file_path, *args , **kwargs):
    '''
    obj, file_path
    '''
 
    dbfile=open(file_path, 'wb')
    pickle.dump(obj=obj, file=dbfile, *args, **kwargs)
    dbfile.close()
    
    print('[INFO] Exported data to ', file_path)
    
    return None

def LoadData(file_path, *args, **kwargs):
    '''
    file_path
    '''
    
    dbfile = open(file_path, 'rb')      
    obj=pickle.load(dbfile, *args, **kwargs) 
    dbfile.close()
    
    print('[INFO] Loaded data from ', file_path)
    
    return obj
    
    
    


