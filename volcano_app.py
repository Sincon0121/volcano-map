import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 제목
st.title("🌋 전 세계 화산 지도")

# CSV 데이터 불러오기
df = pd.read_csv("real_volcano.csv")

# 지도 만들기
m = folium.Map(location=[0, 0], zoom_start=2)

# 마커 추가
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=4,
        popup=row["Volcano Name"],
        color="red",
        fill=True
    ).add_to(m)

# 지도 보여주기
st_data = st_folium(m, width=700, height=500)
