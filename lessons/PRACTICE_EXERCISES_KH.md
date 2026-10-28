# ឧបាយកលបង្ហាប់ Django - អនុវត្ត 60 ល្អបំផុត
## (Django Practical Exercises - 60 Practice Problems)

---

## ⚙️ ផ្នែកទី១៖ គ្រឹះនៃស្ថាបត្យកម្ម (10 Exercises)

### ផ្នែកទី១: គ្រឹះនៃស្ថាបត្យកម្ម និងការរៀបចំដំបូង

**១. បង្កើត Virtual Environment មួយថ្មីសម្រាប់គម្រោងថ្មី**
```bash
# ចម្លើយ
python3 -m venv venv_myproject
source venv_myproject/bin/activate
pip install Django==4.2.0
pip freeze > requirements.txt
```
**ឧបាយកលបង្ហាប់:** ចូលក្នុងថតគម្រោងថ្មី, បង្កើត venv, ដំឡើង Django, រក្សាទុក dependencies។

---

**២. បង្កើត Django project និង 3 apps ផ្សេងគ្នា**
```bash
# ចម្លើយ
django-admin startproject myproject .
python manage.py startapp accounts
python manage.py startapp blog
python manage.py startapp comments
```
**ឧបាយកលបង្ហាប់:** ប្រើ startproject និង startapp commands យ៉ាងត្រឹមត្រូវ។

---

**៣. ពន្យល់ឧបន្ថយលើ MVC vs MVT** 
```python
# MVC: Model, View (controller), Controller (middleware)
# MVT: Model, View (logic), Template (HTML)

# Django ឆ្លើយលើ MVT ដែលខុសគ្នាពី MVC ពីព្រោះ:
# - Template (HTML) ត្រូវបានរបរខ្លួនវាផ្ទាល់
# - View ធ្វើការងារដូច Controller
```
**ឧបាយកលបង្ហាប់:** ទីកន្លែង, ឧបាយកលបង្ហាប់ architecture ផ្សេងគ្នា។

---

**៤. កែប្រែ settings.py ដើម្បីបន្ថែម 2 custom apps**
```python
# ចម្លើយ - settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # (...ថែមលើ apps)
    'accounts',        # Custom app
    'blog',           # Custom app
]
```
**ឧបាយកលបង្ហាប់:** ស្វែងរក INSTALLED_APPS, ដាក់ apps ឌើងក។

---

**៥. កម្ពស់ DATABASE URL ក្នុង settings.py សម្រាប់ PostgreSQL**
```python
# ចម្លើយ
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
**ឧបាយកលបង្ហាប់:** ផ្លាស់ប្តូរ ENGINE, ដាក់ credentials។

---

**៦. បង្កើត .env file ដើម្បីរក្សាទុក secret keys**
```bash
# .env file
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
```
**ឧបាយកលបង្ហាប់:** ដាក់ configuration variables ឯកក្នុង .env file។

---

**៧. ដាក់ใช.env variables ក្នុង settings.py**
```python
# ចម្លើយ
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
```
**ឧបាយកលបង្ហាប់:** ប្រើប្រាស់ decouple library ដើម្បីលើក .env variables។

---

**៨. កំណត់ STATIC_ROOT និង MEDIA_ROOT ក្នុង settings.py**
```python
# ចម្លើយ
import os

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
**ឧបាយកលបង្ហាប់:** កំណត់ paths សម្រាប់ static និង uploaded files។

---

**៩. បង្កើត custom management command**
```python
# management/commands/seed.py
from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):
    def handle(self, *args, **options):
        # ដាក់ seed data
        for i in range(10):
            Account.objects.create(username=f'user{i}', email=f'user{i}@test.com')
```
**ឧបាយកលបង្ហាប់:** បង្កើត custom management commands។

---

**១០. តែងទម្រង់ URL routing សម្រាប់ 3 apps**
```python
# project/urls.py - ចម្លើយ
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('comments/', include('comments.urls')),
]
```
**ឧបាយកលបង្ហាប់:** រៀប URL patterns សម្រាប់ projects ដ៏ធំ។

