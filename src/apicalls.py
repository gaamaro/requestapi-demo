import requests

"""def getpayload():
    url = 'https://gabriielamaro-eval-prod.apigee.net/getintegration'

    r = requests.get(url)


def postpayload():
    url = 'https://gabriielamaro-eval-prod.apigee.net/postintegration'

    r = requests.post(url)


def getpublic():
    url = 'https://gabriielamaro-eval-prod.apigee.net/publicintegration'

    r = requests.get(url)


def getexternal():
    url = 'https://gabriielamaro-eval-prod.apigee.net/external-service'

    r = requests.get(url)"""

def getpayload():
    url = 'http://35.202.84.104:80/actors'

    r = requests.get(url)


def postpayload():
    url = 'http://35.202.84.104:80/films'

    r = requests.post(url)