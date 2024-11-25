# from django.shortcuts import render,redirect
# from .forms import ToDoForm
from django.urls import reverse_lazy
from .models import ToDo
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

# These below functions are for function views
# def todo_home(request): # todo_home or todo_list for showing all the todos
#     item_list=ToDo.objects.all().order_by('-date')
#     return render(request,"todoapp/home.html", {'todos': item_list})

# def todo_create(request):
#     if request.method == 'POST':
#         form=ToDoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         # else:
#         #     message.info(request,)
#     else:
#         form=ToDoForm()
    
#     context={
#         'form':form,
#         'title':'ToDo Form'
#     }
    
#     return render(request,"todoapp/todo_form.html",context)

# Class View

class ToDoListView(LoginRequiredMixin ,ListView):
    model = ToDo
    template_name = 'todoapp/home.html'
    context_object_name = 'todos'
    # ordering = ['-date']

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user).order_by('-date')

class ToDoCreateView(LoginRequiredMixin,CreateView):
    model = ToDo
    fields = ['task','details','status'] # or form_class = ToDoForm
    template_name = 'todoapp/todo_form.html'
    success_url = reverse_lazy('home')
    
    def form_valid (self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ToDoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = ToDo
    fields = ['task','details','status']
    template_name='todoapp/todo_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False
    
class ToDoDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = ToDo
    template_name = 'todoapp/todo_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False

@login_required
def clear_all(request):
    if request.method == "POST" :
        if request.user.is_authenticated:
            ToDo.objects.filter(user=request.user).delete()
    return redirect('home')

