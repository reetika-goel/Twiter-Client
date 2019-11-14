"""
@Authors: Reetika Goel, Sithara Krishna Murthy
@Purpose: It contains Twitter API developer keys
"""

from django.apps import AppConfig

class TwitterapiConfig(AppConfig):
    name = 'TwitterApi'
    consumer_key = "******************"
    consumer_secret = "*****************************************"    # hide all the keys becoz of security reasons
    access_token = "*********************************************"
    access_token_secret = "*******************************************"
