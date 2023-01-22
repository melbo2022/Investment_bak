#ValueError: could not convert string to float:   -m streamlit.cli run
#github change
#git bushから実行

def org():
    import streamlit as st
    import d_FV_depo
    import d_NPER_depo
    import d_PMT_depo
    import d_RATE_depo
    import d_PV_pen
    import d_NPER_pen
    import d_PMT_pen
    import d_RATE_pen
    import d_PV_loan
    import d_NPER_loan
    import d_PMT_loan
    import d_RATE_loan
    import d_PPMT_loan
    import d_IPMT_loan
    import d_CUMPRINC_loan
    import d_CUMIPMT_loan




    option_select1=st.selectbox(
        '積立運用',
        (' ','貯蓄額計算(FV)','積立期間計算(NPER)','積立月額計算(PMT)','運用利率計算(RATE)'))

    option_select2=st.selectbox(
        '年金',
        (' ','年金原資計算(PV)','取崩期間計算(NPER)','取崩月額計算(PMT)','年金原資運用利率計算(RATE)'))

    option_select3=st.selectbox(
        '借入',
        (' ','借入限度額計算(PV)','返済年数計算(NPER)','返済月額計算(PMT)','借入利率計算(RATE)','返済元金計算(PPMT)','返済利息計算(IPMT)','返済利息累計計算(CUMIPMT)','返済元金累計計算(CUMPRINC)'))



#----------------------------------------------------------------------------------------------------------
    if option_select1 == '貯蓄額計算(FV)':
        st.write('貯蓄額計算(FV)')
        d_FV_depo.FV_deposit()

    elif option_select1 == '積立期間計算(NPER)':
        st.write('積立期間計算(NPER)')
        d_NPER_depo.NPER_deposit()

    elif option_select1 == '積立月額計算(PMT)':
        st.write('積立月額計算(PMT)')
        d_PMT_depo.PMT_deposit()

    elif option_select1 == '運用利率計算(RATE)':
        st.write('運用利率計算(RATE)')
        d_RATE_depo.RATE_deposit()

    #---------------------------------------------------------------------------------------------
    elif option_select2 == '年金原資計算(PV)':
        st.write('年金原資計算(PV)')
        d_PV_pen.PV_pension()

    elif option_select2 == '取崩期間計算(NPER)':
        st.write('年金取崩期間計算(NPER)')
        d_NPER_pen.NPER_pension()

    elif option_select2 == '取崩月額計算(PMT)':
        st.write('年金取崩額計算(PMT)')
        d_PMT_pen.PMT_pension()

    elif option_select2 == '年金原資運用利率計算(RATE)':
        st.write('年金原資必要運用利回り計算(RATE)')
        d_RATE_pen.RATE_pension()
    #-------------------------------------------------------------------------------------------
    elif option_select3 == '借入限度額計算(PV)':
        st.write('必要年金原資額計算')
        d_PV_loan.PV_loan()

    elif option_select3 == '返済年数計算(NPER)':
        st.write('借入返済回数計算')
        d_NPER_loan.NPER_loan()

    elif option_select3 == '返済月額計算(PMT)':
        st.write('借入返済額計算')
        d_PMT_loan.PMT_loan()

    elif option_select3 == '借入利率計算(RATE)':
        st.write('借入調達金利')
        d_RATE_loan.RATE_loan()

    elif option_select3 == '返済元金計算(PPMT)':
        st.write('返済元金')
        d_PPMT_loan.PPMT_loan()

    elif option_select3 == '返済利息計算(IPMT)':
        st.write('返済利息')
        d_IPMT_loan.IPMT_loan()

    if option_select3 == '返済元金累計計算(CUMPRINC)':
        st.write('返済元金合計')
        d_CUMPRINC_loan.CUMPRINC_loan()

    if option_select3 == '返済利息累計計算(CUMIPMT)':
        st.write('返済利息合計')
        d_CUMIPMT_loan.CUMIPMT_loan()

#-------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    org()