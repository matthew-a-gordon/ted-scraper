# Scrapy settings for ted-scraper project

BOT_NAME = 'ted-scraper'

SPIDER_MODULES = ['ted-scraper.spiders']
NEWSPIDER_MODULE = 'ted-scraper.spiders'

# Enable scrapy.pipelines.files.FilesPipeline 
# https://docs.scrapy.org/en/latest/topics/media-pipeline.html#enabling-your-media-pipeline
MEDIA_ALLOW_REDIRECTS = True
ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
FILES_STORE = './downloads'

# Enable our custom downloader middleware to intercept requests for video files
# and video detail pages that we've already got and drop them.

DOWNLOADER_MIDDLEWARES = {
    "ted-scraper.middlewares.TedscraperDownloaderMiddleware": 543,
}

# Enable the default FilesPipeline which will download the 

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60

# Logging
LOG_LEVEL = 'DEBUG'

# from https://github.com/ZuInnoTe/scrapy-contrib-bigexporters instructions

# register additional format
FEED_EXPORTERS = {
    'parquet': 'zuinnote.scrapy.contrib.bigexporters.ParquetItemExporter'}
FEEDS = {
    # 'output/data-%(name)s-%(time)s.json': {
    #     'format': 'json',
    #     'encoding': 'utf8',
    #     'store_empty': False,
    #     'fields': None,
    #     'indent': 4,
    #     'item_export_kwargs': {
    #         'export_empty_fields': True,
    #     },
    # },
    'output/data-%(name)s-%(time)s.parquet': {
        'format': 'parquet',
        'encoding': 'utf8',
        'store_empty': False,
        'item_export_kwargs': {
            'compression': 'GZIP',
            'times': 'int64',
            'hasnulls': True,
            'convertallstrings': False,
            'writeindex': False,
            'objectencoding': 'infer',
            'rowgroupoffset': 50000000,
            'items_rowgroup': 10000
        },
    }
}