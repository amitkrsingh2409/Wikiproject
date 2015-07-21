from django.db import models
from django.forms import ModelForm

# Create your models here.

class Wiki(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

class WikiModelForm(ModelForm):
    class Meta:
            model = Wiki
	    fields = ['title', 'body']
