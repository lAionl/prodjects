#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Модуль для авторизации в vk.com
Для устранения необходимости каждый раз вручную
получать token & id
"""

import urllib
import http.cookiejar
import urllib.request
from urllib.parse import urlparse
from urllib.parse import urlencode
from html.parser import HTMLParser
from _pytest.pastebin import url


class FromParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.url = None
        self.params = {}
        self.in_form = False
        self.form_parsed = False
        self.method = "GET"

    def handle_starttag(self, tag, attrs):
        if tag == "form":
            if self.form_parsed:
                raise RuntimeError("second form on page")
            if self.in_form:
                raise RuntimeError("already in form")
            self.in_form = True
        if not self.in_form:
            return
        attrs = dict((name, value) for name, value in attrs)
        if tag == "form":
            self.url = attrs["action"]
            if "method" in attrs:
                self.method = attrs["method"]
        elif tag == "input" and "type" in attrs and "name" in attrs:
            if attrs["type"] in ["hidden", "text", "password"]:
                self.params[attrs["name"]] = attrs["value"] if "value" in attrs else ""

    def handle_endtag(self, tag):
        if tag == "form":
            if not self.in_form:
                raise RuntimeError("unexpected end of <form>")
            self.in_form = False
            self.form_parsed = True

client_id = "4932709"
scope = "audio"
email = "89228129755"
password = "N8hm5o3e"

opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()),
    urllib.request.HTTPRedirectHandler())

response = opener.open(
    "http://oauth.vk.com/oauth/authorize?" + \
    "redirect_url=http://oauth.vk.com/blank.html&response_type=token&" + \
    "client_id=%s&scope=%s&display=wap" % (client_id, ",".join(scope)))

doc = response.read()
parser = FromParser()
parser.feed(doc.decode("utf-8"))
parser.close()
if not parser.form_parsed or parser.url is None or "pass" not in parser.params or "email" not in parser.params:
    raise RuntimeError("something wrong")
parser.params["email"] = email
parser.params["pass"] = password
post = urllib.parse.urlencode(parser.params)
if parser.method == "post":
    response = opener.open(parser.url, post)
else:
    raise NotImplementedError("method '$s'" % parser.method)
doc = response.read()
print(doc)
