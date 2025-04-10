from django.db import models
from django.contrib.auth.models import AbstractUser

# Modèle principal ( Utilsateur)
class User(AbstractUser):
    is_patient = models.BooleanField(default=False, verbose_name="Patient")
    is_doctor = models.BooleanField(default=False, verbose_name="Médecin")

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.username


# Modèle : Appointment (Rendez-vous)
class Appointment(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name="Patient"
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='doctor_appointments',
        verbose_name="Médecin"
    )
    datetime = models.DateTimeField(verbose_name="Date et heure")
    mode = models.CharField(
        max_length=10,
        choices=[("video", "Vidéo"), ("chat", "Chat")],
        verbose_name="Mode de consultation"
    )
    status = models.CharField(
        max_length=20,
        choices=[("pending", "En attente"), ("done", "Effectué")],
        default="pending",
        verbose_name="Statut"
    )

    class Meta:
        verbose_name = "Rendez-vous"
        verbose_name_plural = "Rendez-vous"

    def __str__(self):
        return f"{self.patient.username} - {self.doctor.username} le {self.datetime}"



# Modèle : MedicalRecord (dossier médical)
class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='medical_records',
        verbose_name="Patient"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    diagnosis = models.TextField(verbose_name="Diagnostic")
    treatment = models.TextField(verbose_name="Traitement")
    file = models.FileField(
        upload_to='records/',
        null=True,
        blank=True,
        verbose_name="Fichier médical"
    )

    class Meta:
        verbose_name = "Dossier médical"
        verbose_name_plural = "Dossiers médicaux"

    def __str__(self):
        return f"Dossier de {self.patient.username} - {self.created_at}"


# Modèle : Reminder (Rappel)
class Reminder(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Patient"
    )
    message = models.CharField(max_length=255, verbose_name="Message")
    date_time = models.DateTimeField(verbose_name="Date et heure")

    class Meta:
        verbose_name = "Rappel"
        verbose_name_plural = "Rappels"

    def __str__(self):
        return f"Rappel pour {self.patient.username} le {self.date_time}"


# Modèle : Feedback (avis sur les médecins)
class Feedback(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Patient"
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name="Médecin"
    )
    rating = models.PositiveSmallIntegerField(verbose_name="Note")  # 1 à 5
    comment = models.TextField(verbose_name="Commentaire")

    class Meta:
        verbose_name = "Avis"
        verbose_name_plural = "Avis"

    def __str__(self):
        return f"Avis de {self.patient.username} sur {self.doctor.username}"