---

## 📊 ផ្នែកទី២៖ ស្រទាប់ទិន្នន័យ (10 Exercises)

**១១. បង្កើត User Model ដែលមាន 5 different field types**
```python
# ចម្លើយ - accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)  # TextField
    age = models.IntegerField()  # IntegerField
    is_premium = models.BooleanField(default=False)  # BooleanField
    joined_date = models.DateField(auto_now_add=True)  # DateField
    experience = models.DecimalField(max_digits=5, decimal_places=2)  # DecimalField
    
    def __str__(self):
        return self.user.username
```
**ឧបាយកលបង្ហាប់:** ប្រើ CharField, TextField, IntegerField, BooleanField, DateField, DecimalField។

---

**១២. បង្កើត Post Model ដែលមាន ForeignKey ទៅ User**
```python
# ចម្លើយ - blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
```
**ឧបាយកលបង្ហាប់:** ស្វែងយល់ ForeignKey, on_delete choices, related_name។

---

**១៣. បង្កើត Comment Model ដែលមាន ForeignKey ទៅ Post និង User (Many-to-Many simulation)**
```python
# ចម្លើយ - comments/models.py
from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
```
**ឧបាយកលបង្ហាប់:** បង្កើត relationships រវាង 3 models។

---

**១៤. បង្កើត Tag Model មាន ManyToManyField ទៅ Post**
```python
# ចម្លើយ - blog/models.py (ថែមលើ)
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')
    
    def __str__(self):
        return self.name
```
**ឧបាយកលបង្ហាប់:** ស្វែងយល់ ManyToManyField relationships។

---

**១៥. ដឹងលេខ ORM queries (CRUD) សម្រាប់ Post Model**
```python
# ចម្លើយ - Django ORM
# CREATE
post = Post.objects.create(title='Hello', content='World', author_id=1)

# READ
posts = Post.objects.all()
post = Post.objects.get(id=1)
posts = Post.objects.filter(author_id=1)

# UPDATE
post = Post.objects.get(id=1)
post.title = 'Updated Title'
post.save()

# DELETE
post.delete()
# ឬ
Post.objects.filter(id=1).delete()
```
**ឧបាយកលបង្ហាប់:** CRUD operations ដោយប្រើ ORM។

---

**១៦. តែងលេខ migration files សម្រាប់ 2 apps**
```bash
# ចម្លើយ
python manage.py makemigrations accounts
python manage.py makemigrations blog
python manage.py migrate
python manage.py showmigrations
```
**ឧបាយកលបង្ហាប់:** លើកយក migrations, មើលលក្ខណៈពិសេស។

---

**១៧. ដោះស្រាយ migration conflicts រវាង 2 apps**
```bash
# ចម្លើយ - ឧបករណ៍ការបម្រុង
python manage.py showmigrations
python manage.py migrate --plan
python manage.py migrate accounts
python manage.py migrate blog
```
**ឧបាយកលបង្ហាប់:** រៀប migrations ពិតប្រាកដ។

---

**១៨. បង្កើត model validators សម្រាប់ Email និង Age**
```python
# ចម្លើយ - accounts/models.py
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
from django.db import models

class Account(models.Model):
    email = models.EmailField(validators=[EmailValidator()])
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(120)])
    username = models.CharField(max_length=50, unique=True)
```
**ឧបាយកលបង្ហាប់:** ដាក់ field validators។

---

**១៩. ដឹងលេខ Meta options (ordering, verbose_name, unique_together)**
```python
# ចម្លើយ - blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']  # ជីវិតលម្អិត
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        indexes = [
            models.Index(fields=['author', 'created_at']),
        ]
        unique_together = ['author', 'title']
```
**ឧបាយកលបង្ហាប់:** Meta options សម្រាប់ models។

---

**២០. បង្កើត custom model methods (save, delete, __str__)**
```python
# ចម្លើយ - blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Custom logic មុនពេលរក្សាទុក
        self.title = self.title.title()
        super().save(*args, **kwargs)
    
    def get_comment_count(self):
        return self.comments.count()
```
**ឧបាយកលបង្ហាប់:** Override model methods។

