from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("<str:username>/wishlist", views.wishlist_view, name="wishlist_view"),
    path("listing/<str:listing>/create_comment", views.create_comment, name="create_comment"),
    path("<str:username>/itemsowned", views.items_owned, name="items_owned"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category>", views.category_view, name="category_view"),
    path("listing/<str:listing>", views.listing_view, name="listing_view"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<str:listing>/addwishlist", views.addwishlist, name="add_wish_list"),
    path("listing/<str:listing>/removewishlist", views.removewishlist, name="remove_wish_list"),
    path("listing/<str:listing>/placebid", views.placebid, name="place_bid"),
    path("listing/<str:listing>/end", views.end_listing, name="end_listing"),
]

