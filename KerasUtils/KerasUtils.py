import os
from DataExport import SaveData
from DataExport import LoadData
from keras.models import load_model

#######################################################################################
# save model
#######################################################################################
def SaveKerasModel(model, history, path):
 
    if not(os.path.isdir(path)):
        os.mkdir(path)
        
    # save NN model        
    model.save(path+'model.h5')
    print('[INFO] Saved NN model to '+path)

    # Save model JSON config
    json_config = model.to_json()
    with open(path+'model_config.json', 'w') as json_file:
        json_file.write(json_config)
    print('[INFO] Saved NN model config to '+path)
    
    # Save model weights
    model.save_weights(path+'model_weights.h5')
    print('[INFO] Saved NN model weights to '+path)

    # save training history
    SaveData(history, path+'history.pckl')
    
    return None
    
#######################################################################################
# load model
#######################################################################################
def LoadKerasModel(path):
    
    # load NN model
    model=load_model(path+'model.h5')
    model.summary()
    print('[INFO] Loaded NN model from '+path)
    
    # load training history
    history=LoadData(path+'history.pckl')
    print('[INFO] Loaded NN model history from '+path)
    
    return model, history

#######################################################################################
# load weights
#######################################################################################
def LoadKerasWeights(model, path):
   
    model.load_weights(path+'model_weights.h5')
    
    print('[INFO] Loaded NN model weights from '+path+' ...')
    
    return model
