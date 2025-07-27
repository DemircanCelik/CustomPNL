# ☁️ AWS Deployment Guide for Discord Bot

Deploy your Custom PNL Card Bot on Amazon Web Services

## 🚀 AWS Lightsail (Recommended)

**Best for beginners - Simple, predictable pricing**

### Cost: $3.50/month for 512MB RAM, 1 vCPU

### Step 1: Create Lightsail Instance
1. **Go to**: [AWS Lightsail Console](https://lightsail.aws.amazon.com/)
2. **Click**: "Create instance"
3. **Select**:
   - **Platform**: Linux/Unix
   - **Blueprint**: Ubuntu 22.04 LTS
   - **Instance Plan**: $3.50/month (512 MB RAM)
4. **Name your instance**: `pnl-discord-bot`
5. **Click**: "Create instance"

### Step 2: Connect and Setup
```bash
# Click "Connect using SSH" in Lightsail console
# OR use your own SSH client

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and Git
sudo apt install python3 python3-pip git -y

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

### Step 3: Keep Bot Running
```bash
# Install screen (simple option)
sudo apt install screen -y

# Start bot in screen session
screen -S pnl-bot
python3 bot.py

# Detach from screen: Ctrl+A, then D
# Reattach later: screen -r pnl-bot
```

**Or use systemd service (recommended):**
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
User=ubuntu
WorkingDirectory=/home/ubuntu/your-repo
ExecStart=/usr/bin/python3 /home/ubuntu/your-repo/bot.py
Restart=always
RestartSec=10

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

## 🔧 AWS EC2 (Advanced)

**More control, scalable, industry standard**

### Cost: $5-15/month depending on instance type

### Step 1: Launch EC2 Instance
1. **Go to**: [AWS EC2 Console](https://console.aws.amazon.com/ec2/)
2. **Click**: "Launch Instance"
3. **Configure**:
   - **Name**: `PNL-Discord-Bot`
   - **AMI**: Ubuntu Server 22.04 LTS
   - **Instance Type**: `t3.micro` (1 vCPU, 1GB RAM) - $8.50/month
   - **Key Pair**: Create new or use existing
   - **Security Group**: Allow SSH (port 22)
4. **Launch Instance**

### Step 2: Connect and Setup
```bash
# Connect via SSH
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip git htop -y

# Clone repository
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# Install requirements
pip3 install -r requirements.txt

# Create .env file
nano .env
# Add: DISCORD_TOKEN=your_token_here

# Test bot
python3 bot.py
```

### Step 3: Production Setup with PM2
```bash
# Install Node.js and PM2
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install -g pm2

# Start bot with PM2
pm2 start bot.py --name "pnl-bot" --interpreter python3

# Save PM2 configuration
pm2 save
pm2 startup

# Monitor
pm2 status
pm2 logs pnl-bot
```

---

## ⚡ AWS Lambda (Serverless - Advanced)

**Pay only when used, requires code changes**

### Cost: Usually $0-2/month for small bots

### Prerequisites
⚠️ **Note**: Discord bots typically need persistent connections. Lambda is better for slash-command-only bots.

### Step 1: Prepare Code for Lambda
```python
# Create lambda_function.py
import json
import boto3
from bot import PNLCard
import os

def lambda_handler(event, context):
    # Handle Discord interaction
    if event.get('type') == 1:  # PING
        return {'type': 1}
    
    if event.get('type') == 2:  # APPLICATION_COMMAND
        # Process slash command
        data = event.get('data', {})
        
        if data.get('name') == 'pnl':
            # Extract options
            options = {opt['name']: opt['value'] for opt in data.get('options', [])}
            
            # Generate PNL card
            # ... (your PNL logic here)
            
            return {
                'type': 4,  # CHANNEL_MESSAGE_WITH_SOURCE
                'data': {
                    'content': 'PNL card generated!',
                    'flags': 64  # EPHEMERAL
                }
            }
    
    return {'statusCode': 200}
```

### Step 2: Deploy to Lambda
1. **Package your code** with dependencies
2. **Create Lambda function**
3. **Set up API Gateway** for Discord webhooks
4. **Configure Discord** to use your webhook URL

---

## 🏗️ AWS Elastic Beanstalk

**Platform-as-a-Service, easier than EC2**

### Cost: $10-20/month

### Step 1: Prepare Application
```bash
# Create application.py (Beanstalk entry point)
from bot import bot
import os

if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_TOKEN'))
```

### Step 2: Deploy
1. **Install EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize and deploy**:
   ```bash
   eb init
   eb create pnl-bot-env
   eb deploy
   ```

3. **Set environment variables** in EB console

---

## 📊 AWS Services Comparison

| Service | Monthly Cost | Difficulty | Best For | Uptime |
|---------|--------------|------------|----------|---------|
| **Lightsail** | $3.50-5 | ⭐⭐ Easy | Small bots | 99.9% |
| **EC2** | $5-15 | ⭐⭐⭐ Medium | Production | 99.95% |
| **Lambda** | $0-5 | ⭐⭐⭐⭐⭐ Hard | Event-driven | 99.95% |
| **Beanstalk** | $10-20 | ⭐⭐⭐ Medium | Auto-scaling | 99.95% |

## 🎯 Recommendation

**For your Discord bot: Start with AWS Lightsail**

### Why Lightsail?
- ✅ **Simple**: Easy setup, no complex configuration
- ✅ **Cheap**: Fixed $3.50/month pricing
- ✅ **Reliable**: AWS infrastructure
- ✅ **Perfect for bots**: Right amount of resources

### When to upgrade?
- **To EC2**: When you need more control or resources
- **To Lambda**: When you want serverless (requires code changes)
- **To Beanstalk**: When you need auto-scaling

---

## 🔧 AWS-Specific Tips

### Security
```bash
# Update security group to only allow your IP for SSH
# In EC2 console: Security Groups → Edit inbound rules
```

### Monitoring
```bash
# Install CloudWatch agent (optional)
sudo apt install amazon-cloudwatch-agent -y
```

### Backups
```bash
# Create snapshots of your instance
# In Lightsail/EC2 console: Create snapshot
```

### Cost Optimization
- **Use t3.micro** for small bots
- **Set up billing alerts**
- **Stop instances when not needed** (for testing)

---

## 🚀 Quick Start: Lightsail Deployment

```bash
# 1. Create Lightsail instance (Ubuntu 22.04, $3.50/month)
# 2. SSH into instance
# 3. Run these commands:

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/yourusername/your-repo.git
cd your-repo
pip3 install -r requirements.txt
nano .env  # Add DISCORD_TOKEN=your_token
python3 bot.py  # Test
# Use screen or systemd service for persistent running
```

**Your bot will be live on AWS in ~10 minutes!** 🎉 