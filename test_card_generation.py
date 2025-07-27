#!/usr/bin/env python3
"""
Test script for PNL card generation
This script allows you to test card generation without setting up Discord
"""

import os
import sys
from PIL import Image

# Add the current directory to Python path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from bot import PNLCard
    import config
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("💡 Make sure you have installed all dependencies with: pip install -r requirements.txt")
    sys.exit(1)

def generate_sample_cards():
    """Generate sample Solana PNL cards for testing"""
    
    # Get current SOL price (using synchronous request for testing)
    try:
        import requests
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd')
        if response.status_code == 200:
            sol_price = response.json()['solana']['usd']
        else:
            sol_price = 100.0  # Fallback price
    except:
        sol_price = 100.0  # Fallback price
    
    print(f"🚀 Using SOL price: ${sol_price:.2f}")
    
    # Sample trading data
    samples = [
        {
            'name': 'profit_example',
            'username': 'CryptoHawk',
            'coin_name': 'SOL',
            'bought_sol': 10.0,
            'sold_sol': 15.0,
            'holding_sol': 5.0,
            'description': 'Profitable SOL trade'
        },
        {
            'name': 'loss_example',
            'username': 'DiamondHands',
            'coin_name': 'SOL',
            'bought_sol': 20.0,
            'sold_sol': 12.0,
            'holding_sol': 8.0,
            'description': 'Loss-making SOL trade'
        },
        {
            'name': 'big_win',
            'username': 'MoonLambo',
            'coin_name': 'SOL',
            'bought_sol': 50.0,
            'sold_sol': 100.0,
            'holding_sol': 25.0,
            'description': 'Big SOL win'
        }
    ]
    
    print("🎨 Generating sample Solana PNL cards...")
    print("=" * 50)
    
    for i, sample in enumerate(samples, 1):
        try:
            print(f"({i}/{len(samples)}) Creating {sample['description']}...")
            
            # Create PNL card with custom background
            background_path = None
            if os.path.exists(config.BACKGROUNDS_FOLDER):
                for file in os.listdir(config.BACKGROUNDS_FOLDER):
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')) and not file.startswith('.'):
                        background_path = f"{config.BACKGROUNDS_FOLDER}/{file}"
                        break
            
            pnl_card = PNLCard(
                username=sample['username'],
                coin_name=sample['coin_name'],
                bought_sol=sample['bought_sol'],
                sold_sol=sample['sold_sol'],
                sol_price=sol_price,
                background_path=background_path
            )
            
            # Generate the card image
            card_image = pnl_card.generate_card()
            
            # Save to file
            filename = f"sample_{sample['name']}.png"
            with open(filename, 'wb') as f:
                f.write(card_image.getvalue())
            
            # Display trade info
            print(f"   👤 User: {sample['username']}")
            print(f"   📊 SOL: {sample['bought_sol']:.1f} bought → {sample['sold_sol']:.1f} sold → {sample['holding_sol']:.1f} holding")
            # Format SOL amount with K if >= 1000
            pnl_sol_abs = abs(pnl_card.pnl_sol)
            pnl_sol_formatted = f"{pnl_sol_abs/1000:.1f}K" if pnl_sol_abs >= 1000 else f"{pnl_sol_abs:.1f}"
            # Format USD amount with K if >= 1000
            pnl_usd_abs = abs(pnl_card.pnl_usd)
            pnl_usd_formatted = f"{pnl_usd_abs/1000:.1f}K" if pnl_usd_abs >= 1000 else f"{pnl_usd_abs:.2f}"
            print(f"   💰 P&L: {'+' if pnl_card.is_profit else '-'}{pnl_sol_formatted} SOL (${pnl_usd_formatted})")
            print(f"   💾 Saved as: {filename}")
            print()
            
        except Exception as e:
            print(f"   ❌ Error creating {sample['description']}: {e}")
            print()
    
    print("✅ Sample generation complete!")
    print(f"📁 Check the current directory for sample_*.png files")

def test_custom_card():
    """Allow user to create a custom Solana test card"""
    print("\n🎯 Create Your Own Solana Test Card")
    print("-" * 40)
    
    try:
        # Get current SOL price
        try:
            import requests
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd')
            if response.status_code == 200:
                sol_price = response.json()['solana']['usd']
            else:
                sol_price = 100.0
        except:
            sol_price = 100.0
        
        print(f"🚀 Current SOL price: ${sol_price:.2f}")
        
        username = input("👤 Enter username (e.g., CryptoMaster): ").strip()
        if not username:
            username = "TestTrader"
            
        coin_name = input("🪙 Enter coin name (e.g., SOL): ").strip()
        if not coin_name:
            coin_name = "SOL"
        
        bought_sol = input(f"💰 Enter {coin_name.upper()} bought (e.g., 50): ").strip()
        bought_sol = float(bought_sol) if bought_sol else 50.0
        
        sold_sol = input(f"💸 Enter {coin_name.upper()} sold (e.g., 60): ").strip()
        sold_sol = float(sold_sol) if sold_sol else 60.0
        
        
        print(f"\n🎨 Creating {username}'s {coin_name.upper()} PNL card...")
        
        # Create and generate card with custom background
        background_path = None
        if os.path.exists(config.BACKGROUNDS_FOLDER):
            for file in os.listdir(config.BACKGROUNDS_FOLDER):
                if file.lower().endswith(('.png', '.jpg', '.jpeg')) and not file.startswith('.'):
                    background_path = f"{config.BACKGROUNDS_FOLDER}/{file}"
                    break
        
        pnl_card = PNLCard(username, coin_name, bought_sol, sold_sol, sol_price, background_path)
        card_image = pnl_card.generate_card()
        
        # Save the card
        filename = f"custom_{username.lower()}_{coin_name.lower()}_pnl.png"
        with open(filename, 'wb') as f:
            f.write(card_image.getvalue())
        
        print(f"✅ Custom card created: {filename}")
        # Format SOL amount with K if >= 1000
        pnl_sol_abs = abs(pnl_card.pnl_sol)
        pnl_sol_formatted = f"{pnl_sol_abs/1000:.1f}K" if pnl_sol_abs >= 1000 else f"{pnl_sol_abs:.1f}"
        # Format USD amount with K if >= 1000
        pnl_usd_abs = abs(pnl_card.pnl_usd)
        pnl_usd_formatted = f"{pnl_usd_abs/1000:.1f}K" if pnl_usd_abs >= 1000 else f"{pnl_usd_abs:.2f}"
        print(f"📊 P&L: {'+' if pnl_card.is_profit else '-'}{pnl_sol_formatted} {coin_name.upper()} (${pnl_usd_formatted})")
        
    except ValueError:
        print("❌ Invalid input. Please use numbers for SOL amounts.")
    except KeyboardInterrupt:
        print("\n🛑 Cancelled by user")
    except Exception as e:
        print(f"❌ Error creating custom card: {e}")

def main():
    print("🚀 Custom PNL Card Generation Test")
    print("=" * 45)
    print("Generate cyberpunk-style trading reports with custom backgrounds!")
    
    while True:
        print("\nChoose an option:")
        print("1. Generate sample cards (3 examples)")
        print("2. Create custom test card")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            generate_sample_cards()
        elif choice == '2':
            test_custom_card()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main() 