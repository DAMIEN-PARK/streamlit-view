import streamlit as st

view = [100,150,30]
st.write('# Youtube view')    ## 마크다운 같은 포맷이 들어 갈 수 있음. 
st.write('## raw')
view
st.write('## Bar chart')
st.bar_chart(view)

import pandas as pd     ## pd 별명
sview = pd.Series(view)     ## 판다스 데이터 타입 시리즈로 컨버팅. sview라고 이름
sview       ## sview가 최적화 된 데이터를 화면에 표시
