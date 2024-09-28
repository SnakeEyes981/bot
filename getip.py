import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        public_ip = response.text
    except Exception as e:
        public_ip = "Unable to get IP address: " + str(e)
    
    return public_ip

if __name__ == "__main__":
    ip_address = get_public_ip()
    print(f"Public IP Address: {ip_address}")
