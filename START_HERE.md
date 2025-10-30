# 🚀 START HERE - Quick Setup

## What You Have

✨ **Professional Load Bank Checklist System**
- Beautiful modern design
- Email notifications
- Google Sheets integration
- Mobile optimized

---

## 3-Step Setup

### 📤 STEP 1: Deploy (10 min)

1. Upload to GitHub:
   - Go to https://github.com
   - New repository: `loadbank-checklist`
   - Upload ALL files from this folder
   
2. Deploy to Render:
   - Go to https://render.com
   - Sign in with GitHub
   - New Web Service
   - Connect your repo
   - Click Deploy

✅ **Form is now live!** (but email/sheets not working yet)

---

### 📧 STEP 2: Add Email (5 min)

1. Get Gmail App Password:
   - https://myaccount.google.com/apppasswords
   - Enable 2-Step Verification first
   - Create app password
   - Copy the 16-character code

2. Add to Render:
   - Open your service in Render
   - Environment tab
   - Add variables (see ENV_QUICK_REF.md)
   - Save

✅ **Email notifications working!**

---

### 📊 STEP 3: Add Google Sheets (15 min)

1. Create Google Cloud project:
   - https://console.cloud.google.com
   - New project
   - Enable Google Sheets API
   - Enable Google Drive API

2. Create Service Account:
   - IAM & Admin → Service Accounts
   - Create service account
   - Download JSON key

3. Add to Render:
   - Minify JSON (remove line breaks)
   - Add GOOGLE_SHEETS_CREDS variable
   - Save

✅ **Complete system ready!**

---

## 📚 Documentation

- **COMPLETE_SETUP_GUIDE.md** - Detailed step-by-step with screenshots
- **ENV_QUICK_REF.md** - Environment variables quick reference
- **WHATS_NEW.md** - All the new features explained
- **README.txt** - Overview

---

## ⏱️ Time Required

- Basic deployment: 10 min
- Email setup: 5 min
- Google Sheets: 15 min
- **Total: 30 minutes**

---

## 🎯 After Setup

Your URL: `https://your-app.onrender.com`

**Share with customers!**

You'll receive:
- ✉️ Email for every submission
- 📊 Data in Google Sheets
- 💾 Downloadable Excel backup

---

## 🆘 Need Help?

1. Read COMPLETE_SETUP_GUIDE.md (most detailed)
2. Check ENV_QUICK_REF.md (environment vars)
3. Test with /health endpoint
4. Check Render logs for errors

---

## ✅ Quick Test

After setup, submit a test form:
1. Form submits successfully ✓
2. Email received ✓
3. Data in Google Sheets ✓
4. Can download Excel ✓

All working? **You're done!** 🎉

---

Ready to start? Open **COMPLETE_SETUP_GUIDE.md** now!
