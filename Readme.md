# 🔐 SpectraLogAI  
### AI-Assisted Forensic SIEM & SOC Platform

SpectraLogAI is a **forensic-first Security Information and Event Management (SIEM)** platform designed to address real-world cybersecurity challenges such as fragmented logs, alert fatigue, and slow investigations.

The project simulates a **modern Security Operations Center (SOC)** by ingesting logs from multiple devices, generating alerts, and visualizing events through dashboards — while laying the foundation for **AI-powered, explainable forensic investigations**.

---

## 🚨 Problem Statement

Cybercrime investigations and SOC operations face major challenges:

- Massive volumes of logs from Windows systems, mobile devices, servers, and applications
- Logs stored in different formats and locations
- Manual forensic analysis taking days or weeks
- Alerts without explanation or context
- Difficulty correlating events across multiple devices

As a result, many security incidents remain unresolved due to slow and complex analysis workflows.

---

## 💡 Proposed Solution

**SpectraLogAI** provides a **unified forensic log investigation framework** that:

- Centralizes logs from multiple sources
- Enables SOC-style alerting and monitoring
- Visualizes events and timelines for analysts
- Evolves toward AI-driven correlation, explainability (XAI), and LLM-based investigation assistance

The platform is built **incrementally in stages**, mirroring real-world SOC and SIEM development.

---

## 🧱 System Architecture (Current)




Future stages will extend this architecture with correlation, enrichment, and AI layers.

---

## ✅ Development Progress

### 🟢 Stage 1 – Multi-Source Log Ingestion & Storage  
**Status:** Completed

**Features Implemented:**
- Windows and Android log generation
- Proper `@timestamp` handling
- Centralized log ingestion into Elasticsearch
- Separate indices / data views
- Field mapping verification in Kibana
- Searchable and structured log storage

**Outcome:**  
A unified, centralized log store forming the base of a forensic SIEM.

🎥 **Stage 1 Demo Video:**  
*(Add GitHub video asset link here)*

---

### 🟢 Stage 2 – SOC Alerts & Dashboards  
**Status:** Completed

**Features Implemented:**
- SOC-style alert rules
- Custom test logs for rule validation
- Alert triggering and verification
- Dedicated dashboards for:
  - Windows logs
  - Android logs
  - SOC alerts
- Timeline-based event visualization

**Outcome:**  
A functional SOC monitoring environment with alerts and dashboards.

🎥 **Stage 2 Demo Video:**  
*(Add GitHub video asset link here)*

---

## 📊 Dashboards Available

- 🖥️ Windows Security Events Dashboard  
- 📱 Android Activity Logs Dashboard  
- 🚨 SOC Alerts Dashboard  
- ⏱️ Event Timelines & Trends  

These dashboards replicate real SOC analyst workflows.

---

## 🛠️ Technology Stack

- **Elasticsearch** – Centralized log storage & search  
- **Kibana** – Dashboards, alerts, and SOC views  
- **PowerShell / Scripts** – Log generation & testing  
- **REST APIs** – Log ingestion  
- **JSON** – Normalized log format  

---

## 🔮 Roadmap

### Stage 3 – Correlation, Enrichment & XAI (yet to be created)
- Cross-platform event correlation
- IP and geo-location enrichment
- Attack timeline reconstruction
- Explainable alerts (why an event is suspicious)

### Stage 4 – AI Copilot & Forensic Automation (yet to be created)
- Natural-language SOC queries
- AI-assisted investigation summaries
- Automated incident reporting
- Evidence integrity and chain-of-custody concepts

---

## 🎯 Intended Use Cases

- SOC analyst training and simulation  
- Cybercrime investigation workflows  
- Hackathon and academic demonstrations  
- Affordable security monitoring for education and government  
- Foundations for AI-assisted DFIR platforms  

---

## 🌟 Unique Value Proposition

SpectraLogAI is designed to evolve beyond traditional SIEM tools by focusing on:

- **Explainability** instead of black-box alerts  
- **Investigation-first workflows**  
- **Multi-device and multi-source correlation**  
- **Accessibility for non-expert analysts**  

---

## 📜 License

This project is developed for **educational, research, and hackathon purposes**.

---

## 🤝 Contributions

Feedback, suggestions, and contributions are welcome.  
Feel free to open issues or submit pull requests.
