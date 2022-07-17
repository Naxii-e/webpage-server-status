#
#   Copyright (c) 2021 Naxii
#   This code is released under the MIT License, see LICENSE.
#

from flask import Flask, render_template, jsonify
import requests, datetime

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config["JSON_SORT_KEYS"] = False

# add your website
hosts = [
    "https://example.com/",
    "https://exempla.com/",
    "https://google.com/",
    "https://amazon.co.jp/",
    "https://yahoo.co.jp/",
    "https://github.com/"
    "https://z0xp.net/",
    "https://z0xp.dev/"

]

# add a display name for your website
displayname = [
    "[Example]",
    "[Error Example]",
    "Google",
    "Amazon",
    "Yahoo",
    "GitHub"
    "z0xp.net",
    "z0xp.dev"
]

def alert(msg):
    print(f"[INFO] {msg}")

@app.route("/") 
def index():
    result = []
    dt_now = datetime.datetime.now()
    for (resp, dn) in zip(hosts, displayname):
        try:
            requests.get(resp, timeout=1.5)
            
        except requests.exceptions.ConnectTimeout:
            result.append({'host': resp, 'dn': dn, 'res': 'timeouterror'})
            alert(f"{resp} はタイムアウトしています。")
        except requests.exceptions.SSLError:
            result.append({'host': resp, 'dn': dn, 'res': 'sslerror'})
            alert(f"{resp} はSSL/TLSエラーを起こしています。")
        except requests.exceptions.ConnectionError:
            result.append({'host': resp, 'dn': dn, 'res': 'connectionerror'})
            alert(f"{resp} は接続できません。")
        except requests.exceptions.TooManyRedirects:
            result.append({'host': resp, 'dn': dn, 'res': 'toomanyredirectserror'})
            alert(f"{resp} はリダイレクトエラーを起こしています。")
        else:
            result.append({'host': resp, 'dn': dn, 'res': 'ok'})
            alert(f"{resp} は正常です。")
    return render_template("index.html", title="Status", result=result, time=dt_now.strftime('%Y.%m.%d %H:%M:%S'))


@app.route("/api")
def api():
    result = []
    dt_now = datetime.datetime.now()
    for (resp, dn) in zip(hosts, displayname):
        try:
            requests.get(resp, timeout=1.5)
        except requests.exceptions.ConnectTimeout:
            result.append({'host': resp, 'dn': dn, 'res': 'timeouterror'})
        except requests.exceptions.SSLError:
            result.append({'host': resp, 'dn': dn, 'res': 'sslerror'})
        except requests.exceptions.ConnectionError:
            result.append({'host': resp, 'dn': dn, 'res': 'connectionerror'})
        except requests.exceptions.TooManyRedirects:
            result.append({'host': resp, 'dn': dn, 'res': 'toomanyredirectserror'})
        else:
            result.append({'host': resp, 'dn': dn, 'res': 'ok'})
    data = [
        result
    ]
    return jsonify({
        'api': 'ok',
        'time': dt_now,
        'data': data
    })


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == "__main__":
    app.run(debug=True, port=5000,host="0.0.0.0")
