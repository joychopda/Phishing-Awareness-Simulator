# Phishing-Awareness-Simulator
This Python script simulates a phishing email campaign in a small organization and generates both a summary report and an incident response template. It's designed for cybersecurity professionals and students focusing on **GRC**, **Security Awareness**, or **SOC operations**.

## 🧠 What It Does

- Simulates phishing behavior for a set of users
- Randomly assigns whether users **clicked** or **reported** a phishing email
- Calculates key metrics like **Click Rate** and **Report Rate**
- Outputs:
  - A detailed **JSON report** of the campaign
  - A professional **incident response report** in plain text

## 🛠️ Tech Stack

- Python 3.x
- Standard libraries: `random`, `datetime`, `json`, `logging`

## 📁 Output Files

- `phishing_campaign_report.json` – structured data for auditing or dashboards
- `incident_response_report.txt` – ready-to-share executive summary

## 📦 How to Use

```bash
python phishing_simulation.py
