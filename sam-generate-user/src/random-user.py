import sys
import os
from random import choice, randint
from dataclasses import dataclass, asdict
import boto3

this = sys.modules[__name__]


class Container:
    def __init__(self):
        self.adresses = ["DS 2-103", "MG 1-245", "OB 54-2"]
        self.names = ["John Black", "Jack Sparrow", "Agent Smith"]

    def get_address(self):
        return choice(self.adresses)

    def get_name(self):
        return choice(self.names)


@dataclass
class User:
    name: str
    address: str
    age: int


this.container = Container()


def get_age():
    return randint(10, 60)

def get_ssm_paramter():
    param_name=os.environ['SSM_PARAM']
    client=boto3.client('ssm')
    response=client.get_parameter(Name=param_name)
    return response

def lambda_handler(event, context):  
    name = this.container.get_name()
    address = this.container.get_address()
    age = get_age()
    user = User(name, address, age)


    param=get_ssm_paramter()
    value=param['Parameter']['Value']
    return f'{value}-->{asdict(user)}'