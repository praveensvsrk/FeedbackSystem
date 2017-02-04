from __future__ import unicode_literals

from django.db import models
class Reporter1(models.Model):
    class Meta:
        unique_together = (('name', 'age'),)
    name = models.CharField(primary_key=True, max_length=70)
    age = models.IntegerField(default=1)
    name2 = models.IntegerField()

    def __str__(self): # __unicode__ on Python 2
        return self.name

class Rep2(models.Model):
    key = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=6)
    def __str__(self):
        return self.key

class Rep3(models.Model):
    name = models.ForeignKey(Reporter1, related_name='rep_name')
    age = models.ForeignKey(Reporter1, related_name='rep_age')
    def __str__(self):
        return self.name.name

class Rep4(models.Model):
    fname = models.OneToOneField(Rep3, primary_key=True)



    '''
class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    def __str__(self): # __unicode__ on Python 2
        return self.headline'''


class AcademicYear(models.Model):
    academic_year_code = models.IntegerField(primary_key=True)
    academic_year = models.CharField(max_length=10)

    def __str__(self):
        return str(self.academic_year_code)


class Department(models.Model):
    department_code = models.CharField(primary_key=True, max_length=10)
    department_name = models.CharField(max_length=30)
    inception_year = models.ForeignKey(AcademicYear)

    def __str__(self):
        return self.department_code


class Faculty(models.Model):
    faculty_code = models.CharField(primary_key=True, max_length=10)
    faculty_first_name = models.CharField(max_length=30)
    faculty_last_name = models.CharField(max_length=30)
    faculty_tel = models.CharField(max_length=30)
    faculty_email = models.CharField(max_length=30)
    home_department = models.CharField(max_length=30)
    joining_date = models.DateTimeField()
    relieved_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.faculty_last_name


class Regulation(models.Model):
    regulation_code = models.CharField(primary_key=True, max_length=10)
    effective_from = models.IntegerField()
    total_required_credits = models.ForeignKey(AcademicYear)

    def __str__(self):
        return self.regulation_code


class Program(models.Model):
    program_code = models.IntegerField(primary_key=True)
    program_name = models.CharField(max_length=30)
    inception_year = models.ForeignKey(AcademicYear)
    owner_department = models.ForeignKey(Department)

    def __str__(self):
        return self.program_name


class SubjectType(models.Model):
    subject_type = models.IntegerField(primary_key=True)
    subject_type_desc = models.CharField(max_length=30)

    def __str__(self):
        return str(self.subject_type)


class SubjectDeliveryType(models.Model):
    subject_delivery_type = models.IntegerField(primary_key=True)
    delivery_type_desc = models.CharField(max_length=30)

    def __str__(self):
        return str(self.subject_delivery_type)


class ProgramStructure(models.Model):
    class Meta:
        unique_together = (('regulation_code', 'program_code', 'subject_code'),)

    regulation_code = models.ForeignKey(Regulation)
    program_code = models.ForeignKey(Program)
    semester = models.IntegerField()
    subject_code = models.CharField(primary_key=True, max_length=30)
    subject_name = models.CharField(max_length=30)
    subject_type = models.ForeignKey(SubjectType)
    subject_delivery_type = models.ForeignKey(SubjectDeliveryType)
    number_hpw = models.IntegerField()
    number_credits = models.IntegerField()

    def __str__(self):
        return self.subject_code


class SubjectOption(models.Model):
    class Meta:
        unique_together = (('regulation_code', 'program_code', 'subject_code', 'subject_option_code'),)

    regulation_code = models.ForeignKey(ProgramStructure, related_name='SO_PS_regulation_code')
    program_code = models.ForeignKey(ProgramStructure, related_name='SO_PS_program_code')
    subject_code = models.ForeignKey(ProgramStructure, related_name='SO_PS_subject_code')
    subject_option_code = models.CharField(primary_key=True, max_length=30)
    subject_option_name = models.CharField(max_length=30)
    offered_by = models.ForeignKey(Department)

    def __str__(self):
        return self.subject_option_code


class FeedbackType(models.Model):
    cycle_no = models.IntegerField(primary_key=True)
    feedback_type_desc = models.CharField(max_length=70)

    def __str__(self):
        return str(self.cycle_no)


class FeedbackQuestion(models.Model):
    class Meta:
        unique_together = (('effective_from', 'cycle_no', 'question_no'),)

    effective_from = models.DateField()
    cycle_no = models.ForeignKey(FeedbackType)
    question_no = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=100)

    def __str__(self):
        return str(self.question_no)


