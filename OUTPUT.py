import math
import API

def def_outputs(input_requests: list)-> list:
    '''This function help about information that user wants from the directions   '''
    output_requests = list()
    for input_request in input_requests:
        if "LATLONG" == input_request:
            output_requests.append(Latlong())
        if "STEPS" == input_request:
            output_requests.append(TotalSteps())
        if "TOTALTIME" == input_request:
            output_requests.append(TotalTime())
        if "TOTALDISTANCE" == input_request:
            output_requests.append(TotalDistance())
        if "ELEVATION" == input_request:
            output_requests.append(Elevations())
    return output_requests

class Latlong:
    def print_result(self,directions):
        '''This function is for LATLONG part'''
        print("LATLONGS")
        for i in range(0, len(directions['route']['locations'])):
            (lat, lng) = directions['route']['locations'][i]['latLng'].values()

            if lng < 0:
                lng = -lng
                ns = "S"
            else:
                lng = lng
                ns = "N"
            if lat < 0:
                lat = -lat
                ew = "W"
            else:
                lat = lat
                ew = "E"

            print("%.2f%s %.2f%s" % (lng, ns, lat, ew))
        print()



class TotalSteps:


    def print_result(self,directions):
        '''This function is for the DIRECTION'''
        print("DIRECTIONS")
        for j in range(0,len(directions['route']['legs'])):
            for i in range(0,len(directions['route']['legs'][j]['maneuvers'])):
                print(directions['route']['legs'][j]['maneuvers'][i]['narrative'])
        print()


class TotalTime:
    def print_result(self,directions):
        '''This function is for the TOTAL TIME'''
        time = int(int(math.ceil(directions['route']['time']/60)))

        print("TOTAL TIME: %d %s" % (time, " minutes"))
        print()
class TotalDistance:

    def print_result(self,directions):
        '''This function is for the TOTAL DISTANCE'''
        distance = int(int(math.ceil(directions['route']['distance'])))

        print("TOTAL DISTANCE: %d %s" % (distance, " miles"))
        print()



class Elevations:

    def build_address_elevation(self,directions: dict) -> list:
        '''This function take dictionary of addresses(Elevation) and then return  the URL '''

        map_parameters_elevation = [('key', API.MAP_API_KEY_ELEVATION), ('shapeFormat', 'raw')]
        base = API.BASE_MAP_URL_ELEVATION + API.urllib.parse.urlencode(map_parameters_elevation)
        URL_elevations = []
        for i in range(0, len(directions['route']['locations'])):
            (lng, lat) = directions['route']['locations'][i]['latLng'].values()

            address = base + '&latLngCollection=' + str(lat) + "," + str(lng)
            URL_elevations.append(address)
        addresses = list()
        for i in range(0, len(URL_elevations)):
            addresses.append(API.get_result_elevation(URL_elevations[i]))
        return addresses

    def meter_to_foot(self,height):
        HEIGHT = height * 3.28
        return HEIGHT
    def print_result(self,directions):
        '''This function is for the ELEVATION'''
        elevations = self.build_address_elevation(directions)
        print("ELEVATIONS")
        for i in range(0,len(elevations)):
            height = (int(elevations[i]['elevationProfile'][0]['height']))
            print(math.ceil(self.meter_to_foot(height)))
        print()


def run_information_Generator(print_results: ['Print_Result'], directions):
    for print_result in print_results:
        print_result.print_result(directions)

    return


