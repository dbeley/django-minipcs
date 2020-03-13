from django.contrib import admin
from app.models import MiniPC, CPU, BRAND
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


# class MiniPCAdmin(admin.ModelAdmin):
#     pass


class CPUResource(resources.ModelResource):
    class Meta:
        model = CPU


class BRANDResource(resources.ModelResource):
    class Meta:
        model = BRAND


class MiniPCResource(resources.ModelResource):
    class Meta:
        model = MiniPC


class CPUAdmin(ImportExportModelAdmin):
    resource_class = CPUResource


class BRANDAdmin(ImportExportModelAdmin):
    resource_class = BRANDResource


class MiniPCAdmin(ImportExportModelAdmin):
    resource_class = MiniPCResource


admin.site.register(MiniPC, MiniPCAdmin)
admin.site.register(CPU, CPUAdmin)
admin.site.register(BRAND, BRANDAdmin)
