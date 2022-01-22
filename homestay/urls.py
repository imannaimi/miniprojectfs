from homestay import views
from django.urls import path

urlpatterns=[
    path('', views.index, name="index_homestay"),
    path('create/', views.create_homestay, name="create_homestay"),
    path('update/<int:homestay_id>', views.update_homestay, name="update_homestay"),
    path('delete/<int:homestay_id>', views.delete_homestay, name="delete_homestay")
]