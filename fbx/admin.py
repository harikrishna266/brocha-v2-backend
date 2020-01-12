from django.contrib import admin
from fbx.models import Fbx

# Register your models here.


class FbxAdmin(admin.ModelAdmin):
  list_display = ('name', 'fbx', 'normals', 'bump', 'texture','status')





admin.site.register(Fbx)

