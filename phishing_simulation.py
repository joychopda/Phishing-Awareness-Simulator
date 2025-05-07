import random
from datetime import datetime
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

class User:
    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name
        self.clicked = False
        self.reported = False

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class PhishingCampaign:
    def __init__(self, users: List[User]):
        self.users = users
        self.report_data = {}

    def simulate(self):
        """Simulate user behavior during a phishing campaign."""
        for user in self.users:
            user.clicked = random.choice([True, False])
            user.reported = not user.clicked and random.choice([True, False])
        logging.info("Phishing simulation complete.")

    def generate_report(self) -> Dict:
        """Compile phishing campaign results."""
        total = len(self.users)
        clicked = [u for u in self.users if u.clicked]
        reported = [u for u in self.users if u.reported]

        self.report_data = {
            "total_users": total,
            "click_count": len(clicked),
            "report_count": len(reported),
            "click_rate": (len(clicked) / total) * 100,
            "report_rate": (len(reported) / total) * 100,
            "campaign_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "clicked_users": [u.to_dict() for u in clicked],
            "reported_users": [u.to_dict() for u in reported]
        }

        with open("phishing_campaign_report.json", "w") as f:
            json.dump(self.report_data, f, indent=4)

        logging.info("Phishing campaign report generated.")
        return self.report_data

    def generate_incident_response(self):
        """Create a high-level incident response summary."""
        if not self.report_data:
            raise ValueError("Report data not found. Run generate_report() first.")

        clicked = "\n".join([f"  - ID: {u['id']}, Name: {u['name']}" for u in self.report_data["clicked_users"]])
        reported = "\n".join([f"  - ID: {u['id']}, Name: {u['name']}" for u in self.report_data["reported_users"]])

        response = f"""
=== Incident Response Report ===
Campaign Date: {self.report_data['campaign_date']}
Total Users Targeted: {self.report_data['total_users']}

- Clicked Link: {self.report_data['click_count']} ({self.report_data['click_rate']:.2f}%)
- Reported Email: {self.report_data['report_count']} ({self.report_data['report_rate']:.2f}%)

Users who clicked the link:
{clicked if clicked else '  None'}

Users who reported the phishing email:
{reported if reported else '  None'}

Analysis:
- Elevated click rates indicate weak phishing awareness.
- Reporting users showed proactive security behavior.

Recommendations:
- Enroll clickers in follow-up security training.
- Reinforce positive behavior through recognition.
- Track user behavior in future campaigns.

Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

        with open("incident_response_report.txt", "w") as f:
            f.write(response.strip())

        logging.info("Incident response report generated.")

# === Run the simulation ===
if __name__ == "__main__":
    employees = [
        User(1, "Steve Jobs"),
        User(2, "Steve Wozniak"),
        User(3, "Jon Ive"),
        User(4, "Tim Cook")
    ]

    campaign = PhishingCampaign(employees)
    campaign.simulate()
    report = campaign.generate_report()
    campaign.generate_incident_response()
