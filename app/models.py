from django.db import models


# Create your models here.
class CPU(models.Model):
    def __str__(self):
        return self.brand + " - " + self.model

    BRANDS_CHOICES = (
        ("Intel", "Intel"),
        ("AMD", "AMD"),
        ("Qualcomm", "Qualcomm"),
        ("Samsung", "Samsung"),
        ("Huawei", "Huawei"),
    )

    brand = models.CharField(
        choices=BRANDS_CHOICES, max_length=100, blank=False
    )
    model = models.CharField(max_length=100, blank=False, unique=True)
    release_date = models.CharField(max_length=100, blank=True, null=True)
    core_number = models.PositiveIntegerField(blank=True, null=True)
    hyperthreading = models.BooleanField(blank=True, null=True)
    lithography = models.PositiveIntegerField(blank=True, null=True)
    tdp = models.DecimalField(
        decimal_places=1, max_digits=4, blank=True, null=True
    )
    performance = models.DecimalField(
        decimal_places=2, max_digits=6, blank=True, null=True
    )
    gpu = models.CharField(max_length=100, blank=True, null=True)
    gpu_performance = models.DecimalField(
        decimal_places=2, max_digits=6, blank=True, null=True
    )


class BRAND(models.Model):
    def __str__(self):
        return self.name

    BRANDS_CHOICES = (
        ("Chuwi", "Chuwi"),
        ("Pretech", "Pretech"),
        ("iLife", "iLife"),
        ("TopJoy", "TopJoy"),
        ("GPD", "GPD"),
        ("Cube", "Cube"),
        ("Acer", "Acer"),
        ("Asus", "Asus"),
        ("Microsoft", "Microsoft"),
        ("Weibu", "Weibu"),
        ("One", "One"),
        ("Mag", "Mag"),
        ("Xiami", "Xiaomi"),
        ("Samsung", "Samsung"),
        ("Peakago", "Peakago"),
    )

    name = models.CharField(
        choices=BRANDS_CHOICES, max_length=100, blank=False
    )

    country = models.CharField(max_length=100, blank=True)

    logo = models.ImageField(upload_to="", blank=True, null=True)
    logo_source = models.CharField(max_length=100, blank=True, null=True)


# Create your models here.
class MiniPC(models.Model):
    def __str__(self):
        return f"{self.brand.name} - {self.model} ({self.cpu.model})"

    SCREEN_CHOICES = (
        ("IPS", "IPS"),
        ("TN", "TN"),
        ("VA", "VA"),
        ("MVA", "MVA"),
        ("OLED", "OLED"),
    )

    # General
    brand = models.ForeignKey(
        BRAND, on_delete=models.CASCADE, blank=False, null=False
    )
    model = models.CharField(max_length=100, blank=False)
    comment = models.CharField(max_length=5000, blank=True, null=True)
    alias = models.CharField(max_length=500, blank=True, null=True)
    release_date = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="", blank=True, null=True)
    image_source = models.CharField(max_length=100, blank=True, null=True)
    recommended_price = models.PositiveIntegerField(blank=True, null=True)
    min_price = models.PositiveIntegerField(blank=True, null=True)
    # Dimensions
    # gram
    weight = models.PositiveIntegerField(blank=True, null=True)
    # mm
    length = models.DecimalField(
        decimal_places=2, max_digits=5, blank=True, null=True
    )
    # mm
    width = models.DecimalField(
        decimal_places=2, max_digits=5, blank=True, null=True
    )
    # mm
    height = models.DecimalField(
        decimal_places=2, max_digits=5, blank=True, null=True
    )
    # Internal Components
    cpu = models.ForeignKey(
        CPU, on_delete=models.CASCADE, blank=True, null=True
    )
    os = models.CharField(max_length=100, blank=True, null=True)
    storage = models.CharField(max_length=100, blank=True, null=True)
    storage_capacity = models.PositiveIntegerField(blank=True, null=True)
    m2_sata_port = models.PositiveIntegerField(blank=True, null=True)
    length_m2_sata_port = models.PositiveIntegerField(blank=True, null=True)
    m2_nvme_port = models.PositiveIntegerField(blank=True, null=True)
    length_m2_nvme_port = models.PositiveIntegerField(blank=True, null=True)
    # Gb
    ram_min_capacity = models.PositiveIntegerField(blank=True, null=True)
    ram_max_capacity = models.PositiveIntegerField(blank=True, null=True)
    ram_technology = models.CharField(max_length=100, blank=True, null=True)
    ram_extension = models.BooleanField(blank=True, null=True)
    # pixels
    screen_resolution_x = models.PositiveIntegerField(blank=True, null=True)
    # pixels
    screen_resolution_y = models.PositiveIntegerField(blank=True, null=True)
    # inches
    screen_size = models.DecimalField(
        decimal_places=2, max_digits=4, blank=True, null=True
    )
    screen_technology = models.CharField(
        choices=SCREEN_CHOICES, max_length=20, blank=True, null=True
    )
    touchscreen = models.BooleanField(blank=True, null=True)
    stylus_compatibility = models.BooleanField(blank=True, null=True)
    battery_wattage = models.DecimalField(
        decimal_places=2, max_digits=5, blank=True, null=True
    )
    battery_capacity = models.PositiveIntegerField(blank=True, null=True)
    battery_voltage = models.DecimalField(
        decimal_places=2, max_digits=4, blank=True, null=True
    )
    # External Components
    HINGE_CHOICES = (
        ("360-degree", "360-degree"),
        ("Laptopt-like hinge", "Laptop-like hinge"),
    )
    tablet_hinge = models.CharField(
        choices=HINGE_CHOICES, max_length=100, blank=True, null=True
    )
    INPUT_CHOICES = (
        ("None", "None"),
        ("Touchpad", "Touchpad"),
        ("Trackpoint", "Trackpoint"),
        ("Optical Touch Sensor", "Optical Touch Sensor"),
        ("Touchpad + Gamepad", "Touchpad + Gamepad"),
        ("Gamepad", "Gamepad"),
    )
    input_devices = models.CharField(
        choices=INPUT_CHOICES, max_length=100, blank=True, null=True
    )
    lit_keyboard = models.BooleanField(blank=True, null=True)
    fingerprint_sensor = models.BooleanField(blank=True, null=True)
    # Connectivity
    usb2 = models.PositiveIntegerField(blank=True, null=True, default=0)
    usb3 = models.PositiveIntegerField(blank=True, null=True, default=0)
    usbC = models.PositiveIntegerField(blank=True, null=True, default=0)
    mini_hdmi = models.BooleanField(blank=True, null=True)
    micro_hdmi = models.BooleanField(blank=True, null=True)
    hdmi = models.BooleanField(blank=True, null=True)
    vga = models.BooleanField(blank=True, null=True)
    dvi = models.BooleanField(blank=True, null=True)
    thunderbolt = models.BooleanField(blank=True, null=True)
    ethernet = models.BooleanField(blank=True, null=True)
    microsd_slot = models.BooleanField(blank=True, null=True)
    sd_slot = models.BooleanField(blank=True, null=True)
    jack = models.BooleanField(blank=True, null=True)
    wifi_version = models.CharField(max_length=100, blank=True, null=True)
    bluetooth_version = models.CharField(max_length=100, blank=True, null=True)
