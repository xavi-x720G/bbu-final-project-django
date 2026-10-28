"""
Django Management Command: setup_test_data
Build Bright University (BBU) - Student Management System

Sets up initial deployment state:
1. Creates all three role test accounts:
   - Admin / Superuser (admin / admin123456)
   - Faculty / Teacher (teacher / teacher123456)
   - Regular Student (student / student123456)
2. Automatically generates dummy test data (Khmer students, IT courses, enrollments) if DB is empty
"""

from datetime import date
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment


class Command(BaseCommand):
    help = 'Prepares database for deployment by creating 3 role test accounts (Admin, Teacher, Student) and populating test data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--admin-user',
            type=str,
            default='admin',
            help='Superuser username (default: admin)',
        )
        parser.add_argument(
            '--admin-pass',
            type=str,
            default='admin123456',
            help='Superuser password (default: admin123456)',
        )
        parser.add_argument(
            '--admin-email',
            type=str,
            default='admin@bbu.edu.kh',
            help='Superuser email (default: admin@bbu.edu.kh)',
        )
        parser.add_argument(
            '--teacher-user',
            type=str,
            default='teacher',
            help='Teacher username (default: teacher)',
        )
        parser.add_argument(
            '--teacher-pass',
            type=str,
            default='teacher123456',
            help='Teacher password (default: teacher123456)',
        )
        parser.add_argument(
            '--student-user',
            type=str,
            default='student',
            help='Student username (default: student)',
        )
        parser.add_argument(
            '--student-pass',
            type=str,
            default='student123456',
            help='Student password (default: student123456)',
        )
        parser.add_argument(
            '--student-count',
            type=int,
            default=100,
            help='Number of test students to seed if database is empty (default: 100)',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force re-seeding test data even if students already exist',
        )
        parser.add_argument(
            '--no-input', '--noinput',
            action='store_false',
            dest='interactive',
            default=True,
            help='Do NOT prompt the user for input of any kind.',
        )

    def handle(self, *args, **options):
        admin_username = options['admin_user']
        admin_password = options['admin_pass']
        admin_email = options['admin_email']

        teacher_username = options['teacher_user']
        teacher_password = options['teacher_pass']

        student_username = options['student_user']
        student_password = options['student_pass']

        student_count = options['student_count']
        force = options['force']

        self.stdout.write(self.style.MIGRATE_HEADING("⚙️  Running Deployment & 3-Role Test Account Setup..."))

        # ----------------------------------------------------------------------
        # 1. Role 1: Create or update Admin / Superuser
        # ----------------------------------------------------------------------
        admin_user, created_admin = User.objects.get_or_create(username=admin_username)
        admin_user.email = admin_email
        admin_user.first_name = "System"
        admin_user.last_name = "Administrator"
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.set_password(admin_password)
        admin_user.save()

        status_txt = "Created" if created_admin else "Updated"
        self.stdout.write(self.style.SUCCESS(f"  👑 [{status_txt}] Superuser Admin: '{admin_username}' / '{admin_password}'"))

        # ----------------------------------------------------------------------
        # 2. Role 2: Create or update Faculty / Teacher
        # ----------------------------------------------------------------------
        teacher_user, created_teacher = User.objects.get_or_create(username=teacher_username)
        teacher_user.email = 'teacher@bbu.edu.kh'
        teacher_user.first_name = 'Vichea (វិជ្ជា)'
        teacher_user.last_name = 'Heng (ហេង)'
        teacher_user.is_staff = True
        teacher_user.is_superuser = False
        teacher_user.set_password(teacher_password)
        teacher_user.save()

        status_txt = "Created" if created_teacher else "Updated"
        self.stdout.write(self.style.SUCCESS(f"  👨‍🏫 [{status_txt}] Faculty Teacher: '{teacher_username}' / '{teacher_password}'"))

        # ----------------------------------------------------------------------
        # 3. Role 3: Create or update Regular Student
        # ----------------------------------------------------------------------
        student_user, created_student = User.objects.get_or_create(username=student_username)
        student_user.email = 'student@bbu.edu.kh'
        student_user.first_name = 'Dara'
        student_user.last_name = 'Sok'
        student_user.is_staff = False
        student_user.is_superuser = False
        student_user.set_password(student_password)
        student_user.save()

        # Ensure linked Student profile
        student_profile, created_profile = Student.objects.update_or_create(
            user=student_user,
            defaults={
                'student_id': 'STU-BBU-001',
                'khmer_name': 'សុខ ដារ៉ា',
                'date_of_birth': date(2003, 5, 15),
                'gender': 'M',
                'phone_number': '012888999',
                'address': 'Street 271, Sangkat Boeung Tumpun',
                'city': 'Phnom Penh (ភ្នំពេញ)',
                'country': 'Cambodia (កម្ពុជា)',
                'is_active': True,
            }
        )

        status_txt = "Created" if created_student else "Updated"
        self.stdout.write(self.style.SUCCESS(f"  🎓 [{status_txt}] Regular Student: '{student_username}' / '{student_password}' (ID: STU-BBU-001)"))

        # ----------------------------------------------------------------------
        # 4. Check and seed sample test data
        # ----------------------------------------------------------------------
        existing_students = Student.objects.count()
        existing_courses = Course.objects.count()

        if existing_students <= 1 or force:
            self.stdout.write(self.style.NOTICE(f"  🌱 Populating test data ({student_count} Khmer students, IT courses, enrollments)..."))
            try:
                from scripts.generate_khmer_data import run_seed
                run_seed(student_count)
                self.stdout.write(self.style.SUCCESS(f"  ✅ Test data created: {Student.objects.count()} students, {Course.objects.count()} courses, {Enrollment.objects.count()} enrollments."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  ❌ Error seeding test data: {e}"))
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"  ℹ️ Database already contains {existing_students} students and {existing_courses} courses. Skipping bulk seeding (pass --force to re-seed)."
                )
            )

        # ----------------------------------------------------------------------
        # 5. Ensure sample student enrollments & transcript exist
        # ----------------------------------------------------------------------
        available_courses = Course.objects.all()[:3]
        if available_courses.exists() and not student_profile.enrollments.exists():
            grade_data = [
                (available_courses[0], 92.5, 'A', 'COMPLETED', Decimal('4.0')),
            ]
            if len(available_courses) > 1:
                grade_data.append((available_courses[1], 84.0, 'B', 'COMPLETED', Decimal('3.0')))
            if len(available_courses) > 2:
                grade_data.append((available_courses[2], None, None, 'ENROLLED', None))

            for item in grade_data:
                c, scr, grd, stt, _ = item
                Enrollment.objects.get_or_create(
                    student=student_profile,
                    course=c,
                    defaults={
                        'score': scr,
                        'grade': grd,
                        'status': stt,
                        'attendance_percentage': Decimal('95.0'),
                        'notes': 'Test enrollment for student demo account',
                    }
                )

            # Update GPA
            completed = [item[4] for item in grade_data if item[4] is not None]
            if completed:
                student_profile.gpa = round(sum(completed) / len(completed), 2)
                student_profile.save(update_fields=['gpa'])

        self.stdout.write(self.style.SUCCESS("✨ Setup completed! All 3 role accounts are ready to use."))
