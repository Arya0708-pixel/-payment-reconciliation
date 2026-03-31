import streamlit as st
from data_generator import generate_data
from reconciliation import hybrid_reconcile

st.title("Hybrid Payment Reconciliation Demo")

platform, bank = generate_data()

st.subheader("Platform Transactions")
st.dataframe(platform)

st.subheader("Bank Settlements")
st.dataframe(bank)

report = hybrid_reconcile(platform, bank)

st.subheader("Reconciliation Report")
st.json(report)