from django.urls import path
from .views import showarticle,show_topics,send_input_data,create_topic

app_name = 'My Blog'

urlpatterns = [

    path('', showarticle),
    path('topics',show_topics),
    path('input',send_input_data),
    path('topic/add,create_topic'),
    path('topic/add',create_topic, name='add_topic')

]