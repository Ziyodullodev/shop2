from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from userapp.views import LoginView, RegView, Logout

from mainapp.views import Page_category, Page_category_all, Page_category_bolim, \
    Page_components, Page_content, Page_blank_starter, \
    Page_payment, Page_detail_product,  Page_index,  Page_index_2,\
    Page_profile_main, Page_profile_addres, Update_profile_adress,  Page_offers, Page_profile_setting,\
    Page_profile_seller, Page_listing_grid,  Page_listing_grid_all, Page_listing_large

from buyurtma.views import Page_shopping_cart, Page_profile_wishlist,  Page_profile_orders, Add_shopping_cart, \
    Delete_ProductView, Add_profile_wishlist, Page_profile_delete_wishlist, HisobotView, PaymentPageView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('page-user-login/', LoginView.as_view(), name="page-user-login"),
    path('page-user-register/', RegView.as_view(), name="page-user-register"),
    path('logout/', Logout, name="logout"),

    path('page-blank-starter/', Page_blank_starter.as_view(), name="page-blank-starter"),

    path('page-category/', Page_category_all.as_view(), name="page-category"),
    path('page-category-bolim/', Page_category_bolim.as_view(), name="page-category-bolimi"),
    path('page-category/<int:pk>/', Page_category.as_view(), name="page-category"),

    path('page-content/', Page_content.as_view(), name="page-content"),

    path('page-components/', Page_components.as_view(), name="page-components"),

    path('page-detail-product/<int:pk>/', Page_detail_product.as_view(), name="page-detail-product"),

    path('page-index/', Page_index.as_view(), name="page-index"),

    path('', Page_index_2.as_view(), name="page-index-2"),

    path('page-listing-grid/', Page_listing_grid_all.as_view(), name="page-listing-grid"),
    path('page-listing-grid/<int:pk>/', Page_listing_grid.as_view(), name="page-listing-grid"),

    path('page-listing-large/', Page_listing_large.as_view(), name="page-listing-large"),

    path('page-offers/', Page_offers.as_view(), name="page-offers"),

    path('page-payment/', Page_payment.as_view(), name="page-payment"),

    path('page-profile-address/', Page_profile_addres.as_view(), name="page-profile-address"),
    path('add-profile-address/', Update_profile_adress.as_view(), name="del"),



    path('page-profile-main/', Page_profile_main.as_view(), name="page-profile-main"),

    path('page-profile-orders/', Page_profile_orders.as_view(), name="page-profile-orders"),

    path('page-profile-seller/', Page_profile_seller.as_view(), name="page-profile-seller"),

    path('page-profile-setting/', Page_profile_setting.as_view(), name="page-profile-setting"),

    path('page-profile-wishlist/', Page_profile_wishlist.as_view(), name="page-profile-wishlist"),
    path('add-profile-wishlist/<int:pk>/', Add_profile_wishlist.as_view(), name="add-profile-wishlist"),
    path('delete/<int:pk>/', Page_profile_delete_wishlist.as_view(), name="delete"),

    path('page-shopping-cart/', Page_shopping_cart.as_view(), name="page-shopping-cart"),
    path('add-shopping-cart/<int:pk>/', Add_shopping_cart.as_view(), name="add-shopping-cart"),
    path('remove/<int:pk>/', Delete_ProductView.as_view(), name="remove"),


    path('payment/<int:pk>', PaymentPageView.as_view(), name="payment"),
    # path('payment2/<int:pk>', PaymentPageView.as_view(), name="payment-post"),
    path('hisobot/', HisobotView.as_view(), name="hisobot"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)