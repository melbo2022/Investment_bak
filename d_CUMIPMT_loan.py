#投資シミュレーション
#借入額における指定期間の借入利息合計を算出する-------------------------------------------------------------
def CUMIPMT_loan():

    #モジュールをインポートする
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

    #---パラメータボックスを作る------------------------------------------------------------------
    #パラメータボックスを作る
    # rate (必須): 利率
    # nper (必須): 複利計算期間数 (支払回数)
    # pv (必須): 現在価値 (返済の場合: 借入金額, 貯蓄の場合: 積立済金額)
    # start_period: 計算開始の支払回数
    # end_period: 計算終了の支払回数
    # when: 支払期日、いつ支払いが行われるか。 (end/0: 各期の期末, start/1: 各期の機種)

    #CUMIPMT(rate,nper,pv,start_period,end_period,type)


    #--tkinterによるテキストボックス作成----------------------------------------------------------------
    # メインウィンドウを作成
    app_cumipmt_l = tk.Toplevel()
    # ウィンドウのサイズを設定
    app_cumipmt_l.geometry('450x350+500+100')
    # 画面タイトル
    app_cumipmt_l.title('指定期間返済利息合計計算')

    #--テキストボックス-------------------------------------------------------------------------
    # ラベル
    label1 = tk.Label(app_cumipmt_l,text='利率（年利）')
    label1.place(x=30, y=20)

    label2 = tk.Label(app_cumipmt_l,text='返済期間（年）')
    label2.place(x=30, y=70)

    label3 = tk.Label(app_cumipmt_l,text='借入額')
    label3.place(x=30, y=120)

    label4 = tk.Label(app_cumipmt_l,text='計算開始_回目(月)')
    label4.place(x=30, y=170)

    label5 = tk.Label(app_cumipmt_l,text='計算終了_回目(月)')
    label5.place(x=30, y=220)

    label6 = tk.Label(app_cumipmt_l,text='支払期日(0:期末, 1:期首)')
    label6.place(x=30, y=270)

    # テキストボックス
    textBox1 = tk.Entry(app_cumipmt_l)
    textBox1.insert(0,"0.015")
    textBox1.place(x=250, y=20)

    textBox2 = tk.Entry(app_cumipmt_l)
    textBox2.insert(1,"20")
    textBox2.place(x=250, y=70)

    textBox3 = tk.Entry(app_cumipmt_l)
    textBox3.insert(2,"30000000")
    textBox3.place(x=250, y=120)

    textBox4 = tk.Entry(app_cumipmt_l)
    textBox4.insert(3,"1")
    textBox4.place(x=250, y=170)

    textBox5 = tk.Entry(app_cumipmt_l)
    textBox5.insert(4,"120")
    textBox5.place(x=250, y=220)

    textBox6 = tk.Entry(app_cumipmt_l)
    textBox6.insert(5,"1")
    textBox6.place(x=250, y=270)



    #--要件を確認するメッセージを表示する--ボタン（要件確認）---------------------------------------------------------------------
    # 画面作成
    def exp():

        #テキストの値を取得する
        rate=textBox1.get()
        nper=textBox2.get()
        pv=textBox3.get()
        speriod=textBox4.get()
        eperiod=textBox5.get()
        when=textBox6.get()

        elem_list=[rate,nper,pv,speriod,eperiod,when]
        a=''
        if a in elem_list:
            tk.messagebox.showerror('showerror','空白の要素があります')



        rate=float(rate)*100

        #数値を3桁区切りにする
        pv=int(pv)
        pv="{:,}".format(pv)


        exp="{}円を金利{}%で借入をした。\n{}年で完済する場合の指定期間の返済利息合計額を求める".format(pv,rate,nper)
        tk.messagebox.showinfo(title="指定期間返済利息合計額", message=exp)

    #-----------------------------------------------------------------------------------------------------------
    def img():
        #別ファイルのモジュールをインポートする場合----------------------------------------------------------------
        # import sys
        # from pathlib import Path
        #
        # p_cwd = Path('.')
        # p_hoge_dir = p_cwd.joinpath('img')
        # sys.path.append(str(p_hoge_dir))
        #from img import d_img
        #----------------------------------------------------------------------------------------------
        import d_img
        i='CUMIPMT_loan.png'
        d_img.financial_img(i)


    #--グラフを作成する--ボタン（グラフ）-----------------------------------------------------------------------------
    def fv_gr():
        # テキストボックスの値を取得
        print(textBox1.get())
        print(textBox2.get())
        print(textBox3.get())
        print(textBox4.get())
        print(textBox5.get())
        print(textBox6.get())

        rate=textBox1.get()
        nper=textBox2.get()
        pv=textBox3.get()
        speriod=textBox4.get()
        eperiod=textBox5.get()
        when=textBox6.get()

        #要素が空白の場合にメッセージを出す-------------------------------------------------------
        elem_list=[rate,nper,pv,speriod,eperiod,when]
        a=''
        if a in elem_list:
            tk.messagebox.showerror('showerror','空白の要素があります')
        #----------------------------------------------------------------------------------

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
        ipmt=int(pmt)

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


        #--月単位グラフを作成する準備-------------------------------------------------------------------
        #x軸リストとy軸リストでデータフレームを作成する
        df = pd.DataFrame(list(zip(x_list,y_list)), columns = ['経過月数','借入金残高'])
        print(df)


        #--年度単位グラフを作成する準備------------------------------------------------------------------------------------------
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
        #-----------------------------------------------------------------------------------------------
        #y軸の値のうち各年度の最終月の値を取得する(y_listの12番目の値から12飛ばしで値を取得する）
        y_year_list=y_list[11::12]
        print(y_year_list)

        #年度リストをデータフレームにする
        #--x軸リストとy軸リストでデータフレームを作成する----------------------------------------------------------
        df_year = pd.DataFrame(list(zip(x_year_list,y_year_list)), columns = ['経過年数','借入金残高'])
        print(df_year)

        #--Expressでグラフを描画する-----------------------------------------------------------------------------------------------------------

        fig = px.bar(df,x='経過月数',y='借入金残高')
        fig_year = px.bar(df_year,x='経過年数',y='借入金残高')

        #fig.show()
        fig_year.show()


    #--答えをメッセージボックスで表示する--ボタン（OK)------------------------------------------------------------------------------------
    def val():
        # テキストボックスの値を取得
        print(textBox1.get())
        print(textBox2.get())
        print(textBox3.get())
        print(textBox4.get())
        print(textBox5.get())
        print(textBox6.get())

        rate=textBox1.get()
        nper=textBox2.get()
        pv=textBox3.get()
        speriod=textBox4.get()
        eperiod=textBox5.get()
        when=textBox6.get()

        #要素が空白の場合にメッセージを出す-------------------------------------------------------
        elem_list=[rate,nper,pv,speriod,eperiod,when]
        a=''
        if a in elem_list:
            tk.messagebox.showerror('showerror','空白の要素があります')
        #--計算をする--------------------------------------------------------------------------------
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
        # pmt=npf.pmt(rate/12,nper*12,pv,fv,when)
        # pmt=int(pmt)*-1
        #数値を3桁区切りにする
        # pmt="{:,}".format(pmt)


        #小数以下を切り捨てる
        cumipmt=cumipmt*-1
        #数値を3桁区切りにする
        cumipmt="{:,}".format(cumipmt)
        print('指定期間支払利息合計額 CUMIPMT:',cumipmt)

        #回答をメッセージボックスで表示する
        res="{}回目から{}回目の支払利息合計額は{}円です".format(speriod,eperiod,cumipmt)
        tk.messagebox.showinfo(title="指定期間支払利息合計額", message=res)
        #msg.showinfo("必要積立月額",cumipmt)

    #--ボタンの作成と配置---------------------------------------------------------------------
    #-------------------------------------------------------------------------------------
    # クリック時にExP()関数を呼ぶ
    button3 = tk.Button(app_cumipmt_l,text = '要件確認',command =exp).place(x=30, y=310)
    #---------------------------------------------------------------------------------------
    # イメージ図の作成と配置
    # クリック時にimg()関数を呼ぶ
    #button4 = tk.Button(app_cumipmt_l,text = 'イメージ図',command =img).place(x=100, y=310)
    #-----------------------------------------------------------------------------------------
    # グラフボタンの作成と配置
    # クリック時にFV_gr()関数を呼ぶ
    button2 = tk.Button(app_cumipmt_l,text = 'グラフ',width=5,command =fv_gr).place(x=320, y=310)
    #---------------------------------------------------------------------------------------
    # OKボタンの作成と配置
    # クリック時にval()関数を呼ぶ
    button1 = tk.Button(app_cumipmt_l,text = 'OK',width=5,command = val).place(x=390, y=310)
    #---------------------------------------------------------------------------------------

    #app_cumipmt_l.mainloop()
#--------------------------------------------------------------------------------------------------
# このプログラムは、d_org.pyにおいて選択された場合に動作するが、次のコードがないとimportした瞬間にFV_deposit()が動作してしまう。
if __name__ == "__main__":
    CUMIPMT_loan()

