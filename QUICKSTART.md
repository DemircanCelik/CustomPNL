# 🚀 Quick Start Guide

Get your Solana PNL Card Bot up and running in minutes!

## ⚡ Fast Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Discord Bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to "Bot" section → Add Bot
4. Copy the bot token
5. Enable "Message Content Intent"

### 3. Configure Environment
Create a `.env` file:
```
DISCORD_TOKEN=paste_your_bot_token_here
```

### 4. Run the Bot
```bash
python run_bot.py
```

## 🎯 Test Without Discord

Want to test card generation first?
```bash
python test_card_generation.py
```

## 📱 Basic Commands

Once your bot is running:

- `/pnl` → Create **private** custom PNL card (only you can see it)
- `/info` → Show all commands (private response)

**Example usage:**
```
/pnl username:CryptoTrader coin_name:SOL bought_amount:100 sold_amount:120
```

🔒 **Privacy**: All responses are ephemeral - only you can see your PNL cards!

## 🎨 Cyberpunk Design

The bot features a built-in futuristic cyberpunk design with:
- Dark theme with cyan accents
- Real-time SOL price integration
- Professional trading report layout

## 🔧 Troubleshooting

**Bot not responding?**
- Check "Message Content Intent" is enabled
- Verify bot has permission to send messages

**Import errors?**
- Run `pip install -r requirements.txt`

**API/Price errors?**
- Check internet connection for CoinGecko API
- Bot will use fallback price if API fails

---

**That's it! You're ready to create amazing PNL cards! 🏴‍☠️** 