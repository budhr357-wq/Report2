# 🚨 Report2 — Telegram Auto Reporter (Multi-Session)

Report2 is a **Telegram Auto-Reporter** built with [Pyrogram](https://docs.pyrogram.org/) that automatically reports illegal or harmful content to Telegram using **real API reports** (MTProto).  
It supports **multiple user sessions**, **custom report types**, and **Heroku one-click deployment**.

---

## ⚙️ Features

✅ Real Telegram API report requests (`messages.Report`)  
✅ Multi-session support (`SESSION_1`, `SESSION_2`, `SESSION_3`, …)  
✅ Custom report reasons (child abuse, scam, violence, etc.)  
✅ Adjustable number of reports  
✅ Works automatically after deployment  
✅ Safe rate-limiting between reports  

---

## 🚀 Deploy to Heroku

You can deploy this app to Heroku directly by clicking the button below 👇  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=hhttps://github.com/budhr357-wq/Report2.git)

---

## 🧩 Required Environment Variables

Set these values in Heroku → **Settings → Config Vars**:

| Variable | Description | Example |
|-----------|--------------|----------|
| `API_ID` | Your Telegram API ID from https://my.telegram.org | `123456` |
| `API_HASH` | Your Telegram API Hash | `abcd1234abcd1234abcd1234` |
| `SESSION_1` | Pyrogram session string (user 1) | `BQDf...` |
| `SESSION_2` | Pyrogram session string (user 2, optional) | `BQFg...` |
| `SESSION_3` | Pyrogram session string (user 3, optional) | `BQHg...` |
| `CHANNEL_LINK` | Telegram channel or group link | `https://t.me/example` |
| `MESSAGE_LINK` | Full message link to report | `https://t.me/example/12` |
| `NUMBER_OF_REPORTS` | How many reports to send | `3` |
| `REPORT_TEXT` | Reason for reporting | `Illegal content detected` |
| `REPORT_REASON_CHILD_ABUSE` | `true` / `false` | `true` |
| `REPORT_REASON_VIOLENCE` | `true` / `false` | `false` |
| `REPORT_REASON_ILLEGAL_GOODS` | `true` / `false` | `false` |
| `REPORT_REASON_ILLEGAL_ADULT` | `true` / `false` | `false` |
| `REPORT_REASON_PERSONAL_DATA` | `true` / `false` | `false` |
| `REPORT_REASON_SCAM` | `true` / `false` | `false` |
| `REPORT_REASON_COPYRIGHT` | `true` / `false` | `false` |
| `REPORT_REASON_SPAM` | `true` / `false` | `false` |
| `REPORT_REASON_OTHER` | `true` / `false` | `false` |

Only **one** report type should be set to `true` at a time.  
All others should remain `false`.

---

## 📦 Local Setup (Optional)

If you want to run this locally instead of Heroku:

```bash
git clone https://github.com/Oxeigns/Report2.git
cd Report2
pip install -r requirements.txt
python3 app.py
