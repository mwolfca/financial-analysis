import pandas as pd
import numpy as np
import datetime as dt
import pandas_datareader as pdr
import matplotlib.pyplot as plt 

from pandas import Series, DataFrame
from pandas_datareader import data, wb
from datetime import timedelta, datetime, date


period = [30,60,90,180,270,365,700,1500]

today = dt.date.today()
start = today - timedelta(days=period[7])

panel = pdr.get_data_yahoo(['IMAE.AS'])

filter_period = pd.date_range(start=start, end=today, freq='D')
panel = panel.reindex(filter_period)
panel = panel.fillna(method='ffill')
panel = panel.reset_index()
panel = panel.groupby(['index'],as_index=False).mean()

fig = panel.plot('index',['Close', 'Open'],figsize=(15,10),marker='.',linestyle='-')
