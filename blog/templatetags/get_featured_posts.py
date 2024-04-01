from django import template

register = template.Library()

@register.simple_tag
def get_featured_posts(num_posts):
    from ..models import Article  # Replace with the path to your Article model
    featured_articles = Article.objects.filter(featured=True).order_by('-date')[:num_posts]
    return featured_articles