from __future__ import unicode_literals
from django.apps import AppConfig




class PlaystationConfig(AppConfig):
    name = 'playstation'

    def ready(self):
    	import playstation.signals