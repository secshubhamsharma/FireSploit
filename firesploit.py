#!/usr/bin/env python3

"""
FireSploit - Firebase Public Access Scanner

Author: Shubham Sharma
GitHub: https://github.com/yourusername/FireSploit
"""

import requests
import argparse
import json


def check_public_read(database_url: str) -> bool:
    test_url = f"{database_url}/.json"
    print(f"\n[+] Checking public read access: {test_url}")

    try:
        response = requests.get(test_url, timeout=5)
        if response.status_code == 200 and response.json():
            print("[!] Public read access detected.")
            preview = json.dumps(response.json(), indent=2)
            print("[*] Sample response:")
            print(preview[:500] + "...\n")
            return True
        else:
            print("[✓] No public read access.")
            return False
    except requests.exceptions.RequestException as error:
        print(f"[x] Connection error: {error}")
        return False


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="FireSploit - Firebase public access vulnerability scanner"
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Firebase DB URL (e.g., https://yourapp.firebaseio.com)"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    target_url = args.url.rstrip("/")
    print("  FireSploit Scanner v1.0")
    check_public_read(target_url)


if __name__ == "__main__":
    main()
