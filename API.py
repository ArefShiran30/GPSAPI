import json
import urllib.parse
import urllib.request
import urllib.error


MAP_API_KEY = '8pI5ImthmOkojPTu5ybZyCtFdJFo2igI'

'''  This is API addresses are for (LAT&LONG , STEPS, TOTAL TIME , TOTAL DISTANCE) '''

MAP_API_KEY_ELEVATION = '8pI5ImthmOkojPTu5ybZyCtFdJFo2igI'

'''This API is just for the ELEVATION of our program'''

BASE_MAP_URL = 'http://open.mapquestapi.com/directions/v2/route?'
BASE_MAP_URL_ELEVATION ='http://open.mapquestapi.com/elevation/v1/profile?'


def build_address(addresses:list)->str:
    '''This function take list of addresses and then return  the URL '''

    map_parameters = [('key', MAP_API_KEY),('from',addresses[0])]
    for num_addresses in range(1,len(addresses)):
        map_parameters.append(('to',addresses[num_addresses]))
    return BASE_MAP_URL+ urllib.parse.urlencode(map_parameters)



def get_result(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None
    try:

        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')
        return json.loads(json_text)

    except urllib.error.HTTPError:
        print('MAPQUEST ERROR')
        quit()

    finally:
        if response != None:
            response.close()




def get_result_elevation(url: str) -> dict:
    '''
    This function takes a URL and returns a Python dictionary representing the
    parsed JSON response.
    '''
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')
        return json.loads(json_text)
    finally:

        if response != None:
            response.close()

