import requests

lst = ['feral-file-009-unsupervised-refik-anadol',
       'ratdao-art',
       'lostsoulssanctuary',
       'planetdaos',
       'creativeworkstudios-tokens',
       'rug-radio-membership-pass',
       'cryptoongoonz',
       'ruggenesis-nft',
       'metacard-by-fullsend',
       'wolf-game-migrated']

def get_floor(collection_name):
    url = "https://api.opensea.io/api/v1/collection/" + collection_name

    response = requests.request("GET", url)
    data = response.json()

    #print (data['collection']['stats']['floor_price'])
    return (data['collection']['stats']['floor_price'])

def form_text(list_of_coll):
    text = ''
    floors = {}

    for i in list_of_coll:
        floors[i] = get_floor(i)

    temp = dict(sorted(floors.items(), key=lambda x: x[1], reverse=True))

    for j in temp:
        text+= j + ' : ' + str(temp[j]) + '\n'

    return (text)

def form_floors_dict(list_of_coll):#returns a dictionary of the collections + their floors
    floors = {}

    for i in list_of_coll:
        floors[i] = get_floor(i)

    return dict(sorted(floors.items(), key=lambda x: x[1], reverse=True))

def sum_port(list_of_coll):#returns the combined value of portfolio
    floors = 0
    for i in list_of_coll:
        floors += get_floor(i)
    return (round(floors,4))

def get_current_data(from_sym='BTC', to_sym='USD', exchange=''):#gets the current price of a given cryptocurrency
    url = 'https://min-api.cryptocompare.com/data/price'

    parameters = {'fsym': from_sym,
                  'tsyms': to_sym}

    if exchange:
        parameters['e'] = exchange

    # response comes as json
    response = requests.get(url, params=parameters)
    data = response.json()

    return data['USD']

def final_string(list_of_coll):
    return form_text(lst) + str((round(sum_port(list_of_coll),4))) + ' ETH\n$' + str(round((get_current_data('ETH','USD','coinbase')) * (sum_port(list_of_coll)),2))


#print(form_text(lst))
#print(form_floors_dict(lst))
#print(sum_port(lst))
#print(get_current_data('ETH','USD','coinbase'))
#print(final_string(lst))