---

## 🔗 ផ្នែកទី៣៖ URL Routing និង Views (10 Exercises)

**២១. បង្កើត app URLs ដែលមាន 5 path patterns ផ្សេងគ្នា**
```python
# ចម្លើយ - blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/update/', views.post_update, name='post_update'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
]
```
**ឧបាយកលបង្ហាព:** CRUD URL patterns។

---

**២២. បង្កើត URL patterns ដែលមាន dynamic parameters**
```python
# ចម្លើយ - blog/urls.py (ថែមលើ)
urlpatterns = [
    path('author/<str:username>/', views.author_posts, name='author_posts'),
    path('tag/<int:tag_id>/', views.tag_posts, name='tag_posts'),
    path('post/<slug:slug>/', views.post_detail_slug, name='post_detail_slug'),
]

# views.py
def author_posts(request, username):
    posts = Post.objects.filter(author__username=username)
    return render(request, 'blog/author_posts.html', {'posts': posts})

def tag_posts(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    posts = tag.posts.all()
    return render(request, 'blog/tag_posts.html', {'posts': posts, 'tag': tag})
```
**ឧបាយកលបង្ហាព:** Dynamic URL patterns ដែលមាន parameters។

---

**២៣. បង្កើត FBV សម្រាប់ listing posts ដែលមាន pagination**
```python
# ចម្លើយ - blog/views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)  # 10 posts per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

# template
{% if page_obj.has_other_pages %}
    <nav>
        {% if page_obj.has_previous %}
            <a href="?page=1">First</a>
            <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
        {% endif %}
        
        <span>{{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
        
        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
        {% endif %}
    </nav>
{% endif %}
```
**ឧបាយកលបង្ហាព:** Pagination ក្នុង FBV និង templates។

---

**២៤. បង្កើត FBV ដែលមាន search និង filtering**
```python
# ចម្លើយ - blog/views.py
from django.db.models import Q
from django.shortcuts import render
from .models import Post

def post_search(request):
    query = request.GET.get('q', '')
    posts = Post.objects.all()
    
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct()
    
    return render(request, 'blog/post_search.html', {
        'posts': posts,
        'query': query
    })
```
**ឧបាយកលបង្ហាព:** Search និង filtering ក្នុង views។

---

**២៥. បង្កើត CBV ListView ដែលមាន paginate_by**
```python
# ចម្លើយ - blog/views.py
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context
```
**ឧបាយកលបង្ហាព:** CBV ListView ដែលមាន pagination។

---

**២៦. បង្កើត CBV DetailView ដែលមាន related objects**
```python
# ចម្លើយ - blog/views.py
from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['author_posts'] = Post.objects.filter(
            author=self.object.author
        ).exclude(id=self.object.id)[:5]
        return context
```
**ឧបាយកលបង្ហាព:** DetailView ដែលមាន related objects។

---

**២៧. បង្កើត CBV CreateView ដែលមាន success_url ដែលជ្ឈូលវិលដែលបាន**
```python
# ចម្លើយ - blog/views.py
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```
**ឧបាយកលបង្ហាព:** CreateView ដែលមាន automatic field filling។

---

**២៨. បង្កើត CBV UpdateView និង DeleteView ដែលមាន permission checking**
```python
# ចម្លើយ - blog/views.py
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')
    
    def test_func(self):
        return self.get_object().author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    
    def test_func(self):
        return self.get_object().author == self.request.user
```
**ឧបាយកលបង្ហាព:** Permission checking ក្នុង CBV។

---

**២៩. បង្កើត FBV ដែលបង្ហាញទម្រង់ Create និង Update**
```python
# ចម្លើយ - blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:
        return redirect('blog:post_list')
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})
```
**ឧបាយកលបង្ហាព:** Create និង Update FBV ដែលប្រើ ModelForm។

---

