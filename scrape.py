#!/usr/bin/env python

import re
import os
import getpass
import errno
import itertools
from subprocess import Popen
from mechanize import Browser
from multiprocessing import Pool


def make_sure_path_exists(path):
        print path
        try:
                os.makedirs(path)
        except OSError as exception:
                if exception.errno != errno.EEXIST:
                        raise

def download(url, direc):
	"""Copy the contents of a file from a given URL
	to a local file.
	"""
        make_sure_path_exists(os.getcwd()+ os.sep + direc + os.sep);
	
        if os.path.exists(os.getcwd()+ os.sep + direc + os.sep + url.split('/')[-1]):
		print "Already downloaded", url
		return
	
	import urllib
	webFile = urllib.urlopen(url)
	localFile = open(os.getcwd()+ os.sep + direc + os.sep + url.split('/')[-1], 'wb')
	localFile.write(webFile.read())
	webFile.close()
	localFile.close()

def download_star(url_direc):
        download(*url_direc)

if __name__ == '__main__':
	# Pretend we're just a regular old user (this is naughty, don't try this at home kids)
	br = Browser()
	br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6; en-us) AppleWebKit/531.9 (KHTML, like Gecko) Version/4.0.3 Safari/531.9')]
	br.set_handle_robots(False)
	br.open(raw_input('Enter course page URL: '))
	assert br.viewing_html()

	# Import from a module outside of version control your SUNET id and password
	br.select_form(name="login")
	br["username"] = raw_input('Username: ')
	br["password"] = getpass.getpass();

	# Open the course page for the title you're looking for 
        br.submit()
        br.select_form(name="login")
        br["otp"] = raw_input('Enter Two-Factor Authentification: ')
        response = br.submit()
        
        direc = raw_input("Directory to store videos: ")

	# Build up a list of lectures
	links = []
	for link in br.links(text="Watch Now"):
                link2 = link.attrs[7]
                link3 = eval(link2[1])
                print link3['url'][1]['webm-url']
		links.append(link3['url'][1]['webm-url'])

	print "Downloading %d videos..." % len(links)

	# Make a thread pool and download 5 files at a time
	p = Pool(processes=10)
	p.map(download_star, itertools.izip(links, itertools.repeat(direc)))
