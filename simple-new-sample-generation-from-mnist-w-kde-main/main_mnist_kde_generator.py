#Simple New Sample Generation from MNIST w/KDE
#github ->  https://github.com/john-fante/Simple-New-Sample-Generation-from-MNIST-w-KDE
#kaggle -> https://www.kaggle.com/code/banddaniel/simple-new-sample-generation-from-mnist-w-kde

# Importing dependencies

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KernelDensity


# Reading and showing data
data = pd.read_csv('/kaggle/input/mnist-in-csv/mnist_train.csv')


# For splitting data into class by class
# label_no: class name, exp 2...

def create_class_df(label_no):
    data_new = data[data.label == label_no].reset_index()
    data_label = data_new['label']
    data_new = data_new.drop(['label','index'], axis=1)
    
    return data_new


# Creating data class by class

train_0_data = create_class_df(0)
train_1_data = create_class_df(1)
train_2_data = create_class_df(2)
train_3_data = create_class_df(3)
train_4_data = create_class_df(4)
train_5_data = create_class_df(5)
train_6_data = create_class_df(6)
train_7_data = create_class_df(7)
train_8_data = create_class_df(8)
train_9_data = create_class_df(9)


train = pd.DataFrame(train_0_data)


# This function using for new sample from correspondent class.
# Parameters df:data, sample_number: samples number derive from KDE.

def class_kde_sample_pipeline(df ,sample_number ):
        
    SC = StandardScaler()
    data_scaled = SC.fit_transform(df)
    
    PCA_ = PCA(n_components = 350)
    data_scaled_PCA = PCA_.fit_transform(data_scaled)
    
    KDE = KernelDensity(bandwidth = 0.1)
    KDE_data = KDE.fit(data_scaled_PCA)
    
    samples_data = KDE_data.sample(sample_number)
    samples_data_orig = PCA_.inverse_transform(samples_data)
    inv_SC = SC.inverse_transform(samples_data_orig)
    
    return inv_SC



# Generating new 500 sample each class

new_0_data = class_kde_sample_pipeline(train_0_data, 500)
new_1_data = class_kde_sample_pipeline(train_1_data, 500)
new_2_data = class_kde_sample_pipeline(train_2_data, 500)
new_3_data = class_kde_sample_pipeline(train_3_data, 500)
new_4_data = class_kde_sample_pipeline(train_4_data, 500)
new_5_data = class_kde_sample_pipeline(train_5_data, 500)
new_6_data = class_kde_sample_pipeline(train_6_data, 500)
new_7_data = class_kde_sample_pipeline(train_7_data, 500)
new_8_data = class_kde_sample_pipeline(train_8_data, 500)
new_9_data = class_kde_sample_pipeline(train_9_data, 500)



# Using for create a random sample from a numpy array

def get_random_sample(df):
    idx = random.randint(0, len(df)-1)
    sample = df[idx]
    sample = np.array(sample)
    sample = sample.reshape(28,28)
    return sample





# Plotting random samples from each class that creating with KDE

generated_data = [new_0_data, new_1_data, new_2_data,new_3_data ,new_4_data,
                new_5_data, new_6_data, new_7_data, new_8_data, new_9_data]



fig, axs = plt.subplots(10,5 ,figsize=(20,20), dpi=200 )

count=0

for m in range(10):
    for i in range(5):     
        axs[count][i].imshow(get_random_sample(generated_data[m]) , cmap='gray')
        axs[count][i].set_title('Generated w/KDE', color = 'red')
        
    count +=1
fig.tight_layout(pad=2.0)