# Phishing Attacker Flooder

This Python script is designed to flood phishing attackers that create fake login websites with a large number of bogus email and password combinations.

## Purpose

The purpose of this script is to waste the time and resources of the attackers, who create fake login websites to steal users' login credentials. By flooding their servers with fake login credentials, we can slow down or even disrupt their operations by confusing them with fake data, making it harder for them to steal users' info.

## How it works

The script generates a large number of random email addresses and password combinations, and then sends them to the specified URL using HTTP POST requests. The requests are sent with a randomized user agent and, if specified, a proxy server to make the script more undetectable. The script can be run with or without flood mode enabled, which determines the wait time between requests to make it more or less aggressive.

## Prerequisites

* Python 3.x
* The ***'requests'*** module
* (Already included) A list of user agents to use
* (Optional) A list of proxies to use (Recommended when using ***'--flood'*** and in general :3)

## Usage

To use the script, simply run:

```bash
 # In Linux/Mac OS
 python flooder.py [OPTIONS] url
 
 # In Windows
 py flooder.py [OPTIONS] url
```

Replace url with the URL of the phishing website you want to flood. The following options are available:

* ***'-f'*** or ***'--flood'***: Enable flood mode, which makes the script more aggressive by disabling the wait time between requests.

* ***'-p'*** or ***'--proxy'***: Enable the use of proxies by specifying a list of proxies in proxies.txt.

* ***'-h'*** or ***'--help'***: Display help information.

## Disclaimer

* This script is intended for educational and testing purposes only. The use of this script for any malicious purpose is strictly prohibited. 

* I assume no responsibility for any damages or illegal actions resulting from the use of this script.
