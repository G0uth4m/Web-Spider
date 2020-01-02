import requests
import argparse
import re
import urllib.parse
import os
from bs4 import BeautifulSoup

def get_arguments():
	parser = argparse.ArgumentParser()

	parser.add_argument("-w", "--website-url", dest="url", help="URL")
	parser.add_argument("-u", "--user-agent", dest="user_agent", help="User Agent to use(default=Python requests)")
	parser.add_argument("-p", "--proxy", dest="proxy", help="Format : protocol://IP:port")
	parser.add_argument("-c", "--cookie", dest="cookie", help="Cookies to use")

	options = parser.parse_args()

	if not options.url:
		parser.print_help()
		exit()

	if not options.user_agent:
		options.user_agent = "Python requests"

	return options

def create_web_session(proxy):
	session = requests.session()
	if proxy:
		session.proxies = {'http':proxy, 'https':proxy}

	return session

def extract_links(url, user_agent, session, cookie):
	if cookie:
		response = session.get(url, headers={'User-Agent':user_agent, 'Cookie':cookie})
	else:
		response = session.get(url, headers={'User-Agent':user_agent})
		
	parsed_html = BeautifulSoup(response.text)
	
	links = parsed_html.findAll('a')
	hrefs = [href.get("href") for href in links]
	
	form_actions = parsed_html.findAll('form')
	form_actions = [form_action.get('action') for form_action in form_actions]
	
	return hrefs + form_actions

def crawl(url, unique_links, user_agent, session, cookie):
	links = extract_links(url, user_agent, session, cookie)

	for i in links:
		i = urllib.parse.urljoin(url, i)
		if '#' in i:
			i = i.split('#')[0]
		if urllib.parse.urlparse(url).netloc == urllib.parse.urlparse(i).netloc and i not in unique_links and "logout" not in i:
			print(i)
			unique_links.append(i)
			crawl(i, unique_links, user_agent, session, cookie)

def log(url, unique_links):
	output_dir = "spider_output"

	if not os.path.isdir(output_dir):
		os.mkdir(output_dir)
	os.chdir(output_dir)

	log_file_name = urllib.parse.urlparse(url).hostname + ".txt"

	if os.path.exists(log_file_name):
		os.remove(log_file_name)

	with open(log_file_name, 'a') as log_file:
		for link in unique_links:
			log_file.write(link + '\n')

	print("\n[*] Output stored in " + os.getcwd() + "\\" + log_file_name)

def main():
	options = get_arguments()

	url = options.url
	if url[-1] != "/":
		url = url + "/"
	user_agent = options.user_agent
	proxy = options.proxy
	cookie = options.cookie

	unique_links = []
	session = create_web_session(proxy)

	try:
		crawl(url, unique_links, user_agent, session, cookie)
	except Exception:
		print("[-] Website unreachable")

	log(url, unique_links)

if __name__ == "__main__":
	main()
