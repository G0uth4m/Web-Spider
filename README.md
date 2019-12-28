# Web-Spider
A simple web spider built using python3 to get a sitemap of the whole website.

## Installation
```
$ pip3 install -r requirements.txt
```

## Usage
```
$ python3 spider.py -h
usage: spider.py [-h] [-w URL] [-u USER_AGENT] [-p PROXY] [-c COOKIE]

optional arguments:
  -h, --help            show this help message and exit
  -w URL, --website-url URL
                        URL
  -u USER_AGENT, --user-agent USER_AGENT
                        User Agent to use(default=Python requests)
  -p PROXY, --proxy PROXY
                        Format : protocol://IP:port
  -c COOKIE, --cookie COOKIE
                        Cookies to use
```

## Example
```
$ python3 spider.py -w http://172.28.128.12/dvwa/ --cookie "security=high; PHPSESSID=6ba16e5b2d11d602384bb50f36b91c5c"
http://172.28.128.12/dvwa/dvwa/css/main.css
http://172.28.128.12/dvwa/favicon.ico
http://172.28.128.12/dvwa/
http://172.28.128.12/dvwa/instructions.php
http://172.28.128.12/dvwa/instructions.php?doc=readme
http://172.28.128.12/dvwa/instructions.php?doc=changelog
http://172.28.128.12/dvwa/instructions.php?doc=copying
http://172.28.128.12/dvwa/instructions.php?doc=PHPIDS-license
http://172.28.128.12/dvwa/setup.php
http://172.28.128.12/dvwa/vulnerabilities/brute/
http://172.28.128.12/dvwa/vulnerabilities/exec/
http://172.28.128.12/dvwa/vulnerabilities/csrf/
http://172.28.128.12/dvwa/vulnerabilities/fi/?page=include.php
http://172.28.128.12/dvwa/vulnerabilities/sqli/
http://172.28.128.12/dvwa/vulnerabilities/sqli_blind/
http://172.28.128.12/dvwa/vulnerabilities/upload/
http://172.28.128.12/dvwa/vulnerabilities/xss_r/
http://172.28.128.12/dvwa/vulnerabilities/xss_s/
http://172.28.128.12/dvwa/security.php
http://172.28.128.12/dvwa/security.php?phpids=on
http://172.28.128.12/dvwa/security.php?test=%22><script>eval(window.name)</script>
http://172.28.128.12/dvwa/phpinfo.php
http://172.28.128.12/dvwa/phpinfo.php?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000
http://172.28.128.12/dvwa/about.php

[*] Output stored in C:\Users\gouth\Documents\Scripts\spider_output\172.28.128.12.txt
```

## To use with tor proxy :
```
$ pip3 install requests[socks]
$ sudo apt install tor
```
```
$ python3 spider.py -w http://172.28.128.12/dvwa/ --proxy socks5://127.0.0.1:9050
```

## Author
* **Goutham** - [G0uth4m](https://github.com/G0uth4m)
