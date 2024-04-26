""" scraper.py
This module orchestrates Multiprocess Async scraper process
"""
import sys
import asyncio
from aiohttp import request
from aiomultiprocess import Pool

import logging
_logger = logging.getLogger(__name__)

from info_parser import get_scraped_info

import random 

uagent = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"]

async def fetch_list(url: str) :
    """ Get the URL of each page from the URL list and scrap info  """
    scraped_info_list =[]

    try:
        chosenUserAgent = random.choice(uagent)
    
        headers = {"user-agent": chosenUserAgent}
        async with request("GET", url , headers = headers) as response:
            assert response.status == 200
            html = await response.text()
            scraped_info_list.append( get_scraped_info(url, html) )
    except Exception as err:
        _logger.info(f'Exception  {err} Exception Type:{type(err)}' )

    return scraped_info_list



##### using async for development
async def asyncio_main(scrape_urls: list ):
    """ Implementing web scraping by using asyncio   """
    url_infos    = []
    fetch_list_tasks = [ asyncio.create_task(fetch_list( url  )) for url in scrape_urls ]
    for urls in asyncio.as_completed(fetch_list_tasks):
        url_infos.extend(await urls)
    return url_infos



####### using multiprocess async
async def aiomultiprocess_main(scrape_urls: list):
    """ Integrating multiprocessing and asyncio with the help of aiomultiprocess using Pool method """
    url_infos  = []

    async with Pool() as pool:
        async for urls in pool.map(fetch_list,[ url for url in scrape_urls ]):
            url_infos.extend(urls)

    return url_infos