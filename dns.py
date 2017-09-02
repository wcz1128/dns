#!/usr/bin/python
#coding:utf8

from flask import Flask, render_template, url_for, request,redirect,make_response,session,flash,abort
import hippo

app = Flask(__name__)
app.secret_key='this is test'

@app.route('/', methods=['GET'])
def index():
        newip = request.remote_addr
        rid,ip = hippo.cx_dns()
        print newip,rid,ip
        if newip != ip:
                hippo.xg_dns(rid,newip)
                return "set ok"
        return "same not set"

if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port=518,threaded=True)
