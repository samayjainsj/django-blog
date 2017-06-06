from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from .forms import PostForm
from django.views.generic.edit import UpdateView
from .models import Post, Category

@is_logged_in
class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

@is_logged_in
# Create your views here.
class IndexView(LoggedInMixin, generic.ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()


# Save something in database
def add_post(request):
    # A HTTP POST?
    if request.method == 'POST':
        create_post_form = PostForm(request.POST)

        # Have we been provided with a valid form?
        if create_post_form.is_valid():
            # Save the new post to the database.
            create_post_form.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect(reverse('index'))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(create_post_form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        create_post_form = PostForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'posts/create.html', {'form': create_post_form})


def show_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'posts/show.html', {'post': post})


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect(reverse('index'))


class PostUpdate(UpdateView):
    model = Post
    fields = ('title', 'slug', 'body', 'category', 'user')
