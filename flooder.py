import sys
import requests
import os
import random
import string
import time

chars = string.ascii_letters + string.digits + '^%$!()'
random.seed = (os.urandom(1024))

def print_help():
    print("Usage: python script.py [OPTIONS] URL\n")
    print("Options:")
    print("  -h, --help\t\tShow this help message")
    print("  -f, --flood\t\tEnable flood mode (no delay between requests)")
    print("  -p, --proxy\t\tEnable use of proxies from proxies.txt file")
    print("Examples:")
    print("python script.py -f https://exampleurl.com")
    print("python script.py -p https://exampleurl.com")
    print("python script.py -f -p https://exampleurl.com")


# Check if URL argument is provided
if len(sys.argv) < 2:
    print("Error: No URL provided.")
    print_help()
    sys.exit()

# Set URL argument
url = sys.argv[1]

# Load user agents from a file
with open('user_agents.txt', 'r') as f:
    user_agents = [line.strip() for line in f]
# Add a check just in case of the user modifying the user_agents.txt file
if not user_agents:
    print("Error: User Agents file is empty")
    sys.exit(1)

# Predefined list of email domains
domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "outlook.com", "protonmail.com"]

# Function to generate random names
def generate_name():
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    return "".join(random.choice(consonants) + random.choice(vowels) for i in range(random.randint(3, 8))) + str(random.randint(3,99))

# Function to generate a random email address
def generate_email():
    name = generate_name()
    domain = random.choice(domains)
    return name + "@" + domain

flood_enabled = '-f' in sys.argv or '--flood' in sys.argv

proxies_enabled = '-p' in sys.argv or '--proxy' in sys.argv

if proxies_enabled:
    # Load proxies from a file
    with open('proxies.txt', 'r') as f:
        proxies = [line.strip() for line in f]
if not proxies:
    print("Error: Proxies file is empty")
    sys.exit(1)

try:
    uwu = 0
    while True:
        email = generate_email()
        pass_boi = ''.join(random.choice(chars) for i in range(random.randint(3, 11)))

        # Select a random user agent and proxy from the lists
        user_agent = random.choice(user_agents)
        if proxies_enabled:
            proxy = random.choice(proxies)

            # Parse the proxy URL to extract the protocol, host and port
            parts = proxy.split(':')
            protocol = parts[0]
            host = parts[1][2:] if protocol == 'socks4' else parts[1][2:-1]
            port = int(parts[-1])

            # Set up a session with the user agent and proxy
            session = requests.Session()
            session.headers = {'User-Agent': user_agent}
            session.proxies = {
                protocol: '{}://{}:{}'.format(protocol, host, port)
            }
        else:
            session = requests.Session()
            session.headers = {'User-Agent': user_agent}

        # Send the request with the session
        try:
            response = session.post(url, allow_redirects=False, data={
                'email': email,
                'password': pass_boi
            })

            if response.status_code == 404:
                print("Error 404: Page not found. {}".format("Proxy: " + proxy if proxies_enabled else ""))
            elif response.status_code == 403:
                print("Error 403: Access forbidden. {}".format("Proxy: " + proxy if proxies_enabled else ""))
            elif response.status_code != 200:
                print("Error {}: {}".format(response.status_code, response.reason))
            else:
                print(("username: {0} password: {1} email: {2} user agent: {3}, status_code: {4}").format(email, pass_boi, proxy if proxies_enabled else "N/A", user_agent, response.status_code))
                uwu+=1
        except requests.exceptions.RequestException as e:
                print("Error: {}".format(str(e)))

        # Wait a random amount of time before sending the next request to make the script more undetectable if enabled
        if flood_enabled == False:
            time.sleep(random.uniform(0.5, 2.0))

except KeyboardInterrupt:
    print("Number of Request Sent: " + str(uwu))
