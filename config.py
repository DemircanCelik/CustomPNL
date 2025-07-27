import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Discord Bot Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', '')

# Bot Settings
COMMAND_PREFIX = '!'
BOT_DESCRIPTION = "Custom PNL Card Generator Bot"

# Image Settings
DEFAULT_CARD_WIDTH = 1188
DEFAULT_CARD_HEIGHT = 668
BACKGROUNDS_FOLDER = 'backgrounds'

# Color Settings
COLORS = {
    'text': (255, 255, 255),      # White
    'profit': (0, 255, 0),        # Green
    'loss': (255, 0, 0),          # Red
    'background': (30, 60, 120),   # Ocean blue
    'frame': (101, 67, 33)        # Brown
}

# Font Settings
FONTS = {
    'primary_font': 'fonts/ShareTechMono-Regular.ttf',     # Main font file (can be path to custom font)
    'fallback_font': None,           # Use default if None
    'sizes': {
        'header': 20,                # "MPH >< FNF" header (if used)
        'label': 24,                 # "> COIN_NAME"
        'value': 24,                 # Main text (BOUGHT, SOLD, etc.)
        'small': 24,                 # USD values and subtitles
        'large': 24                  # PROFIT/LOSS text
    }
} 