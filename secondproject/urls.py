from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),

    path('blog/', include('blog.urls')),

    path('portfolio/', include('portfolio.urls')),
]