from yarns.views import YarnsListViews, YarnsDetailViews, BrandListViews, BrandDetailViews
from django.urls import path
from yarns import views


urlpatterns = [
    path('yarns/',views.YarnsListViews.as_view(), name='yarns-list'),
    path('yarns/<int:pk>',views.YarnsDetailViews.as_view (), name='yarns-detail'),
    path('brands/',views.BrandListViews.as_view(), name='brand_list'),
    path('brands/<int:pk>',views.BrandDetailViews.as_view()),
    path('products/',views.ProductListViews.as_view(), name='product_list'),
    path('products/<int:pk>',views.ProductDetailViews.as_view()),
]