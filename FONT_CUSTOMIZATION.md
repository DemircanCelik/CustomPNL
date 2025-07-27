# 🎨 Font Customization Guide

This guide shows you how to customize fonts and text sizes in your PNL cards.

## 📝 **Current Font Settings**

All font settings are in `config.py`. Here's what each font controls:

| Font Type | Usage | Default Size |
|-----------|-------|--------------|
| `header` | "MPH >< FNF" at top | 20px |
| `label` | "> COIN_NAME" | 18px |
| `value` | Main text (BOUGHT, SOLD, etc.) | 24px |
| `small` | USD values and subtitles | 16px |
| `large` | PROFIT/LOSS text | 28px |

## 🔧 **How to Customize**

### 1. Change Font Sizes

Edit the `sizes` section in `config.py`:

```python
'sizes': {
    'header': 25,     # Bigger header
    'label': 20,      # Bigger coin name
    'value': 22,      # Smaller main text
    'small': 14,      # Smaller USD values
    'large': 32       # Bigger profit/loss
}
```

### 2. Change Font Family

Replace `'arial.ttf'` with your custom font:

```python
'primary_font': 'fonts/MyCustomFont.ttf',
```

### 3. Use System Fonts

For Windows system fonts:
```python
'primary_font': 'C:/Windows/Fonts/calibri.ttf',    # Calibri
'primary_font': 'C:/Windows/Fonts/consola.ttf',    # Consolas (monospace)
'primary_font': 'C:/Windows/Fonts/georgia.ttf',    # Georgia
```

## 📁 **Adding Custom Fonts**

1. **Create fonts folder**: Make a `fonts/` directory in your project
2. **Add font files**: Place `.ttf` files in the fonts folder
3. **Update config**: Set the path in `config.py`

Example structure:
```
CustomPNL/
├── fonts/
│   ├── CyberpunkFont.ttf
│   ├── FutureFont.ttf
│   └── SciFiFont.ttf
├── config.py
└── bot.py
```

Then in `config.py`:
```python
'primary_font': 'fonts/CyberpunkFont.ttf',
```

## 🎭 **Font Style Examples**

### Cyberpunk Style
```python
FONTS = {
    'primary_font': 'fonts/orbitron.ttf',  # Futuristic font
    'sizes': {
        'header': 22,
        'label': 20,
        'value': 26,
        'small': 14,
        'large': 32
    }
}
```

### Clean Modern Style  
```python
FONTS = {
    'primary_font': 'C:/Windows/Fonts/segoeui.ttf',  # Segoe UI
    'sizes': {
        'header': 18,
        'label': 16,
        'value': 22,
        'small': 14,
        'large': 28
    }
}
```

### Monospace/Terminal Style
```python
FONTS = {
    'primary_font': 'C:/Windows/Fonts/consola.ttf',  # Consolas
    'sizes': {
        'header': 20,
        'label': 18,
        'value': 24,
        'small': 16,
        'large': 30
    }
}
```

## 🔍 **Finding Font Files**

### Windows
Common font locations:
- `C:/Windows/Fonts/`
- `C:/Users/[Username]/AppData/Local/Microsoft/Windows/Fonts/`

### Popular Font Websites
- **Google Fonts**: https://fonts.google.com/
- **DaFont**: https://www.dafont.com/
- **Font Squirrel**: https://www.fontsquirrel.com/

## ⚠️ **Important Notes**

1. **Font Format**: Use `.ttf` files for best compatibility
2. **File Paths**: Use forward slashes `/` even on Windows
3. **Font Size**: Larger sizes may cause text overflow
4. **Testing**: Use `python test_card_generation.py` to test changes
5. **Fallback**: If custom font fails, system default is used

## 🧪 **Testing Your Changes**

After modifying `config.py`:

1. **Test generation**:
   ```bash
   python test_card_generation.py
   ```

2. **Check the output**: Look at generated cards to see font changes

3. **Adjust as needed**: Fine-tune sizes for best appearance

## 🎨 **Advanced Customization**

### Different Fonts for Different Elements

If you want different fonts for different text elements, you can modify the `bot.py` code directly:

```python
# In generate_card method
try:
    header_font = ImageFont.truetype("fonts/HeaderFont.ttf", 20)
    label_font = ImageFont.truetype("fonts/LabelFont.ttf", 18)
    value_font = ImageFont.truetype("fonts/ValueFont.ttf", 24)
    small_font = ImageFont.truetype("fonts/SmallFont.ttf", 16)
    large_font = ImageFont.truetype("fonts/LargeFont.ttf", 28)
except:
    # Fallback...
```

---

**💡 Tip**: Start with small size adjustments (±2-4px) to see how they affect the layout! 