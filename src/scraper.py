 
import asyncio
from aiohttp import request
import aiomultiprocess

from info_parser import find_contact_tel

class PyScraper:

    def __init__(self):
        print('Iniciou PyScraper')
        pass



    def test_func(self):
        print('test func works ')
        pass  



    def get_detail_url(base_url: str, html: str) :
        """ Grab the link to the detail page of each book from the HTML code of the list page """
        result = []
        soup = BeautifulSoup(html, "html.parser")
        a_tags = soup.select("article.product_pod div.image_container a")
        for a_tag in a_tags:
            result.append(urljoin(base_url, a_tag.get("href")))
        return result


## outside of class 
async def fetch_list(url: str) :      
    """ Get the URL of each detail page from the list page URL """
    #print(f"fetch_list: begin to process url: {url}")
    async with request("GET", url) as response:
            html = await response.text()
            #urls = get_detail_url(url, html)
    #return urls
    return html 


async def asyncio_main(scrape_url ):
    """ Implementing web scraping by using asyncio   """
    detail_urls, phone_list = [], [] 
    fetch_list_tasks = [ asyncio.create_task(fetch_list( url  )) for url in scrape_url ]
    for urls in asyncio.as_completed(fetch_list_tasks):
        detail_urls.extend(await urls)

    for item in detail_urls:
        file = open('read.txt', 'w') 
        file.write(str(detail_urls)) 
        file.close() 
        phone_list.extend(find_contact_tel(item))
    return phone_list   

 