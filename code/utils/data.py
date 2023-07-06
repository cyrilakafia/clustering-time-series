import pickle
import pandas as pd

data_dir = '../data/'

def read_pickle(f):
    return pickle.load(open(f, 'rb'))

def write_pickle(obj, f):
    pickle.dump(obj, open(f, 'wb'))

def load_network():
    return pd.read_pickle(data_dir + 'network.p')

# to load my custom dataset - Cyril
def load_my_network(file):
    return pd.read_pickle(data_dir + file)