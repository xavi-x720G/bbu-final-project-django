# 🎨 មគ្គុទ្ទេសក៍ការរៀបចំ និងប្រើប្រាស់ Static Files ក្នុង Django
# (Comprehensive Guide to Setting Up and Using Static Files in Django)

**Build Bright University (BBU) - Student Management System**  
**ឯកសារបង្រៀន និងអនុវត្តជាក់ស្តែងសម្រាប់គ្រូ និងនិស្សិត**

---

## 📑 មាតិកា (Table of Contents)
1. [សេចក្តីផ្តើម (Introduction)](#១-សេចក្តីផ្តើម-introduction)
2. [ភាពខុសគ្នារវាង Static Files និង Media Files (Static vs Media)](#២-ភាពខុសគ្នារវាង-static-files-និង-media-files)
3. [រចនាសម្ព័ន្ធថតឯកសារ (Folder Structure)](#៣-រចនាសម្ព័ន្ធថតឯកសារ-folder-structure)
4. [ការកំណត់រចនាសម្ព័ន្ធក្នុង settings.py (Settings Configuration)](#៤-ការកំណត់រចនាសម្ព័ន្ធក្នុង-settingspy)
5. [ការរៀបចំ URL Routing ក្នុង urls.py (URL Configuration)](#៥-ការរៀបចំ-url-routing-ក្នុង-urlspy)
6. [ការប្រើប្រាស់ក្នុង Templates (Using in HTML Templates)](#៦-ការប្រើប្រាស់ក្នុង-templates)
7. [ការដាក់ដំណើរការក្នុង Production (Production & collectstatic)](#៧-ការដាក់ដំណើរការក្នុង-production)
8. [បញ្ហាជួបញឹកញាប់ និងដំណោះស្រាយ (Troubleshooting & FAQs)](#៨-បញ្ហាជួបញឹកញាប់-និងដំណោះស្រាយ-troubleshooting)
9. [លំហាត់អនុវត្តន៍ជាក់ស្តែង (Hands-on Practice Exercises)](#៩-លំហាត់អនុវត្តន៍ជាក់ស្តែង-hands-on-exercises)

---

## ១. សេចក្តីផ្តើម (Introduction)

### តើអ្វីជា Static Files?
នៅក្នុង Django **Static Files** គឺជាឯកសារអចិន្ត្រៃយ៍ដែលអ្នកសរសេរកូដ (Developers) បង្កើតឡើងដើម្បីតុបតែង និងផ្តល់មុខងារបន្ថែមដល់ Website។ ឯកសារទាំងនោះរួមមាន៖
- 🎨 **CSS Files** (Cascading Style Sheets) - សម្រាប់កំណត់ពណ៌ ទំហំ និង Layout
- ⚡ **JavaScript Files** (JS) - សម្រាប់ Interactive features, AJAX, modal popups, animation
- 🖼️ **Images / Icons** - រូបភាព Logo, Icons, Background images ដែលជាផ្នែកនៃការរចនា Web
- 🔤 **Web Fonts** - Font files (e.g., `.woff`, `.woff2`, `.ttf`) ដូចជា Khmer Fonts (Battambang, Moul, Kantumruy)

Django មាន Built-in App មួយឈ្មោះថា `django.contrib.staticfiles` ដែលជួយគ្រប់គ្រង និងទាញយកឯកសារ Static ទាំងអស់នេះមកបង្ហាញនៅលើ Web Browser យ៉ាងរហ័ស។

---

## ២. ភាពខុសគ្នារវាង Static Files និង Media Files

និស្សិតភាគច្រើនតែងតែច្រឡំរវាង **Static Files** និង **Media Files**។ សូមពិនិត្យតារាងប្រៀបធៀបខាងក្រោម៖

| លក្ខណៈវិនិច្ឆ័យ (Feature) | Static Files 🎨 | Media Files 📸 |
|---|---|---|
| **ប្រភព (Source)** | បង្កើតដោយ **Developer / Programmer** | បង្ហោះឡើង (Uploaded) ដោយ **End-Users** |
| **ឧទាហរណ៍ (Examples)** | `style.css`, `main.js`, `bbu_logo.png` | រូបថតនិស្សិត (`profile_picture`), ឯកសារ CV, Assignment PDF |
| **ការផ្លាស់ប្តូរ (Mutability)** | កម្រប្រែប្រួលក្នុងពេល Runtime (Read-only) | កើនឡើង និងប្រែប្រួលជាប្រចាំពេល Users ប្រើប្រាស់ |
| **Settings Variable** | `STATIC_URL`, `STATICFILES_DIRS`, `STATIC_ROOT` | `MEDIA_URL`, `MEDIA_ROOT` |
| **របៀបហៅក្នុង Template** | `{% static 'path/file.ext' %}` | `{{ object.field_name.url }}` |
| **Security Risk** | ទាប (Safe Code Assets) | ខ្ពស់ (ត្រូវ Validate ប្រភេទ File និងទំហំមុន Upload) |

---

## ៣. រចនាសម្ព័ន្ធថតឯកសារ (Folder Structure)

Django ផ្តល់ជម្រើសពីរក្នុងការរៀបចំ Static Files៖

### វិធីសាស្ត្រទី១៖ Global Static Folder (អនុវត្តក្នុងគម្រោងនេះ ⭐)
ដាក់ឯកសារទាំងអស់ក្នុងថត `static/` មួយនៅ Root Project ងាយស្រួលគ្រប់គ្រងសម្រាប់ Theme ទូទៅនៃ Website៖

```text
django_lesson/
├── manage.py
├── student_system/
│   ├── settings.py
│   └── urls.py
├── static/                     📁 Global Static Directory
│   ├── css/
│   │   ├── style.css          # CSS ទូទៅរបស់ Website
│   │   └── khmer_fonts.css    # Style សម្រាប់អក្សរខ្មែរ
│   ├── js/
│   │   └── main.js            # JavaScript logic
│   └── images/
│       ├── bbu_logo.png       # និមិត្តសញ្ញាសាកលវិទ្យាល័យ
│       └── favicon.ico        # Icon នៅលើ Tab Browser
├── templates/
│   └── base.html
└── ...
```

### វិធីសាស្ត្រទី២៖ App-Level Static Folder
រៀបចំដាច់ដោយឡែកតាម App នីមួយៗ (ស័ក្តិសមសម្រាប់ Reusable Django Apps)៖
```text
students/
├── static/
│   └── students/              # ត្រូវបង្កើត Subfolder ឈ្មោះដូច App ដើម្បីកុំឱ្យជាន់ឈ្មោះគ្នា
│       ├── css/
│       │   └── student_card.css
│       └── js/
│           └── student_filter.js
```

---

## ៤. ការកំណត់រចនាសម្ព័ន្ធក្នុង settings.py

បើកឯកសារ `student_system/settings.py` ហើយពិនិត្យ ឬកំណត់ Variable សំខាន់ៗចំនួន ៤ ដូចខាងក្រោម៖

```python
# ==============================================================================
# 1. ពិនិត្យមើល INSTALLED_APPS
# ត្រូវប្រាកដថាមាន 'django.contrib.staticfiles' នៅក្នុងបញ្ជី
# ==============================================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # <-- ត្រូវតែមានជានិច្ច
    # ... apps ផ្សេងទៀត
]

# ==============================================================================
# 2. STATIC_URL (URL Prefix សម្រាប់ Browser)
# ==============================================================================
# នេះជាផ្លូវ URL សម្រាប់ឱ្យ Browser ចូលទាញយក Static Files
# ឧទាហរណ៍: http://127.0.0.1:8000/static/css/style.css
STATIC_URL = 'static/'

# ==============================================================================
# 3. STATICFILES_DIRS (កន្លែងដែល Django ត្រូវស្វែងរកកំឡុងពេល Development)
# ==============================================================================
# បញ្ជាក់ប្រាប់ Django ឱ្យដឹងថាឯកសារ static របស់គម្រោងស្ថិតនៅក្នុងថត static/ នៅ root
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# ==============================================================================
# 4. STATIC_ROOT (កន្លែងប្រមូលផ្តុំឯកសារពេលដាក់ឱ្យដំណើរការ Production)
# ==============================================================================
# កន្លែងដែលពាក្យបញ្ជា "python manage.py collectstatic" នឹងចម្លងឯកសារទាំងអស់ទៅ
# ហាមចង្អុល STATIC_ROOT ទៅកន្លែងតែមួយជាមួយ STATICFILES_DIRS ដាច់ខាត!
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ==============================================================================
# 5. MEDIA FILES (សម្រាប់រូបថតនិស្សិតដែល Upload)
# ==============================================================================
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## ៥. ការរៀបចំ URL Routing ក្នុង urls.py

ក្នុងអំឡុងពេល Development (`DEBUG = True`) Django អាចជួយ Serve ទាំង Static Files និង Media Files ដោយបន្ថែមការកំណត់ក្នុង `student_system/urls.py`៖

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    # ... URLs ផ្សេងៗទៀត
]

# បន្ថែមនៅខាងក្រោមបង្អស់សម្រាប់ Development Server
if settings.DEBUG:
    # សម្រាប់ Media Files (រូបថតនិស្សិត upload)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # សម្រាប់ Static Files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

---

## ៦. ការប្រើប្រាស់ក្នុង Templates

ដើម្បីប្រើប្រាស់ Static Files ក្នុង HTML Template អ្នកត្រូវអនុវត្ត ៣ ជំហាន៖

### ជំហានទី១៖ Load Static Tag នៅលើគេបង្អស់នៃ Template
```html
{% load static %}
```
> ⚠️ **សំខាន់បំផុត**: ត្រូវដាក់ `{% load static %}` នៅបន្ទាត់ទីមួយ ឬបន្ទាប់ពី `{% extends 'base.html' %}`!

### ជំហានទី២៖ ហៅប្រើ CSS និង Favicon ក្នុង `<head>`
```html
<!-- ហៅប្រើ Favicon -->
<link rel="icon" type="image/x-icon" href="{% static 'images/favicon.ico' %}">

<!-- ហៅប្រើ CSS File -->
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<link rel="stylesheet" href="{% static 'css/khmer_fonts.css' %}">
```

### ជំហានទី៣៖ ហៅប្រើរូបភាព និង JavaScript
```html
<!-- ហៅប្រើរូបភាព Logo សាកលវិទ្យាល័យ -->
<img src="{% static 'images/bbu_logo.png' %}" alt="BBU Logo" class="navbar-logo" width="40" height="40">

<!-- ហៅប្រើ JavaScript នៅចុងបញ្ចប់នៃ <body> -->
<script src="{% static 'js/main.js' %}"></script>
```

---

### ឧទាហរណ៍ជាក់ស្តែង៖ គំរូ base.html ពេញលេញ

```html
{% load static %}
<!DOCTYPE html>
<html lang="km">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}ប្រព័ន្ធគ្រប់គ្រងនិស្សិត - BBU{% endblock %}</title>

    <!-- Bootstrap 5 CSS (CDN) -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom Project CSS (Static Files) -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">

    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navbar with University Logo -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="/">
                <img src="{% static 'images/bbu_logo.png' %}" alt="Logo" width="32" height="32" class="me-2">
                <span>Build Bright University</span>
            </a>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="container my-4">
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="text-center py-3 bg-light">
        <p class="mb-0">© 2026 Build Bright University - Student Management System</p>
    </footer>

    <!-- Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Custom Project JS (Static Files) -->
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

---

## ៧. ការដាក់ដំណើរការក្នុង Production

នៅពេលដាក់ដំណើរការលើ Server ពិតប្រាកដ (Render, Heroku, VPS, AWS) អ្នកត្រូវកំណត់ `DEBUG = False`។ ក្នុងស្ថានភាពនេះ Django នឹង **មិន** Serve Static Files ដោយស្វ័យប្រវត្តិតាមរយៈ Python ឡើយដើម្បីធានាល្បឿន និង Security។

### ជំហានទី១៖ ដំណើរការ Collectstatic Command
ដំណើរការ Command នេះដើម្បីប្រមូលឯកសារ Static ទាំងអស់ពីគ្រប់ Apps ចូលទៅក្នុងថត `STATIC_ROOT` (ថត `staticfiles/`)៖

```bash
python manage.py collectstatic --noinput
```

### ជំហានទី២៖ ប្រើប្រាស់ WhiteNoise (ដំណោះស្រាយល្អបំផុតសម្រាប់ Heroku/Render)

WhiteNoise អនុញ្ញាតឱ្យ Python Web Application អាច Serve Static Files ផ្ទាល់ខ្លួនបានយ៉ាងលឿនដោយមិនចាំបាច់មាន Nginx៖

1. ដំឡើង WhiteNoise៖
   ```bash
   pip install whitenoise
   ```

2. បន្ថែម WhiteNoise ក្នុង `MIDDLEWARE` ក្នុង `student_system/settings.py` (ត្រូវដាក់នៅក្រោម `SecurityMiddleware`)៖
   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- បន្ថែមត្រង់នេះ
       'django.contrib.sessions.middleware.SessionMiddleware',
       # ... middlewares ផ្សេងទៀត
   ]
   ```

3. បន្ថែម Storage Compression & Caching ក្នុង `settings.py`៖
   ```python
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

---

## ៨. បញ្ហាជួបញឹកញាប់ និងដំណោះស្រាយ (Troubleshooting)

### បញ្ហាទី១៖ `TemplateSyntaxError: Invalid block tag on line X: 'static'`
- **មូលហេតុ**: ភ្លេចដាក់ `{% load static %}` នៅលើគេបង្អស់នៃ Template File។
- **ដំណោះស្រាយ**: បន្ថែមបន្ទាត់ `{% load static %}` នៅបន្ទាត់ទីមួយនៃ File ឬបន្ទាប់ពី `{% extends %}`។

### បញ្ហាទី២៖ CSS/JS មិន Update (Browser នៅបង្ហាញ Style ចាស់)
- **មូលហេតុ**: Web Browser បានធ្វើ Caching លើឯកសារ Static ចាស់។
- **ដំណោះស្រាយ**:
  - ធ្វើ Hard Refresh: ចុច `Ctrl + F5` (Windows) ឬ `Cmd + Shift + R` (macOS)
  - ឬបន្ថែម Cache-busting version parameter ក្នុង Template:
    ```html
    <link rel="stylesheet" href="{% static 'css/style.css' %}?v=1.1">
    ```

### បញ្ហាទី៣៖ 404 Not Found លើ Static Files កំឡុងពេល Development
- **មូលហេតុ**:
  1. ភ្លេចកំណត់ `STATICFILES_DIRS = [BASE_DIR / 'static']` ក្នុង `settings.py`
  2. ឈ្មោះ File ឬឈ្មោះ Folder ខុស (Case-sensitive)
- **ដំណោះស្រាយ**: ពិនិត្យផ្លូវ Path នៃ Folder `static/` ឱ្យប្រាកដថាឈ្មោះដូចគ្នាទាំងស្រុង។

### បញ្ហាទី៤៖ Error ពេល run `collectstatic`: `STATIC_ROOT must not be in STATICFILES_DIRS`
- **មូលហេតុ**: អ្នកបានកំណត់ `STATIC_ROOT` និង `STATICFILES_DIRS` ទៅកាន់ Folder តែមួយ (ឧ. `static/`)។
- **ដំណោះស្រាយ**:
  - `STATICFILES_DIRS` = `BASE_DIR / 'static'` (កន្លែងសរសេរកូដ)
  - `STATIC_ROOT` = `BASE_DIR / 'staticfiles'` (កន្លែង collect សម្រាប់ deploy)

---

## ៩. លំហាត់អនុវត្តន៍ជាក់ស្តែង (Hands-on Exercises)

### លំហាត់ទី១ (កម្រិតដំបូង): បង្កើត Custom CSS Styling
1. បង្កើតឯកសារ `static/css/style.css`
2. សរសេរ CSS Class សម្រាប់ Badge ពិន្ទុ និង Table Hover៖
   ```css
   .bbu-gradient-header {
       background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
       color: #ffffff;
   }
   .student-avatar-thumb {
       width: 44px;
       height: 44px;
       object-fit: cover;
       border-radius: 50%;
       border: 2px solid #e2e8f0;
   }
   ```
3. ភ្ជាប់ចូលក្នុង `templates/base.html` តាមរយៈ `{% static 'css/style.css' %}`

### លំហាត់ទី២ (កម្រិតមធ្យម): បង្កើត Interactive Alert តាមរយៈ JavaScript
1. បង្កើតឯកសារ `static/js/main.js`
2. សរសេរ Script សម្រាប់បិទ Notification Alert ដោយស្វ័យប្រវត្តក្រោយ ៤ វិនាទី៖
   ```javascript
   document.addEventListener('DOMContentLoaded', function() {
       setTimeout(function() {
           const alerts = document.querySelectorAll('.alert');
           alerts.forEach(function(alert) {
               alert.style.transition = 'opacity 0.5s ease';
               alert.style.opacity = '0';
               setTimeout(() => alert.remove(), 500);
           });
       }, 4000);
   });
   ```
3. ភ្ជាប់ចូលក្នុង `templates/base.html` ដោយប្រើ `{% static 'js/main.js' %}`

### លំហាត់ទី៣ (កម្រិតខ្ពស់): រៀបចំ Production Collectstatic
1. បើក Terminal ក្នុងថត `django_lesson/`
2. ដំណើរការ Command:
   ```bash
   python manage.py collectstatic
   ```
3. ពិនិត្យមើល Folder `staticfiles/` ថាតើឯកសារ CSS, JS, និង Admin Styles ទាំងអស់ត្រូវបានប្រមូលផ្តុំយ៉ាងត្រឹមត្រូវដែរឬទេ!

---

**ឯកសារយោងផ្លូវការ (Official Reference)**:
- [Django Documentation - Managing Static Files](https://docs.djangoproject.com/en/4.2/howto/static-files/)
- [Django Documentation - The staticfiles app](https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/)
