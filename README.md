# 🛡️ RiskBot – AI Compliance Copilot

I started with a simple bias-rewrite tool (graniteguard_og.py) and evolved it into a full multi-agent AI system (riskbot.py) powered by automation and compliance workflows.

RiskBot is an intelligent multi-agent system that audits business communication for **bias**, **tone issues**, and **legal risk** – and automates the next steps using AI and simulated enterprise integrations.

Built using IBM Granite models, RiskBot simulates real-world HR/legal compliance workflows powered by autonomous agents.

---

## 🤖 Features

| Agent | Role |
|-------|------|
| 🧠 `RiskAnalyzerAgent` | Flags bias, tone, and legal risks using keyword analysis |
| ✍️ `RewriteAgent` | Rewrites problematic text to be inclusive and compliant |
| 📣 `NotifyAgent` | Sends Slack/email-style alert (simulated) |
| 📝 `ActionAgent` | Creates Jira/Notion-like task for compliance team |
| 📦 `AuditLoggerAgent` | Logs full event to `audit_log.csv` |
| 🔍 `Log Viewer` | Displays real-time `riskbot_live_log.txt` inside the app |

---

## 🧪 Example Input

```text
We are looking for young, energetic men to lead our aggressive new sales team. Foreigners and women might not be a good fit for this role due to cultural dynamics.
```

✅ Output:
- 🚩 Risks: Age, Gender, Nationality, Tone
- ✅ Rewrite: Inclusive and compliant version
- 📣 Alert simulated
- 📝 Task filed
- 📦 Logged to `audit_log.csv`
- 🔍 Logged to `riskbot_live_log.txt`

---

## 🖥️ Run It Locally

```bash
streamlit run streamlit_riskbot_app.py
```

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `riskbot.py` | Multi-agent automation core (with live logging) |
| `streamlit_riskbot_app.py` | Web interface with live logs and downloads |
| `audit_log.csv` | Output file created after each run |
| `riskbot_live_log.txt` | Human-readable real-time event log |
| `requirements.txt` | All dependencies |
| `.gitignore` | Prevents `.env` upload |

---

## 🔐 Security

- Use `.env` for storing `API_KEY`, `PROJECT_ID`, etc.
- Ensure `.env` is listed in `.gitignore` to avoid leaks.

---

## 🏁 Project Status

✅ MVP complete  
🧠 Multi-agent logic functional  
🖥️ Real-time logging + CSV audit  
🚀 Ready for deployment or extension

---

## 🌐 Live Usage Ideas

- Slack or Gmail webhook integration
- Monitoring uploaded contracts or job posts
- Chrome extension to trigger RiskBot from anywhere

---
