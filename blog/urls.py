from django.urls import path, include 
from .views import Index, BlogView, DetailArticleView, LikeArticle, Featured, DeleteArticleView, add_comment, search, add_article
from django.conf.urls.static import static
from django.conf import settings 

# URL patterns for the application
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),  # Including TinyMCE URLs
    path('', Index.as_view(), name='index'),  # Mapping the root URL to the Index view
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),  # Mapping article detail URLs
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),  # Mapping article like URLs
    path('featured/', Featured.as_view(), name='featured'),  # Mapping featured articles URLs
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),  # Mapping article deletion URLs
    path('cityguide/', include('cityguide.urls')),  # Including cityguide URLs
    path('food/', include('food.urls')),  # Including food URLs
    path('traveltips/', include('traveltips.urls')),  # Including traveltips URLs
    path('blog/', BlogView.as_view(), name='blog'),  # Mapping blog URLs
    path('article/<int:pk>/add_comment/', add_comment, name='add_comment'),  # Mapping add_comment URLs
    path('search/', search, name='search'),
    path('add_article/', add_article, name='add_article'),
]

# Adding URL patterns for serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
