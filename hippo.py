#!/usr/bin/python
#coding:utf8
'for my av'
__author__ = 'Hippo'

import random
import datetime
import urllib
import urllib2
import base64
import hashlib
import hmac
import time
import json


AccessKeyId_str = "xxxxxxxxxxxxxxxxx"
hmac_key = "xxxxxxxx&"
DomainName_str = "xxx.com"
RRKeyWord_str = "www"


def cx_dns():
        #public request value
        Format=['Format','JSON']
        Version=['Version','2015-01-09']
        AccessKeyId=['AccessKeyId',AccessKeyId_str]
        SignatureMethod=['SignatureMethod','HMAC-SHA1']
        Timestamp=['Timestamp',datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")]
        SignatureVersion=['SignatureVersion','1.0']
        SignatureNonce=['SignatureNonce','%014d' % random.randint(0,99999999999999)]


        Action=['Action','DescribeDomainRecords']
        DomainName=['DomainName',DomainName_str]

        RRKeyWord=['RRKeyWord',RRKeyWord_str]

        test=[]
        test.append(Action)
        test.append(AccessKeyId)
        test.append(DomainName)
        test.append(SignatureMethod)
        test.append(SignatureNonce)
        test.append(SignatureVersion)
        test.append(Timestamp)
        test.append(Version)
        test.append(Format)
        test.append(RRKeyWord)

        test.sort()

        url=''
        for name,value in test:
                if url == '': 
                        url = urllib.quote(name)+'='+urllib.quote(value)
                else:
                        url+='&'+urllib.quote(name)+'='+urllib.quote(value)

        qurl='GET&%2F&'+urllib.quote(url)

        afterbase=base64.b64encode(hmac.new(hmac_key,qurl,digestmod=hashlib.sha1).digest())
        q=urllib.quote(afterbase)

        sig=urllib.quote(afterbase).replace('/','%2F')

        url=''
        for name,value in test:
                if url == '': 
                        url = 'http://alidns.aliyuncs.com/?'+urllib.quote(name)+'='+urllib.quote(value)
                else:
                        url+='&'+urllib.quote(name)+'='+urllib.quote(value)

        url+='&'+urllib.quote('Signature')+'='+sig
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')]
        tnum=0
        while True:
                try:
                        html = opener.open(url).read()
                except :
                        tnum += 1
                        print r'retry %s ' % tnum
                        time.sleep(1)
                        if tnum > 3:
                                print r'read err %s ' % url
                                return "",""
                s=json.loads(html)
                return s['DomainRecords']['Record'][0]['RecordId'],s['DomainRecords']['Record'][0]['Value']


def xg_dns(rid,ip):
        #public request value
        Format=['Format','JSON']
        Version=['Version','2015-01-09']
        AccessKeyId=['AccessKeyId',AccessKeyId_str]
        SignatureMethod=['SignatureMethod','HMAC-SHA1']
        Timestamp=['Timestamp',datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")]
        SignatureVersion=['SignatureVersion','1.0']
        SignatureNonce=['SignatureNonce','%014d' % random.randint(0,99999999999999)]


        Action=['Action','UpdateDomainRecord']

        RecordId=['RecordId',rid]
        RR=['RR', RRKeyWord_str]
        Type=['Type','A']
        Value=['Value',ip]

        test=[]
        test.append(Action)
        test.append(AccessKeyId)
        test.append(SignatureMethod)
        test.append(SignatureNonce)
        test.append(SignatureVersion)
        test.append(Timestamp)
        test.append(Version)
        test.append(Format)


        test.append(RecordId)
        test.append(RR)
        test.append(Type)
        test.append(Value)


        test.sort()

        url=''
        for name,value in test:
                if url == '': 
                        url = urllib.quote(name)+'='+urllib.quote(value)
                else:
                        url+='&'+urllib.quote(name)+'='+urllib.quote(value)

        qurl='GET&%2F&'+urllib.quote(url)

        afterbase=base64.b64encode(hmac.new(hmac_key,qurl,digestmod=hashlib.sha1).digest())
        q=urllib.quote(afterbase)

        sig=urllib.quote(afterbase).replace('/','%2F')

        url=''
        for name,value in test:
                if url == '': 
                        url = 'http://alidns.aliyuncs.com/?'+urllib.quote(name)+'='+urllib.quote(value)
                else:
                        url+='&'+urllib.quote(name)+'='+urllib.quote(value)

        url+='&'+urllib.quote('Signature')+'='+sig
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')]
        while True:
                try:
                        html = opener.open(url).read()
                        return 0
                except :
                        tnum += 1
                        print r'retry %s ' % tnum
                        time.sleep(1)
                        if tnum > 3:
                                print r'read err %s ' % url
                                return -1
