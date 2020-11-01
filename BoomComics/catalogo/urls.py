from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'), 
    path('Mangas/<int:tip_list>',views.mangas,name='manga'), 
    path('DC/<int:tip_dc>',views.dc,name='dc'), 
    path('MARVEL/<int:tip_m>',views.marvel,name='marvel'), 
    path('contacto/',views.contacto,name='contacto'),
    path('comic/<str:pk>',views.ComicDetailView.as_view(),name='comic-detail'),   
]
urlpatterns+=[
    path('comic/create/',views.ComicCreate.as_view(),name='comic_create'),
    path('comic/<str:pk>/update',views.ComicUpdate.as_view(),name='comic_update'),
    path('comic/<str:pk>/delete',views.ComicDelete.as_view(),name='comic_delete'),
]
