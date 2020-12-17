from django.urls import path
from hello.models import LogMessage
from . import views
from django.contrib import admin

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:20],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [    
    # path('', views.hello, name='hello'),
    # path("hello/<name>", views.hello_there, name="hello_there"),
    path("", home_list_view, name="home"),
    # path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("admin/", admin.site.urls),
]

