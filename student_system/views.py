from django.shortcuts import render
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment

def home(request):
    """Home page with system statistics and 3-role demo test accounts"""
    test_accounts = [
        {
            'role_title': 'អ្នកគ្រប់គ្រងប្រព័ន្ធ (Admin / Superuser)',
            'role_key': 'admin',
            'username': 'admin',
            'password': 'admin123456',
            'badge': 'Superuser & Staff',
            'badge_class': 'bg-dark text-white',
            'border_class': 'border-dark',
            'icon': '👑',
            'description': 'សិទ្ធិខ្ពស់បំផុតក្នុងប្រព័ន្ធ អាចចូលផ្ទាំងគ្រប់គ្រង Django Admin Panel និងគ្រប់គ្រងទិន្នន័យទាំងអស់។',
            'scope': [
                'ចូលប្រើ Django Admin Panel (/admin/)',
                'បង្កើត កែប្រែ និងលុបនិស្សិតទាំងអស់',
                'គ្រប់គ្រងវគ្គសិក្សា និងការចុះឈ្មោះពេញលេញ',
            ],
            'login_url': '/admin/',
            'button_text': 'ចូលគ្រប់គ្រង (Admin)',
            'btn_class': 'btn-dark',
        },
        {
            'role_title': 'សាស្ត្រាចារ្យ (Faculty / Teacher)',
            'role_key': 'teacher',
            'username': 'teacher',
            'password': 'teacher123456',
            'badge': 'Faculty / Staff',
            'badge_class': 'bg-primary text-white',
            'border_class': 'border-primary',
            'icon': '👨‍🏫',
            'description': 'សិទ្ធិជាគ្រូបង្រៀន/បុគ្គលិក អាចមើលបញ្ជីសិស្សទាំងអស់ គ្រប់គ្រងវគ្គសិក្សា និងដាក់ពិន្ទុ Grade។',
            'scope': [
                'មើលបញ្ជីឈ្មោះនិស្សិតទូទាំងសាកលវិទ្យាល័យ',
                'គ្រប់គ្រងវគ្គសិក្សា និងកែប្រែការចុះឈ្មោះ',
                'ដាក់ពិន្ទុ (Add Grades) និងលុប/កែប្រែទិន្នន័យ',
            ],
            'login_url': '/login/',
            'button_text': 'ចូលជាគ្រូ (Teacher)',
            'btn_class': 'btn-primary',
        },
        {
            'role_title': 'និស្សិត (Regular Student)',
            'role_key': 'student',
            'username': 'student',
            'password': 'student123456',
            'badge': 'Student: STU-BBU-001',
            'badge_class': 'bg-success text-white',
            'border_class': 'border-success',
            'icon': '🎓',
            'description': 'សិទ្ធិជានិស្សិតធម្មតា មើលនិងកែប្រែបានតែប្រវត្តិរូបផ្ទាល់ខ្លួន មិនអាចមើល កែប្រែ ឬលុបអ្នកដទៃឡើយ។',
            'scope': [
                'មើល និងកែប្រែបានតែប្រវត្តិរូបផ្ទាល់ខ្លួន',
                'មើល Transcript និងលទ្ធផលសិក្សាផ្ទាល់ខ្លួន',
                '🔒 ត្រូវបានរារាំង មិនឱ្យមើល កែប្រែ ឬលុបអ្នកដទៃ (403)',
            ],
            'login_url': '/login/',
            'button_text': 'ចូលជានិស្សិត (Student)',
            'btn_class': 'btn-success',
        },
    ]

    context = {
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
        'active_students': Student.objects.filter(is_active=True).count(),
        'active_courses': Course.objects.filter(status='ACTIVE').count(),
        'test_accounts': test_accounts,
    }
    return render(request, 'home.html', context)

