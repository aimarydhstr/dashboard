import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import logging

st.set_option('deprecation.showPyplotGlobalUse', False)

# Membaca file CSV
data = pd.read_csv("all_data.csv")

# Judul dashboard
st.title('Dashboard Penggunaan Sepeda')

# Tampilkan data mentah jika diinginkan
if st.checkbox('Tampilkan data mentah'):
    st.write(data)

# Tampilkan plot jumlah pengguna terdaftar berdasarkan waktu pada hari kerja dan hari libur
st.subheader('Pola Penggunaan Sepeda Berdasarkan Waktu')
fig, ax = plt.subplots(figsize=(10, 5))
data[data['workingday_y'] == 1].groupby('hr')['registered_y'].mean().plot(label='Hari Kerja')
data[data['workingday_y'] == 0].groupby('hr')['registered_y'].mean().plot(label='Hari Libur')
plt.title('Pola Penggunaan Sepeda Berdasarkan Waktu\n Hari Kerja vs Hari Libur')
plt.xlabel('Jam')
plt.ylabel('Jumlah Pengguna Terdaftar')
plt.legend()
st.pyplot(fig)

# Tampilkan scatter plot hubungan suhu dengan jumlah pengguna sepeda pada hari kerja dan hari libur
st.subheader('Hubungan Suhu dengan Jumlah Pengguna Sepeda')
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(data[data['workingday_x'] == 1]['temp_x'], data[data['workingday_x'] == 1]['cnt_x'], color='blue', label='Hari Kerja')
ax.scatter(data[data['workingday_x'] == 0]['temp_x'], data[data['workingday_x'] == 0]['cnt_x'], color='orange', label='Hari Libur')
plt.title('Hubungan Suhu dengan Jumlah Pengguna Sepeda\n Hari Kerja vs Hari Libur')
plt.xlabel('Suhu')
plt.ylabel('Jumlah Pengguna Sepeda')
plt.legend()
st.pyplot(fig)
