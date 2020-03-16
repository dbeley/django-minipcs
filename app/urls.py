from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("", views.IndexView.as_view(), name="index"),
    # path("", views.IndexView.as_view(), name="index"),
    path(
        "model/<int:pk>/", views.model_detail.as_view(), name="model_detail",
    ),
    # path("cpu/<int:cpu_id>/", views.cpu_detail.as_view(), name="cpu_detail"),
    # path(
    #     "brand/<int:brand_id>/",
    #     views.brand_detail.as_view(),
    #     name="brand_detail",
    # ),
    path("model_list", views.MiniPCListView.as_view(), name="model_list"),
    path("cpu_list", views.CPUListView.as_view(), name="cpu_list"),
    path("brand_list", views.BRANDListView.as_view(), name="brand_list"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
