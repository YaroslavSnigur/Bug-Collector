from django.contrib import admin
from .models import Bug, Treatment, Agent, Photo

admin.site.register(Bug)
admin.site.register(Treatment)
admin.site.register(Agent)
admin.site.register(Photo)

