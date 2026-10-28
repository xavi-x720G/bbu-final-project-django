from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Enrollment
from .forms import EnrollmentForm, GradeForm, EnrollmentFilterForm

# Function-Based Views (FBV)

@login_required
def enrollment_list(request):
    """List all enrollments with filtering options (Students see only own enrollments)"""
    enrollments = Enrollment.objects.select_related('student', 'course')
    
    # Students are restricted to viewing only their own enrollments
    if not request.user.is_staff:
        if hasattr(request.user, 'student'):
            enrollments = enrollments.filter(student=request.user.student)
        else:
            enrollments = enrollments.none()

    form = EnrollmentFilterForm(request.GET or None)
    
    # Apply filters
    if form.is_valid():
        if form.cleaned_data.get('status'):
            enrollments = enrollments.filter(status=form.cleaned_data['status'])
        
        if form.cleaned_data.get('student') and request.user.is_staff:
            enrollments = enrollments.filter(
                student__student_id__icontains=form.cleaned_data['student']
            )
        
        if form.cleaned_data.get('course'):
            enrollments = enrollments.filter(
                course__code__icontains=form.cleaned_data['course']
            )
    
    context = {
        'enrollments': enrollments,
        'form': form,
    }
    return render(request, 'enrollments/enrollment_list.html', context)

@login_required
def enrollment_detail(request, pk):
    """Display detailed information about an enrollment"""
    enrollment = get_object_or_404(Enrollment, pk=pk)
    
    # Permission check: Staff or enrollment owner
    if not request.user.is_staff and (not hasattr(request.user, 'student') or enrollment.student != request.user.student):
        raise PermissionDenied("You are not authorized to view this enrollment.")
    
    context = {'enrollment': enrollment}
    return render(request, 'enrollments/enrollment_detail.html', context)

@login_required
def enrollment_create(request):
    """Create a new enrollment (Staff only)"""
    if not request.user.is_staff:
        raise PermissionDenied("Only instructors and staff can create enrollments.")

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save()
            return redirect('enrollments:enrollment_detail', pk=enrollment.pk)
    else:
        form = EnrollmentForm()
    
    context = {'form': form, 'title': 'Create Enrollment'}
    return render(request, 'enrollments/enrollment_form.html', context)

@login_required
def enrollment_update(request, pk):
    """Update enrollment information (Staff only)"""
    if not request.user.is_staff:
        raise PermissionDenied("Only instructors and staff can update enrollments.")

    enrollment = get_object_or_404(Enrollment, pk=pk)
    
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollments:enrollment_detail', pk=enrollment.pk)
    else:
        form = EnrollmentForm(instance=enrollment)
    
    context = {'form': form, 'enrollment': enrollment, 'title': 'Update Enrollment'}
    return render(request, 'enrollments/enrollment_form.html', context)

@login_required
def enrollment_delete(request, pk):
    """Delete an enrollment (Staff only)"""
    if not request.user.is_staff:
        raise PermissionDenied("Only instructors and staff can delete enrollments.")

    enrollment = get_object_or_404(Enrollment, pk=pk)
    
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollments:enrollment_list')
    
    context = {'enrollment': enrollment}
    return render(request, 'enrollments/enrollment_confirm_delete.html', context)

@login_required
def add_grade(request, pk):
    """Add or update grade for an enrollment (Staff only)"""
    if not request.user.is_staff:
        raise PermissionDenied("Only instructors and staff can assign grades.")

    enrollment = get_object_or_404(Enrollment, pk=pk)
    
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollments:enrollment_detail', pk=enrollment.pk)
    else:
        form = GradeForm(instance=enrollment)
    
    context = {'form': form, 'enrollment': enrollment}
    return render(request, 'enrollments/add_grade.html', context)

@login_required
def student_transcript(request, student_id):
    """Generate transcript for a student showing all enrollments and grades (Staff or own profile)"""
    from students.models import Student
    
    student = Student.objects.filter(student_id=student_id).first()
    if not student and str(student_id).isdigit():
        student = Student.objects.filter(pk=int(student_id)).first()
    if not student:
        raise Http404("Student not found")

    # Permission check: Only staff or the student themselves can view the transcript
    if not request.user.is_staff and student.user != request.user:
        raise PermissionDenied("You are not authorized to view other students' transcripts.")

    enrollments = student.enrollments.all()
    
    # Calculate GPA
    completed_courses = enrollments.filter(status='COMPLETED', score__isnull=False)
    average_score = completed_courses.aggregate(Avg('score'))['score__avg'] if completed_courses else 0
    
    context = {
        'student': student,
        'enrollments': enrollments,
        'average_score': round(average_score, 2) if average_score else 0,
        'total_courses': enrollments.count(),
        'completed_courses': completed_courses.count(),
    }
    return render(request, 'enrollments/student_transcript.html', context)

# Class-Based Views (CBV)

class EnrollmentListView(LoginRequiredMixin, ListView):
    """Class-based view for listing enrollments"""
    model = Enrollment
    template_name = 'enrollments/enrollment_list.html'
    context_object_name = 'enrollments'
    paginate_by = 20
    
    def get_queryset(self):
        qs = Enrollment.objects.select_related('student', 'course').order_by('-enrollment_date')
        if not self.request.user.is_staff:
            if hasattr(self.request.user, 'student'):
                return qs.filter(student=self.request.user.student)
            return qs.none()
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EnrollmentFilterForm(self.request.GET or None)
        return context

class EnrollmentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Class-based view for enrollment details"""
    model = Enrollment
    template_name = 'enrollments/enrollment_detail.html'
    context_object_name = 'enrollment'

    def test_func(self):
        enrollment = self.get_object()
        return self.request.user.is_staff or (hasattr(self.request.user, 'student') and enrollment.student == self.request.user.student)

class EnrollmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """Class-based view for creating a new enrollment (Staff only)"""
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollments:enrollment_list')

    def test_func(self):
        return self.request.user.is_staff

class EnrollmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Class-based view for updating enrollment information (Staff only)"""
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollments:enrollment_list')

    def test_func(self):
        return self.request.user.is_staff

class EnrollmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Class-based view for deleting an enrollment (Staff only)"""
    model = Enrollment
    template_name = 'enrollments/enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollments:enrollment_list')

    def test_func(self):
        return self.request.user.is_staff
