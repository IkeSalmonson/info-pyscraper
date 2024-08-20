""" info_parser.py
This module parses html and text strings
"""
import re
#import phonenumbers
from bs4 import BeautifulSoup

import logging
_logger = logging.getLogger(__name__)

URL_REGEX = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
PHONE_CANDIDATE_REGEX = "(?:([+]\\d{1,4})[-.\\s]?)?(?:([(]\\d{1,3}[)])[-.\\s]?)?(\\d{1,4})[-.\\s]?(\\d{1,4})[-.\\s]?(\\d{1,9})"

re_url = re.compile(URL_REGEX)
re_phone_candidate = re.compile(PHONE_CANDIDATE_REGEX)
re_logo = re.compile("logo", re.IGNORECASE)

def validate_url(url: str) :
    """ Get valid URLs from input """
    _logger.info("input size {} input {}".format(len(url), url))
    return url , re_url.search( url) is not None

def format_input( input_string):
    """ Format input for scraping """
    input_string_line = []
    for line in input_string.split('\n'):
        input_string_line.append(line)
    not_urls = []
    urls = []
    for line in input_string_line  :
        validated_string , is_url =  validate_url(line)
        if is_url:
            urls.append(validated_string)
        else:
            not_urls.append(validated_string)
    return urls, not_urls


def find_logo_image(  html_soup: BeautifulSoup ) -> str:
    """Find logo image in html and format as full URL """
    logo_candidates = []
    logo_candidates = html_soup.find_all("img")
    for logo in logo_candidates:
        if re_logo.search(logo['src'] ):
            return logo['src']
    
    logo_candidates_class_ = html_soup.find_all(  class_=re_logo )
    for logo in logo_candidates_class_:
        if re_logo.search(logo['src'] ):
            return logo['src']
        else:
            return 'no img logo'   
    ### ELSE SEARCH \/
    #logo_candidates_class_ = html_soup.find_all("img", class_=re_logo )
    #logo_candidates_href = html_soup.find_all("img",href=re_logo )
    #logo_candidates_id = html_soup.find_all("img" , id=re_logo )
    #logo_candidates.extend(logo_candidates_href)
    #logo_candidates.extend( logo_candidates_class_)
    #logo_candidates.extend( logo_candidates_id)
    #logo_src =  list(filter(lambda a: hasattr(a, 'src') is True , logo_candidates))
    #_logger.info(f"logo_src > {logo_src}") 
        # Decision tree:
        # html tag Logo
        # img link contains logo
        # img link contains company name
        # img link leads to / or /home or home/*
    #Return format
    ## if complete URL > return 
    ## if relative path URL > return url_root + relative_path    
 

def find_contact_phone( html_soup: BeautifulSoup ) -> list:
    """ Search and format phone in html page"""
    phone_list =[]
    phone_candidates = html_soup.find_all(text=re_phone_candidate , recursive=True )

    phone_list =  list(filter(lambda x: len(x)<=20 , phone_candidates))
    # Check for formated phones
    #if len(phone_list) > 0:
    #   return phone_list
    #else:
        #try other phone formats
        # au format: 13 + 4 digits
        # Letter as number Ex: 0800 TENANT
    return phone_list


def get_scraped_info(base_url: str, html: str) :
    """ Identify and format information from the HTML page """
    soup = BeautifulSoup(html, "html.parser")
    logo_src_url = find_logo_image(soup)
    contact_phone = find_contact_phone(soup)
    result_dict = {"logo":logo_src_url , "phones":  contact_phone ,"website":base_url}

    return result_dict
