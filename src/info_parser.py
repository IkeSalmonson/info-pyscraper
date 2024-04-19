import re 

class InfoParse:
    def __init__(self, html_string ):
        self.html_string = html_string

     
    def find_logo_image(self, html_string ):
        re.Matchs(self.html_string , "*logo*") 
        # html tag Logo 
        # img link contains logo 
        # img link contains company name 
        # img link leads to / or /home or home/*

        raise TypeError("Logo image not found ")
    

    def find_contact_tel(self, html_string ):
        re.Matchs(self.html_string , "*tel*") 
        # html text begins with Tel, tel, cel, Cel  
        # html text is US, BR, Latam standard format    
        # au format: 13 + 4 digits 
        #Known flaws: Letter as number Ex: 0800 TENANT 
        raise TypeError("Tel contact info not found ")


