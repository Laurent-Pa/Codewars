import re
"""On importe la library pour gérer les Regex"""
def domain_name(url):
     # Enlever le protocole (http:// ou https:// ou www.)
    pattern = r'^(?:https?://)?(?:www\.)?([^./]+)'
    match = re.match(pattern, url)

    if match:
        return match.group(1)
    return None


url = "http://google.com"
print(domain_name(url))
url = "https://123.net"
print(domain_name(url))
url = "www.xakep.ru"
print(domain_name(url))
url = "icann.org"
print(domain_name(url))

# Solution sans utiliser de Regex
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
