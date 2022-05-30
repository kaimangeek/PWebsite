from django.shortcuts import render, redirect
from .models import Articles, Comment
from .forms import ArticlesForm
from rest_framework import generics, permissions
from django.views.generic import DetailView, UpdateView, DeleteView
from . import serializers
from .permissions import IsOwnerOrReadOnly


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class CommentView(DetailView):
    model = Comment
    template_name = 'news/comment_view.html'
    context_object_name = 'comment'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    permission_classes = [IsOwnerOrReadOnly]

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'
    permission_classes = [IsOwnerOrReadOnly]


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Вы заполнили поля неправильно'


    form = ArticlesForm()

    data = {
        'error': error,
        'form': form
    }

    return render(request, 'news/create.html', data)

class ArticlesList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticlesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticlesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]