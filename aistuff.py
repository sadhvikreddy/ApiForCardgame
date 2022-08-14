import json
from numpy import argsort
from tensorflow import keras
import pandas as pd

class aistuff:
    def __init__(self):
        self.model = keras.models.load_model('./modellossingNN.h5')
        self.zero = 0
        self.hundred = 100
        self.p1imin = 0
        self.p1imax = 0
        self.p2imin = 0
        self.p2imax = 0
        self.turnmax = 0
        self.setMinMaxForNorm('./Minmaxloss.json')
        
    def getPredictions(self, turn, p1h, p1i, p2h, p2i, p1t0, p1t1, p1t2, p2t0, p2t1, p2t2):
        turnnorm = self.normalize(turn,self.zero,self.turnmax)
        p1hn = self.normalize(p1h,self.zero,self.hundred)
        p1in = self.normalize(p1i, self.p1imin, self.p1imax)
        p2hn = self.normalize(p2h,self.zero,self.hundred)
        p2in = self.normalize(p2i,self.p2imin, self.p2imax)
        p1t0n = self.encodeBinary(p1t0)
        p1t1n = self.encodeBinary(p1t1)
        p1t2n = self.encodeBinary(p1t2)
        p2t0n = self.encodeBinary(p2t0)
        p2t1n = self.encodeBinary(p2t1)
        p2t2n = self.encodeBinary(p2t2)
        x = [turnnorm,p1hn,p1in,p2hn,p2in,p1t0n,p1t1n,p1t2n,p2t0n,p2t1n,p2t2n]
        column = ["turn","p1h","p1i","p2h","p2i","p1t0","p1t1","p1t2","p2t0","p2t1","p2t2"]
        df = pd.DataFrame(columns=column)
        df.loc[0] = x
        prediction = self.model.predict(df[:],verbose = 0)
        return argsort(prediction[0])
    
    def normalize(self, x, xmin, xmax):
        return ((x-xmin)/(xmax-xmin))
    
    def encodeBinary(self, x):
        if(x == "true"):
            return 1
        else:
            return 0 

    def setMinMaxForNorm(self, jsonFile):
        f = open(jsonFile, "r")
        data = json.loads(f.read())
        self.turnmax = data['Turn']['Max']
        self.p1imin= data['p1']['Min']
        self.p1imax= data['p1']['Max']
        self.p2imin= data['p2']['Min']
        self.p2imax= data['p2']['Max']
        f.close()
