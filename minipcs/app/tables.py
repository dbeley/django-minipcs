import django_tables2 as tables
from .models import CPU, BRAND, MiniPC


class MiniPCTable(tables.Table):
    name = tables.Column(order_by=("release_date", "storage_capacity"))

    class Meta:
        model = MiniPC
        template_name = "django_tables2/bootstrap.html"
        fields = (
            "brand",
            "model",
            "alias",
            "cpu",
            "cpu.tdp",
            "cpu.performance",
            "cpu.gpu_performance",
            "release_date",
            "recommended_price",
            # "min_price",
            "weight",
            "length",
            "width",
            "height",
            # "os",
            "storage",
            "storage_capacity",
            "m2_sata_port",
            "length_m2_sata_port",
            "m2_nvme_port",
            "length_m2_nvme_port",
            "ram_min_capacity",
            "ram_max_capcity",
            "ram_technology",
            "screen_resolution_x",
            "screen_resolution_y",
            "screen_size",
            "screen_technology",
            "touchscreen",
            "stylus_compatibility",
            "battery_wattage",
            "battery_capacity",
            "battery_voltage",
            "table_hinge",
            "input_devices",
            "lit_keyboard",
            "fingerprint_sensor",
            "usb2",
            "usb3",
            "usbC",
            "mini_hdmi",
            "micro_hdmi",
            "hdmi",
            "vga",
            "dvi",
            "thunderbolt",
            "ethernet",
            "microsd_slot",
            "sd_slot",
            "jack",
            "wifi_version",
            "bluetooth_version",
        )


class CPUTable(tables.Table):
    class Meta:
        model = CPU
        template_name = "django_tables2/bootstrap.html"
        fields = (
            "brand",
            "model",
            "release_date",
            "core_number",
            "hyperthreading",
            "lithography",
            "tdp",
            "performance",
            "gpu",
            "gpu_performance",
        )


class BRANDTable(tables.Table):
    class Meta:
        model = BRAND
        template_name = "django_tables2/bootstrap.html"
        exclude = ("id", "logo", "logo_source")
