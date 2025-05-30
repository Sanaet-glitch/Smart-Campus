"""
Models for the attendance app.
Defines Student and AttendanceRecord models for tracking attendance.
"""

from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime

class Student(models.Model):
    """Model representing a student with admission number and name."""
    admission_number = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.admission_number} - {self.first_name} {self.last_name}"

class AttendanceRecord(models.Model):
    """Model for tracking student attendance, including verification and status."""
    session = models.ForeignKey('core.ClassSession', on_delete=models.CASCADE, related_name='attendance_records')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    
    # Verification data
    timestamp = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Internal use only
    
    # Status information
    is_verified = models.BooleanField(default=True)
    verification_method = models.CharField(max_length=20, default="GPS")
    
    class Meta:
        unique_together = ['session', 'student']  # Prevent duplicate attendance
        
    def save(self, *args, **kwargs):
        self.timestamp = localtime()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.student} - {self.session} - {'✓' if self.is_verified else '✗'}"
