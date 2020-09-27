import pandas  # Loading data / handling data frames
import numpy as np
import matplotlib.pyplot as plt

#green = [1]
#blue = [0]
#red = [2]
#(blue-red)/green

def res_out(imags):
    np.seterr(divide='ignore', invalid='ignore')
    output_matrix = ((imags[0].astype('float32')-imags[2].astype('float32'))/imags[1].astype('float32'))
    output_matrix = output_matrix[0,:,:]
    plt.imshow(output_matrix, aspect='auto', cmap='RdYlBu')
    cbar = plt.colorbar()
    cbar.set_label('Chl-a mg/m³')
    plt.show()


def mci_out(S_imags_rspld):    
    np.seterr(divide='ignore', invalid='ignore')
    output_matrix = (S_imags_rspld[4].astype('float32')-S_imags_rspld[3].astype('float32')*((705-665)/(740/665))*(S_imags_rspld[5].astype('float32')-S_imags_rspld[3].astype('float32'))
    output_matrix = output_matrix[0,:,:]
    
    plt.imshow(output_matrix, aspect='auto')
    cbar = plt.colorbar()
    cbar.set_label('Chl-a mg/m³')
    plt.show()



#from ml_visualization import res_out
#from ml_visualization import mci_out

