from django import forms
from .models import Order, Material, Macro, Cutting

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('order','number','kind','standards','texture','length',)

class CuttingForm(forms.ModelForm):
    class Meta:
        model = Cutting
        fields = '__all__'

class MacroForm(forms.ModelForm):
    class Meta:
        model = Macro
        fields = '__all__'