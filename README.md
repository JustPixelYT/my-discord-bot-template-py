# Discord.py Bot Template

A production-ready Discord bot template with essential moderation commands and extensible architecture. Get your bot running in under 5 minutes.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![discord.py Version](https://img.shields.io/badge/discord.py-2.3%2B-purple)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

## ✨ Features

- **Ready-to-use commands** — Ping, help, kick, and ban commands out of the box
- **Easy configuration** — Environment-based setup with `.env` file
- **Extensible architecture** — Clean code structure ready for custom commands
- **Permission handling** — Built-in permission level checks for moderation commands
- **Error handling** — Graceful error messages for common failures

## 📋 Prerequisites

- Python 3.8 or higher
- Discord Developer account
- Bot token from Discord Developer Portal
- Basic familiarity with terminal/command line

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/JustPixelYT/my-discord-bot-template-py.git
cd my-discord-bot-template-py

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your bot token

# Run the bot
python bot.py
```

## 📦 Installation

### 1. Clone or Fork

```bash
git clone https://github.com/JustPixelYT/my-discord-bot-template-py.git
cd my-discord-bot-template-py
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
DISCORD_TOKEN=your_bot_token_here
BOT_PREFIX=!
```

> ⚠️ **Security Warning**: Never commit your `.env` file to version control. Add it to `.gitignore` immediately. Your bot token provides full access to your bot — treat it like a password.

## 🛠️ Usage

Start the bot:

```bash
python bot.py
```

On successful startup, you'll see:
```
Bot is ready!
Logged in as: YourBotName#1234
Bot ID: 123456789012345678
```

## 📖 Command Reference

| Command | Description | Permission Level | Example Usage |
|---------|-------------|------------------|---------------|
| `ping` | Check bot latency and response | Everyone | `!ping` |
| `help` | Display available commands | Everyone | `!help` |
| `kick` | Remove a member from the server | Moderator | `!kick @user reason` |
| `ban` | Ban a member from the server | Administrator | `!ban @user reason` |

## 🔧 Discord Developer Portal Setup

### 1. Create a Discord Application

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Enter your bot's name and click "Create"

### 2. Create a Bot User

1. Navigate to "Bot" in the left sidebar
2. Click "Add Bot" → "Yes, do it!"
3. Under "Token", click "Reset Token" to reveal your bot token
4. **Copy this token** and paste it in your `.env` file

### 3. Configure Bot Permissions

1. Still in the "Bot" section, scroll to "Privileged Gateway Intents"
2. Enable required intents (typically: Server Members Intent, Message Content Intent)
3. Under "Permissions", set:
   - Kick Members
   - Ban Members
   - Send Messages
   - Embed Links

### 4. Invite Bot to Your Server

1. Go to "OAuth2" → "URL Generator"
2. Select scopes: `bot`, `applications.commands`
3. Select permissions from step 3
4. Copy the generated URL and open it in your browser
5. Select your server and authorize

## 📁 Project Structure

```
my-discord-bot-template-py/
├── .env                  # Environment variables (DO NOT COMMIT)
├── .env.example          # Template for .env
├── .gitignore            # Git ignore rules
├── bot.py                # Main bot entry point
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── cogs/                 # Extend with custom commands
    └── README.md         # Instructions for adding cogs
```

## 🤝 Contributing

Contributions are welcome! Please follow the standard GitHub flow:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Code Style Expectations:**
- Follow PEP 8 guidelines
- Add docstrings to new functions
- Test commands before submitting
- Keep PRs focused and concise

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Acknowledgments

- **[discord.py Documentation](https://discordpy.readthedocs.io/)** — Official library docs
- **[Issue Tracker](https://github.com/JustPixelYT/my-discord-bot-template-py/issues)** — Report bugs or request features
- **[Discord Developer Docs](https://discord.com/developers/docs/intro)** — Discord API reference

**Author:** JustPixelYT

Built with ❤️ using [discord.py](https://github.com/Rapptz/discord.py)