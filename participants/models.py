from django.db import models


class Guesses(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    sport = models.ForeignKey('sports.Sport', on_delete=models.CASCADE, blank=True, related_name = 'sport+')
    gold = models.ForeignKey('sports.Athlete', on_delete=models.CASCADE, blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey('sports.Athlete', on_delete=models.CASCADE, blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey('sports.Athlete', on_delete=models.CASCADE, blank=True, null=True, related_name = 'bronze+')
    score = models.IntegerField(default=0)
    class Meta:
        verbose_name = "Guess"
        verbose_name_plural = "Guesses"