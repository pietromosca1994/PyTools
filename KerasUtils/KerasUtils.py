import os
from DataExport import SaveData
from DataExport import LoadData
from tensorflow.keras.models import load_model
from tensorflow.keras.models import load_weights

#######################################################################################
# save model
#######################################################################################
def SaveKerasModel(model, path):
 
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
    
    return None
    
#######################################################################################
# load model
#######################################################################################
def LoadKerasModel(path):
    
    # load NN model
    model=load_model(path)
    model.summary()
    print('[INFO] Loaded NN model from '+path)

    return model

#######################################################################################
# load weights
#######################################################################################
def LoadKerasWeights(model, path):
   
    model.load_weights(path)
    
    print('[INFO] Loaded NN model weights from '+path+' ...')
    
    return model
