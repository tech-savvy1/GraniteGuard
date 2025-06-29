
# streamlit_riskbot_app.py – Frontend for RiskBot Agent System

import streamlit as st
from riskbot import run_riskbot

st.set_page_config(page_title="RiskBot – AI Compliance Copilot", layout="wide")
st.title("🛡️ RiskBot – AI Compliance Copilot")

st.markdown("""
Enter any **job post**, **policy**, or **HR communication** below and let RiskBot:
- Detect bias, tone, or legal risks
- Rewrite the message to be inclusive
- Simulate notifications, Jira tasks, and audit logging
""")

sample_input = "We are looking for young, energetic men to lead our aggressive new sales team. Foreigners and women might not be a good fit for this role due to cultural dynamics."

with st.expander("💡 Try Sample Text"):
    st.code(sample_input)

input_text = st.text_area("✍️ Paste business message here:", height=200)
author = st.text_input("🧑 Enter author name:", "Rakesh Sharma")

if st.button("🤖 Run RiskBot"):
    if not input_text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Running RiskBot agents..."):
            result = run_riskbot(input_text, author=author)

        st.success("RiskBot completed its analysis!")

        st.subheader("🚩 Detected Risks")
        for risk in result["risks"]:
            st.markdown(f"- **{risk['type']}**: {risk['detail']}")

        st.subheader("✅ Inclusive Rewrite")
        st.success(result["rewrite"])

        st.subheader("📣 Notification Summary")
        st.info(f"Alert sent to HR for content by {result['author']} with risk level **{result['risk_level']}**.")

        st.subheader("📝 Action Summary")
        st.markdown("- Task created in compliance system (simulated)")

        st.subheader("📦 Audit Log Entry")
        st.code("audit_log.csv updated ✅")
