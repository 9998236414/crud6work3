from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('add/',views.add),
    path('add/addrecord/', views.addrecord),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('update/updaterecord/<int:id>', views.updaterecord)
]