from django.urls import path
from myapp import views
urlpatterns = [path('',views.home,name='home'),path('about/',views.about,name='about'),path('contact/',views.contact,name='contact'),path('products/',views.productView,name='productview'),path('products/',views.productList,name='products'),path('addproduct/',views.addProduct.as_view(),name='addproduct'),path('update/<int:pk>',views.updateProduct.as_view(),name='updateproduct'),path('productlist/',views.productList.as_view(),name='productlist'),path('productdetails/<int:pk>',views.productDetails.as_view(),name='productdetails'),path('deleteproduct/<int:pk>',views.deleteProduct.as_view(),name='deleteproduct'),
]
