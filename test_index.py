#!/usr/bin/env python
import requests
import json
import sys
from log_parser import time_helper
from log_parser import parse_helper
t = time_helper.time_helper()
p = parse_helper.parse_helper()

url = 'http://ripe.corp.vdms.io/data/processed/results-tbm-1046.json'

class store:
    def __init__(self):
        self.data = {}

    def add_the_things(self, dns_server,  rtt, asn, probeID, timestamp):
        print rtt
        self.data[‘asn’] = asn
        self.data[‘dns_server’] = dns_server
        self.data[‘rtt’] = rtt
        self.data[‘probeID’] = probeID
        self.data[‘timestamp’] = t.to_sdi(timestamp)
        p.write_json(‘file’, self.data)

    def return_data():
        return self.data

s = store()

if __name__ == ‘__main__‘:


    def get_the_things(url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            try:
                for item in data:
                    timestamp = item.get(‘timestamp’, 0)
                    probeID = item.get(‘prb_id’)
                    asn = item.get(‘asn_v4’)
                    _d = item.get(‘result’)
                    rtt = _d.get(‘rt’)
                    answers = _d.get(‘answers’)
                    for _x in answers:
                        dns_server = _x.get(‘RDATA’)
                    #print dns_server, rtt, asn, probeID, timestamp
                    s.add_the_things(dns_server, rtt, asn, probeID, timestamp)
            except:
                pass
    get_the_things(url)

    s.return_data
