import sys
import asyncio
from scraper import aiomultiprocess_main #, asyncio_main
from info_parser import format_input

import logging 
import logging.config

logging.config.fileConfig('config/logger.conf', disable_existing_loggers=False)
_logger = logging.getLogger(__name__)


if __name__ == '__main__':
    _logger.info("Initializing scrapper")
    input_string = sys.stdin.read()

    scrape_urls , not_url = format_input(input_string)
    _logger.info("input valid urls {} , not urls {}".format(len(scrape_urls),len(not_url)))
    ## Development aux function: asyncio_main()
    #url_infos = asyncio.run(asyncio_main(scrape_urls))

    ## More perfomance: aiomultiproces
    url_infos = asyncio.run(aiomultiprocess_main(scrape_urls))

    for output_string in url_infos:
        print(output_string)

    sys.exit(0)
