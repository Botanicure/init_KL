#!/usr/bin/env python3
"""Send a message through a Telegram bot."""

import json
import urllib.parse
import urllib.request

BOT_TOKEN = "8779592026:AAF8rj_pBAVjE1KG3ChTVx7paWL6TRS2JUw"
CHAT_ID = "8627815136"

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_telegram_message(text: str, parse_mode: str = "Markdown") -> dict:
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
    }
    if parse_mode:
        payload["parse_mode"] = parse_mode

    data = urllib.parse.urlencode(payload).encode("utf-8")
    request = urllib.request.Request(TELEGRAM_API_URL, data=data)

    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode("utf-8")
        return json.loads(response_data)


if __name__ == "__main__":
    message = "Hello from Notebook - Odette!"
    parse_mode = None  # 或 "Markdown", "HTML", "MarkdownV2"
    result = send_telegram_message(message, parse_mode)
    print(json.dumps(result, indent=2, ensure_ascii=False))
