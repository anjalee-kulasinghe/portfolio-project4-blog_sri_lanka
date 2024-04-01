from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import CommentForm
from .templatetags import get_featured_posts

class Index(View):
    def get(self, request):
        featured_posts = get_featured_posts.get_featured_posts(3)  # Pass the argument here
        context = {'featured_posts': featured_posts}
        return render(request, 'blog/index.html', context)

# Define a class-based view for displaying a list of articles
class BlogView(ListView):
    # Display a list of articles on the blog page
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/blog.html'
    paginate_by = 1


# Define a class-based view for displaying a list of featured articles
class Featured(ListView):
    # Display a list of featured articles
    model = Article
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blog/featured.html'
    paginate_by = 1

# Define a class-based view for displaying details of a single article
class DetailArticleView(DetailView):
    # Display details of a single article
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        # Provide additional context data for the template
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        context['pk'] = self.kwargs.get('pk')  # Add this line to include pk in the context
        return context

# Define a class-based view for handling user liking or unliking an article
class LikeArticle(View):
    # Handle user liking or unliking an article
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)
        article.save()
        return redirect('detail_article', pk)

# Define a class-based view for handling deletion of an article
class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Handle deletion of an article
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        # Ensure that only the author of the article can delete it
        article = Article.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == article.author.id

# Define a function for adding comments to an article
@login_required
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.commenter = request.user
            comment.save()
            # Redirect back to the article detail view after adding the comment
            return redirect('detail_article', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'article': article})


# Define a function for search with key word
def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        # Perform case-insensitive search on both title and content fields
        results = Article.objects.filter(title__icontains=query) | Article.objects.filter(content__icontains=query)
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})