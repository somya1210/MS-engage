# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Query,Comment
from query.forms import QueryForm,CommentForm

# using class based generic views for query app
#1st for list view of query
class CommentViews(generic.CreateView):
    model=Comment
    form_class = CommentForm
    template_name='query/create_comment.html'
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

def LikeViews(request,pk):
  post=get_object_or_404(Query,id=request.POST.get('query_id'))
  liked=False
  if post.likes.filter(id=request.user.id).exists():
      post.likes.remove(request.user)
      liked=False
  else:
      post.likes.add(request.user)
      liked=True
  return HttpResponseRedirect(reverse('post_detail',args=[str(post.slug)]))

class HomePage(generic.ListView):

  queryset = Query.objects.all().order_by('-created_on')
  template_name = 'query/index.html'



class DetailView(generic.DetailView):
 model = Query
 template_name = 'query/query_detail.html'
 def get_context_data(self,*args,**kwargs):
     context=super(DetailView,self).get_context_data(*args,**kwargs)
     forlike=get_object_or_404(Query,slug=self.kwargs['slug'])
     total_like=forlike.total_likes()
     context["total_like"]=total_like
     liked=False
     if forlike.likes.filter(id=self.request.user.id).exists():
         liked=True
     context["liked"]=liked
     return context



class AddQueryview(generic.CreateView):
    model=Query
    form_class = QueryForm
    template_name = 'query/create_query.html'




#4th update your query

class UpdateQueryView(generic.UpdateView):
    model = Query
    form_class = QueryForm
    template_name = 'query/update_query.html'

#5th delete query

class DeleteQueryView(generic.DeleteView):
    model = Query
    template_name = 'query/remove_query.html'
    success_url = reverse_lazy('home')















