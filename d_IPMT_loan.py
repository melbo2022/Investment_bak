#ValueError: could not convert string to float:   -m streamlit.cli run
#投資シミュレーション

#---モジュールをインポートする-----------------------------------------------------------------------------------------------
def IPMT_loan():
    import streamlit as st
    import numpy as np
    import numpy_financial as npf
    import pandas as pd

    import time
    # import matplotlib.pyplot as plt
    #日本語フォントをインポートする(matplotlib)
    # import matplotlib as mpl
    # mpl.rc('font', family="MS Gothic")

    # import plotly.graph_objects as go
    # import plotly.express as px
    # from plotly.subplots import make_subplots
    from PIL import Image

    import D_ORIGIN

    """
     # 借入額における指定回の返済利息を算出する
     """
    #------------------------------------------------------------------------------------------------------------------
    #イメージ画像チェックボックス
    option_check=st.checkbox('イメージ画像:　例（デフォルト値)')

    #--イメージ画像を表示する-----------------------------------------------------------------------------------------------
    #チェックボックス処理
    if option_check==True:
        image=Image.open("./IPMT_loan.png")
        st.write("3千万円を金利1.5%で借入をした。\n20年で完済する場合の指定回の返済利息額を求める")
        st.image(image,caption='IPMT（指定回借入返済利息額計算）',use_column_width=True)

        #戻るボタン配置(Trueのとき呼び出し元へ戻る）
        # return_btn=st.button('戻る')
        # if return_btn:
        #
        #     D_ORIGIN.org()
    #------------------------------------------------------------------------------------------------------------------

    #with st.form(key='invest_form'):
    #将来価値 (Future Value)
    rate=st.sidebar.text_input('利率 <年利回り1.5%の場合：0.015>','0.015')
    per=st.sidebar.text_input('指定返済期（月回）','120')
    nper=st.sidebar.text_input('返済期間（年数）','20')
    pv=st.sidebar.text_input('借入額','30000000')
    fv=st.sidebar.text_input('将来借入残金','0')
    when=st.sidebar.text_input('支払期日 (0: 各期の期末, 1: 各期の期首)','1')



    #---指定した回数における積立残高を表示する---nper=st.sidebar.text_input('指定時回数')---------------------------------------
    #nper_p=st.sidebar.text_input('・回目の残高を指定')
    #nper_p=int(nper_p)


    #グラフを年度単位か月単位かを選択する-------------------------------------------------------------------------------------
    option_radio=st.sidebar.radio('グラフ表示',
                                  ('','月単位','年単位'))

    #OK,キャンセルボタンを作成
    submit_btn=st.sidebar.button('OK')
    #cancel_btn=st.sidebar.button('キャンセル')


    if submit_btn:
        #将来価値を算出する------------------------------------------------------------------------------------------------
        rate=float(rate)
        per=int(per)
        nper=int(nper)
        pv=int(pv)
        fv=int(fv)
        when=int(when)

        ipmt=npf.ipmt(rate/12,per,nper*12,pv,fv,when)
        ipmt=int(ipmt)

        pmt=npf.pmt(rate/12,nper*12,pv,fv,when)
        pmt=int(pmt)


        #数値を3桁区切りにする
        # pmt="{:,}".format(pmt)
        # print('月額取崩し可能額 PMT:',pmt)


        #st.write('ipmt(rate/12,per,nper*12,pv,fv,when)')
        ipmt = "{:,}".format(ipmt)
        st.write('返済利息額;',ipmt)

        #--指定したポイントにおける将来価値を算出する---------------------------------------------------------------------------
        # fv_point=npf.fv(rate/12,nper_p*12, pmt, pv,when)
        # print('指定時積立残高 FV:',fv_point)
        #
        # st.write(nper_p,'回目の積立金残高:',fv_point)


        #--年度単位グラフを作成する準備---------------------------------------------------------------------------------------

        #X軸の値を作成する
        x_list=[]
        for i in range(1,nper*12+1):
            x_list.append(i)
        print(x_list)

        #Y軸の値を作成する
        y_list=[]
        for k in range(1,nper*12+1):
            val=npf.fv(rate/12,k,pmt,pv,when)
            y_list.append(val)
        print(y_list)



        #--月単位グラフを作成する準備---------------------------------------------------------------------------------------
        #x軸リストとy軸リストでデータフレームを作成する
        df = pd.DataFrame(list(zip(x_list,y_list)), columns = ['経過月数','借入金残高'])
        df=df.set_index('経過月数')
        print(df)


        #--月単位グラフを作成する準備----------------------------------------------------------------------------------------
        #x軸リストとy軸リストでデータフレームを作成する
        df = pd.DataFrame(list(zip(x_list,y_list)), columns = ['経過月数','借入金残高'])
        print(df)


        #--年度単位グラフを作成する準備--------------------------------------------------------------------------------------
        #X軸の値を年度ごとに変更

        x_year_list=[]
        for i in x_list:
            val=i%12
            if val==0:
                n=i//12
                x_year_list.append(n)
            else:
                continue

        print(x_year_list)
        #--------------------------------------------------------------------------------------------------------------
        #y軸の値のうち各年度の最終月の値を取得する(y_listの12番目の値から12飛ばしで値を取得する）
        y_year_list=y_list[11::12]
        print(y_year_list)

        #年度リストをデータフレームにする
        #--x軸リストとy軸リストでデータフレームを作成する-----------------------------------------------------------------------
        df_year = pd.DataFrame(list(zip(x_year_list,y_year_list)), columns = ['経過年数','借入金残高'])
        df_year=df_year.set_index('経過年数')
        print(df_year)



        #--- streamlitでグラフを描画する--------------------------------------------------------------------------------------

        if option_radio !='':
            radio=option_radio

            if radio=='月単位':
                st.bar_chart(df)

            elif radio=='年単位':
                st.bar_chart(df_year)



#このプログラムは、d_org.pyにおいて選択された場合に動作するが、次のコードがないとimportした瞬間にFV_deposit()が動作してしまう。
if __name__ == "__main__":
    IPMT_loan()