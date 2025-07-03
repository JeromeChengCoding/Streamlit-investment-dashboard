import streamlit as st
import pandas as pd
import altair as alt
from streamlit_gsheets import GSheetsConnection

# 建立連線物件，連結至 Google Sheet
conn = st.connection("gsheets", type=GSheetsConnection)

# 讀取資料表
df = conn.read()

# 將日期欄位轉換為日期格式（假設欄位名為 '日期'）
df.columns = ["日期", "淨值"]
df['日期'] = pd.to_datetime(df['日期'])
df = df.dropna(subset=['日期'])

# 建立應用程式佈局
st.title("基金介紹頁面")

# 分成兩個欄位: 左側介紹文字、右側淨值圖表
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("基金介紹")
    st.write("本基金採用多元化資產配置策略，聚焦於穩健成長並兼顧風險控管。")
    st.write("透過對各產業進行深入研究與選股，力求在各種市場環境中維持長期穩定回報。")
    st.subheader("成分股與資產配置")
    st.write("以下範例供參考：")
    st.markdown("- A公司（30%）")
    st.markdown("- B公司（25%）")
    st.markdown("- C公司（20%）")
    st.markdown("- 其他資產與現金等（25%）")

with col2:
    st.subheader("歷史淨值走勢")
    # 以日期作為 x 軸，淨值作為 y 軸繪製折線圖
    chart = (
        alt.Chart(df)
        .mark_line(point=False)
        .encode(
            x="日期:T",
            y="淨值:Q",
            tooltip=["日期", "淨值"]
        )
        .properties(width="container", height=300)
        .interactive()
    )
    st.altair_chart(chart, use_container_width=True)

