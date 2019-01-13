from django.urls import reverse
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic import DeleteView
from . models import Order, Material, Macro, Cutting
from .forms import OrderForm, MaterialForm, MacroForm, CuttingForm


        
def orders(request, order=None):
        order_list = Order.objects.all()
        material_list = Material.objects.all()

        if request.method == 'POST':
                order_new = OrderForm(request.POST, instance=order)
                if order_new.is_valid():
                        order_new = order_new.save() #Model Form에서 제공
                        return redirect('macro:orders')
        else:
                order_new = OrderForm(instance=order)
        
        
        return render(request, 'macro/orders.html', {
                'order_list': order_list,
                'material_list': material_list,
                'order_new': order_new,                                            
        })

def orders_edit(request, pk):
        order = get_object_or_404(Order, pk=pk)
        return orders(request, order)

def orders_delete(request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect('macro:orders')

# orders_delete = DeleteView.as_view(model=Order, form_class=OrderForm)

def materials(request, material=None):
        order_list = Order.objects.all()
        material_list = Material.objects.all()    

        if request.method == 'POST':
                material_new = MaterialForm(request.POST, instance=material)
                if material_new.is_valid():
                        material_new = material_new.save(commit=False) 
                        # pk = request.GET.get('pk','')
                        # material_new.order = 'Order object(3)'
                        material_new.save()
                        return redirect('macro:materials')
        else:  
                material_new = MaterialForm(instance=material)
                pk = request.GET.get('pk','') 
        
        qs = Order.objects.all()
        mqs = Material.objects.all()
        q1 = request.GET.get('q1','')
        q2 = request.GET.get('q2','')
        q3 = request.GET.get('q3','')
        if q1 or q2 or q3:
                qs = qs.filter(project__icontains = q1,workpackage__icontains = q2,workpiece__icontains = q3)
                order_list = qs     
                qs = qs[0]             
                mqs = mqs.filter(order = qs)
                material_list = mqs
        if pk:
                qs = qs.filter(id__icontains = pk)
                order_list = qs
                qs = qs[0]
                mqs = mqs.filter(order = qs)
                material_list = mqs   
        

        return render(request, 'macro/materials.html', {
                'order_list': order_list,
                'material_list': material_list,
                'material_new': material_new,  
                'q1' : q1,  
                'q2' : q2,  
                'q3' : q3,  
                'pk' : pk,                        
        })

def materials_edit(request, pk):
        material = get_object_or_404(Material, pk=pk)
        return materials(request, material)

def materials_delete(request, pk):
        material = get_object_or_404(Material, pk=pk)
        material.delete()
        return redirect('macro:materials')

def cuttings(request, cutting=None):
        material_list = Material.objects.all()
        cutting_list = Cutting.objects.all() 
        macro_list = Macro.objects.all() 

        if request.method == 'POST':
                cutting_new = CuttingForm(request.POST, instance=cutting)
                if cutting_new.is_valid():
                        cutting_new = cutting_new.save() #Model Form에서 제공
                        
                        return redirect('macro:cuttings')
        else:  
                cutting_new = CuttingForm(instance=cutting) 
                pk = request.GET.get('pk','')   

        qs = Material.objects.all()
        mqs = Cutting.objects.all()
        qm1 = request.GET.get('qm1','')
        qm2 = request.GET.get('qm2','')
        qm3 = request.GET.get('qm3','')
        if qm1 or qm2 or qm3:
                qs = qs.filter(number__icontains = qm1,kind__icontains = qm2,standards__icontains = qm3)
                material_list = qs
                qs = qs[0]
                mqs = mqs.filter(material = qs)
                cutting_list = mqs
        if pk:
                qs = qs.filter(id__icontains = pk)
                material_list = qs
                qs = qs[0]
                mqs = mqs.filter(material = qs)
                cutting_list = mqs

        return render(request, 'macro/cuttings.html', {
                'material_list': material_list,
                'cutting_list': cutting_list,
                'cutting_new': cutting_new,  
                'macro_list' : macro_list,
                'qm1' : qm1,  
                'qm2' : qm2,  
                'qm3' : qm3,
                'pk' : pk,                          
        })

def cuttings_edit(request, pk):
        cutting = get_object_or_404(Cutting, pk=pk)
        return cuttings(request, cutting)

def cuttings_delete(request, pk):
        cutting = get_object_or_404(Cutting, pk=pk)
        cutting.delete()
        return redirect('macro:cuttings')

def macros(request, macro=None):
        macro_list = Macro.objects.all()

        if request.method == 'POST':
                macro_new = MacroForm(request.POST, instance=macro)
                if macro_new.is_valid():
                        macro_new = macro_new.save() #Model Form에서 제공
                        return redirect('macro:macros')
        else:
                macro_new = MacroForm(instance=macro)        
        
        return render(request, 'macro/macros.html', {
                'macro_list': macro_list,
                'macro_new': macro_new,                                      
        })

def macros_edit(request, pk):
        macro = get_object_or_404(Macro, pk=pk)
        return macros(request, macro)

def macros_delete(request, pk):
        macro = get_object_or_404(Macro, pk=pk)
        macro.delete()
        return redirect('macro:macros')

def cuttings_test(request):
        cutting_list= Cutting.objects.all()
        macro_list = Macro.objects.all()
        return render(request, 'macro/test', {   
                'cutting_list' : cutting_list,
                'macro_list' : macro_list,               
        })

def canvas_ajax(request):
    result = '안녕하세요'
    return HttpResponse('result= {}'.format(result))
        