**៣០. បង្កើត decorator សម្រាប់ check object ownership**
```python
# ចម្លើយ - blog/decorators.py
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Post

def is_post_owner(function):
    def wrapper(request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            return HttpResponseForbidden('You are not allowed to access this post')
        return function(request, pk, *args, **kwargs)
    return wrapper

# Usage
@login_required
@is_post_owner
def post_update(request, pk):
    ...
```
**ឧបាយកលបង្ហាព:** Custom decorators សម្រាប់ permission checking។

---

## 📝 ផ្នែកទី៤៖ Templates និង Forms (10 Exercises)

**៣១. បង្កើត base template ដែលមាន navbar, footer, និង block content**
```html
<!-- ចម្លើយ - templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Blog{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{% url 'blog:post_list' %}">My Blog</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'blog:post_list' %}">Home</a>
                    </li>
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'blog:post_create' %}">Create Post</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'login' %}">Login</a>
                    </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
    
    <main class="container my-5">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                </div>
            {% endfor %}
        {% endif %}
        
        {% block content %}{% endblock %}
    </main>
    
    <footer class="bg-light text-center py-4 mt-5">
        <p>&copy; 2024 My Blog. All rights reserved.</p>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
**ឧបាយកលបង្ហាព:** Template inheritance ដែលមាន navbar, footer, messages។

---

**៣២. បង្កើត child template ដែលមាន extends និង block overrides**
```html
<!-- ចម្លើយ - templates/blog/post_list.html -->
{% extends 'base.html' %}

{% block title %}Blog Posts - My Blog{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8">
        <h1>Blog Posts</h1>
        {% if posts %}
            {% for post in posts %}
            <div class="card mb-4">
                <div class="card-body">
                    <h5 class="card-title">
                        <a href="{% url 'blog:post_detail' post.pk %}">{{ post.title }}</a>
                    </h5>
                    <p class="card-text">{{ post.content|truncatewords:30 }}</p>
                    <small class="text-muted">By {{ post.author.username }} on {{ post.created_at|date:"M d, Y" }}</small>
                </div>
            </div>
            {% endfor %}
        {% else %}
            <p>No posts found.</p>
        {% endif %}
    </div>
    
    <div class="col-md-4">
        <h3>Sidebar</h3>
        <!-- Sidebar content -->
    </div>
</div>
{% endblock %}
```
**ឧបាយកលបង្ហាព:** Child template ដែលប្រើ extends និង override blocks។

---

**៣३. ដឹងលេខ template tags និង filters**
```html
<!-- ចម្លើយ -->
<!-- Tags -->
{% if condition %}...{% endif %}
{% for item in items %}...{% endfor %}
{% for item in items %}...{% empty %}...{% endfor %}
{% url 'blog:post_detail' post.pk %}
{% csrf_token %}

<!-- Filters -->
{{ post.created_at|date:"M d, Y" }}
{{ post.content|truncatewords:30 }}
{{ post.title|lower }}
{{ post.title|upper }}
{{ post.title|slugify }}
{{ 123.456|floatformat:2 }}
{{ items|length }}
{{ items|first }}
{{ items|last }}
```
**ឧបាយកលបង្ហាព:** Common template tags និង filters។

---

**៣४. បង្កើត include template សម្រាប់ reusable component**
```html
<!-- templates/blog/partials/post_card.html -->
<div class="card mb-4">
    <div class="card-body">
        <h5 class="card-title">
            <a href="{% url 'blog:post_detail' post.pk %}">{{ post.title }}</a>
        </h5>
        <p class="card-text">{{ post.content|truncatewords:20 }}</p>
        <small class="text-muted">By {{ post.author.username }}</small>
    </div>
</div>

<!-- templates/blog/post_list.html -->
{% extends 'base.html' %}

{% block content %}
{% for post in posts %}
    {% include 'blog/partials/post_card.html' %}
{% endfor %}
{% endblock %}
```
**ឧបាយកលបង្ហាព:** Include templates សម្រាប់ reusable components។

---

**៣५. បង្កើត ModelForm សម្រាប់ Post model**
```python
# ចម្លើយ - blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter post content'
            }),
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return title
```
**ឧបាយកលបង្ហាព:** ModelForm ដែលមាន custom widgets និង validation។

---

**៣६. បង្កើត custom Form ដែលមាន multiple models**
```python
# ចម្លើយ - blog/forms.py
from django import forms
from .models import Post, Comment

