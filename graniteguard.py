import streamlit as st
import requests
import time
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()

# ------------------ LOGO ------------------
logo = Image.open("graniteguard.png")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo, width=150)

# -------------- CONFIGURATION -------------
API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
MODEL_ID = os.getenv("MODEL_ID")

# -------------------- GET TOKEN --------------------
@st.cache_data(ttl=3000)
def get_access_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={API_KEY}"
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

# -------------------- RISK CHECK --------------------
def analyze_risks(text):
    token = get_access_token()
    url = f"https://{REGION}.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model_id": MODEL_ID,
        "input": f"""
You are an expert compliance and DEI auditor. Read the following business text and identify:
1. Biased language (gender, age, race, etc.)
2. Aggressive or unprofessional tone
3. Legal or regulatory risk

Return a clear report with:
- Summary of risks
- Line-by-line analysis with issue labels
- Suggestions to fix the problems

Text to analyze:
\"\"\"{text}\"\"\"
""",
        "parameters": {"decoding_method": "greedy", "max_new_tokens": 300},
        "project_id": PROJECT_ID
    }
    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    return result.get("results", [{}])[0].get("generated_text", "No response.")

# -------------------- REWRITE --------------------
def rewrite_text(text):
    token = get_access_token()
    url = f"https://{REGION}.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-01"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model_id": MODEL_ID,
        "input": f"""
Rewrite the following text to:
- Remove bias
- Improve tone
- Ensure inclusivity and legal compliance

Keep the original meaning.

Text:
\"\"\"{text}\"\"\"
""",
        "parameters": {"decoding_method": "greedy", "max_new_tokens": 300},
        "project_id": PROJECT_ID
    }
    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    return result.get("results", [{}])[0].get("generated_text", "No rewrite response.")

# -------------------- STREAMLIT UI --------------------
st.set_page_config(page_title="GraniteGuard – AI Ethics Auditor", layout="wide")
st.sidebar.title("🛡️ GraniteGuard")
st.sidebar.markdown("Powered by IBM Granite via watsonx.ai")

st.title("📊 Real-Time AI Ethics Auditor")
st.markdown("Analyze business messages for **bias, tone issues**, and **legal risk** – and instantly rewrite them safely.")

user_input = st.text_area("✍️ Paste your business message here:", height=200)

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Analyze with Granite"):
        if not user_input.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("Analyzing for risks..."):
                try:
                    report = analyze_risks(user_input)
                    st.subheader("📋 AI Ethics Audit Report")
                    st.code(report)
                except Exception as e:
                    st.error(f"Error during analysis: {e}")

with col2:
    if st.button("✍️ Rewrite to Fix"):
        if not user_input.strip():
            st.warning("Please enter some text.")
        else:
            with st.spinner("Rewriting to be inclusive and compliant..."):
                try:
                    rewrite = rewrite_text(user_input)
                    st.subheader("✅ Bias-Free Rewritten Text")
                    st.success(rewrite)
                except Exception as e:
                    st.error(f"Rewrite failed: {e}")
