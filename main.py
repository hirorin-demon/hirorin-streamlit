import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

####@#データフレーム
st.title('streamlit 調査結果')
df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[6,7,8,100]
})

st.dataframe(df,1000,1000)

#####@マークダウン

"""
# 大
## 中
### 小
```python
import streamlit as st
import numpy as np
import pandas as pd
st.title('streamlit 調査結果')
df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[6,7,8,100]
})
#st.dataframe(df.style.highlight_min(axis=1),width=600,height=600)
#st.dataframe(df.style.highlight_min(axis=0),width=200,height=200)
st.dataframe(df,1000,1000)
```
"""

#####@チャート
df1 = pd.DataFrame(
    np.random.rand(20,6),
    columns=['a','b','c','d','e','f']
)
st.dataframe(df1)
st.line_chart(df1)
st.area_chart(df1)

#####@ map
df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)
st.map(df2)

#####@ image
st.write('STREAMLIT イメージ表示')
img = Image.open('sample.png')
st.image(img,caption='名簿画像',use_column_width=True)

#####@ 自由にコーディング
st.write('【自由に書きました】')
df99  = pd.read_csv("sample2.csv",encoding="cp932")
st.dataframe(df99)