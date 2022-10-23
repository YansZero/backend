from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('add/addRecord/',views.addRecord,name='addRecord'),
    path('update/<int:id>',views.update,name='update'),
    path('update/updateRecord/<int:id>',views.updateRecord,name='updateRecord'),
    path('delete/<int:id>',views.deleteRecord,name='delete'),
]