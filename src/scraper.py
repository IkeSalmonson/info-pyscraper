import asyncio
from aiohttp import request
from aiomultiprocess import Pool
from bs4 import BeautifulSoup
import re 
import sys 


import logging
 

from info_parser import find_contact_tel

class PyScraper:

    def __init__(self):
        print('Iniciou PyScraper')
        pass



    def test_func(self):
        print('test func works ')
        pass  
 
########

def get_scraped_info(base_url: str, html: str) :
    """ Grab the link to the detail page of each book from the HTML code of the list page """
    print('get_scraped_info')
    result = []
    soup = BeautifulSoup(html, "html.parser")
    print('base_url %s ' % base_url)
    logo_candidate = soup.find_all(href=re.compile("logo") )
    print('len logo_candidate> ', len(logo_candidate))
    regex_phone_candidate = r"(?:([+]\d{1,4})[-.\s]?)?(?:([(]\d{1,3}[)])[-.\s]?)?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,9})"
    contact_tel_candidate = soup.find_all(text=re.compile(regex_phone_candidate) )
    print('len contact_tel_candidate  ', len(contact_tel_candidate))   
 
    return logo_candidate

#####


async def fetch_list(url: str) :      
    """ Get the URL of each page from the URL list and scrap info  """ 
    print('fetch_list >> ', url )
    scraped_info_list =[]    
    try: 
        headers = {"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        async with request("GET", url , headers = headers) as response:
            print('response status ', response.status)
            assert response.status == 200
            html = await response.text()
            print('before call get_scraped_info')
            scraped_info_list.append(   get_scraped_info(url, html) )
    except Exception as err:
        print('Exception', err , 'Exception Type:', type(err), file=sys.stderr) 
        

    return scraped_info_list 
 
 

##### using async for develpment  


async def asyncio_main(scrape_urls: list ):
    """ Implementing web scraping by using asyncio   """
    print('asyncio_main')
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
  
    print('aiomultiprocess_main info_pages' , url_infos)
    return url_infos
 
 