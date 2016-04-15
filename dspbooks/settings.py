# -*- coding: utf-8 -*-

import appdirs
import ctypes
import logging
import os
import subprocess
import sys

from colorama import Fore, Style, init
from time import sleep

init(autoreset=True)

# Scrapy settings for dspbooks project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dspbooks'

SPIDER_MODULES = ['dspbooks.spiders']
NEWSPIDER_MODULE = 'dspbooks.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dspbooks (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dspbooks.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'dspbooks.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {'dspbooks.pipelines.DspbooksPipeline': 200}
FILES_STORE = os.path.join(appdirs.user_data_dir(), 'dspbooksspider')


# make shortcut to files
def make_shortcut():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s] %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    success = True
    shortcut_name = 'saved_books'

    if not os.path.exists(FILES_STORE):
        os.makedirs(FILES_STORE)

    if sys.platform.lower().startswith('win'):
        src = unicode(os.path.join(os.curdir, shortcut_name))
        if not os.path.exists(src):
            kdll = ctypes.windll.LoadLibrary("kernel32.dll")        
            dest = unicode(FILES_STORE)
            ecode = kdll.CreateSymbolicLinkW(src, dest, 1)
            if ecode == 0:
                success = False
    else:
        cm = 'ln -sf "{}" "{}"'.format(FILES_STORE, shortcut_name)
        ecode = subprocess.call(cm, shell=True)
        if ecode == 1:
            success = False
        else:
            # Removes strange recursive symlink
            cm = 'rm -f "{}/dspbooksspider"'.format(FILES_STORE)
            subprocess.Popen(cm, shell=True)

    if success:
        t = Fore.GREEN + Style.BRIGHT
        logger.info(t + 'Link to downloaded data made with name: "{}"'.format(shortcut_name))
    else:
        logger.setLevel(logging.ERROR)
        logger.error(Fore.RED + '''Failed to make shortcut.
The data is saved at {}'''.format(FILES_STORE))

    # give user chance to see the message
    sleep(4)
make_shortcut()

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

DOWNLOAD_HANDLERS = {
    's3': None,
}
