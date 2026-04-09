# init_KL
初始化 KL 的 VScode 與 Github

## Telegram Bot Message Sender

使用 `send_telegram_message.py` 可以透過你剛建立的 Telegram bot 傳送訊息到 `telegram:8627815136`。

執行方式：

```bash
python send_telegram_message.py "Hello from the bot!"
```

如果你想要改用不同的訊息格式，傳入 `--mode`：

```bash
python send_telegram_message.py "<b>Bold text</b>" --mode HTML
```
