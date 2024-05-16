import config
import streamlit as st
from soxo188 import parse_soxo188_api

st.title('Kết quả xổ số mới nhất')
st.header("Vui lòng chọn Tỉnh thành?")
option = st.selectbox("", (config.PROVINCES.keys()))
st.markdown(f':red[Kết quả xổ số: {option}]')
results = parse_soxo188_api(option)
list(map(lambda result: st.write(result), results)) 