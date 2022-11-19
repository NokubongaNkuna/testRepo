from django import forms
from .models import Article,Topic

class InputForm(forms.Form):
    name = forms.Charfield()
    email = forms.EmailField()

    class TopicForm(forms.ModelForm):
        class meta():
            model = Topic
            fields = ("topic_name")

            class ArticleForm(forms.ModelForm):
                class meta():
                    model = Article
                    Exception['created_at',]