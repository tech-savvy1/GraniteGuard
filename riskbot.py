
# riskbot.py – Multi-Agent Automation Flow for RiskBot

import os
from datetime import datetime
from dotenv import load_dotenv
import csv

# Simulated agent behavior – each is a function

# Load secrets
load_dotenv()
API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
MODEL_ID = os.getenv("MODEL_ID")

def RiskAnalyzerAgent(text):
    risks = [
        {"type": "Age Bias", "detail": "Uses word 'young'"},
        {"type": "Gender Bias", "detail": "Excludes women"},
        {"type": "Nationality Bias", "detail": "Mentions foreigners not suitable"},
        {"type": "Tone", "detail": "Aggressive tone used"}
    ]
    return risks

def RewriteAgent(text):
    return "We are looking for motivated professionals to lead our dynamic sales team. We welcome candidates from all backgrounds who thrive in diverse environments."

def NotifyAgent(author, risk_level, risks):
    print("\n📣 Slack/Email Message Sent:")
    print(f"@HR Lead – A high-risk message was detected from {author} (Urgency: {risk_level})")
    print("Risks:")
    for r in risks:
        print(f" - {r['type']}: {r['detail']}")

def ActionAgent(author):
    print("\n📝 Task Created in Jira/Notion:")
    print(f"- Task: Review risky content from {author}")
    print("- Status: Open | Priority: 🔴 High")

def AuditLoggerAgent(author, risks, rewrite_text):
    file = "audit_log.csv"
    with open(file, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), author, ', '.join([r['type'] for r in risks]), rewrite_text, "Logged"])
    print("\n📦 Logged to audit_log.csv")

def run_riskbot(input_text, author="Anonymous"):
    print("\n🤖 Running RiskBot on input text...")
    risks = RiskAnalyzerAgent(input_text)
    risk_level = "HIGH" if len(risks) >= 3 else "MEDIUM"
    rewritten = RewriteAgent(input_text)
    NotifyAgent(author, risk_level, risks)
    ActionAgent(author)
    AuditLoggerAgent(author, risks, rewritten)
    return {
        "original": input_text,
        "risks": risks,
        "rewrite": rewritten,
        "author": author,
        "risk_level": risk_level
    }

if __name__ == "__main__":
    sample_input = "We are looking for young, energetic men to lead our aggressive new sales team. Foreigners and women might not be a good fit for this role due to cultural dynamics."
    result = run_riskbot(sample_input, author="Rakesh Sharma")
