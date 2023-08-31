import urllib.request
def download_data():
  with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()