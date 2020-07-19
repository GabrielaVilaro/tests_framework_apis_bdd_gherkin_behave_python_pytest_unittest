import os


class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json_Data = basedir + u"/data/"
    data_body = basedir + u"/data/data_body"
    data_responses = basedir + u"/data/data_responses"

    Environment = 'Twitter.test'
    #Twitter.test

    if Environment == 'PetStore':
        # API
        API_hostAddressBase = "https://petstore.swagger.io/v2/"

        API_headers = {
            'version': '1.0-preview.1',
            'content-type': 'application/json',
        }

        API_body = {}

        Scenary = {
            'pet': '501'
        }

    if Environment == 'Twitter.test':
        # API
        API_hostAddressBase = "https://api.twitter.com/"

        api_key = "8HRTI5U2gFOhJbNqOPqyw2Fjl"
        api_secret = "Z068HodLUjbfOQytarJ62L6Svxx0dzGCEvgr2wHwf4StBpZSiF"

        API_headers = {"Content-Type": "application/json"}

        API_body = {}
        API_subBody_dict = {}
        API_subBody_array = []

        Scenary = {
            'User_Test1': 'StevenWilsonHQ',
            'User_Test2': 'mysquality'
        }
