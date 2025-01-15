import os
import logging
import colorama
from colorama import Fore, Style
import art 
import discord
import asyncio
from multiprocessing import Process
from tenacity import retry, stop_after_attempt, wait_exponential
import signal
import sys

colorama.init(autoreset=True)

def signal_handler(sig, frame):
    print(f"{Style.BRIGHT}{Fore.RED}[-] Bot terminated by user.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def DarkkPy():
    darkkpy = art.text2art("Overload")
    print(f"┏━━━°⌜ 赤い糸 ⌟°━━━┓")
    print(f"{Style.BRIGHT}{Fore.RED}{darkkpy}")
    print(f"┗━━━°⌜ 赤い糸 ⌟°━━━┛")
    print(Style.BRIGHT + "╔════•●•════╗")
    print(f"{Style.BRIGHT}{Fore.GREEN}  [+] AUTO SPAMMER")
    print(f"{Style.BRIGHT}{Fore.CYAN}  [+] Made By DarkkPy")
    print(Style.BRIGHT + "╚════•●•════╝")

def getToken(file_path):
    try:
        with open(file_path, "r") as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
        return tokens
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}[-] Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}[-] Error reading tokens from file: {e}")
        return []

@retry(stop=stop_after_attempt(5), wait=wait_exponential(min=1, max=10))
async def send_message(target_channel, message, token):
    await target_channel.send(message)
    print(f"{Style.BRIGHT}{Fore.CYAN}[+] Account {token[:10]} sent: {message}")

def run_bot(token, channel_id, message, verbose):
    class SpamBot(discord.Client):
        async def on_ready(self):
            print(f"\n{Style.BRIGHT}{Fore.GREEN}[+] Account {token[:10]}... is ready and will spam channel {channel_id}.")
            target_channel = self.get_channel(channel_id)
            if not target_channel:
                print(f"{Style.BRIGHT}{Fore.YELLOW}[-] Account {token[:10]} cannot find the channel {channel_id} or has no access.")
                await self.close()
                return

            while True:
                try:
                    await send_message(target_channel, message, token)

                    if verbose == 'y':
                        print(f"{Style.BRIGHT}{Fore.YELLOW}[+] Message sent by account {token[:10]}.")

                    await asyncio.sleep(0.05)

                except discord.errors.HTTPException as e:
                    if e.status == 429:
                        retry_after = e.retry_after if hasattr(e, 'retry_after') else 2
                        print(f"{Style.BRIGHT}{Fore.RED}[-] Account {token[:10]} is rate limited. Retrying after {retry_after} seconds.")
                        await asyncio.sleep(retry_after)

                except discord.errors.Forbidden:
                    print(f"{Style.BRIGHT}{Fore.YELLOW}[-] Account {token[:10]} does not have permission to send messages to the channel.")
                    break

                except discord.errors.NotFound:
                    print(f"{Style.BRIGHT}{Fore.RED}[-] Channel {channel_id} not found or account {token[:10]} was removed.")
                    break

                except discord.errors.LoginFailure:
                    print(f"{Style.BRIGHT}{Fore.RED}[-] Invalid token for account {token[:10]}.")
                    break

                except Exception as e:
                    print(f"{Style.BRIGHT}{Fore.RED}[-] Unexpected error for account {token[:10]}: {e}")
                    break

        async def on_disconnect(self):
            print(f"{Style.BRIGHT}{Fore.YELLOW}[-] Account {token[:10]} has been disconnected.")

    bot = SpamBot()
    try:
        bot.run(token, bot=False)
    except discord.errors.LoginFailure:
        print(f"{Style.BRIGHT}{Fore.RED}[-] Account {token[:10]} failed to log in due to invalid token.")
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}[-] Unexpected error for account {token[:10]} during startup: {e}")


if __name__ == "__main__":
    DarkkPy()

    while True:
        verbose = input(f"{Style.BRIGHT}{Fore.CYAN} »--•--« Enable verbose mode (y/n): ").strip().lower()
        if verbose in ['y', 'n']:
            break
        else:
            print(f"{Style.BRIGHT}{Fore.RED}[-] Invalid input. Please enter 'y' for yes or 'n' for no.")

    while True:
        try:
            channel_id = int(input(f"{Style.BRIGHT}{Fore.CYAN} »--•--« Enter the channel ID: "))
            break
        except ValueError:
            print(f"{Style.BRIGHT}{Fore.RED}[-] Invalid channel ID. Please enter a numeric value.")

    message = input(f"{Style.BRIGHT}{Fore.CYAN} »--•--« Enter the message to spam: ")
    
    token_file = "tokens.txt"
    tokens = getToken(token_file)

    if not tokens:
        print(f"{Style.BRIGHT}{Fore.RED}[-] No valid tokens found. Exiting.")
    else:
        processes = []
        for token in tokens:
            p = Process(target=run_bot, args=(token, channel_id, message, verbose))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()
