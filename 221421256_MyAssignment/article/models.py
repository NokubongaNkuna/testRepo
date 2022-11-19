from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name = models.CharField(max_length= 300)

    def __str__(self) :
        return self.Topic_name

        class article(models.Model):
            title = models.CharField(max_length=300)
            Topic =models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='articles')
            article = models.TextField(auto_now_add=True)

            def __str__(self):
                return self.title