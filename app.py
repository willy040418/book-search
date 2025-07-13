import streamlit as st
import json
import pandas as pd

# Judul aplikasi
st.title('Books to Scrape - Search App')

# Load data dari file JSON (pastikan file books.json ada di folder data/)
try:
    with open('data/books.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
except FileNotFoundError:
    st.error("File data/books.json tidak ditemukan. Pastikan sudah menjalankan Scrapy crawl.")
    df = pd.DataFrame()  # Dataframe kosong jika error

# Input pencarian
search_term = st.text_input('Cari Buku berdasarkan Judul:', '')

# Filter data berdasarkan pencarian (case-insensitive)
if search_term:
    filtered_df = df[df['title'].str.contains(search_term, case=False, na=False)]
    st.write(f"Menampilkan {len(filtered_df)} hasil untuk '{search_term}':")
    st.dataframe(filtered_df)
else:
    st.write("Semua Buku:")
    st.dataframe(df)

# Tambahan: Tampilkan statistik sederhana
if not df.empty:
    st.subheader('Statistik Data')
    st.write(f"Jumlah Buku Total: {len(df)}")
    st.write(f"Rata-rata Harga: {df['price'].str.replace('£', '').astype(float).mean():.2f} £")