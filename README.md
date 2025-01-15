## Overload Spammer
**Overload Spammer** is a Discord bot designed to automate sending spam messages to a specific channel on Discord. With support for multiple bot tokens and a customizable messages, making your "raiding" slash "packing" faster, please also submit a pull request if you want to improve it.

---
## Features
- 🌐 **Multi-token support**: Use multiple Discord accounts by adding tokens to `tokens.txt`.
- ⏱ **Rate limit handling**: Automatically retries when Discord's rate limits are hit.
- 📝 **Customizable message**: Configure the message to spam.
- 📊 **Verbose mode**: Get detailed logs for each message sent.

---

## Requirements

- Python 3.7+  
- Dependencies can be installed with `pip` from the `requirements.txt`.

---

## Installation

1. Clone the repository:
```
   git clone git@github.com:darkkpy/overload.git
   cd overload
```

2. Install the required dependencies:

pip install -r requirements.txt


3. Create a tokens.txt file in the same directory and add your Discord bot tokens. Each token should be on a new line:

```
token1
token2
token3
```

## Usage

1. Run the script:

`python main.py`

2. Follow the prompts to:

`Enable verbose mode (y/n).`

Enter the channel ID where you want the bot to send messages.

Provide the message you want the bot to spam.

3. The bot will then begin sending the message to the specified channel using all tokens from tokens.txt.


## Example Output

```bash
┏━━━°⌜ 赤い糸 ⌟°━━━┓
  ___                      _                    _
 / _ \ __   __  ___  _ __ | |  ___    __ _   __| |
| | | |\ \ / / / _ \| '__|| | / _ \  / _` | / _` |
| |_| | \ V / |  __/| |   | || (_) || (_| || (_| |
 \___/   \_/   \___||_|   |_| \___/  \__,_| \__,_|

┗━━━°⌜ 赤い糸 ⌟°━━━┛
╔════•●•════╗
  [+] AUTO SPAMMER
  [+] Made By DarkkPy
╚════•●•════╝

 »--•--« Enable verbose mode (y/n): y
 »--•--« Enter the channel ID: 1329102050050445354
 »--•--« Enter the message to spam: Testing

[+] Account ODc4MTYyNT... is ready and will spam channel 1329102050050445354.
[+] Account ODc4MTYyNT sent: Testing
[+] Message sent by account ODc4MTYyNT.
[+] Account ODc4MTYyNT sent: Testing
[+] Message sent by account ODc4MTYyNT.
[+] Account ODc4MTYyNT sent: Testing
[+] Message sent by account ODc4MTYyNT.
[+] Account ODc4MTYyNT sent: Testing
[+] Message sent by account ODc4MTYyNT.
```

# Disclaimer

⚠️ Do not use this bot for malicious purposes.
Spamming on Discord is against Discord's Terms of Service and can result in your account(s) being banned.
Use responsibly and only with permission from the server owner(s).

# License

This project is licensed under the MIT License

Contact
Author: DarkkPy
GitHub: https://github.com/darkkpy
