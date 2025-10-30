# 🔑 Environment Variables Quick Reference

## Copy-Paste These in Render.com → Environment Tab

### EMAIL SETUP (Required for notifications)

```
ADMIN_EMAIL
your-email@gmail.com

SMTP_SERVER
smtp.gmail.com

SMTP_PORT
587

SMTP_USERNAME
your-email@gmail.com

SMTP_PASSWORD
your-gmail-app-password-here
```

**Get Gmail App Password:**
1. https://myaccount.google.com/apppasswords
2. Enable 2-Step Verification first
3. Create app password
4. Copy 16-character code

---

### GOOGLE SHEETS SETUP (Required for Sheets integration)

```
GOOGLE_SHEETS_CREDS
{"type":"service_account","project_id":"your-project-123",...entire json...}

GOOGLE_SHEET_NAME
Load Bank Checklist Submissions
```

**Get Service Account JSON:**
1. https://console.cloud.google.com
2. Create project
3. Enable Google Sheets API + Drive API
4. IAM & Admin → Service Accounts → Create
5. Keys tab → Add Key → Create new key → JSON
6. Open downloaded JSON file
7. Minify it (remove line breaks, make one line)
8. Paste entire JSON as value

**Minify JSON online:**
https://www.freeformatter.com/json-formatter.html

---

## Testing After Setup

### Check if variables are set:
Go to: `your-url.onrender.com/health`

Should show:
```json
{
  "status": "healthy",
  "email_configured": true,
  "google_sheets_configured": true
}
```

If false, check your environment variables!

---

## Common Mistakes

❌ Using regular Gmail password (use App Password!)
❌ JSON with line breaks (must be minified)
❌ Missing quotes in JSON
❌ Forgot to enable Google Sheets API
❌ Forgot to enable 2-Step Verification
❌ Typos in variable names (case-sensitive!)

---

## All Variables Summary

| Variable | Required | Example | Notes |
|----------|----------|---------|-------|
| ADMIN_EMAIL | Yes | user@gmail.com | Your email |
| SMTP_SERVER | Yes | smtp.gmail.com | Gmail SMTP |
| SMTP_PORT | Yes | 587 | Standard port |
| SMTP_USERNAME | Yes | user@gmail.com | Same as admin |
| SMTP_PASSWORD | Yes | abcd efgh ijkl mnop | App password |
| GOOGLE_SHEETS_CREDS | Yes | {...json...} | Minified JSON |
| GOOGLE_SHEET_NAME | Yes | Sheet Name | Can customize |

---

## Order of Setup

1. ✅ Deploy to Render first (without env vars)
2. ✅ Get Gmail App Password
3. ✅ Add email env vars
4. ✅ Test email (submit form)
5. ✅ Set up Google Cloud
6. ✅ Add Sheets env vars
7. ✅ Test Sheets (submit form)
8. ✅ Check /health endpoint

---

## Need Help?

See COMPLETE_SETUP_GUIDE.md for detailed instructions with screenshots!
