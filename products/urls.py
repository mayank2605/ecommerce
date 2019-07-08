

from django.urls import path

from products.views import productlistview,productdetailslugview

urlpatterns = [
    #path('products-fbv/<int:pk>/',product_detail_view),
    #path('products/<int:pk>/',productdetailview.as_view()),
    path('products/<str:slug>/',productdetailslugview.as_view()), 
    #path('featured/<int:pk>/',productfeaturedDetailview.as_view()),
   #path('featured/',productfeaturedlistview.as_view()),
   
    #path('products-fbv/',product_list_view),
    path('products/',productlistview.as_view(),name='detail')


   
]

