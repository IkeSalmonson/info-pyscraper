#info_parser 
import re 
import sys 

class InfoParse:


    def __init__(self ):
        pass 
       
       

 
    def validateURL(self, url):
        regex = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
        r = re.compile(regex)
        if (re.search(r, url)):
            return url , True 
        else:
            return url , False
 
    def format_input(self, input_string):
        #split input by line 
        input_string_line = [ line for line in input_string.split('\n')  ]
        #validate if url 
        not_a_url = []
        url_list = []
        for line in input_string_line  :
            validated_string , is_url =  self.validateURL(line)
            if is_url:
                url_list.append(validated_string)
            else: 
                not_a_url.append(validated_string)

        return url_list, not_a_url
     
    def find_logo_image(self, html_string ):
        re.Matchs(self.html_string , "*logo*") 
        # html tag Logo 
        # img link contains logo 
        # img link contains company name 
        # img link leads to / or /home or home/*

        raise TypeError("Logo image not found ")
    

def find_contact_tel(  html_string ):
                                ## 1 a 4 digitos 
    regex_phone_candidate = r"(?:([+]\d{1,4})[-.\s]?)?(?:([(]\d{1,3}[)])[-.\s]?)?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,9})"
    r = re.compile(regex_phone_candidate)
    phone_list = re.findall(r , html_string)

        # Captures US, BR, Latam , +  phone format    
    return phone_list
#        if len(phone_list) > 0:
#            return phone_list
#        else:      
            #try other phone formats 
        # au format: 13 + 4 digits 
        #Known flaws: Letter as number Ex: 0800 TENANT 


