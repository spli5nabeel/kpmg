import requests
import json

url = 'http://169.254.169.254/latest/'
endpoint = ["meta-data/"]


def prepareMetaData(endpoint,url):
    result = {}
    for ep in endpoint:
        next_url = url + ep
        res = requests.get(next_url)
        val = res.text
        if ep[-1] == '/':
            values = res.text.splitlines()
            result[ep[:-1]] = prepareMetaData(values,next_url)
        result[ep] = val
    return result

print(url)
print(endpoint)
prepareMetaData(endpoint, url)