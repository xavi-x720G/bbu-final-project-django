# 📸 មគ្គុទ្ទេសក៍ការរៀបចំ និងប្រើប្រាស់ Media Files ក្នុង Django
# (Comprehensive Guide to Setting Up and Using Media Files in Django)

**Build Bright University (BBU) - Student Management System**  
**ឯកសារបង្រៀន និងអនុវត្តជាក់ស្តែងសម្រាប់គ្រូ និងនិស្សិត**

---

## 📑 មាតិកា (Table of Contents)
1. [សេចក្តីផ្តើម (Introduction to Media Files)](#១-សេចក្តីផ្តើម-introduction)
2. [ភាពខុសគ្នារវាង Static Files និង Media Files](#២-ភាពខុសគ្នារវាង-static-files-និង-media-files)
3. [តម្រូវការដំឡើងបណ្ណាល័យ Pillow (Pillow Installation)](#៣-តម្រូវការដំឡើងបណ្ណាល័យ-pillow)
4. [ការកំណត់រចនាសម្ព័ន្ធក្នុង settings.py (Settings Configuration)](#៤-ការកំណត់រចនាសម្ព័ន្ធក្នុង-settingspy)
5. [ការរៀបចំ URL Routing ក្នុង urls.py (URL Configuration)](#៥-ការរៀបចំ-url-routing-ក្នុង-urlspy)
6. [ការកំណត់ Models ជាមួយ ImageField & FileField (Models Definition)](#៦-ការកំណត់-models-ជាមួយ-imagefield--filefield)
7. [ការបង្កើត Form និង View សម្រាប់ File Uploads (Forms & Views)](#៧-ការបង្កើត-form-និង-view-សម្រាប់-file-uploads)
8. [ការបង្ហាញរូបភាពក្នុង HTML Templates (Template Rendering)](#៨-ការបង្ហាញរូបភាពក្នុង-html-templates)
9. [ការគ្រប់គ្រងឯកសារ និងសុវត្ថិភាព (File Management & Security)](#៩-ការគ្រប់គ្រងឯកសារ-និងសុវត្ថិភាព-file-management--security)
10. [ការដាក់ដំណើរការក្នុង Production (Cloud Storage)](#១០-ការដាក់ដំណើរការក្នុង-production-cloud-storage)
11. [បញ្ហាជួបញឹកញាប់ និងដំណោះស្រាយ (Troubleshooting & FAQs)](#១១-បញ្ហាជួបញឹកញាប់-និងដំណោះស្រាយ-troubleshooting)
12. [លំហាត់អនុវត្តន៍ជាក់ស្តែង (Hands-on Practice Exercises)](#១២-លំហាត់អនុវត្តន៍ជាក់ស្តែង-hands-on-exercises)

---

## ១. សេចក្តីផ្តើម (Introduction)

### តើអ្វីជា Media Files?
នៅក្នុង Django **Media Files** គឺជាឯកសារទាំងឡាយណាដែលត្រូវបាន **បង្ហោះឡើង (Uploaded)** ដោយអ្នកប្រើប្រាស់ (End-Users ឬ Admins) កំឡុងពេលកម្មវិធីកំពុងដំណើរការ (Runtime)។ ឯកសារទាំងនោះរួមមាន៖
- 👤 **រូបថតផ្ទាល់ខ្លួន (Profile Pictures / Avatars)** (ឧ. រូបថតនិស្សិត `profile_picture`)
- 📄 **ឯកសារសិក្សា (Documents)** (ឧ. Assignment submissions, Syllabus PDF, Resumes)
- 🖼️ **រូបភាពព័ត៌មាន ឬសកម្មភាព (Course Banners / Event Photos)**
- 📊 **ឯកសារទិន្នន័យ (CSV, Excel sheets, ZIP files)**

ខុសពី Static Files ដែលជាកូដរបស់ Developer ឯកសារ Media Files ត្រូវតែគ្រប់គ្រងប្រកបដោយការប្រុងប្រយ័ត្នខ្ពស់ ព្រោះវាទាក់ទងនឹងទំហំផ្ទុក (Storage capacity) និងសុវត្ថិភាព (Security) របស់ Server។

---

## ២. ភាពខុសគ្នារវាង Static Files និង Media Files

| លក្ខណៈវិនិច្ឆ័យ (Feature) | Static Files 🎨 | Media Files 📸 |
|---|---|---|
| **អ្នកបង្កើត (Origin)** | Developer / អ្នកសរសេរកូដ | End-Users / សិស្ស / គ្រូ (Upload) |
| **គោលបំណង (Purpose)** | តុបតែង UI (CSS, JS, Logos, Icons) | រក្សាទុកព័ត៌មានអ្នកប្រើប្រាស់ (Photos, Documents) |
| **Folder ក្នុង Project** | `static/` (កន្លែងសរសេរ) & `staticfiles/` (collectstatic) | `media/` (ឧ. `media/profiles/`, `media/documents/`) |
| **Settings ក្នុង settings.py** | `STATIC_URL`, `STATICFILES_DIRS`, `STATIC_ROOT` | `MEDIA_URL`, `MEDIA_ROOT` |
| **បណ្ណាល័យចាំបាច់** | មិនទាមទារបន្ថែម | ទាមទារបណ្ណាល័យ **Pillow** សម្រាប់រូបភាព |
| **របៀបហៅក្នុង Template** | `{% static 'css/style.css' %}` | `{{ student.profile_picture.url }}` |
| **Production Storage** | WhiteNoise ឬ Web Server (Nginx) | Cloud Storage (AWS S3, Cloudinary) |

---

## ៣. តម្រូវការដំឡើងបណ្ណាល័យ Pillow

ដើម្បីប្រើប្រាស់ `models.ImageField` នៅក្នុង Django អ្នក **ត្រូវតែដំឡើងបណ្ណាល័យ Pillow** (Python Imaging Library fork) ជាមុនសិន។ ប្រសិនបើគ្មាន Pillow ទេ Django នឹងបង្ហាញ Error មិនអនុញ្ញាតឱ្យ Migrate ឬដំណើរការបានឡើយ៖

```bash
# 1. ដំណើរការ Virtual Environment
source venv/bin/activate  # macOS / Linux
# ឬ venv\Scripts\activate សម្រាប់ Windows

# 2. ដំឡើង Pillow
pip install Pillow

# 3. រក្សាទុកក្នុង requirements.txt
pip freeze > requirements.txt
```

> 💡 **ចំណាំ**: ប្រសិនបើអ្នកចង់ Upload តែឯកសារធម្មតា (ដូចជា PDF, DOCX, ZIP) ដោយប្រើ `models.FileField` នោះមិនចាំបាច់មាន Pillow ក៏បានដែរ។ ប៉ុន្តែសម្រាប់ `ImageField` គឺត្រូវតែមាន Pillow ដាច់ខាត។

---

## ៤. ការកំណត់រចនាសម្ព័ន្ធក្នុង settings.py

បើកឯកសារ `student_system/settings.py` ហើយកំណត់ Settings ពីរសំខាន់៖

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# MEDIA FILES CONFIGURATION
# ==============================================================================

# 1. MEDIA_URL: URL Prefix សម្រាប់ Browser ចូលទាញយករូបភាព
# ឧទាហរណ៍: http://127.0.0.1:8000/media/profiles/student1.jpg
MEDIA_URL = 'media/'

# 2. MEDIA_ROOT: ផ្លូវ Absolute Path លើ Hard Disk នៃម៉ាស៊ីន Server
# កន្លែងដែល Django នឹងរក្សាទុកឯកសារដែលបាន Upload ពិតប្រាកដ
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## ៥. ការរៀបចំ URL Routing ក្នុង urls.py

កំឡុងពេល Development (`DEBUG = True`) Django មិនទាន់ Serve Media Files ដោយស្វ័យប្រវត្តិទេ លុះត្រាតែយើងប្រាប់វាក្នុង `student_system/urls.py`៖

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('courses/', include('courses.urls')),
    path('enrollments/', include('enrollments.urls')),
    path('api/', include('student_system.api_urls')),
]

# បន្ថែមនៅខាងក្រោមបង្អស់សម្រាប់ Development Server
if settings.DEBUG:
    # អនុញ្ញាតឱ្យ Browser មើលឃើញរូបភាពដែល Upload ក្នុង Folder media/
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> ⚠️ **ការព្រមានសុវត្ថិភាព**: `static(settings.MEDIA_URL, ...)` ប្រើសម្រាប់តែពេល `DEBUG = True` (Development) ប៉ុណ្ណោះ។ ពេលឡើង Production (`DEBUG = False`) យើងត្រូវប្រើ Nginx ឬ Cloud Storage (AWS S3, Cloudinary) ដើម្បី Serve Media Files។

---

## ៦. ការកំណត់ Models ជាមួយ ImageField & FileField

### គំរូ Student Model ក្នុងគម្រោងយើង (`students/models.py`)

```python
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    student_id = models.CharField(max_length=20, unique=True)
    khmer_name = models.CharField(max_length=150, blank=True)
    
    # 📸 ImageField សម្រាប់រូបថតសិស្ស
    # upload_to='profiles/' មានន័យថា File នឹងត្រូវរក្សាទុកក្នុង media/profiles/
    profile_picture = models.ImageField(
        upload_to='profiles/', 
        blank=True, 
        null=True,
        help_text="រូបថតសិស្ស (JPG, PNG, WEBP)"
    )
    
    date_of_birth = models.DateField()
    # ... fields ផ្សេងៗទៀត
```

### ជម្រើសកម្រិតខ្ពស់: Dynamic Upload Path (បែងចែក Folder តាមឆ្នាំ ឬ User ID)

យើងអាចបង្កើត Function មួយដើម្បីរៀបចំ Path ដោយស្វ័យប្រវត្ត៖

```python
import os

def student_avatar_path(instance, filename):
    """រក្សាទុកក្នុងទម្រង់: media/profiles/STU1001/filename.jpg"""
    ext = filename.split('.')[-1]
    filename = f"{instance.student_id}_avatar.{ext}"
    return os.path.join('profiles', instance.student_id, filename)

class Student(models.Model):
    # ...
    profile_picture = models.ImageField(upload_to=student_avatar_path, blank=True, null=True)
```

បន្ទាប់ពីកែប្រែ Model រួច ត្រូវតែ Run Migrations ជានិច្ច៖
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ៧. ការបង្កើត Form និង View សម្រាប់ File Uploads

### ១. Form Definition (`students/forms.py`)

```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'khmer_name', 'date_of_birth', 'gender', 
                  'phone_number', 'address', 'city', 'country', 'profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

    # Custom Validation សម្រាប់ពិនិត្យទំហំ File (មិនឱ្យលើស 2MB)
    def clean_profile_picture(self):
        picture = self.cleaned_data.get('profile_picture')
        if picture:
            max_size = 2 * 1024 * 1024  # 2 Megabytes
            if picture.size > max_size:
                raise forms.ValidationError("រូបថតមិនអាចមានទំហំធំជាង 2MB ឡើយ!")
        return picture
```

---

### ២. View Logic (`students/views.py`)

> ⚠️ **កំហុសញឹកញាប់បំផុតរបស់និស្សិត**: ភ្លេចដាក់ `request.FILES` ក្នុង View!
> ប្រសិនបើដាក់តែ `request.POST` នោះ Django នឹងមិនអាចទទួលបាន File ដែល Upload ឡើយ!

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm, UserForm

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        # ⚠️ ត្រូវតែមាន request.FILES ជានិច្ចនៅពេល Form មាន File Upload!
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        user_form = UserForm(request.POST, instance=student.user)
        
        if student_form.is_valid() and user_form.is_valid():
            student_form.save()
            user_form.save()
            return redirect('students:student_detail', pk=student.pk)
    else:
        student_form = StudentForm(instance=student)
        user_form = UserForm(instance=student.user)
    
    return render(request, 'students/student_form.html', {
        'student_form': student_form,
        'user_form': user_form,
        'student': student,
    })
```

---

### ៣. HTML Form Template (`templates/students/student_form.html`)

> ⚠️ **កំហុសទី២ របស់និស្សិត**: ភ្លេចដាក់ `enctype="multipart/form-data"` ក្នុង Tag `<form>`!  
> ប្រសិនបើគ្មាន `enctype="multipart/form-data"` នោះ Browser នឹងផ្ញើតែ Text មិនផ្ញើ Binary Image Data ឡើយ!

```html
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    
    <div class="mb-3">
        <label for="id_profile_picture" class="form-label">រូបថតសិស្ស (Profile Picture)</label>
        {{ student_form.profile_picture }}
        {% if student_form.profile_picture.errors %}
            <div class="text-danger small">{{ student_form.profile_picture.errors }}</div>
        {% endif %}
    </div>

    <!-- បង្ហាញរូបភាពបច្ចុប្បន្ន (បើសិនជាមាន) -->
    {% if student.profile_picture %}
        <div class="mb-3">
            <p class="text-muted mb-1">រូបភាពបច្ចុប្បន្ន:</p>
            <img src="{{ student.profile_picture.url }}" alt="Current Photo" width="80" height="80" class="rounded-circle border">
        </div>
    {% endif %}

    <button type="submit" class="btn btn-primary">រក្សាទុក</button>
</form>
```

---

## ៨. ការបង្ហាញរូបភាពក្នុង HTML Templates

### របៀបហៅរូបភាពក្នុង Template ដោយសុវត្ថិភាព

> 💡 **ចំណាំសំខាន់**: ត្រូវប្រើ `{% if student.profile_picture %}` ជានិច្ចមុននឹងហៅ `.url`!  
> ប្រសិនបើសិស្សមិនទាន់មានរូបភាព ហើយយើងហៅ `{{ student.profile_picture.url }}` ដោយគ្មាន `if` នោះ Django នឹងបោះ Error: `ValueError: The 'profile_picture' attribute has no file associated with it.`

#### ឧទាហរណ៍ទី១៖ បង្ហាញក្នុង Student Detail Profile
```html
<div class="card p-3 text-center">
    {% if student.profile_picture %}
        <img src="{{ student.profile_picture.url }}" 
             alt="{{ student.get_primary_name }}" 
             class="rounded-circle mx-auto mb-3" 
             style="width: 120px; height: 120px; object-fit: cover; border: 3px solid #667eea;">
    {% else %}
        <!-- បង្ហាញអក្សរកាត់ ឬ Default Avatar ប្រសិនបើគ្មានរូបភាព -->
        <div class="rounded-circle bg-secondary text-white d-flex align-items-center justify-content-center mx-auto mb-3" 
             style="width: 120px; height: 120px; font-size: 2.5rem; font-weight: bold;">
            {{ student.get_primary_name|slice:":1" }}
        </div>
    {% endif %}

    <h4>{{ student.get_primary_name }}</h4>
    <p class="text-muted">{{ student.student_id }}</p>
</div>
```

#### ឧទាហរណ៍ទី២៖ បង្ហាញ Thumbnail តូចៗក្នុងតារាង Student List
```html
<table class="table table-hover align-middle">
    <thead>
        <tr>
            <th>#</th>
            <th>រូបថត</th>
            <th>ឈ្មោះជាភាសាខ្មែរ</th>
            <th>Student ID</th>
        </tr>
    </thead>
    <tbody>
        {% for student in students %}
        <tr>
            <td>{{ forloop.counter }}</td>
            <td>
                {% if student.profile_picture %}
                    <img src="{{ student.profile_picture.url }}" 
                         alt="Avatar" 
                         class="rounded-circle" 
                         style="width: 40px; height: 40px; object-fit: cover;">
                {% else %}
                    <span class="badge bg-light text-secondary border rounded-circle p-2">👤</span>
                {% endif %}
            </td>
            <td><strong>{{ student.get_primary_name }}</strong></td>
            <td>{{ student.student_id }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

---

## ៩. ការគ្រប់គ្រងឯកសារ និងសុវត្ថិភាព (File Management & Security)

### ១. លុប File ចាស់ចេញពី Disk ពេលលុប Object (Signals)
តាមលំនាំដើមរបស់ Django នៅពេលដែល Record ក្នុង Database ត្រូវបាន Delete ឯកសាររូបភាពក្នុង Hard Disk **មិនត្រូវបានលុបដោយស្វ័យប្រវត្តិទេ**។ ដើម្បីឱ្យប្រព័ន្ធលុប File ស្វ័យប្រវត្ត យើងអាចប្រើ Django Signal `post_delete`៖

```python
# students/signals.py
import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Student

@receiver(post_delete, sender=Student)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """លុបរូបភាពចាស់ចេញពី Storage ពេលលុប Student"""
    if instance.profile_picture:
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)

@receiver(pre_save, sender=Student)
def auto_delete_old_file_on_change(sender, instance, **kwargs):
    """លុបរូបភាពចាស់ចេញពេល User Update រូបភាពថ្មី"""
    if not instance.pk:
        return False

    try:
        old_file = Student.objects.get(pk=instance.pk).profile_picture
    except Student.DoesNotExist:
        return False

    new_file = instance.profile_picture
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
```

---

## ១០. ការដាក់ដំណើរការក្នុង Production (Cloud Storage)

នៅលើ Cloud Platforms ដូចជា **Render, Heroku, Fly.io** ម៉ាស៊ីន Server ប្រើប្រាស់ **Ephemeral Filesystem** (រាល់ពេល Server Restart ឬ Deploy ថ្មី ឯកសារក្នុង Disk មូលដ្ឋាននឹងត្រូវបាត់បង់)។

ដូច្នេះ សម្រាប់ Production យើងត្រូវរក្សាទុក Media Files នៅលើ Cloud Storage Service ដូចជា៖
1. **Amazon AWS S3** (Amazon Simple Storage Service)
2. **Cloudinary** (ងាយស្រួលសម្រាប់រូបភាព និង Auto-optimize)
3. **Google Cloud Storage (GCS)**

### របៀបតភ្ជាប់ជាមួយ Cloudinary ឬ AWS S3 ដោយប្រើ `django-storages`:

```bash
pip install django-storages boto3
```

កំណត់ក្នុង `student_system/settings.py` សម្រាប់ Production៖
```python
if not DEBUG:
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'ap-southeast-1'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

---

## ១១. បញ្ហាជួបញឹកញាប់ និងដំណោះស្រាយ (Troubleshooting)

### បញ្ហាទី១៖ Upload រួច តែគ្មាន File រក្សាទុកក្នុង Database ឬ Folder
- **មូលហេតុ**: 
  1. ភ្លេចដាក់ `enctype="multipart/form-data"` ក្នុង Tag `<form>` ក្នុង Template
  2. ភ្លេចដាក់ `request.FILES` ក្នុង View (ឧ. សរសេរតែ `StudentForm(request.POST)`)
- **ដំណោះស្រាយ**:
  - បន្ថែម `<form method="POST" enctype="multipart/form-data">`
  - ក្នុង View: `StudentForm(request.POST, request.FILES, instance=student)`

### បញ្ហាទី២៖ `ValueError: The 'profile_picture' attribute has no file associated with it.`
- **មូលហេតុ**: អ្នកបានហៅ `{{ student.profile_picture.url }}` ដោយមិនបាន Check ថា Student នោះមានរូបភាពឬអត់។
- **ដំណោះស្រាយ**: ត្រូវព័ទ្ធជុំវិញដោយ Tag `{% if student.profile_picture %}` ជានិច្ច។

### បញ្ហាទី៣៖ 404 Not Found ពេលចុចលើ Link រូបភាពក្នុង Development
- **មូលហេតុ**: ភ្លេចបន្ថែម `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` ក្នុង `student_system/urls.py`។
- **ដំណោះស្រាយ**: បន្ថែមបន្ទាត់ URL pattern ខាងលើនៅក្រោម `if settings.DEBUG:`.

### បញ្ហាទី៤៖ `Cannot use ImageField because Pillow is not installed.`
- **មូលហេតុ**: មិនទាន់បានដំឡើងបណ្ណាល័យ Pillow ក្នុង Python Virtual Environment។
- **ដំណោះស្រាយ**: ដំណើរការ `pip install Pillow`។

---

## ១២. លំហាត់អនុវត្តន៍ជាក់ស្តែង (Hands-on Exercises)

### លំហាត់ទី១ (កម្រិតដំបូង): បន្ថែម Placeholder Default Avatar
- **គោលដៅ**: បើ Student មិនទាន់មានរូបថត ត្រូវបង្ហាញរូបភាព Default Avatar ស្វ័យប្រវត្តិ។
- **ដំណោះស្រាយ**:
  1. ដាក់រូបភាព `default_avatar.png` ក្នុងថត `static/images/default_avatar.png`
  2. សរសេរក្នុង Template:
     ```html
     {% if student.profile_picture %}
         <img src="{{ student.profile_picture.url }}" class="rounded-circle" width="50" height="50">
     {% else %}
         <img src="{% static 'images/default_avatar.png' %}" class="rounded-circle" width="50" height="50">
     {% endif %}
     ```

### លំហាត់ទី២ (កម្រិតមធ្យម): បន្ថែម File Validation សម្រាប់កម្រិតប្រភេទ File
- **គោលដៅ**: អនុញ្ញាតឱ្យ Upload តែប្រភេទរូបភាព `.jpg`, `.jpeg`, `.png`, `.webp` ប៉ុណ្ណោះ ហាម Upload `.exe`, `.py`, ឬ `.zip`។
- **ដំណោះស្រាយ**: ប្រើ `FileExtensionValidator`:
  ```python
  from django.core.validators import FileExtensionValidator

  profile_picture = models.ImageField(
      upload_to='profiles/',
      validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])],
      blank=True, null=True
  )
  ```

### លំហាត់ទី៣ (កម្រិតខ្ពស់): បន្ថែម Course Syllabus PDF FileField
- **គោលដៅ**: បន្ថែមមុខងារឱ្យសាស្ត្រាចារ្យអាច Upload មាតិកាមេរៀន (Syllabus PDF) ទៅក្នុង `Course` Model។
- **ដំណោះស្រាយ**:
  1. ក្នុង `courses/models.py` បន្ថែម:
     ```python
     syllabus = models.FileField(upload_to='syllabi/', blank=True, null=True)
     ```
  2. Run `makemigrations` និង `migrate`
  3. បង្ហាញប៊ូតុងទាញយកក្នុង `templates/courses/course_detail.html`:
     ```html
     {% if course.syllabus %}
         <a href="{{ course.syllabus.url }}" class="btn btn-outline-primary" target="_blank">📥 ទាញយក Course Syllabus (PDF)</a>
     {% endif %}
     ```

---

**ឯកសារយោងផ្លូវការ (Official Reference)**:
- [Django Documentation - Managing files](https://docs.djangoproject.com/en/4.2/topics/files/)
- [Django Documentation - FileField and ImageField](https://docs.djangoproject.com/en/4.2/ref/models/fields/#filefield)
- [Pillow (PIL Fork) Documentation](https://pillow.readthedocs.io/)
