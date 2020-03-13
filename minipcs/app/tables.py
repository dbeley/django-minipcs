import django_tables2 as tables
from .models import CPU, BRAND, MiniPC


class MiniPCTable(tables.Table):
    class Meta:
        model = MiniPC
        template_name = "django_tables2/bootstrap.html"


class CPUTable(tables.Table):
    class Meta:
        model = CPU
        template_name = "django_tables2/bootstrap.html"


class BRANDTable(tables.Table):
    class Meta:
        model = BRAND
        template_name = "django_tables2/bootstrap.html"
