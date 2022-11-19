from django.shortcuts import render,redirect
from .models import Topic,Article
from . import forms

# Create your views here.

def create_topic(request):
  if request.method == "post":
    form = forms.TopicForm(request.post)
    if forms.is_valid():
      forms.save()

  else:

   print("You made an error")
 
  return render(request,'input.html',{'form':forms})
forms= forms.TopicForm()

 

def send_input_data(request):
  form = forms.InputForm()
  if request.method =="post":
    form= forms.InputForm(request.post)
    if form.is_valid():
      print("Form Is Valid")
  else:
   print( "Form Is Not Valid")

  return render(request,'input.html',{'form':form})

def show_topics(request):
  topics = Topic.objects.all()
  return render(request,'topic.html',{'topics':topics})

def showarticle(request) :
    title = 'My last project'
    author = 'Nokubonga'
    article_text = """
    Industrial revolutions have always dominated and changed the world in a big way.
     The first one happened way back in 18th century, and the second industrial revolution
      occurred almost two centuries later, in the 20th century. The third one happened
       only a half-century later, while the fourth one was observed within three decades.
     By the speed these transformations are occurring, a fifth industrial revolution is already 
     around the corner.

     The next technology revolution will be faster and more scalable, and will be adopted by a lot more
      people as compared to the previous ones. Everyone on the planet will undergo a “personal” revolution 
      by the kind of technology at their disposal. 3D-printing, wearable technology, robots.
       driverless cars … everything will be readily available and will make lives simpler and faster.
        With every industrial revolution brought a substantial increase in the GDP, 
        and lifestyles improved manifold. The next revolutionary technology, however, does not aim to
         simply improve the lifestyle or help people make more money; rather, it focuses on the higher 
         form of intelligence. Now humankind is ready to take the big plunge and step into space.
          With ideas such as SpaceX and affordable space travel,
           a future that we cannot imagine today might be possible tomorrow.
    
    """

    return render(request,'blog.html',{'title':title,'author':author,'article_text':article_text})