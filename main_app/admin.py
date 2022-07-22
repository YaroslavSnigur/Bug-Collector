from django.contrib import admin
from .models import Bug, Treatment, Agent

admin.site.register(Bug)
admin.site.register(Treatment)
admin.site.register(Agent)