class CourseOffered(models.Model):
    course_code = models.IntegerField(primary_key=True)
    regulation_code = models.ForeignKey(ProgramStructure, related_name='CO_PS_regulation_code')
    program_code = models.ForeignKey(ProgramStructure, related_name='CO_PS_program_code')
    subject_code = models.ForeignKey(ProgramStructure, related_name='CO_PS_subject_code')
    academic_year = models.ForeignKey(AcademicYear)
    semester = models.CharField(max_length=7)
    course_name = models.CharField(max_length=30)
    faculty_name = models.ForeignKey(Faculty)

    def __str__(self):
        return str(self.course_code)


class StudentType(models.Model):
    student_type = models.IntegerField(primary_key=True)
    student_type_desc = models.CharField(max_length=30)

    def __str__(self):
        return str(self.student_type)


class Student(models.Model):
    student_reg_no = models.CharField(primary_key=True, max_length=15)
    student_first_name = models.CharField(max_length=30)
    student_last_name = models.CharField(max_length=30)
    student_type = models.ForeignKey(StudentType)
    academic_year_code = models.ForeignKey(AcademicYear)
    regulation_code = models.ForeignKey(Regulation)

    def __str__(self):
        return self.student_reg_no


# CHECK THIS

class CourseRegistration(models.Model):
    class Meta:
        unique_together = (('course_code', 'student_reg_no'),)

    course_code = models.ForeignKey(CourseOffered)
    student_reg_no = models.OneToOneField(Student, primary_key=True)

    def __str__(self):
        self.student_reg_no


class CourseFeedbackAssignment(models.Model):
    class Meta:
        unique_together = (('course_code', 'student_reg_no', 'cycle_no'),)

    course_code = models.ForeignKey(CourseRegistration, related_name='CourseRegistration_course_code')
    student_reg_no = models.OneToOneField(CourseRegistration, primary_key=True,
                                          related_name='CourseRegistration_student_reg_no')
    cycle_no = models.ForeignKey(FeedbackType)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    feedback_weighting = models.IntegerField()
    is_given = models.IntegerField()

    def __str__(self):
        return str(self.course_code) + self.student_reg_no


class FeedbackCommentLog(models.Model):
    class Meta:
        unique_together = (('feedback_no', 'course_code', 'cycle_no'),)

    feedback_no = models.IntegerField(primary_key=True)
    course_code = models.ForeignKey(CourseOffered)
    cycle_no = models.ForeignKey(FeedbackType)
    feedback_weightING = models.IntegerField()
    feedback_comments = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.feedback_no)


class FeedbackRatingLog(models.Model):
    class Meta:
        unique_together = (('feedback_no', 'course_code', 'cycle_no', 'question_no'),)

    feedback_no = models.ForeignKey(FeedbackCommentLog, related_name='FeedbackCommentLog_feedback_no')
    course_code = models.ForeignKey(FeedbackCommentLog, related_name='FeedbackCommentLog_course_code')
    cycle_no = models.ForeignKey(FeedbackCommentLog, related_name='FeedbackCommentLog_cycle_no')
    question_no = models.IntegerField(primary_key=True)
    feedback_weighting = models.IntegerField()
    rating_answer = models.IntegerField()

    def __str__(self):
        return str(self.feedback_no) + str(self.question_no)


class FeedbackRatingAggregate(models.Model):
    class Meta:
        unique_together = (('course_code', 'cycle_no'),)

    course_code = models.OneToOneField(CourseOffered, primary_key=True)
    cycle_no = models.ForeignKey(FeedbackType)
    Rating_5_count_1 = models.IntegerField()
    Rating_5_count_2 = models.IntegerField()
    Rating_4_count_1 = models.IntegerField()
    Rating_4_count_2 = models.IntegerField()
    Rating_3_count_1 = models.IntegerField()
    Rating_3_count_2 = models.IntegerField()
    Rating_2_count_1 = models.IntegerField()
    Rating_2_count_2 = models.IntegerField()
    Rating_1_count_1 = models.IntegerField()
    Rating_1_count_2 = models.IntegerField()

    def __str__(self):
        return self.course_code


class UserType(models.Model):
    user_type = models.IntegerField(primary_key=True)
    user_type_desc = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user_type)


class Users(models.Model):
    user_type = models.ForeignKey(UserType)
    id_no = models.CharField(max_length=30, primary_key=True)
    crypt_password = models.CharField(max_length=30)
    last_login_time = models.DateTimeField()

    def __str__(self):
        return self.id_no

