import pandas as pd
import numpy as np
from scipy.interpolate import interp1d

def interpolate(df:pd.DataFrame, N=1000)-> pd.DataFrame:
    
    new_index = np.linspace(df.index[0], df.index[-1],N)
    df_plot=pd.DataFrame(index=new_index)
    for key,values in df.items():
        f = interp1d(x=df.index, y=values)
        df_plot[key] = f(new_index)

    return df_plot