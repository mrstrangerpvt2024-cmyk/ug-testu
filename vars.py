import os
from os import environ

# API Configuration
API_ID = int(os.environ.get("API_ID", "22470912"))
API_HASH = os.environ.get("API_HASH", "511be78079ed5d4bd4c967bc7b5ee023")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

CREDIT = os.environ.get("CREDIT", "€ समययात्री £")

# MongoDB Configuration
MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://ugbot31:ugbot1234@cluster0.n1uexk5.mongodb.net/UGxPRO?retryWrites=true&w=majority&appName=Cluster0"
)
DATABASE_NAME = os.environ.get("DATABASE_NAME", "UGxPRO")  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "7678862761"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "6126688051").split()]  # Default to owner ID

# Channel Configuration
PREMIUM_CHANNEL = "https://t.me/+wg5NEbdx1SM4YzY1"

# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "https://postimg.cc/WtCcmJPx").split()))

# Web Server Configuration (Fixed .lower() error)
web_server_value = os.environ.get("WEB_SERVER", "False")
if isinstance(web_server_value, str):
    WEB_SERVER = web_server_value.lower() == "true"
else:
    WEB_SERVER = False

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>\n\n Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name: {name}
🆔 User ID: {user_id}
📅 Expiry: {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully!</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin @ItsUGBot to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}




