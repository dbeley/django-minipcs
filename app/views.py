from django.shortcuts import render
from django.template import loader
from django.views import generic
from django_tables2 import SingleTableView, SingleTableMixin
import django_filters
from django_filters.views import FilterView
from .models import MiniPC, CPU, BRAND
from .tables import MiniPCTable, CPUTable, BRANDTable


class model_detail(generic.DetailView):
    model = MiniPC
    template = loader.get_template("app/minipc_detail.html")


def index(request):
    minipcs = MiniPC.objects.all().order_by("-release_date")
    context = {"minipcs": minipcs}
    return render(request, "app/minipc_index.html", context)


class MiniPCFilter(django_filters.FilterSet):
    class Meta:
        model = MiniPC
        fields = ["model", "brand", "cpu"]


class MiniPCListView(SingleTableMixin, FilterView):
    model = MiniPC
    table_class = MiniPCTable
    template = loader.get_template("app/minipc_filter.html")
    filterset_class = MiniPCFilter


class CPUListView(SingleTableView):
    model = CPU
    table_class = CPUTable
    template = loader.get_template("app/cpu_list.html")


class BRANDListView(SingleTableView):
    model = BRAND
    table_class = BRANDTable
    template = loader.get_template("app/brand_list.html")