class PostWithCommentForm(forms.Form):
    post_title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    post_content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    comment_text = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    def clean_post_title(self):
        title = self.cleaned_data.get('post_title')
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError('A post with this title already exists.')
        return title
```
**ឧបាយកលបង្ហាព:** Custom forms ដែលមាន multiple model fields។

---

**៣७. ដឹងលេខ form rendering methods (as_p, as_table, as_ul, render manually)**
```html
<!-- ចម្លើយ - templates/blog/post_form.html -->

<!-- Method 1: as_p -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>

<!-- Method 2: as_table -->
<form method="post">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <button type="submit">Submit</button>
</form>

<!-- Method 3: as_ul -->
<form method="post">
    {% csrf_token %}
    {{ form.as_ul }}
    <button type="submit">Submit</button>
</form>

<!-- Method 4: Manual rendering -->
<form method="post">
    {% csrf_token %}
    <div class="form-group">
        <label for="{{ form.title.id_for_label }}">{{ form.title.label }}</label>
        {{ form.title }}
        {% if form.title.errors %}
            <small class="text-danger">{{ form.title.errors }}</small>
        {% endif %}
    </div>
    
    <div class="form-group">
        <label for="{{ form.content.id_for_label }}">{{ form.content.label }}</label>
        {{ form.content }}
        {% if form.content.errors %}
            <small class="text-danger">{{ form.content.errors }}</small>
        {% endif %}
    </div>
    
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```
**ឧបាយកលបង្ហាព:** Different form rendering methods និង error display។

---

**៣८. បង្កើត form ដែលមាន CSRF protection និង validation errors**
```html
<!-- ចម្លើយ - templates/blog/comment_form.html -->
<form method="post">
    {% csrf_token %}
    
    {% if form.non_field_errors %}
        <div class="alert alert-danger">
            {% for error in form.non_field_errors %}
                <p>{{ error }}</p>
            {% endfor %}
        </div>
    {% endif %}
    
    <div class="form-group mb-3">
        <label for="{{ form.text.id_for_label }}" class="form-label">Comment</label>
        <textarea name="text" id="{{ form.text.id_for_label }}" class="form-control" rows="4"></textarea>
        {% if form.text.errors %}
            <div class="text-danger small mt-1">
                {% for error in form.text.errors %}
                    <p>{{ error }}</p>
                {% endfor %}
            </div>
        {% endif %}
    </div>
    
    <button type="submit" class="btn btn-primary">Post Comment</button>
</form>
```
**ឧបាយកលបង្ហាព:** CSRF protection និង form error handling។

---

**៣९. ដឹងលេខ dynamic form field rendering ក្នុង template**
```html
<!-- ចម្លើយ - templates/blog/dynamic_form.html -->
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    
    {% for field in form %}
    <div class="form-group mb-3">
        {% if field.field.widget.input_type == 'checkbox' %}
            <div class="form-check">
                {{ field }}
                <label class="form-check-label" for="{{ field.id_for_label }}">
                    {{ field.label }}
                </label>
            </div>
        {% elif field.field.widget.input_type == 'radio' %}
            <fieldset>
                <legend>{{ field.label }}</legend>
                {{ field }}
            </fieldset>
        {% elif field.type == 'FileField' %}
            <label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>
            {{ field }}
        {% else %}
            <label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>
            {{ field }}
        {% endif %}
        
        {% if field.errors %}
            <div class="text-danger small">
                {% for error in field.errors %}
                    {{ error }}
                {% endfor %}
            </div>
        {% endif %}
    </div>
    {% endfor %}
    
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```
**ឧបាយកលបង្ហាព:** Dynamic form field rendering ក្នុង templates។

---

**៤០. បង្កើត inline formset សម្រាប់ related models**
```python
# ចម្លើយ - blog/forms.py
from django.forms import inlineformset_factory
from .models import Post, Comment

