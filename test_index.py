#!/usr/bin/env python
import requests
import json
import sys

url = 'http://ripe.corp.vdms.io/data/processed/results-tbm-1046.json'
list_one = []

def get_prb(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            for item in data:
                if 'prb_id' in item:
                    list_one.append('PROBE ID :', item['prb_id'])
        except:
            pass

def get_rtt(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            for item in data:
                if 'result' in item and 'rt' in item['result']:
                    print'RTT :', item['result']['rt']

        except:
            pass

def get_asn(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            for item in data:
                if 'asn_v4' in item:
                    print'ASN :', item['asn_v4']
        except:
            pass

def get_src(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            for item in data:
                if 'from' in item:
                    print'SOURCE :', item['from']
        except:
            pass


print list_one
print get_src(url)
print get_asn(url)
print get_rtt(url)
