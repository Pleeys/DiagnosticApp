from django.db import models


# class Patients(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#     ]
#     patient_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     date_of_birth = models.DateField()
#     diagnoses_confirmed = models.ManyToManyField(Diagnoses)

# class Doctors(models.Model):
#     doctor_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     specialization = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()

# class Diagnoses(models.Model):
#     diagnosis_id = models.AutoField(primary_key=True)
#     ICD10_code = models.CharField(max_length=20)
#     diagnosis_description = models.CharField(max_length=200)
#     emotional_symptoms = models.ManyToManyField('Symptom')
#     cognitive_symptoms = models.ManyToManyField('Symptom')
#     behavioral_symptoms = models.ManyToManyField('Symptom')
#     interpersonal_symptoms = models.ManyToManyField('Symptom')

# class Visits(models.Model):
#     visit_id = models.AutoField(primary_key=True)
#     patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
#     doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
#     diagnosis_id = models.ForeignKey(Diagnoses, on_delete=models.CASCADE)
#     visit_date = models.DateTimeField()

# class Comments(models.Model):
#     comment_id = models.AutoField(primary_key=True)
#     diagnosis_id = models.ForeignKey(Diagnoses, on_delete=models.CASCADE)
#     date_added = models.DateTimeField()
#     content = models.TextField()

# class Symptom(models.Model):
#     symptom_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)