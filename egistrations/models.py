from djongo import models

class Registration(models.Model):
    STATUT_CHOICES = [
        ('Laïc', 'Laïc'),
        ('Prêtre', 'Prêtre'),
        ('Religieuse', 'Religieuse'),
    ]

    pelerin_id = models.CharField(max_length=20)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    numero = models.CharField(max_length=20)
    diocese = models.CharField(max_length=100)
    paroisse = models.CharField(max_length=150, blank=True)
    statut_vocationnel = models.CharField(max_length=20, choices=STATUT_CHOICES)
    amount_paid = models.IntegerField(default=50000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pelerin_id
