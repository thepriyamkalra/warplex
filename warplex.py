import argparse
import json
import random
import time
from datetime import datetime
from string import ascii_letters, digits
from typing import Iterable
from urllib import error, request

__all__ = ["sendRequest"]


def getArguments() -> argparse.Namespace:
    """Get all the command-line argument

    Returns:
        argparse.Namespace: A container for all the command-line arguments
    """
    parser = argparse.ArgumentParser(description='Extend your WARP+ quota by X amount.')
    parser.add_argument(
        "id",
        type=str,
        help="Your Cloudflare WARP+ ID"
    )
    parser.add_argument(
        "amount",
        type=int,
        nargs="?",
        default=1000,
        help="[Default = 1000] The amount of requests to be made (1request = 1GB)"
    )
    return parser.parse_args()

def toString(s: Iterable[str]) -> str:
    """Converts an iterable of strings into a single string

    Args:
        s (Iterable[str]): The iterable of strings
        
    Returns:
        str: The merged string
    """
    return "".join(s)

def matchFormat(n: int, source: int) -> str:
    """Matches the format of two integers and returns it as a string
    Example: 1 and 100 -> '001'

    Args:
        n (int): The integer to be matched
        source (int): The integer to match from

    Returns:
        str: The matched integer as a string
    """
    nstr: str = str(n)
    return "0" * (len(str(source)) - len(nstr)) + nstr

def randSeq(length: int, src: str) -> str:
    """Generates a random sequence of charecters of
    a given length, choosing them from a given
    source string

    Args:
        length (int): The length of the random string
        src (str): The source string to pick random characters from

    Returns:
        str: The string of random charecters
    """
    return toString(random.choice(src) for _ in range(length))

def randString(length: int) -> str:
    """Generates a random string containing letters and numbers

    Args:
        length (int): The length of the random string

    Returns:
        str: The random string
    """
    return randSeq(length, ascii_letters + digits)

def randDigits(length: int) -> str:
    """Generates a random string containing numbers

    Args:
        length (int): The length of the random string

    Returns:
        str: The random string
    """
    return randSeq(length, digits)

def sendRequest(id:str, endpoint: str = f"https://api.cloudflareclient.com/v0a{randDigits(3)}/reg") -> int:
    """Send a post request to the endpoint using your id as the referrer,
    Effectively adding 1GB to your Cloudflare WARP+ Quota.

    Args:
        endpoint (str): The API endpoint you wish to send the request to
        id (str): Your cloudflare WARP+ ID to be included as the referrer

    Returns:
        int: The response code from the server
    """
    installId: str = randString(22)
    postBody: str = json.dumps({
        "key": randString(43) + "=",
        "install_id": installId,
        "fcm_token": f"{installId}:APA91b{randString(134)}",
        "referrer": id,
        "warp_enabled": False,
        "tos": datetime.now().isoformat()[:-3] + "+02:00",
        "type": "Android",
        "locale": "es_ES",
    })
    headers: dict[str, str] = {
        "Content-Type": "application/json; charset=UTF-8",
        "Host": "api.cloudflareclient.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.1"
    }
    req = request.Request(endpoint, postBody.encode("utf-8"), headers)
    return request.urlopen(req).getcode()

def main() -> None:
    """Handles the execution of the command line tool"""
    arguments: argparse.Namespace = getArguments()
    amount: int = arguments.amount
    progress: int = -1

    print(f"\nAdding {amount} GB to your WARP+ Quota, Grab a coffee.")
    while amount != progress:
        try: response = sendRequest(arguments.id)
        except error.HTTPError: response = time.sleep(18) # None
        except error.URLError: exit("\nCouldn't send request. Check your network connection.")
        if response == 200:
            # Infinite loop if the response is never 200
            # But I am going to keep this anyways XD
            progress += 1
        print(end=f"\rProgress: {100 * progress // amount}%, ETA: {matchFormat(18 * (amount - progress), 18 * amount)} seconds")

    print("\n\nAll done.")

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: exit("\n[KeyboardInterrupt]")
