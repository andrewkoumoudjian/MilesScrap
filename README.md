# LeadBot - AI-Powered Lead Generation Bot

LeadBot is an AI-powered lead generation system that identifies potential leads from social media based on business milestones like funding announcements, product launches, or expansions. It uses OpenRouter for natural language processing and can be deployed to Google Cloud.

## Features

- **Intelligent Lead Discovery**: Scans Twitter and LinkedIn for business milestone events
- **AI Analysis**: Uses OpenRouter for NLP to extract entities, classify milestones, and score leads
- **Customizable Filters**: Filter by location, company size, seniority level, and more
- **Scheduled Searches**: Save searches for daily updates
- **User Management**: Register, login, and manage saved leads
- **Export Functionality**: Download leads as CSV files

## Requirements

- Python 3.9+
- Google Cloud Platform account
- Twitter Developer API access
- OpenRouter API key
- SMTP email account (for notifications)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/leadbot.git
cd leadbot