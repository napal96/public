from django.urls import path, re_path, register_converter
from . import views


app_name = 'macro'

urlpatterns =[    
    path('', views.orders, name='orders'),
    path('orders/', views.orders, name='orders'),
    path('orders_edit/<int:pk>', views.orders_edit, name='orders_edit'),
    path('orders_delete/<int:pk>', views.orders_delete, name='orders_delete'),
    path('materials/', views.materials, name='materials'),
    path('materials_edit/<int:pk>', views.materials_edit, name='materials_edit'),
    path('materials_delete/<int:pk>', views.materials_delete, name='materials_delete'),
    path('cuttings/', views.cuttings, name='cuttings'),  
    path('cuttings_edit/<int:pk>', views.cuttings_edit, name='cuttings_edit'),
    path('cuttings_delete/<int:pk>', views.cuttings_delete, name='cuttings_delete'), 
    path('macros/', views.macros, name='macros'),  
    path('macros_edit/<int:pk>', views.macros_edit, name='macros_edit'),
    path('macros_delete/<int:pk>', views.macros_delete, name='macros_delete'),
    path('ajax', views.canvas_ajax, name='canvas_ajax'),
]