from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import redirect


class PostModel(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self):
        return reverse('post_detail_view', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    post = models.ForeignKey('blog.PostModel', related_name = 'comments', on_delete = models.CASCADE)
    author = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    approved_comment = models.BooleanField( default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return redirect('post_list_view')  # might need to do return redirect(reverse('post_list_view'))

    def __str__(self):
        return self.text
