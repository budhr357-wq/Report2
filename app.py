import os
import json
import asyncio
import random
from pyrogram import Client
from pyrogram.raw import functions, types

# ========== Load Config ==========

with open("config.json", "r") as f:
    CONFIG = json.load(f)

API_ID = int(os.getenv("API_ID", CONFIG["API_ID"]))
API_HASH = os.getenv("API_HASH", CONFIG["API_HASH"])
CHANNEL_LINK = os.getenv("CHANNEL_LINK", CONFIG["CHANNEL_LINK"])
MESSAGE_LINK = os.getenv("MESSAGE_LINK", CONFIG["MESSAGE_LINK"])
REPORT_TEXT = os.getenv("REPORT_TEXT", CONFIG["REPORT_TEXT"])
NUMBER_OF_REPORTS = int(os.getenv("NUMBER_OF_REPORTS", CONFIG["NUMBER_OF_REPORTS"]))

# Collect sessions dynamically
SESSIONS = []
for k, v in os.environ.items():
    if k.startswith("SESSION_") and v.strip():
        SESSIONS.append(v.strip())

if not SESSIONS:
    raise Exception("No sessions found! Please set SESSION_1, SESSION_2, etc. in Heroku config vars.")

print(f"✅ Found {len(SESSIONS)} sessions. Target: {NUMBER_OF_REPORTS} reports total.")

# Determine reason type
def get_reason():
    if CONFIG.get("REPORT_REASON_CHILD_ABUSE"): return types.InputReportReasonChildAbuse()
    if CONFIG.get("REPORT_REASON_VIOLENCE"): return types.InputReportReasonViolence()
    if CONFIG.get("REPORT_REASON_ILLEGAL_GOODS"): return types.InputReportReasonIllegalDrugs()
    if CONFIG.get("REPORT_REASON_ILLEGAL_ADULT"): return types.InputReportReasonPornography()
    if CONFIG.get("REPORT_REASON_PERSONAL_DATA"): return types.InputReportReasonPersonalDetails()
    if CONFIG.get("REPORT_REASON_SCAM"): return types.InputReportReasonSpam()
    if CONFIG.get("REPORT_REASON_COPYRIGHT"): return types.InputReportReasonCopyright()
    if CONFIG.get("REPORT_REASON_SPAM"): return types.InputReportReasonSpam()
    if CONFIG.get("REPORT_REASON_OTHER"): return types.InputReportReasonOther()
    return types.InputReportReasonOther()

REASON = get_reason()

async def send_report(session_str, index):
    """Send single report from one session."""
    try:
        async with Client(f"reporter_{index}", api_id=API_ID, api_hash=API_HASH, session_string=session_str) as app:
            chat = await app.get_chat(CHANNEL_LINK)
            msg_id = int(MESSAGE_LINK.split("/")[-1])
            msg = await app.get_messages(chat.id, msg_id)
            peer = await app.resolve_peer(chat.id)

            await app.invoke(
                functions.messages.Report(
                    peer=peer,
                    id=[msg.id],
                    reason=REASON,
                    message=REPORT_TEXT
                )
            )
            print(f"[✅] Report sent from session #{index} ({app.me.first_name})")
    except Exception as e:
        print(f"[❌] Session #{index} failed: {e}")

async def main():
    print("🚀 Starting multi-session reporter...")

    tasks = []
    used_sessions = random.sample(SESSIONS, min(NUMBER_OF_REPORTS, len(SESSIONS)))
    for i, session in enumerate(used_sessions, start=1):
        tasks.append(send_report(session, i))
        await asyncio.sleep(2)  # avoid flood

    await asyncio.gather(*tasks)
    print("✅ All reports completed!")

if __name__ == "__main__":
    asyncio.run(main())
