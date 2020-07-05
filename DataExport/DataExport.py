import pickle
import json
import os

def SaveData(obj, path, *args , **kwargs):
    '''
    obj, file_path
    '''
 
    dbfile=open(path, 'wb')
    pickle.dump(obj=obj, file=dbfile, *args, **kwargs)
    dbfile.close()
    
    print('[INFO] Exported data to ', path)
    
    return None

def LoadData(path, *args, **kwargs):
    '''
    file_path
    '''
    filename, file_extension=os.path.splitext(path)
    dbfile = open(path, 'rb') 
    
    if file_extension=='.pckl':     
        obj=pickle.load(dbfile, *args, **kwargs)
    elif file_extension=='.json':
        obj=json.load(dbfile, *args, **kwargs)
    
    dbfile.close()
    
    print('[INFO] Loaded data from ', path)
    
    return obj   