#VERSION: 1.21
#AUTHORS: anon
from helpers import retrieve_url, download_file
from novaprinter import prettyPrinter
import json
class pantsu(object):
    url = 'https://nyaa.net'
    name = 'pantsu'
    supported_categories = {'all': '_',
                            'anime': '3_',
                            'books': '4_',
                            'music': '2_',
                            'pictures': '6_',
                            'software': '1_',
                            'games': '1_2'}
    engine_url='pantsu'
    def __init__(self):
        pass
    def download_torrent(self, info):
        print(download_file(info))
    def search(self, what, cat='all'):
        per_page=100
        url = self.url+'/api/search/?c='+self.supported_categories[cat]+'&q='+what+'&limit='+str(1)+'&page='+str(1)
        count = json.loads(retrieve_url(url))['totalRecordCount']
        pages=count/per_page
        
        if count%per_page != 0:
            pages=int(count/per_page)+1
            
        for page, x in enumerate(range(pages),start=1):
            url = self.url+'/api/search/?c='+self.supported_categories[cat]+'&q='+what+'&limit='+str(per_page)+'&page='+str(page)
            link = json.loads(retrieve_url(url))
            for animu in link['torrents']:
                dic={}
                dic['link'] = animu['magnet']
                dic['name'] = animu['name']
                dic['size'] = str(animu['filesize'])+'B'
                dic['seeds']= animu['seeders']
                dic['leech']= animu['leechers']
                dic['desc_link']=self.url+'/view/'+str(animu['id'])
                dic['engine_url']=self.engine_url
                prettyPrinter(dic)
