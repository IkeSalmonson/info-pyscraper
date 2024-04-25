 
import asyncio
from aiohttp import request
from aiomultiprocess import Pool
from bs4 import BeautifulSoup
import re 

from info_parser import find_contact_tel

class PyScraper:

    def __init__(self):
        print('Iniciou PyScraper')
        pass



    def test_func(self):
        print('test func works ')
        pass  


## outside of class 
def WORKINget_scraped_info(base_url: str, html: str) :
    """ Grab the link to the detail page of each book from the HTML code of the list page """
    print('get_scraped_info')
    result = []
    soup = BeautifulSoup(html, "html.parser")
    print('base_url ', base_url)
    logo_tags = soup.select('img')
    print('logo_tags', logo_tags)    
 
    return logo_tags

########

def get_scraped_info(base_url: str, html: str) :
    """ Grab the link to the detail page of each book from the HTML code of the list page """
    print('get_scraped_info')
    result = []
    soup = BeautifulSoup(html, "html.parser")
    print('base_url ', base_url)
    logo_candidate = soup.find_all(href=re.compile("logo"), id='link1')
    logo_tags = soup.select('img')
    print('logo_tags in getscraped', logo_tags)   
 
    return logo_tags

#####


async def fetch_list(url: str) :      
    """ Get the URL of each page from the list page URL """ 
    print('fetch_list >> ', url )
    scraped_info_list =[]
    async with request("GET", url) as response:
            html = await response.text()
            print('before call get_scraped_info')
            scraped_info_list.append(   get_scraped_info(url, html) )
    return scraped_info_list 
 
 

##### using async for develpment  


async def asyncio_main(scrape_urls ):
    """ Implementing web scraping by using asyncio   """
    info_pages    = [] 
    fetch_list_tasks = [ asyncio.create_task(fetch_list( url  )) for url in scrape_urls ]
    for urls in asyncio.as_completed(fetch_list_tasks):
        info_pages.extend(await urls)
 
    return info_pages   



####### using multiprocess async 
async def aiomultiprocess_main(scrape_urls):
    """ Integrating multiprocessing and asyncio with the help of aiomultiprocess using Pool method """
    info_pages  = [] 
    print('before poll loop')
    async with Pool() as pool: 
        print('in poll loop')
        async for urls in pool.map(fetch_list,[ url for url in scrape_urls ]):
            info_pages.extend(urls)
            print('in poll loop scrape_urls '  , scrape_urls)
    print('aiomultiprocess_main info_pages' , info_pages)
 
 