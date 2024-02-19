
import API
import OUTPUT


def number_of_map()->int:
    '''This function get number of the
    maps as input that we try to use'''
    location_number = int(input())
    return location_number


def number_of_output() -> int:
    '''This function get the number of
    the output that we need to use'''
    info_number = int(input())
    return info_number


def user_input_address()->str:
    '''This function got all the input from
    the user and these inputs are the addresses
    that user type in the system and return those
    input in right format   '''

    address_str = input()
    return address_str

def make_list_of_addresses (numberloction:int)->list:
    '''This function make list of addresses and put this in the list '''
    address_list = []
    for number_of_adresses in range(numberloction):
        address_list.append(user_input_address())
    #print(address_list)
    return address_list




def showing_output_title()->list: # This function return list
    '''this function show us the output for of titles '''
    number = number_of_output()
    output_list = []
    for i in range(number):
        user_output_title = input()
        output_list.append(user_output_title)


    #print(output_list)
    return output_list


def user_interface():
    '''This function everything happend and call the functions'''
    address_num = number_of_map()
    address_in_list = make_list_of_addresses(address_num)  # all address in one list
    URL = API.build_address(address_in_list)
    output_titles = showing_output_title()
    result = API.get_result(URL)

    if result['info']['statuscode'] == 0:
        OUTPUT.run_information_Generator(OUTPUT.def_outputs(output_titles),result)
    elif result ['info'] ['statuscode'] == 400:
            print()
            print('NO ROUTE FOUND')

    else:
        print('MAPQUEST ERROR')
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
if __name__ == '__main__':
    user_interface()


