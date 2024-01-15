import psutil
import requests
import time

# Replace 'YOUR_API_KEY' with your actual AbuseIPDB API key
ABUSEIPDB_API_KEY = 'API_KEY'  # Replace with your AbuseIPDB API key
CHECK_INTERVAL = 5  # Refresh interval in seconds
THRESHOLD_CONFIDENCE = 0
THRESHOLD_REPORTS = 5

# Function to retrieve external IP addresses with active connections
def get_external_ips():
    external_ips = set()
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr and conn.raddr.ip:
            external_ips.add(conn.raddr.ip)
    return external_ips

# Function to query AbuseIPDB API for an IP address
def query_abuseipdb(ip):
    url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}'
    headers = {'Key': ABUSEIPDB_API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', None)
        if data:
            return {
                'IP': ip,
                'Confidence': data.get('abuseConfidenceScore', 0),
                'Reports': data.get('totalReports', 0),
                'ISP': data.get('isp', 'N/A'),
                'Domain': data.get('domainName', 'N/A'),
                'Country': data.get('countryCode', 'N/A')
            }
        else:
            return None
    else:
        print(f"Error querying AbuseIPDB for IP {ip}: {response.status_code}")
        return None

# Main function for continuous monitoring and checking
def main():
    while True:
        external_ips = get_external_ips()
        for ip in external_ips:
            ip_data = query_abuseipdb(ip)
            if ip_data:
                if (ip_data['Confidence'] >= THRESHOLD_CONFIDENCE or
                        ip_data['Reports'] >= THRESHOLD_REPORTS):
                    print(f"IP: {ip_data['IP']}, Confidence: {ip_data['Confidence']}, "
                          f"Reports: {ip_data['Reports']}, ISP: {ip_data['ISP']}, "
                          f"Domain: {ip_data['Domain']}, Country: {ip_data['Country']}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()