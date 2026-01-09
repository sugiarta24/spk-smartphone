import streamlit as st
import pandas as pd
from ahp import ahp_weights
from topsis import topsis

st.title("SPK Pemilihan Smartphone Terbaik")

df = pd.read_csv("dataset_smartphone.csv")
st.dataframe(df)

st.subheader("Bobot Kriteria (AHP)")
pairwise = [
    [1, 3, 3, 5, 5, 7],
    [1/3, 1, 2, 3, 3, 5],
    [1/3, 1/2, 1, 3, 3, 5],
    [1/5, 1/3, 1/3, 1, 2, 3],
    [1/5, 1/3, 1/3, 1/2, 1, 3],
    [1/7, 1/5, 1/5, 1/3, 1/3, 1],
]

weights = ahp_weights(pairwise)
st.write("Bobot:", weights)

data = df.iloc[:,1:].values
impacts = ['cost','benefit','benefit','benefit','benefit','benefit']

score = topsis(data, weights, impacts)
df['Skor'] = score
df = df.sort_values('Skor', ascending=False)

st.subheader("Hasil Ranking")
st.dataframe(df)
