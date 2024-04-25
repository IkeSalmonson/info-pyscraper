""" scraper.py
This module orchestrates Multiprocess Async scraper process
"""
import sys
import asyncio
from aiohttp import request
from aiomultiprocess import Pool



from info_parser import get_scraped_info


async def fetch_list(url: str) :
    """ Get the URL of each page from the URL list and scrap info  """

    scraped_info_list =[]
    try:
        headers = {"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        async with request("GET", url , headers = headers) as response:

            assert response.status == 200
            html = await response.text()

            scraped_info_list.append( get_scraped_info(url, html) )
    except Exception as err:
        print('Exception', err , 'Exception Type:', type(err), file=sys.stderr)

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