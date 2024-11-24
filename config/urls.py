from django.contrib import admin
from django.urls import path, include 
from base import views
from django.contrib.auth.views import LogoutView
from base.views import LogoutView
 
urlpatterns = [
    path('admin/', admin.site.urls),
 
    # ログインアカウント
    path('login/', views.Login.as_view(), name='login'),
    path('login1/', views.Login1.as_view()),
    path('login2/', views.Login2.as_view()),
    path('login3/', views.Login3.as_view()),
    path('login4/', views.Login4.as_view()),
    path('login5/', views.Login5.as_view()),



    # Account
    path('logout/', LogoutView.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('account/', views.AccountUpdateView.as_view()),
    path('profile/', views.ProfileUpdateView.as_view()),
 
    # 顧客Order
    path('orders/', views.OrderIndexView.as_view()),
 
    # スタッフOrder
    path('order/', views.OrderStaffView.as_view(), name='order'),
    path('order01/', views.OrderAllStaffView.as_view(), name='order01'),
    path('order02/', views.OrderAll01StaffView.as_view(), name='order02'),

    path('order0000/', views.OrderStaffView01.as_view(), name='order0000'),
    path('order0100/', views.OrderAllStaffView01.as_view(), name='order0100'),
    path('order0200/', views.OrderAll01StaffView01.as_view(), name='order0200'),

    path('orderd/', views.OrderdStaffView.as_view(), name='orderd'),
    path('orderd00/', views.OrderdStaffView01.as_view(), name='orderd00'),
    path('ordernd/', views.OrderndStaffView.as_view(), name='ordernd'),
    path('ordernd00/', views.OrderndStaffView01.as_view(), name='ordernd00'),

    # アイテムを追加する
    path('item0000/', views.ItemCreateView.as_view(), name='item0000'),
    path('itemcate/', views.ItemCategoryView.as_view(), name='itemcate'),
    path('item1111/', views.ItemCountView.as_view(), name='item1111'),
    path('item1111/<str:pk>/', views.UpdateCount),
    path('item2222/<str:pk>/', views.Delitem),
    path('item3333/<str:pk>/', views.UpdateSort),

    # スタッフの会計画面
    path('payment/<str:id>/', views.OrderPaymentView.as_view(), name='payment'),
    path('payment01/', views.OrderPayment01View.as_view(), name='payment01'),
    path('paid/<str:id>', views.OrderPaidView.as_view(), name='paid'),

    # オーダーに入れる
    path('checkout/', views.ConfirmedView.as_view()),
    path('success/', views.PaySuccessView.as_view(), name='success'),
 
    # Cart
    path('cart/remove/<str:pk>/', views.remove_from_cart),
    path('cart/add/', views.AddCartView.as_view()),
    path('cart/', views.CartListView.as_view()),  # カートページ
 
    # Items
    path('items/<str:pk>/', views.ItemDetailView.as_view()),
    path('categories/<str:pk>/', views.CategoryListView.as_view()),
    path('tags/<str:pk>/', views.TagListView.as_view()),
 
    path('', views.IndexListView.as_view(), name="index"),  # トップページ

    #調理開始
    path("cooking/<str:id>/<str:pk>/", views.CookingView, name="cooking"),

    #調理開始
    path("served/<str:id>/<str:pk>/", views.ServedView, name="served"),

    #キャンセル
    path("cancel/<str:id>/<str:pk>/", views.CancelView, name="cancel"),


]

