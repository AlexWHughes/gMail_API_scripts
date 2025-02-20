# 🚀 Google Workspace Out of Office Automation

Automate your Google Workspace **Out of Office** replies using Python and the **Gmail API** with domain-wide delegation.  

This repository provides two Python scripts to help Google Workspace admins manage Out of Office settings for users without needing to log into individual accounts.

---

## 📦 **Features**

1. **Set Out of Office Reply:**  
   - Enables an **HTML-rich** Out of Office reply (no plain text fallback).
   - Disables any **existing** Out of Office before applying the new one.
   - Runs until manually disabled (no start or end dates).

2. **View Current Out of Office Status:**  
   - Retrieves the current Out of Office settings for a user.
   - Displays:
     - ✅ Status: **ON** or **OFF**  
     - 📝 Subject  
     - 💬 Message (HTML)  
     - 📧 Send only to contacts?  
     - 🌍 Send only within domain?  

---

## 💼 **Requirements**

Before running the scripts, ensure you have:
- ✅ **Google Workspace** with **domain-wide delegation** enabled.
- 📧 **Gmail API** enabled in **Google Cloud Console**.
- 🔑 **Service account JSON key** downloaded and placed in your project directory.

---

## 🧩 **Setup & Installation**

1. **Clone this repository:**
```bash
git clone https://github.com/your-alexwhughes/google-workspace-ooo-automation.git
cd google-workspace-ooo-automation
```

2. **Install dependencies using `pip`:**
```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

3. **Add your service account JSON file:**  
Place your service account key file in the project directory and update the script:
```python
SERVICE_ACCOUNT_FILE = 'path/to/your/service_account.json'
```

4. **Configure Domain-Wide Delegation:**  
- In **Google Admin Console** > **Security** > **API Controls** > **Domain-wide Delegation**, add your service account **Client ID**.  
- Authorize the following scope:
  ```plaintext
  https://www.googleapis.com/auth/gmail.settings.basic
  ```

---

## 💾 **Usage**

### 🟢 **1. Set Out of Office Reply**
This script sets an **HTML-rich** Out of Office reply with no start or end dates.

```bash
python set_out_of_office.py
```
- **Note:** Email addresses are currently **hard-coded** within the script. Since Out of Office is typically set infrequently, this should be sufficient for most use cases.  
- 💡 Feel free to open a **Pull Request (PR)** if you have a more dynamic solution that doesn’t rely on third-party tools!

---

### 🔍 **2. View Current Out of Office Status**
Use this script to **check** the current Out of Office status for a user.

```bash
python view_out_of_office.py
```
- Displays whether Out of Office is **ON** or **OFF**, plus the **subject** and **HTML message** if applicable.

---

## ⚙️ **Configuration Options**
You can modify the following parameters in the scripts:
- **User email** (e.g., `'user@example.com'`)
- **Out of Office subject** (e.g., `'Out of Office'`)
- **HTML message** (customize the reply message using rich text formatting)

---

## 💡 **Tips & Troubleshooting**
- Ensure your service account has the following **Google Cloud IAM roles**:
  - **Service Account User**  
  - **Service Account Token Creator**
- If you encounter `403: insufficientPermissions`, ensure that domain-wide delegation is properly configured in **Google Admin Console**.
- Use `userId='me'` when making API requests to impersonate the user (via domain-wide delegation).

---

## 👥 **Contributing**
Contributions are welcome!  
- 📝 **Feature Requests:** Open a **GitHub Issue**  
- 🐛 **Bug Reports:** Open a **GitHub Issue**  
- 💾 **Pull Requests:** Feel free to **submit PRs** for improvements

---

## 📜 **License**
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

### 🚀 **Now you’re ready to automate Google Workspace Out of Office replies like a pro!**  
**Happy coding!** 😊

