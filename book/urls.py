from django.urls import path
from .views import BookSearch, FilterCategory, BookListView, RateCreateAPIView
from . import views

urlpatterns = [
    path("addbook/", views.add_book, name="addbook"),
    path("loadbook/", views.BookListView.as_view(), name="BookListView"),
    path("bookprofile/", views.bookprofile, name="bookprofile"),
    path("delete/", views.Delete, name="Delete"),
    #path('bookprofile/<int:id>/', views.bookprofile.as_view(), name='delete'),
    path('search/', views.BookSearch.as_view(), name="BookSearch"),
    path('category/', views.FilterCategory.as_view(), name="FilterCategory"),
    path('comments/' , views.CommentList.as_view(), name="comments"),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name = "comment-detail"),
    path('rate/create/', views.RateCreateAPIView.as_view(), name="RateCreate"),
    path('favourite/create/', views.Favouritecc, name="Favouritecc"),


]