CommentFormSet = inlineformset_factory(
    Post,
    Comment,
    fields=['text'],
    extra=1  # Number of empty forms
)

# views.py
def post_with_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        formset = CommentFormSet(request.POST, instance=post)
        if formset.is_valid():
            formset.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        formset = CommentFormSet(instance=post)
    
    return render(request, 'blog/post_with_comments.html', {
        'formset': formset,
        'post': post
    })

# template
<form method="post">
    {% csrf_token %}
    {{ formset.management_form }}
    
    {% for form in formset %}
        {{ form.as_p }}
    {% endfor %}
    
    <button type="submit">Save</button>
</form>
```
**ឧបាយកលបង្ហាព:** Inline formsets សម្រាប់ related models។

---

## 🔐 ផ្នែកទី៥៖ Admin និង Authentication (10 Exercises)

**៤១. ចុះឈ្មោះ model ក្នុង admin.py ដែលមាន list_display**
```python
# ចម្លើយ - blog/admin.py
from django.contrib import admin
from .models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'comment_count']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content', 'author__username']
    
    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = 'Number of Comments'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'post', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['text', 'author__username', 'post__title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
```
**ឧបាយកលបង្ហាព:** Admin registration ដែលមាន list_display, list_filter, search_fields។

---

**៤२. បង្កើត custom admin actions សម្រាប់ bulk operations**
```python
# ចម្លើយ - blog/admin.py
from django.contrib import admin
from .models import Post

def mark_as_published(modeladmin, request, queryset):
    # Custom action
    queryset.update(status='published')
mark_as_published.short_description = "Mark selected posts as published"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at']
    actions = [mark_as_published]
    
    def mark_as_draft(self, request, queryset):
        queryset.update(status='draft')
    mark_as_draft.short_description = "Mark selected posts as draft"
```
**ឧបាយកលបង្ហាព:** Custom admin actions សម្រាប់ bulk operations។

---

**៤३. បង្កើត readonly_fields ក្នុង admin**
```python
# ចម្លើយ - blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    readonly_fields = ['created_at', 'updated_at', 'slug']
    
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'content', 'author')
        }),
        ('Metadata', {
            'fields': ('slug', 'created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )
```
**ឧបាយកលបង្ហាព:** Readonly fields និង fieldsets ក្នុង admin។

---

**៤४. ឌើងក filter_horizontal សម្រាប់ ManyToManyField**
```python
# ចម្លើយ - blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    filter_horizontal = ['tags']  # For ManyToMany fields
    
    # Or use filter_vertical
    # filter_vertical = ['tags']
```
**ឧបាយកលបង្ហាព:** filter_horizontal សម្រាប់ ManyToMany relations។

---

**៤५. បង្កើត custom admin site template**
```python
# ចម្លើយ - project/urls.py
from django.contrib import admin

admin.site.site_header = "Student Management Admin"
admin.site.site_title = "Student Admin"
admin.site.index_title = "Welcome to Student Management Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    ...
]

# Create custom admin template
# templates/admin/base_site.html
{% extends "admin/base_site.html" %}

{% block title %}Custom Title - Admin{% endblock %}

{% block branding %}
<h1 id="site-name">
    <a href="{% url 'admin:index' %}">🎓 Student Management System</a>
</h1>
{% endblock %}
```
**ឧបាយកលបង្ហាព:** Custom admin site configuration និង templates។

---

**៤६. ដឹងលេខ Django authentication system ដូច User, Group, Permission**
```python
# ចម្លើយ
# Create user
from django.contrib.auth.models import User
user = User.objects.create_user('john', 'john@example.com', 'password123')

# Add group
from django.contrib.auth.models import Group
group = Group.objects.get(name='Teachers')
user.groups.add(group)

# Add permission
from django.contrib.auth.models import Permission
permission = Permission.objects.get(codename='add_post')
user.user_permissions.add(permission)

# Check permissions
user.has_perm('blog.add_post')
user.has_perm('blog.delete_post')
```
**ឧបាយកលបង្ហាព:** User, Group, Permission management។

---

**៤७. បង្កើត login/logout views និង templates**
```python
# ចម្លើយ - accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('blog:post_list')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')

# or FBV
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:post_list')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('accounts:login')

# accounts/urls.py
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

# templates/accounts/login.html
<form method="post">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
</form>
```
**ឧបាយកលបង្ហាព:** Login/Logout views និង templates។

---

**៤८. ប្រើ @login_required decorator និង LoginRequiredMixin**
```python
# ចម្លើយ - blog/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

# FBV
@login_required(login_url='accounts:login')
def post_create(request):
    # Only authenticated users can access
    return render(request, 'blog/post_form.html')

# CBV
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'accounts:login'
    redirect_field_name = 'next'
    model = Post
    form_class = PostForm
```
**ឧបាយកលបង្ហាព:** Login required protection។

---

**៤९. ប្រើ @permission_required decorator និង PermissionRequiredMixin**
```python
# ចម្លើយ - blog/views.py
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

# FBV
@login_required
@permission_required('blog.add_post', raise_exception=True)
def post_create(request):
    # Only users with 'add_post' permission
    return render(request, 'blog/post_form.html')

# CBV
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = ('blog.delete_post',)  # Or 'blog.change_post'
    template_name = 'blog/post_confirm_delete.html'
```
**ឧបាយកលបង្ហាព:** Permission required protection។

---

**៥०. បង្កើត custom permission ក្នុង model**
```python
# ចម្លើយ - blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        permissions = [
            ('can_publish_post', 'Can publish posts'),
            ('can_moderate_comments', 'Can moderate comments'),
        ]

# Check custom permission
user.has_perm('blog.can_publish_post')

# Add custom permission to group
from django.contrib.auth.models import Permission, Group
permission = Permission.objects.get(codename='can_publish_post')
group = Group.objects.get(name='Publishers')
group.permissions.add(permission)
```
**ឧបាយកលបង្ហាព:** Custom permissions ក្នុង models។

---

## 🌐 ផ្នែកទី៦៖ REST API និង Deployment (10 Exercises)

**៥១. បង្កើត ModelSerializer សម្រាប់ Post model**
```python
# ចម្លើយ - blog/serializers.py
from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    comments_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_name', 'comments_count', 'created_at']
        read_only_fields = ['created_at', 'id']
    
    def get_comments_count(self, obj):
        return obj.comments.count()
```
**ឧបាយកលបង្ហាព:** ModelSerializer ដែលមាន custom fields។

---

**៥२. បង្កើត ViewSet សម្រាប់ Post model**
```python
# ចម្លើយ - blog/views.py (API)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['author', 'created_at']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']
```
**ឧបាយកលបង្ហាព:** ViewSet សម្រាប់ API endpoints។

---

**៥३. បង្កើត Router និង register ViewSets**
```python
# ចម្លើយ - blog/urls.py (API)
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls

# project/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
]
```
**ឧបាយកលបង្ហាព:** Router configuration។

---

**៥४. បង្កើត custom action ក្នុង ViewSet**
```python
# ចម្លើយ - blog/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    @action(detail=True, methods=['post'])
    def mark_as_favorite(self, request, pk=None):
        post = self.get_object()
        # Add to favorites logic
        return Response({'status': 'post marked as favorite'})
    
    @action(detail=False, methods=['get'])
    def recent_posts(self, request):
        recent = Post.objects.all()[:5]
        serializer = self.get_serializer(recent, many=True)
        return Response(serializer.data)
