This new version has fewer dependencies and is generally more useful...

Installation
============
    git clone git@github.com:mdenton8/SCPD-Scraper.git
    sudo easy_install mechanize

Running
=======
    python scrape.py

Notes
=====
Update of the SCPD scraper. Only one depency, mechanize. Works with new SCPD and does not store a plain-text password. Works with enw two-factor. Asks for page URL as well as a directory to store videos in. Tries to check if the file still exists, not totally sure that works.

Since this uses multiprocessing, it might be tricky to Ctrl-C out of.  You can always just `killall python`
