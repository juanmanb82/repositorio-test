

from http.client import responses
import pip._vendor.requests

"""    
    Vamos a probar funciones matematicas
"""


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def pruebaLlamadaAPI():
    
    # SOAP request URL
    url = "http://asdjbonardi-nbk:8088/mockCalculatorSoap"
    # structured XML
    payload = """			
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
                <soapenv:Header/>
                    <soapenv:Body>
                        <tem:Add>
                            <tem:intA>2</tem:intA>
                            <tem:intB>3</tem:intB>
                        </tem:Add>
                    </soapenv:Body>
            </soapenv:Envelope>
"""
    # headers
    headers = {}
    # POST request
    response = pip._vendor.requests.request("POST", url, headers=headers, data=payload)
    #test

    # prints the response
    print(response.text)
    print(response)
    return (response.text)

