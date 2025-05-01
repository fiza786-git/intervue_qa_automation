# Intervue QA Automation

This project is an end-to-end Selenium automation script for testing key workflows on the [Intervue.io](https://www.intervue.io) website. It includes login automation, search functionality, menu interaction via hover/click, and logout.

## 📂 Project Structure

intervue_qa_automation/ ├── Intervue.py # Main automation test script ├── README.md # Project documentation and setup instructions

## 🚀 Features Automated

- Navigation through website sections: Products, Solutions, Pricing, Resources, Contact Us
- Hover actions (Pricing, Contact Us)
- Login with test credentials
- Search functionality using a popup modal
- Dropdown interaction with search suggestions
- Logout functionality from user dropdown menu

![Automation Demo](intervue_qa_gif.gif)


## 🛠️ Tech Stack

- Python
- Selenium WebDriver
- ChromeDriver
- WebDriverWait & ActionChains for interaction

## ✅ Prerequisites

- Python 3.7+
- Google Chrome installed
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) matching your Chrome version
- Git (optional but recommended)

## 📦 Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/fiza786-git/intervue_qa_automation.git
   cd intervue_qa_automation
   Install required Python packages:
   pip install selenium

## How to Run
Simply run the script using Python:
python Intervue.py

⚠️ The script uses hardcoded credentials for demo purposes. Please replace them with environment variables or a secure method in production environments.

🧰 What the Script Does
Launches https://www.intervue.io
Hovers and clicks through the navigation:
Products
Solutions
Hovers on Pricing and Contact Us
Clicks Login, switches to a new tab
Enters email and password
Clicks on search icon and types "hello"
Selects an item from the suggestion list
Opens profile dropdown
Logs out

📄 License
This project is for educational/demonstration purposes. No license included.


