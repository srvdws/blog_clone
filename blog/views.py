from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
    redirect_field_name = 'blog/postmodel_detail.html'  # should this not be a view? or url?
    form_class = forms.PostForm
    model = models.PostModel


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/postmodel_detail.html'  # should this not be a view? or url?
    form_class = forms.PostForm
    model = models.PostModel


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.PostModel
    success_url = reverse_lazy('postmodel_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = "blog/postmodel_list.html"
    model = models.PostModel

    def get_queryset(self):
        return models.PostModel.objects.filter(published_date__isn = True).order_by('created_date')


############################
#     COMMENTS VIEWS       #
############################

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(models.PostModel, pk = pk)

    if request == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = forms.CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(models.CommentModel, pk = pk)
    comment.approve()
    return redirect('post_detail', pk = comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(models.CommentModel, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk = post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(models.PostModel, pk = pk)
    post.publish()
    return redirect('post_detail', pk = pk)















