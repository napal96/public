from django.db import models

# Create your models here.
class Order(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER.MODEL, on_delete=models.CASECADE)
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=30)
    project = models.CharField(max_length=30)
    workpackage = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=1)
    workpiece = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __int__(self):
        return self.id

class Material(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1)
    kind = models.CharField(max_length=30)
    standards = models.CharField(max_length=30)
    texture = models.CharField(max_length=30, default='ss400')
    length = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    macros = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __int__(self):
        return self.order

class Cutting(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    area = models.CharField(max_length=15)
    macro_name = models.CharField(max_length=15)
    macro_code = models.CharField(max_length=30)
    distance = models.PositiveIntegerField()
    height = models.PositiveIntegerField(blank=True, default=None)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['material']

    def __int__(self):
        return self.material

class Macro(models.Model):
    area = models.CharField(max_length=15)
    macro_name = models.CharField(max_length=30)
    macro_code = models.CharField(max_length=100)
    canvas_code = models.TextField(blank=True)
    rnc_code = models.TextField(blank=True)
    cad_code = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['macro_name']

    def __int__(self):
        return self.macro_name



