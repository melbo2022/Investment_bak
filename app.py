#test1
#-m streamlit.cli run
#pip install pandas-datareader
import pandas_datareader.data as DataReader
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
#株価を抽出してグラフにする
#日本語フォントをインポートする(matplotlib)
import matplotlib as mpl
mpl.rc('font', family="MS Gothic")

#データ取得の日付を設定
symd_s="2022/6/1"
symd_e="2022/7/31"

#取得する銘柄を指定
cur='^N225'

symd_sd = datetime.datetime.strptime(symd_s,'%Y/%m/%d')
symd_ed = datetime.datetime.strptime(symd_e,'%Y/%m/%d')

#データを取得してデータフレームにする
df_term=DataReader.get_data_yahoo(cur,start=symd_sd,end=symd_ed)

#データフレームをstreamlitで表示する
st.dataframe(df_term,width=1500,height=500)

#close列をグラフにする
df_termG=pd.DataFrame({cur:df_term['Close']})
fig = plt.figure(figsize=(12,9))
ax = plt.axes()
plt.plot(df_termG)
st.pyplot(fig)

#st.pyplot(plt)   ←この形は使えなくなった


