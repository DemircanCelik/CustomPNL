# 🚀 Solana PNL Card Bot

A Discord bot that generates custom Solana Profit and Loss (PNL) trading cards 
## ✨ Features

- **🔒 Private PNL Cards**: All generated cards are only visible to you (ephemeral responses)
- **🏴‍☠️ Multi-Coin Support**: Generate PNL cards for any cryptocurrency (SOL, BTC, ETH, Memecoins, etc.)
- **📈 Real-Time Price Integration**: Fetches current SOL price via CoinGecko API
- **🎨 Cyberpunk Design**: Futuristic, dark-themed interface with cyan accents
- **⚡ Slash Commands**: Modern Discord slash command interface with parameter hints
- **💰 Automatic USD Conversion**: Shows both coin amounts and USD equivalents with K formatting
- **📊 Profit/Loss Visualization**: Clear color-coded indicators (green for profit, red for loss)

## 🚀 Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- A Discord Bot Token (see Discord Bot Setup below)

### 2. Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

### 3. Discord Bot Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section
4. Click "Add Bot"
5. Copy the bot token and paste it in your `.env` file
6. Under "Privileged Gateway Intents", enable "Message Content Intent"
7. Go to "OAuth2" > "URL Generator"
8. Select these scopes:
   - `bot`
   - `applications.commands`
9. Select these bot permissions:
   - Send Messages
   - Attach Files
   - Embed Links
10. Copy the generated URL and invite the bot to your server

### 4. You're Ready!

The bot now uses a built-in cyberpunk design inspired by futuristic interfaces. No additional background setup needed!

## 🎮 Usage

### Commands

#### `/pnl`
Create a **private** custom PNL card with direct input (only visible to you):
```
/pnl username:CryptoMaster coin_name:SOL bought_amount:100 sold_amount:120
```
Parameters:
- `username`: Your username/trader name
- `coin_name`: Coin symbol (e.g., SOL, BTC, ETH)
- `bought_amount`: Amount of the coin you bought
- `sold_amount`: Amount of the coin you sold

#### `/info`
Show help and command information (private response):
```
/info
```

### Example Usage

1. **Create a Custom PNL Card**:
   ```
   /pnl username:CryptoMaster coin_name:SOL bought_amount:100 sold_amount:120
   ```
   This will:
   - Use "CryptoMaster" as your trader name
   - Create a SOL trading card
   - Show 100 SOL bought, 120 SOL sold
   - Calculate P&L: +20 SOL profit
   
   The bot will:
   - Fetch current SOL price (e.g., $85.50)
   - Calculate your P&L: +20 SOL profit ($1,710)
   - Generate a cyberpunk-style card showing all details

## 🎨 Card Information

Each Solana PNL card displays:

- **Header**: "MPH >< FNF" futuristic branding
- **PROFIT/LOSS**: Your net P&L in SOL with USD equivalent
- **BOUGHT**: Amount of SOL purchased with USD value
- **SOLD**: Amount of SOL sold with USD value  
- **HOLDING**: Current SOL holdings with USD value
- **USER**: Your trader name and "SOLANA TRADER" designation
- **Footer**: "AFTER ACTION REPORT" with cyberpunk styling

## 🔧 Configuration

You can modify the bot settings in `config.py`:

- **Colors**: Change the color scheme
- **Card Dimensions**: Adjust card size
- **Command Prefix**: Change from `!` to another prefix
- **Backgrounds Folder**: Change the backgrounds directory name

## 🐛 Troubleshooting

### Common Issues

1. **"Invalid input" error**:
   - Make sure you're using numbers for prices and holdings
   - Use dots for decimals (e.g., 0.5, not 0,5)

2. **Bot not responding**:
   - Check that the bot has "Message Content Intent" enabled
   - Verify the bot has permission to send messages in the channel

3. **Background not found**:
   - Ensure the background file exists in the backgrounds folder
   - Check that the file extension matches (jpg, png, jpeg)
   - Use `!backgrounds` to see available backgrounds

4. **Font issues**:
   - The bot uses system fonts with fallbacks
   - If text looks wrong, try installing Arial font

## 📝 Dependencies

- `discord.py`: Discord bot framework
- `Pillow`: Image generation and manipulation  
- `python-dotenv`: Environment variable management
- `aiohttp`: Async HTTP client for API calls
- `requests`: HTTP library for price data fetching

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the bot!

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Trading! 🚀💰** 