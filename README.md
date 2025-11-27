# 📧 HR Email Automation – Resume Mailer

Automatically send your personalized résumé to HR professionals listed in a CSV file using Python. This project is designed for high-volume, personalized outreach to maximize your job search efficiency.

---

## ✨ Features

- **Bulk Processing:** Reads HR email addresses from a CSV file and sends emails to multiple recipients
- **Personalized HTML Emails:** Professional-looking emails with rich HTML formatting
- **Attachment Handling:** Securely attaches your résumé (PDF) to every email
- **Security First:** Uses environment variables for credentials—no hardcoded sensitive data
- **Error Reporting:** Logs success and errors for each recipient in the console
- **Gmail Compatible:** Works seamlessly with Gmail using App Passwords

---

## 📂 Project Structure

```
email_to_hr/
├── .env                    # Environment variables (email, password, file path)
├── .env.example            # Template for environment setup
├── email_to_hr.py          # Main Python script
├── hr_emails.csv           # CSV file with HR contacts
├── hr_emails_template.csv  # Template CSV file
├── pratham_resume.pdf      # Your résumé (replace with yours)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/PrathamPShetty/bulk-email-to-hr.git
cd email_to_hr
```

### 2. Set Up Virtual Environment

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
FILENAME=./pratham_resume.pdf
```

> **🔐 Security Note:** For Gmail, you must use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

**How to Generate Gmail App Password:**
1. Go to your Google Account settings
2. Navigate to Security → 2-Step Verification
3. Scroll down to "App passwords"
4. Generate a new app password for "Mail"
5. Copy the 16-character password to your `.env` file

### 5. Prepare Your CSV File

Your `hr_emails.csv` must contain HR email addresses in the **3rd column (index 2)**:

| Name | Email | Title | Company |
|------|-------|-------|---------|
| Akanksha Puri | akanksha.puri@sourcefuse.com | Associate Director HR | SourceFuse Technologies |
| Akanksha Sogani | akanksha.sogani@perennialsys.com | Head HR | Perennial Systems |
| Akhil Jogiparthi | akhil@ibhubs.co | Vice President - Talent | iB Hubs |

### 6. Customize Your Email

Edit `email_to_hr.py` to personalize the subject and body:

```python
subject = "Seeking Opportunity for Developer Role – Your Name"

body = """
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; font-size: 15px; color: #333;">
    <p>Dear Hiring Manager,</p>
    
    <p>I am reaching out to express my interest in an opportunity as a Developer at your organization. 
    I specialize in <b>Artificial Intelligence</b> and <b>Full-Stack Development</b>...</p>
    
    <!-- Customize your content here -->
    
    <p>Thank you for your time and consideration.</p>
    
    <p>Best regards,<br>Your Name</p>
</body>
</html>
"""
```

### 7. Run the Script

```bash
python email_to_hr.py
```

The script will:
- Read all HR emails from the CSV
- Send personalized emails with your résumé attached
- Display success/failure status for each recipient

---

## 📋 Requirements

- Python 3.7+
- Gmail account with App Password enabled
- PDF résumé file

**Python Packages:**
```
python-dotenv
pandas
```

---

## ⚙️ Configuration Options

### Email Settings

Edit these variables in `email_to_hr.py`:









## ⭐ Support

If this project helped you in your job search, please consider:
- Starring the repository on [GitHub](https://github.com/PrathamPShetty/bulk-email-to-hr)
- Sharing it with others who might benefit
- Contributing improvements

---

