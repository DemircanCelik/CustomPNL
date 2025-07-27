# 🚀 Discord Bot Deployment Guide

Deploy your Custom PNL Card Bot to run 24/7 in the cloud!

## 🆓 Railway (Recommended - Free)

**Perfect for beginners, 500 free hours/month**

### Step 1: Prepare Your Code
1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

### Step 2: Deploy on Railway
1. Go to [Railway.app](https://railway.app)
2. **Sign up** with GitHub
3. **Click "New Project"** → "Deploy from GitHub repo"
4. **Select your repository**
5. **Add Environment Variable**:
   - Key: `DISCORD_TOKEN`
   - Value: Your Discord bot token
6. **Deploy!** 🚀

**Your bot will be live in ~2 minutes!**

---

## 🆓 Render (Alternative Free Option)

### Step 1: Create account
1. Go to [Render.com](https://render.com)
2. Sign up with GitHub

### Step 2: Deploy
1. **New** → **Web Service**
2. **Connect your GitHub repo**
3. **Settings**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
4. **Add Environment Variable**:
   - `DISCORD_TOKEN` = your token
5. **Deploy**

---

## 💰 DigitalOcean (Reliable Paid - $5/month)

**Best for serious bots that need 100% uptime**

### Step 1: Create Droplet
1. Sign up at [DigitalOcean](https://digitalocean.com)
2. **Create Droplet**:
   - **Image**: Ubuntu 22.04
   - **Size**: Basic $4/month
   - **Add SSH Key** (recommended)

### Step 2: Setup Bot
```bash
# Connect to your droplet
ssh root@your_droplet_ip

# Update system
apt update && apt upgrade -y

# Install Python and dependencies
apt install python3 python3-pip git -y

# Clone your repository
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# Install requirements
pip3 install -r requirements.txt

# Create .env file
nano .env
# Add: DISCORD_TOKEN=your_token_here

# Test the bot
python3 bot.py
```

### Step 3: Keep Bot Running (PM2)
```bash
# Install PM2
npm install -g pm2

# Start bot with PM2
pm2 start bot.py --name "pnl-bot" --interpreter python3

# Save PM2 config
pm2 save
pm2 startup

# Check status
pm2 status
```

---

## 🏠 Raspberry Pi (One-time $35-75)

**Perfect for learning and full control**

### Step 1: Setup Raspberry Pi
1. **Install Raspberry Pi OS**
2. **Enable SSH** in settings
3. **Connect to network**

### Step 2: Install Bot
```bash
# SSH into Pi
ssh pi@your_pi_ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Git and Python
sudo apt install git python3-pip -y

# Clone your bot
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# Install requirements
pip3 install -r requirements.txt

# Create .env file
nano .env
# Add your Discord token

# Test bot
python3 bot.py
```

### Step 3: Auto-start on Boot
```bash
# Create service file
sudo nano /etc/systemd/system/pnl-bot.service
```

Add this content:
```ini
[Unit]
Description=PNL Card Discord Bot
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/your-repo
ExecStart=/usr/bin/python3 /home/pi/your-repo/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl enable pnl-bot.service
sudo systemctl start pnl-bot.service

# Check status
sudo systemctl status pnl-bot.service
```

---

## 🆓 Replit (Beginner-Friendly)

### Step 1: Setup
1. Go to [Replit.com](https://replit.com)
2. **Create new Repl** → **Import from GitHub**
3. **Paste your GitHub repo URL**

### Step 2: Configure
1. **Add Secret** (environment variable):
   - Key: `DISCORD_TOKEN`
   - Value: Your bot token
2. **Click Run** ▶️

### Step 3: Keep Always On ($5/month)
1. **Upgrade to Always On** in settings
2. Your bot will run 24/7

---

## 📊 Comparison Table

| Platform | Cost/Month | Difficulty | Uptime | Best For |
|----------|------------|------------|---------|----------|
| Railway | Free | ⭐ Easy | 95% | Beginners |
| Render | Free | ⭐⭐ Easy | 90% | Testing |
| Replit | $5 | ⭐ Very Easy | 99% | Beginners |
| DigitalOcean | $5 | ⭐⭐⭐ Medium | 99.9% | Production |
| Raspberry Pi | $0* | ⭐⭐⭐⭐ Hard | 95%* | Learning |
| AWS/GCP | $5-15 | ⭐⭐⭐⭐⭐ Hard | 99.9% | Enterprise |

*One-time cost, depends on your internet

---

## 🔧 Troubleshooting

### Common Issues

**Bot not starting:**
```bash
# Check logs
pm2 logs pnl-bot  # For PM2
docker logs container_name  # For Docker
```

**Environment variables not working:**
- Make sure `.env` file exists
- Check variable names are exact
- Restart the service after changes

**Memory issues:**
- Use smaller instances
- Add swap space on VPS
- Optimize image processing

### Useful Commands

**Railway:**
```bash
# Check logs
railway logs

# Redeploy
git push origin main
```

**DigitalOcean:**
```bash
# Check bot status
pm2 status

# Restart bot
pm2 restart pnl-bot

# View logs
pm2 logs pnl-bot
```

---

## 🎯 Recommended Path

1. **Start with Railway** (free, easy)
2. **Test your bot** for a few days
3. **Upgrade to DigitalOcean** when you need 24/7 reliability
4. **Consider Raspberry Pi** for learning

**Most Popular**: Railway → DigitalOcean

---

**Need help?** Check the deployment platform's documentation or ask in their support channels! 