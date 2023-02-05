from django.db import models
# added below
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
# from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField


# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = (
                ('draft', 'Draft'),
                ('published', 'Published'))
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    contributor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="csiblog_posts")
    date = models.DateTimeField(auto_created=True)
    revised = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    content = RichTextField(max_length=5000, blank=True, null=True)
    no_of_likes = models.ManyToManyField(
        User, related_name="csiblog_no_of_likes")
    excerpt = models.TextField()
    status = models.CharField(max_length=10)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name + ' |  ' + (str(self.contributor))

    # def get_absolute_url(self):
    #     return reverse("postadd", kwargs={"slug": self.slug})

    # def no_of_likes(self):
    #     return self.no_of_likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="csiblog_comment")
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="csiblog_posts")
    added = models.DateTimeField(auto_created=True)
    mainbody = RichTextField(max_length=5000, blank=True, null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-added']

    def __str__(self):
        return self.name + ' | ' + (str(self.post_contributor))
