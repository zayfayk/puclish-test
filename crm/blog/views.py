from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer, Category
from .forms import CustomerForm, CustomerEdit

class HomeView(ListView):
    model = Customer
    template_name = 'home.html'
    ordering = ['-post_date']
    
    def get_context_data(self,  *args, **kwargs):

        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetalisView(DetailView):
    model = Customer
    template_name = 'post_detalis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_customers'] = Customer.objects.filter(author=self.object.author).exclude(pk=self.object.pk)
        return context

class AddPostView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    fields = ['customer_country_catalog']
    template_name = 'add_category.html'
    success_url = reverse_lazy('home')

class Updatepost(UpdateView):
    model = Customer
    form_class = CustomerEdit
    template_name = 'update_post.html'

class DeletPost(DeleteView):
    model = Customer
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')

class UserPostsListView(ListView):
    model = Customer
    template_name = 'user_posts_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.filter(author=self.request.user)

def CategoryView(request, cats):
    category_post = Customer.objects.filter(category__customer_country_catalog=cats)
    return render(request, 'Categories.html', {'cats': cats, 'category_post': category_post})
