# tests_framework_apis_bdd_gherkin_behave_python_pytest_unittest
Framework de tests sobre APIs, en esta ocasión usando BDD con Gherkin y Behave, hecho en Python

Test sobre APIs, del curso de Udemy https://www.udemy.com/course/la-guia-completa-test-de-api-rest-con-python/ (Segunda Parte)

Los test fueron hechos con BDD, usando Gherkin y Behave.

BDD Hace fácilmente entendibles los test, en la carpeta features/steps/WebApiFeature.feature se puede ver esta implementación.

Requisitos:

    Python >= 3.5
    Instalar las dependencias del proyecto: pip3 install -r requirements.txt
    Pycharm
    
**APIs usadas:**

Pet Store: https://petstore.swagger.io/

Twiitter: https://developer.twitter.com/ (Se debe solicitar a Twitter permisos para usar sus APIs.)

**Reporte HTML usando Allure Framework, se corre con el comando ***allure serve allure_result_folder***

<a href="https://ibb.co/R7C79G4"><img src="https://i.ibb.co/jHLHT9Z/Screen-Shot-2020-07-19-at-18-00-38.png" alt="Screen-Shot-2020-07-19-at-18-00-38" border="0"></a>

**En el archivo functions/Inicializar.py se debe hacer un switch entre 'Twitter.test' y 'TetStore.test' para ver los correr respectivos tests de uno u otro.**

    Environment = 'Twitter.test'
          #'PetStore.test'
          #"Twitter.test"
        
