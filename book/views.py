from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView 
from django.http import Http404
from .models import AddBook
from .serializers import BookSerializer
from rest_framework import filters,generics,status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def add_book(request):
    data = dict(request.POST)
    print(data)
    addbook = AddBook.objects.filter(title=data['title'][0])
    if list(addbook) != []:
        return Response({'message': 'book has added'})
    addbook = AddBook.objects.create(      
        title=data['title'][0],
        genre=data['genre'][0],
        authors=data['authors'][0],
        publication_date=data['publication_date'][0],
    )
    addbook.save()
    if "Description" in request.data.keys() :
        addbook.Description=data['Description'][0]
    addbook.save()
    if "publisher" in request.data.keys() :
        addbook.publisher=data['publisher'][0]
    addbook.save()
    if "Base64" in request.data.keys() :
        base64=data['Base64'][0] 
        newsrc = open('book/image/' + str(addbook.id) + '.txt', 'a')
        newsrc.write(base64)
        newsrc.close()
        
    addbook.bookAvatar = 'book/image/' + str(addbook.id) + '.txt'
    addbook.save()
    return Response({'message': 'New book added'}, status=status.HTTP_201_CREATED)
    


class show_books(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        queryset = AddBook.objects.all()
        return queryset



@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def show_booksdddd(request):
    books = AddBook.objects.all()
    data = []
    print(books)
    for i in range(len(books)):
        data.append({'id':books[i].id,'name':books[i].title})
    return Response(data , status=status.HTTP_200_OK)


class bookprofile(APIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self,request,pk):
        book = AddBook.objects.get(id=data['id'][0])
        return book


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def bookprofilemmmmm(request):
    if request.method == 'POST':
        data = dict(request.POST)
        book = AddBook.objects.get(id=data['id'][0])
        serializer = BookSerializer(book)
        return Response(serializer.data)



class BookSearch(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


    def get_queryset(self):
        searchedword = self.request.query_params.get('q', None)
        queryset = AddBook.objects.all()
        if searchedword is None:
            return queryset
        if searchedword is not None:
            if searchedword == "":
                raise Http404
            queryset = queryset.filter(
                Q(title__icontains=searchedword) |
                Q(Description__icontains=searchedword) |
                Q(authors__icontains=searchedword) |
                Q(publisher__icontains=searchedword) 
        )
            if len(queryset) == 0:
                raise Http404
        return queryset




class FilterCategory(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        q = self.request.query_params.get('q', None)
        queryset = AddBook.objects.filter(Q(genre=q) | Q(authors=q))
        return queryset
        

class created(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(request):
        if request.method == 'POST':
            data = dict(request.POST)
            book = AddBook.objects.get(id=data['id'][0])
            return book
