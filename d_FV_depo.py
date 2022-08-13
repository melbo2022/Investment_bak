#ValueError: could not convert string to float:   -m streamlit.cli run
#投資シミュレーション

#---モジュールをインポートする----------------------------------------------------------------------------------------------
def FV_deposit():
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
     # 積立額の将来価値を算出する
     """
    #------------------------------------------------------------------------------------------------------------------
    #イメージ画像チェックボックス
    option_check=st.checkbox('イメージ画像:　例（デフォルト値)')

    #--イメージ画像を表示する----------------------------------------------------------------------------------------------
    #チェックボックス処理
    if option_check==True:
        image=Image.open("./FV_depo.png")
        st.write("毎月2万円を利回り3%で30年間積立てた場合いくらになるか？")
        st.image(image,caption='FV（将来貯蓄額計算）',use_column_width=True)

        #戻るボタン配置(Trueのとき呼び出し元へ戻る）
        return_btn=st.button('戻る')
        if return_btn:

            D_ORIGIN.org()
#----------------------------------------------------------------------------------------------------------------------
    #将来価値 (Future Value)
    rate=st.sidebar.text_input('利率 <年利回り3%の場合：0.03>','0.03')
    nper=st.sidebar.text_input('積立期間（年数）','30')
    pmt=st.sidebar.text_input('毎月の支払額 <マイナス入力>','-20000')
    pv=st.sidebar.text_input('現在残高','0')
    when=st.sidebar.text_input('支払期日 (0: 各期の期末, 1: 各期の期首)','1')

    #---指定した回数における積立残高を表示する---nper=st.sidebar.text_input('指定時回数')---------------------------------------
    #nper_p=st.sidebar.text_input('・回目の残高を指定')
    #nper_p=int(nper_p)


    #グラフを年度単位か月単位かを選択する--------------------------------------------------------------------------------------
    option_radio=st.sidebar.radio('グラフ表示',
                                  ('','月単位','年単位'))

    #OK,キャンセルボタンを作成
    submit_btn=st.sidebar.button('OK')
    cancel_btn=st.sidebar.button('キャンセル')


    if submit_btn:
        #将来価値を算出する------------------------------------------------------------------------------------------------
        rate=float(rate)
        nper=int(nper)
        pmt=int(pmt)
        pv=int(pv)
        when=int(when)

        fv=npf.fv(rate/12,nper*12, pmt, pv,when)
        print('将来価値 FV:',fv)
        st.write('fv(rate/12,nper*12, pmt, pv,when)')
        st.write('最終積立金残高;',fv)

        #--指定したポイントにおける将来価値を算出する---------------------------------------------------------------------------
        # fv_point=npf.fv(rate/12,nper_p*12, pmt, pv,when)
        # print('指定時積立残高 FV:',fv_point)
        #
        # st.write(nper_p,'回目の積立金残高:',fv_point)


        #--月単位グラフを作成する準備----------------------------------------------------------------------------------------
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
        df = pd.DataFrame(list(zip(x_list,y_list)), columns = ['経過月数','積立合計額'])
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
        df_year = pd.DataFrame(list(zip(x_year_list,y_year_list)), columns = ['経過年数','積立合計額'])
        print(df_year)

        #--Expressでグラフを描画する---------------------------------------------------------------------------------------

        fig = px.bar(df,x='経過月数',y='積立合計額')
        fig_year = px.bar(df_year,x='経過年数',y='積立合計額')

        if option_radio !='':
            radio=option_radio

            if radio=='月単位':
                fig.show()
            elif radio=='年単位':
                fig_year.show()



#このプログラムは、d_org.pyにおいて選択された場合に動作するが、次のコードがないとimportした瞬間にFV_deposit()が動作してしまう。
if __name__ == "__main__":
    FV_deposit()



