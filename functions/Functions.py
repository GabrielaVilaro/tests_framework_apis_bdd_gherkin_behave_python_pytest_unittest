import random
import string
import objectpath as objectpath
import pytest
from functions.Inicializar import Inicializar
import json
import requests
import re
import datetime


class Functions(Inicializar):

    def ReplaceWithContextValues(self, text):
        patron_de_busqueda = r"(?<=Escenario:)\w+"
        variables = re.findall(str(patron_de_busqueda), text, re.IGNORECASE)
        self.N = 0
        for variable in variables:
            if variable == 'today':
                dateToday = str(datetime.date.today().strftime("%Y-%m-%d"))
                text = re.sub('(Escenario:)' + variable, dateToday, text, re.IGNORECASE)
                continue
            text = re.sub('(Escenario:)' + variable, Inicializar.Scenary[variable], text, re.IGNORECASE)
        return text

    def ReplaceWithQueryValues(self, text):
        patron_de_busqueda = r"(?<=Query:)\w+"
        variables = re.findall(str(patron_de_busqueda), text, re.IGNORECASE)
        for variable in variables:
            text = re.sub('Query:' + variable, str(self.QUERY[variable]), text, re.IGNORECASE)
        return text

    def get_full_host(self, _PartHost):
        _RegexPartHost = str(Functions.ReplaceWithContextValues(self, _PartHost))
        self._endpoint = Inicializar.API_hostAddressBase + _RegexPartHost
        print(self._endpoint)
        return self._endpoint

    def do_a_get(self):
        new_header = Inicializar.API_headers
        self._response = requests.get(self._endpoint, headers=new_header)
        return self._response

    def print_api_response(self):
        self.json_response = json.loads(self._response.text)
        print(json.dumps(self.json_response, indent=3))

    def response_is(self, code):
        print("status code is: " + str(self._response.status_code))
        assert self._response.status_code == int(
            code), f'El codigo de respuesta no es el esperado {self._response.status_code} != {code}'

    def set_body_values(self, entity, value):
        def set_ramdon_values(self):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(6))

        if value.lower() == "random":
            value = set_ramdon_values(self)
            if entity.lower() == "email":
                value = set_ramdon_values(self) + "@tests.com"

        value = Functions.ReplaceWithQueryValues(self, value)
        Inicializar.API_body[entity] = str(value)
        self._new_body = Inicializar.API_body
        print(self._new_body)
        return self._new_body

    def set_initial_json_body(self, file):
        self.New_Body = Functions.get_json_inData(self, file)
        Inicializar.API_body = self.New_Body
        print((json.dumps(Inicializar.API_body, indent=4)))

    def get_json_inData(self, file):
        json_path = Inicializar.Json_Data + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_inData: " + file)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)

    def do_a_put(self):
        new_header = Inicializar.API_headers
        print(self._new_body)
        self._response = requests.put(self._endpoint, headers=new_header, data=json.dumps(self._new_body))
        return self._response

    def do_a_post(self):
        new_header = Inicializar.API_headers
        print(self._new_body)
        self._response = requests.post(self._endpoint, headers=new_header, data=json.dumps(self._new_body))
        return self._response

    def assert_response_expected(self, entity, expected, subPath = 0):
        self.json_response = json.loads(self._response.text)
        PATH_VALUE = self.json_response[entity]

        if expected == "NOT NULL":
            assert str(PATH_VALUE) != None, f"El valor es Null: {PATH_VALUE} != {expected}"
            return

        elif expected == "NULL":
            assert str(PATH_VALUE) == None, f"El valor no es Null: {PATH_VALUE} != {expected}"
            return
        else:
            lista =  isinstance(PATH_VALUE, list)
            dicts = isinstance(PATH_VALUE, dict)
            if lista:
                PATH_VALUE = self.json_response[entity][int(subPath)]
            if dicts:
                PATH_VALUE = self.json_response[entity][subPath]

            assert str(PATH_VALUE) == expected, f"El valor no es el esperado: {PATH_VALUE} != {expected}"

    def expected_results_value(self, file):
        self.json_strings = Functions.get_json_inData(self, file)
        try:
            assert self.json_strings == self.json_response
            print(u"Se cumplió con el valor esperado")
            verificar = True
        except AssertionError:
            verificar = False
            print("La respuesta fue: ")
            print(json.dumps(self.json_response, indent=4))
            print("Se esperaba: ")
            print(json.dumps(self.json_strings, indent=4))
            assert verificar == False

    def new_compare_entity_values(self, path, esperado):
        esperado = str(esperado)
        try:
            tree_obj = objectpath.Tree(self.json_response)
            entity = tuple(tree_obj.execute('$.' + path))
            PATH_VALUE =  str(entity[0])
            print(entity)
        except SyntaxError:
            entity = str(None)
            print("No se pudo obtener ningun valor de la busqueda")

        if esperado == "NOT NULL":
            assert str(PATH_VALUE) != None, f"El valor es Null: {PATH_VALUE} != {esperado}"
            return

        elif esperado == "NULL":
            assert str(PATH_VALUE) == None, f"El valor no es Null: {PATH_VALUE} != {esperado}"
            return
        else:
            assert PATH_VALUE == esperado, f"No es el valor esperado {path}: {PATH_VALUE} != {esperado}"