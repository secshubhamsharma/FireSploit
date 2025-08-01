<h1 align="center">🔥 FireSploit 🔥</h1>
<p align="center"><i>A powerful Firebase misconfiguration scanner and exploitation tool for ethical hackers, developers, and security researchers.</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.6%2B-blue.svg" />
  <img src="https://img.shields.io/github/license/secshubhamsharma/FireSploit" />
  <img src="https://img.shields.io/github/stars/secshubhamsharma/FireSploit?style=social" />
  <img src="https://img.shields.io/github/forks/secshubhamsharma/FireSploit?style=social" />
</p>

---

## Table of Contents

- [About the Vulnerability](#about-the-vulnerability)
- [What FireSploit Does](#what-firesploit-does)
- [Installation](#installation)
- [Demo](#demo)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Best Practices](#best-practices)
- [Legal Disclaimer](#legal-disclaimer)
- [Contributing](#contributing)
- [Author](#author)
- [Support](#support)
- [License](#license)

---

## About the Vulnerability
Let me take you through a real problem that's been silently affection thousand of apps across the world, Firebase a super handy easy to implement backend service that lets your app store and sync data in real-time. 

The problem lies when you set security rules
```
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
This security rules means anyone on the internet can read, write and exfiltrate entire database without authentication 

In 2018, researchers at Appthority and various independent security analysts (including bug bounty hunters) discovered that over 28,000 Firebase apps were publicly exposing sensitive data due to incorrect security rules.


## What FireSploit Does
Scans a Firebase database endpoint for:
 - .read misconfiguration (public access)
 - .write misconfiguration (unauthorized data injection)

Exploits the database (optional):
 - Reads and prints live data
 - Injects a harmless payload to simulate attack

## Demo 
<img width="1261" alt="Screenshot 2025-07-06 at 11 53 48 PM" src="https://github.com/user-attachments/assets/3597d45e-175a-4fb8-9732-9b3f4219e9a2" />


## Installation
```
git clone https://github.com/secshubhamsharma/FireSploit.git
cd FireSploit
pip install -r requirements.txt
```

## Usage
```
# Scan a single Firebase instance
python3 firesploit.py --url https://yourproject.firebaseio.com

# Scan multiple targets from a file
python3 firesploit.py --file firebase_targets.txt

# Save results to a file
python3 firesploit.py --file firebase_targets.txt --output report.txt
```

If `.read` access is open: 
 - It Dumps publicly accessible data

If `.write` access is open: 
 - It offers to inject a safe payload
 ```
 {
  "pwned_by": "FireSploit",
  "status": "vulnerable",
  "timestamp": "2025-07-04"
}

 ```

 ## Project Structure 
```text
FireSploit/
├── firesploit.py          # Main scanner and exploit tool
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── LICENSE                # MIT License file
```

## Best Practices
To secure your Firebase Realtime Database and prevent exploitation by tools like FireSploit, follow these guidelines:

 -  Implement Proper Firebase Security Rules
  - Use strict .read and .write conditions:
 ```   {
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```

 
 -  Avoid Setting Rules to true

## Legal Disclaimer
> **_This project is intended for educational and authorized testing purposes only.  
> Unauthorized access to Firebase projects that you don’t own or control is illegal and unethical.  
> The creator of FireSploit is not responsible for misuse of this tool._**

## Contributing
Want to improve FireSploit? Contributions are welcome!

## Author
**Shubham Sharma**

 - [GitHub: @secshubhamsharma](https://github.com/secshubhamsharma)
 - [LinkedIn: @secshubhamsharma](https://linkedin.com/in/secshubhamsharma)
 - [Email: secshubhamsharma@gmail.com](mailto:secshubhamsharma@gmail.com)
 - [Medium: secshubhamsharma](https://medium.com/@secshubhamsharma)

## Support
If you found this tool helpful
Then ⭐ star the repo and share it with others in the infosec community!

## License
This project is licensed under the MIT License – see the LICENSE file for details.
