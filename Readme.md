#  SpectraLogAI  
### AI-Assisted Forensic SIEM & SOC Platform

SpectraLogAI is a **forensic-first Security Information and Event Management (SIEM)** platform designed to tackle real-world cybersecurity challenges such as fragmented logs, alert fatigue, and slow investigations.

The project simulates a **modern Security Operations Center (SOC)** by ingesting logs from multiple devices, generating alerts, and visualizing security events through dashboards — while laying the foundation for **AI-powered, explainable forensic investigations**.

---

##  Problem Statement

Cybercrime investigations and SOC operations face major challenges:

- Massive volumes of logs from Windows systems, mobile devices, servers, and applications  
- Logs stored across different formats, sources, and locations  
- Manual forensic log analysis taking days or weeks  
- Alerts without sufficient context or explanation  
- Difficulty correlating events across multiple devices  

As a result, many cyber incidents remain unresolved due to slow and complex analysis workflows.

---

##  Proposed Solution

**SpectraLogAI** provides a **unified forensic log investigation framework** that:

- Centralizes logs from multiple platforms  
- Enables SOC-style monitoring and alerting  
- Visualizes security events and timelines  
- Evolves toward AI-driven correlation, explainability (XAI), and LLM-based investigation assistance  

The platform is built **incrementally**, closely reflecting real SOC and forensic workflows.

---

##  Development Progress

### Stage 1 – Multi-Source Log Ingestion & Storage  
**Status:** Completed

**Implemented Features:**
- Windows and Android log generation  
- Proper `@timestamp` handling  
- Centralized log ingestion into Elasticsearch  
- Separate indices / data views  
- Field mapping validation in Kibana  
- Searchable and structured log storage  

**Outcome:**  
A unified log repository forming the foundation of a forensic SIEM.

---

### Stage 2 – SOC Alerts & Dashboards  
**Status:** Completed

**Implemented Features:**
- SOC-style alert rules  
- Custom test logs for rule validation  
- Alert triggering and verification  
- Dedicated dashboards for:
  - Windows logs  
  - Android logs  
  - SOC alerts  
- Timeline-based event visualization  

**Outcome:**  
A functional SOC monitoring environment capable of detecting and visualizing suspicious activity.

---

## 🎥 Demo Video

*<video controls src="Spectra_Demo-1.mp4" title="Demo"></video>*

---

## ▶️ How to Run Locally

### Prerequisites
- Elasticsearch (local instance)
- Kibana (same version as Elasticsearch)
- Windows system (for PowerShell-based log generation)
- Basic understanding of Kibana dashboards

---

### Step 1: Start Elasticsearch and Kibana
Ensure both services are running locally:

- Elasticsearch: `http://localhost:9200`
- Kibana: `http://localhost:5601`

Verify Elasticsearch is running:

```
curl http://localhost:9200
```
---
Step 2: Ingest Logs

-Run the provided PowerShell scripts to generate Windows logs
-Send Android logs as structured JSON requests
-Ensure each log contains a valid @timestamp field

Step 3: Create Data Views in Kibana

-Navigate to Stack Management → Data Views

Create data views for:

-Windows logs index
-Android logs index
-SOC alerts index
-Select @timestamp as the time field

Step 4: Import Dashboards

-Open Kibana → Dashboards
-Import saved dashboards (Windows, Android, SOC)
-Verify that visualizations are populated with log data

Step 5: Trigger Alerts

-Send test logs that match alert rule conditions
-Verify alerts appear in:

Alerts & Rules
SOC Alerts dashboard

---

## Technology Stack

- Elasticsearch – centralized log storage and indexing  
- Kibana – dashboards, alerting, and SOC visualization  
- PowerShell – Windows log generation  
- REST APIs – log ingestion interface  
- JSON – log format and data exchange  
- Elastic Alerting Rules – detection and alert generation  
- Windows OS – development and testing environment  


## Roadmap
Stage 3 – Correlation, Enrichment & Explainability

Cross-platform event correlation

IP and geo-location enrichment

Attack timeline reconstruction

Explainable alerts

Stage 4 – AI Copilot & Forensic Automation

Natural-language SOC queries

AI-assisted investigation summaries

Automated incident reporting

Evidence integrity and chain-of-custody concepts

## Intended Use Cases

SOC analyst training and simulation

Cybercrime investigation workflows

Hackathon and academic demonstrations

Affordable security monitoring for education and government

Foundations for AI-assisted DFIR platforms

## Unique Value Proposition

SpectraLogAI focuses on investigation-first security monitoring by offering:

Explainable security alerts

Multi-device and multi-source log analysis

Analyst-friendly dashboards and timelines

A scalable foundation for AI-assisted forensic analysis

📜 License

This project is developed for educational, research, and hackathon purposes.

🤝 Contributions

Contributions, feedback, and suggestions are welcome.
Please open an issue or submit a pull request to contribute.
