import pandas as pd
import openpyxl as xl
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Bao cao doanh thu", page_icon=":bar_chart:")


def get_data_from_excel():
    df = pd.read_excel(io = r"F:\Python\Giao diện tkinterr\ds2021.xlsx", 
    engine="openpyxl", 
    sheet_name="sale",
    skiprows=3,
    usecols="B:R",
    nrows=1010)
    return df

df = get_data_from_excel()
#print(df)
st.write("viet linh tinh cai gì vao day")
st.sidebar.header("loc du lieu tai day")

city = st.sidebar.multiselect("chon thanh pho",
options=df["Thanh_pho"].unique(), default=df["Thanh_pho"].unique())

GT = st.sidebar.multiselect("chon Gioi tinh",
options=df["Gioi_tinh"].unique(), default=df["Gioi_tinh"].unique())

df_selection = df.query("Thanh_pho == @city & Gioi_tinh == @GT")

st.title = ("Doanh so ban hang")

left_column, middle_column, right_column = st.columns(3)


total_sale = int(df_selection["Tong"].sum())
with left_column:
    st.subheader("Tong doanh so: ")
    st.subheader(f"Ty VND {total_sale}")