```
**ឧបាយកលបង្ហាព:** Custom actions ក្នុង ViewSet។

---

**៥५. ដឹងលេខ API pagination**
```python
# ចម្លើយ - settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Or custom pagination
# api/pagination.py
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'api.pagination.CustomPagination',
}
```
**ឧបាយកលបង្ហាព:** API pagination configuration។

---

**៥६. ដឹងលេខ API authentication**
```python
# ចម្លើយ - settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Generate token
from rest_framework.authtoken.models import Token
token = Token.objects.create(user=user)
print(token.key)

# API request with token
# headers: Authorization: Token <token_key>
```
**ឧបាយកលបង្ហាព:** Token authentication ក្នុង API។

---

**៥७. ដឹងលេខ API filtering និង searching**
```python
# ចម្លើយ - blog/views.py
from django_filters import rest_framework as filters
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # Filtering
    filterset_fields = ['author', 'created_at']
    
    # Searching
    search_fields = ['title', 'content', 'author__username']
    
    # Ordering
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']

# API requests:
# GET /api/posts/?author=1
# GET /api/posts/?search=django
# GET /api/posts/?ordering=title
```
**ឧបាយកលបង្ហាព:** Filtering, searching, ordering ក្នុង API។

---

**៥८. ដឹងលេញ CORS configuration សម្រាប់ frontend ដែលបេះ domains**
```python
# ចម្លើយ - settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'https://frontend.example.com',
]

