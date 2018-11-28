from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone


class AboutView(TemplateView):
    template_name = 'about_page.html'


class PostListView(ListView):
    model = models.PostModel

    def get_queryset(self):
        return models.PostModel.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = models.PostModel


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'  # should this not be a view? or url?
    form_class = forms.PostForm
    model = models.PostModel


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'  # should this not be a view? or url?
    form_class = forms.PostForm
    model = models.PostModel


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.PostModel
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = "blog/post_list.html"
    model = models.PostModel

    def get_queryset(self):
        return models.PostModel.objects.filter(published_date__isn = True).order_by('created_date')


