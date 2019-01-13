from django.contrib import admin
from . models import Order, Material, Macro, Cutting

# Register your models here.
@admin.register(Order)
class OrderAdimin(admin.ModelAdmin):
    list_display = ['id','company','project','workpackage','workpiece','quantity']
    list_display_links = ['workpackage', 'workpiece']
    search_fields = ['workpackage']

@admin.register(Material)
class MaterialAdimin(admin.ModelAdmin):
    list_display = ['order','number','kind', 'standards','texture','length','quantity']
    list_display_links = ['order']
    search_fields = ['order']

@admin.register(Cutting)
class CuttingAdimin(admin.ModelAdmin):
    list_display =['material'] 
    search_fields = ['material']

@admin.register(Macro)
class MacroAdimin(admin.ModelAdmin):
    list_display =['macro_name'] 
    search_fields = ['macro_name']