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

## 🧰 Tech Stack

| Technology | Purpose / Usage |
|-----------|------------------|
| Windows OS | Development, testing, and primary log source |
| PowerShell | Generate Windows security, system, and application logs |
| REST APIs | Secure log ingestion from external sources |
| JSON | Standardized log data format |
| Filebeat / Winlogbeat | Collect and forward logs to ingestion pipeline |
| Logstash | Parse, validate, normalize, and enrich logs |
| Elasticsearch | Centralized log storage, indexing, and fast search |
| Elastic Alerting Rules | Detection logic and alert generation |
| AI / ML Engine | Event correlation and anomaly detection |
| SHAP / LIME (XAI) | Explainability for AI-generated alerts |
| LLM Investigator Assistant | Natural language queries and investigation support |
| Kibana | Dashboards, SOC visualization, and log exploration |



## Roadmap
### Stage 3 – Correlation, Enrichment & Explainability
**Status:** In Progress

**Current Progress:**
- Correlation, XAI, enrichment, dashboard, alerts, and logs API routes are wired for frontend integration
- Backend request/response contracts now match the current frontend API client
- Elasticsearch access now fails fast with fallback responses when ES is offline

**Pending for Completion:**
- Cross-platform event correlation using real Elasticsearch-backed logic
- IP and geo-location enrichment from real enrichment sources
- Attack timeline reconstruction from actual linked case and event data
- Explainable alerts generated from real model outputs and investigation context

### Stage 4 – AI Copilot & Forensic Automation

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
