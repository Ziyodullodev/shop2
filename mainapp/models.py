from django.db import models

class Bolim(models.Model):
    nom = models.CharField(max_length=40)
    rasm = models.FileField(upload_to="bolim")

    def __str__(self):
        return self.nom

class Ichki(models.Model):
    nom = models.CharField(max_length=40)
    rasm = models.FileField(upload_to="ichki")
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, related_name="ichki_bolimlar")

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=40)
    rasm = models.FileField(upload_to="mahsulot")
    batafsil = models.TextField()
    brend = models.CharField(max_length=35)
    kafolaat = models.CharField(max_length=35, blank=True)
    mavjud = models.BooleanField(default=True)
    yetkazish = models.CharField(max_length=20, blank=True)
    ichki = models.ForeignKey(Ichki, on_delete=models.CASCADE, related_name="mahsulotlar")
    narx = models.PositiveIntegerField()
    aksiya = models.PositiveSmallIntegerField(default=0)
    mamlakat = models.CharField(max_length=45, default="China")

    def __str__(self):
        return self.nom
