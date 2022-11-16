from ast import Not
from email.mime import application
from symtable import Symbol
from wsgiref.util import application_uri
from xmlrpc.client import APPLICATION_ERROR
from logic import *

rain = Symbol("rain") #it is raining
hagrid = Symbol("hagarid") #harry visited hagrid
doubledore =Symbol("doubledore") #harry visited doubledore

Knowledge = Implication (Not(rain),hagrid)

print(Knowledge.formula())