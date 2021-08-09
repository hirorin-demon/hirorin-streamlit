from datetime import timedelta
from posixpath import expanduser
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit.proto.Components_pb2 import ComponentInstance
from streamlit.proto.RootContainer_pb2 import SIDEBAR
import time

st.write('プログレスバーを表示します')
'start'
latest_iteration = st.empty()
bar=st.progress(0)
for i  in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'入力を直ぐにやめてください。'




####@#データフレーム
# st.title('streamlit 調査結果')

# ccc=[]

#セレクトボックス
# option = st.selectbox(
#     '好きな数字を選んでね！',
#     list(range(1,10))
# )
# 'あなたの好きな数字は',option,'ですね'

# ###@ テキストボックス
# coment = st.sidebar.text_input('試合を終えて、今の気持ちを教えてください。')
# '感想：',coment

# ###@ スライダー
# level1 = st.sidebar.slider('あなたの今の調子は？',0,60,30)
# 'あなたの調子は',level1,'ですね。'

####@ カラム
# leftC,rightC = st.beta_columns(2)
# but_left=leftC.button('右カラムに文字を表示')
# if but_left:
#     rightC.write("左ボタンがクリックされました")

####@ エキスパンダー
exp = st.beta_expander('問い合わせ1')
exp.write('問合せへの回答1')
exp = st.beta_expander('問い合わせ2')
exp.write('問合せへの回答2')
exp = st.beta_expander('問い合わせ3')
exp.write('問合せへの回答3')
exp = st.beta_expander('問い合わせ4')
exp.write('問合せへの回答4')
exp = st.beta_expander('問い合わせ5')
exp.write('問合せへの回答5')
exp = st.beta_expander('問い合わせ6')
exp.write('問合せへの回答6')
exp = st.beta_expander('問い合わせ7')
exp.write('問合せへの回答7')