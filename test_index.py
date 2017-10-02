#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
import os, gzip, json
import os.path



root = '/Users/nimoore/'
dirs=['results-tbm-1046.json']
data={}

def test_index(dirs):
    for f in dirs:
        filePath = root + f
        print filePath
        if f.startswith('results-tbm'):
            with open(filePath, "r") as myfile:
                for line in myfile:
                    js = json.loads(line)
                    for i in js:
                        if 'prb_id' in i and 'result' in i and 'answers' in i['result'].keys():
                            data={}
                            data['prb_id'] = i['prb_id']
                            data['timestamp']=i['timestamp']
                            data['asn']=i['asn_v4']
                            data['pop']=dict(zip(i['result']['answers'][0].keys(), i['result']['answers'][0].values()))['RDATA'][0]
                            data['rt']=i['result']['rt']
                            with open('/Users/nimoore/data.json', 'a') as outfile:
                                json.dump(data, outfile)
                                outfile.write("\n")
    return