# Or allow all (not recommended for production)
CORS_ALLOW_ALL_ORIGINS = True
```
**ឧបាយកលបង្ហាព:** CORS configuration សម្រាប់ cross-domain requests។

---

**៥९. ប្រដ្ដាប់រៀងលើ environment variables សម្រាប់ production**
```bash
# .env file
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@db.example.com:5432/dbname
STATIC_URL=/static/
STATIC_ROOT=/var/www/static/
MEDIA_URL=/media/
MEDIA_ROOT=/var/www/media/
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password
```

```python
# settings.py - Production configuration
from decouple import config, Csv

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = config('STATIC_ROOT')
MEDIA_URL = '/media/'
MEDIA_ROOT = config('MEDIA_ROOT')
```
**ឧបាយកលបង្ហាព:** Environment configuration សម្រាប់ production។

---

**៦០. ដឹងលេញ deployment checklist**
```bash
# Deployment Checklist
✅ Set DEBUG = False
✅ Set ALLOWED_HOSTS appropriately
✅ Use environment variables for secrets
✅ Collect static files: python manage.py collectstatic
✅ Run migrations: python manage.py migrate
✅ Set up database (PostgreSQL recommended)
✅ Configure email backend
✅ Set up SSL/HTTPS
✅ Configure logging
✅ Use Gunicorn or uWSGI as application server
✅ Set up Nginx or Apache as reverse proxy
✅ Configure cache backend (Redis recommended)
✅ Set up monitoring and error tracking
✅ Configure backup strategy
✅ Test in production-like environment

# Deployment commands
python manage.py check --deploy
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn student_system.wsgi:application --bind 0.0.0.0:8000
```
**ឧបាយកលបង្ហាព:** Production deployment checklist និង commands។

---

# សាកល្បង៖ ដ៏សរុប 60 Practical Exercises

| ផ្នែក | ចំនួនលំហាត់ | ប្រធានបទ |
|------|--------|---------|
| ១. Architecture & Setup | 10 | Project initialization, MVT, Virtual Environment |
| ២. Data Layer | 10 | Models, ORM, Migrations, Relationships |
| ៣. URL & Views | 10 | Routing, FBV, CBV, Views |
| ៤. Templates & Forms | 10 | Template inheritance, Forms, Validation |
| ៥. Admin & Auth | 10 | Admin panel, Authentication, Permissions |
| ៦. API & Deployment | 10 | REST API, Serializers, Deployment |
| **សរុប** | **60** | **Complete Full-Stack Development** |

---

## 💡 ព័ត៌មានលម្អិត:
- រៀនបង្វឹង: ស្វែងយល់តូច មុន ដូច្នេះលំហាត់ នឹងលឹក
- ដាក់ដំណើរការលើ Git: រក្សាទុក កូដរបស់អ្នក ក្នុង version control
- ដូចម្តេច Debug: ប្រើ Django shell និង debugger
- អានឯកសារ: Django documentation គឺ comprehensive!

