from django.conf.urls import url
from django.urls import path
from food import views
from food import UploadFileView

from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [
#     path('food/', views.index, name='index'),
# ]


urlpatterns=[
    path('hello/', views.my_view),
    path('department/', views.departmentApi),
    path('bulkcreate/', UploadFileView.UploadFile)

]