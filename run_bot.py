#!/usr/bin/env python3
"""
Discord PNL Card Bot Runner
This script checks for dependencies and runs the bot
"""

import sys
import os
import subprocess

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'discord.py',
        'Pillow',
        'python-dotenv'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == 'discord.py':
                import discord
            elif package == 'Pillow':
                import PIL
            elif package == 'python-dotenv':
                import dotenv
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def check_env_file():
    """Check if .env file exists and has Discord token"""
    if not os.path.exists('.env'):
        return False, "No .env file found"
    
    try:
        with open('.env', 'r') as f:
            content = f.read()
            if 'DISCORD_TOKEN=' not in content:
                return False, ".env file doesn't contain DISCORD_TOKEN"
            if 'DISCORD_TOKEN=your_discord_bot_token_here' in content:
                return False, "Please replace placeholder token with your actual bot token"
            if 'DISCORD_TOKEN=' in content and content.split('DISCORD_TOKEN=')[1].strip() == '':
                return False, "DISCORD_TOKEN is empty in .env file"
    except Exception as e:
        return False, f"Error reading .env file: {e}"
    
    return True, "Environment file is valid"

def main():
    print("🏴‍☠️ Discord PNL Card Bot Launcher")
    print("=" * 40)
    
    # Check dependencies
    print("📦 Checking dependencies...")
    missing = check_dependencies()
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print("💡 Install them with: pip install -r requirements.txt")
        sys.exit(1)
    else:
        print("✅ All dependencies are installed")
    
    # Check environment file
    print("🔐 Checking environment configuration...")
    env_valid, env_message = check_env_file()
    if not env_valid:
        print(f"❌ {env_message}")
        print("💡 Create a .env file with your Discord bot token:")
        print("   DISCORD_TOKEN=your_actual_bot_token_here")
        sys.exit(1)
    else:
        print("✅ Environment configuration is valid")
    
    # Create backgrounds folder if it doesn't exist
    if not os.path.exists('backgrounds'):
        print("📁 Creating backgrounds folder...")
        os.makedirs('backgrounds')
        print("✅ Backgrounds folder created")
    
    print("\n🚀 Starting Discord PNL Card Bot...")
    print("Press Ctrl+C to stop the bot")
    print("-" * 40)
    
    try:
        # Import and run the bot
        import bot
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Error running bot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 