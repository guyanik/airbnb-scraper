# -*- coding: utf-8 -*-

# Scrapy settings for deepbnb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'deepbnb'

SPIDER_MODULES = ['deepbnb.spiders']
NEWSPIDER_MODULE = 'deepbnb.spiders'

#
# Scraper config
#

# Public development key
AIRBNB_API_KEY = 'd306zoyjsyarp7ifhu67rjxn52tv0t20'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'deepbnb (+https://digitalengineering.io)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# https://docs.python.org/3/library/webbrowser.html
# Open results in web browser
# WEB_BROWSER = 'chromium'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 10
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'deepbnb.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'deepbnb.pipelines.AirbnbScraperPipeline': 300,
}

# https://docs.scrapy.org/en/latest/topics/feed-exports.html
FEED_EXPORTERS = {
    'xlsx': 'deepbnb.exporter.AirbnbExcelItemExporter',
}

FEED_EXPORT_FIELDS = [
    'name',
    'url',
    'price_rate',
    'price_rate_type',
    'total_price',
    'room_and_property_type',
    'min_nights',
    'max_nights',
    'latitude',
    'longitude',
    'monthly_price_factor',
    'weekly_price_factor',
    'room_type',
    'person_capacity',
    'summary',
    'amenities',
    'review_count',
    'review_score',
    'calendar_updated_at',
    'rating_accuracy',
    'rating_checkin',
    'rating_cleanliness',
    'rating_communication',
    'rating_location',
    'rating_value',
    'star_rating',
    'satisfaction_guest',
    'description',
    'neighborhood_overview',
    'notes',
    'additional_house_rules',
    'interaction',
    'access',
    'transit',
    'response_rate',
    'response_time',
]

# Minimum monthly discount percent
# MINIMUM_MONTHLY_DISCOUNT = 0

# Minimum weekly discount percent
# MINIMUM_WEEKLY_DISCOUNT = 0

# Minimum photos per listing
MINIMUM_PHOTOS = 2

# Desired hosting amenities and corresponding IDs. Determined by observing search GET parameters.
PROPERTY_AMENITIES = {
    # 'a/c':     5,
    'kitchen': 8,
    'tv':      58,
    'washer':  33,
    'dryer':   34,
    'wifi':    4,
}

# Blacklisted property types
PROPERTY_TYPE_BLACKLIST = ['Camper/RV', 'Campsite', 'Entire guest suite']

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True

# The initial download delay
AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'