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

    Environment = 'PetStore'

    if Environment == 'PetStore':
        # API
        API_hostAddressBase = "https://petstore.swagger.io/v2/"

        API_headers = {
            'version': '1.0-preview.1',
            'content-type': 'application/json',
        }

        Scenary = {
            'pet': '10'
        }
