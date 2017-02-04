# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('academic_year_code', models.IntegerField(primary_key=True, serialize=False)),
                ('academic_year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffered',
            fields=[
                ('course_code', models.IntegerField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=7)),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=30)),
                ('inception_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.AcademicYear')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('faculty_first_name', models.CharField(max_length=30)),
                ('faculty_last_name', models.CharField(max_length=30)),
                ('faculty_tel', models.CharField(max_length=30)),
                ('faculty_email', models.CharField(max_length=30)),
                ('home_department', models.CharField(max_length=30)),
                ('joining_date', models.DateTimeField()),
                ('relieved_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackCommentLog',
            fields=[
                ('feedback_no', models.IntegerField(primary_key=True, serialize=False)),
                ('feedback_weightING', models.IntegerField()),
                ('feedback_comments', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackQuestion',
            fields=[
                ('effective_from', models.DateField()),
                ('question_no', models.IntegerField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackRatingLog',
            fields=[
                ('question_no', models.IntegerField(primary_key=True, serialize=False)),
                ('feedback_weighting', models.IntegerField()),
                ('rating_answer', models.IntegerField()),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FeedbackCommentLog_course_code', to='Feedback.FeedbackCommentLog')),
                ('cycle_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FeedbackCommentLog_cycle_no', to='Feedback.FeedbackCommentLog')),
                ('feedback_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FeedbackCommentLog_feedback_no', to='Feedback.FeedbackCommentLog')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackType',
            fields=[
                ('cycle_no', models.IntegerField(primary_key=True, serialize=False)),
                ('feedback_type_desc', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_code', models.IntegerField(primary_key=True, serialize=False)),
                ('program_name', models.CharField(max_length=30)),
                ('inception_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.AcademicYear')),
                ('owner_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.Department')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramStructure',
            fields=[
                ('semester', models.IntegerField()),
                ('subject_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=30)),
                ('number_hpw', models.IntegerField()),
                ('number_credits', models.IntegerField()),
                ('program_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('regulation_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('effective_from', models.IntegerField()),
                ('total_required_credits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.AcademicYear')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_reg_no', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('student_first_name', models.CharField(max_length=30)),
                ('student_last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentType',
            fields=[
                ('student_type', models.IntegerField(primary_key=True, serialize=False)),
                ('student_type_desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectDeliveryType',
            fields=[
                ('subject_delivery_type', models.IntegerField(primary_key=True, serialize=False)),
                ('delivery_type_desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectOption',
            fields=[
                ('subject_option_code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('subject_option_name', models.CharField(max_length=30)),
                ('offered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.Department')),
                ('program_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SO_PS_program_code', to='Feedback.ProgramStructure')),
                ('regulation_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SO_PS_regulation_code', to='Feedback.ProgramStructure')),
                ('subject_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SO_PS_subject_code', to='Feedback.ProgramStructure')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectType',
            fields=[
                ('subject_type', models.IntegerField(primary_key=True, serialize=False)),
                ('subject_type_desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_no', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('crypt_password', models.CharField(max_length=30)),
                ('last_login_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('user_type', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type_desc', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('student_reg_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Feedback.Student')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackRatingAggregate',
            fields=[
                ('course_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Feedback.CourseOffered')),
                ('Rating_5_count_1', models.IntegerField()),
                ('Rating_5_count_2', models.IntegerField()),
                ('Rating_4_count_1', models.IntegerField()),
                ('Rating_4_count_2', models.IntegerField()),
                ('Rating_3_count_1', models.IntegerField()),
                ('Rating_3_count_2', models.IntegerField()),
                ('Rating_2_count_1', models.IntegerField()),
                ('Rating_2_count_2', models.IntegerField()),
                ('Rating_1_count_1', models.IntegerField()),
                ('Rating_1_count_2', models.IntegerField()),
                ('cycle_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.FeedbackType')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.UserType'),
        ),
        migrations.AddField(
            model_name='student',
            name='academic_year_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.AcademicYear'),
        ),
        migrations.AddField(
            model_name='student',
            name='regulation_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.Regulation'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.StudentType'),
        ),
        migrations.AddField(
            model_name='programstructure',
            name='regulation_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.Regulation'),
        ),
        migrations.AddField(
            model_name='programstructure',
            name='subject_delivery_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.SubjectDeliveryType'),
        ),
        migrations.AddField(
            model_name='programstructure',
            name='subject_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.SubjectType'),
        ),
        migrations.AddField(
            model_name='feedbackquestion',
            name='cycle_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.FeedbackType'),
        ),
        migrations.AddField(
            model_name='feedbackcommentlog',
            name='course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.CourseOffered'),
        ),
        migrations.AddField(
            model_name='feedbackcommentlog',
            name='cycle_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.FeedbackType'),
        ),
        migrations.AddField(
            model_name='courseoffered',
            name='academic_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.AcademicYear'),
        ),
        migrations.AddField(
            model_name='courseoffered',
            name='faculty_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.Faculty'),
        ),
        migrations.AddField(
            model_name='courseoffered',
            name='program_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CO_PS_program_code', to='Feedback.ProgramStructure'),
        ),
        migrations.AddField(
            model_name='courseoffered',
            name='regulation_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CO_PS_regulation_code', to='Feedback.ProgramStructure'),
        ),
        migrations.AddField(
            model_name='courseoffered',
            name='subject_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CO_PS_subject_code', to='Feedback.ProgramStructure'),
        ),
        migrations.CreateModel(
            name='CourseFeedbackAssignment',
            fields=[
                ('student_reg_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='CourseRegistration_student_reg_no', serialize=False, to='Feedback.CourseRegistration')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('feedback_weighting', models.IntegerField()),
                ('is_given', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='subjectoption',
            unique_together=set([('regulation_code', 'program_code', 'subject_code', 'subject_option_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='programstructure',
            unique_together=set([('regulation_code', 'program_code', 'subject_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='feedbackratinglog',
            unique_together=set([('feedback_no', 'course_code', 'cycle_no', 'question_no')]),
        ),
        migrations.AlterUniqueTogether(
            name='feedbackquestion',
            unique_together=set([('effective_from', 'cycle_no', 'question_no')]),
        ),
        migrations.AlterUniqueTogether(
            name='feedbackcommentlog',
            unique_together=set([('feedback_no', 'course_code', 'cycle_no')]),
        ),
        migrations.AddField(
            model_name='courseregistration',
            name='course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.CourseOffered'),
        ),
        migrations.AlterUniqueTogether(
            name='feedbackratingaggregate',
            unique_together=set([('course_code', 'cycle_no')]),
        ),
        migrations.AlterUniqueTogether(
            name='courseregistration',
            unique_together=set([('course_code', 'student_reg_no')]),
        ),
        migrations.AddField(
            model_name='coursefeedbackassignment',
            name='course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CourseRegistration_course_code', to='Feedback.CourseRegistration'),
        ),
        migrations.AddField(
            model_name='coursefeedbackassignment',
            name='cycle_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feedback.FeedbackType'),
        ),
        migrations.AlterUniqueTogether(
            name='coursefeedbackassignment',
            unique_together=set([('course_code', 'student_reg_no', 'cycle_no')]),
        ),
    ]