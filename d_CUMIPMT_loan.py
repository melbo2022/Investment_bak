#ValueError: could not convert string to float:   -m streamlit.cli run
#投資シミュレーション

#---モジュールをインポートする-----------------------------------------------------------------------------------------------
def CUMIPMT_loan():
    import streamlit as st
    import numpy as np
    import numpy_financial as npf
    import pandas as pd

    import time
    # import matplotlib.pyplot as plt
    #日本語フォントをインポートする(matplotlib)
    # import matplotlib as mpl
    # mpl.rc('font', family="MS Gothic")

    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    from PIL import Image

    import D_ORIGIN

    """
     # 借入額における指定期間の借入利息合計を算出する
     """
    #-------------------------------------------------------------------------------------------------------------------
    #イメージ画像チェックボックス
    option_check=st.checkbox('イメージ画像:　例（デフォルト値)')

    #--イメージ画像を表示する-----------------------------------------------------------------------------------------------
    #チェックボックス処理
    if option_check==True:
        image=Image.open("./CUMIPMT_loan.png")
        st.write("3千万円を金利1.5%で借入をした。\n20年で完済する場合の指定期間の返済利息合計額を求める")
        st.image(image,caption='CUMIPMT（指定期間借入返済利息合計額計算）',use_column_width=True)

        #戻るボタン配置(Trueのとき呼び出し元へ戻る）
        return_btn=st.button('戻る')
        if return_btn:

            D_ORIGIN.org()
    #------------------------------------------------------------------------------------------------------------------
    #将来価値 (Future Value)
    rate=st.sidebar.text_input('利率 <年利回り1.5%の場合：0.015>','0.015')
    nper=st.sidebar.text_input('返済期間（年数）','20')
    pv=st.sidebar.text_input('借入額','30000000')
    speriod=st.sidebar.text_input('計算開始_回目(月)','1')
    eperiod=st.sidebar.text_input('計算終了_回目(月)','120')
    when=st.sidebar.text_input('支払期日 (0: 各期の期末, 1: 各期の期首)','1')

    #---指定した回数における積立残高を表示する------nper=st.sidebar.text_input('指定時回数')
    #nper_p=st.sidebar.text_input('・回目の残高を指定')
    #nper_p=int(nper_p)

    #グラフを年度単位か月単位かを選択する--------------------------------------------------------------------------------------
    option_radio=st.sidebar.radio('グラフ表示',
                                  ('','月単位','年単位'))

    #OK,キャンセルボタンを作成
    submit_btn=st.sidebar.button('OK')
    cancel_btn=st.sidebar.button('キャンセル')

    if submit_btn:
        rate=float(rate)
        nper=int(nper)
        pv=int(pv)
        speriod=int(speriod)
        eperiod=int(eperiod)
        when=int(when)


        rate=float(rate)
        nper=int(nper)
        pv=int(pv)
        speriod=int(speriod)
        eperiod=int(eperiod)
        when=int(when)

        #cumipmtがnumpyで使用できないためipmtより計算する
        cumipmt=0
        for r in range(speriod,eperiod+1):
            ipmt=npf.ipmt(rate/12,r,nper*12,pv,0,when)
            cumipmt=cumipmt+int(ipmt)


        #cumipmt=npf.cumipmt(rate/12,nper*12,pv,speriod,eperiod,when)
        #cumipmt=int(cumipmt)

        pmt=npf.pmt(rate/12,nper*12,pv,0,when)
        pmt=int(pmt)

        #数値を3桁区切りにする
        # pmt="{:,}".format(pmt)
        # print('月額取崩し可能額 PMT:',pmt)

        st.write('返済利息合計額;',cumipmt)

        #--指定したポイントにおける将来価値を算出する---------------------------------------------------------------------------
        # fv_point=npf.fv(rate/12,nper_p*12, pmt, pv,when)
        # print('指定時積立残高 FV:',fv_point)
        # st.write(nper_p,'回目の積立金残高:',fv_point)


        #--年度単位グラフを作成する準備--------------------------------------------------------------------------------------

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
        print(df_year)
        #--Expressでグラフを描画する---------------------------------------------------------------------------------------

        fig = px.bar(df,x='経過月数',y='借入金残高')
        fig_year = px.bar(df_year,x='経過年数',y='借入金残高')

        if option_radio !='':
            radio=option_radio

            if radio=='月単位':
                fig.show()
            elif radio=='年単位':
                fig_year.show()


#このプログラムは、d_org.pyにおいて選択された場合に動作するが、次のコードがないとimportした瞬間にFV_deposit()が動作してしまう。
if __name__ == "__main__":
    CUMIPMT_loan()