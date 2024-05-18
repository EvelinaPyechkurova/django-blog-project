from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # everything after 'articles/' is handled by 'articles' app url patterns
    path('articles/', include('articles.urls')),
    # everything after 'accounts/' is handled by 'accounts' app url patterns
    path('accounts/', include('accounts.urls')),
    path('about/', views.about),
    path('', article_views.article_list, name='home')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)