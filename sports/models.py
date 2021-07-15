from django.db import models

class Sport(models.Model):
    order = models.IntegerField(default=100)
    active = models.BooleanField(default=False)
    sport_name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=50, default='')
    lock_date = models.DateField(auto_now=False, auto_now_add=False)
    award_date = models.DateField(auto_now=False, auto_now_add=False)
    locked = models.BooleanField(default=False)
    
    sport_description = models.TextField(default='Sport Description')
    scoring = models.TextField(default='score')
    favorite = models.TextField(default='favorites')
    competition_dates = models.TextField(default='dates')
    rankings_url = models.URLField(max_length=200, blank=True, help_text="The official website rankings list.")
    menu_image = models.ImageField(blank=True)
    
    INDIVIDUAL = 'IN'
    TEAM = 'TM'
    WINNER_TYPE = (
    (INDIVIDUAL, 'Individual'),
    (TEAM, 'Team'),
    )
    winner_type = models.CharField(max_length=2, choices=WINNER_TYPE, default=TEAM)
    
    awarded = models.BooleanField(default=False)
    gold = models.ForeignKey('sports.Athlete', on_delete=models.CASCADE, blank=True, null=True, related_name = 'gold+')
    silver = models.ForeignKey('sports.Athlete', on_delete=models.CASCADE, blank=True, null=True, related_name = 'silver+')
    bronze = models.ForeignKey('sports.Athlete', on_delete=models.CASCADE, blank=True, null=True, related_name = 'bronze+')
        
    def __str__(self):
        return self.sport_name

class Country(models.Model):
    country = models.CharField(max_length=200, default='', help_text="Full name")
    abbreviation = models.CharField(max_length=3, default='', help_text="3 letter abbreviation")
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
    def __str__(self):
        return self.abbreviation

class Athlete(models.Model):
    athlete_name = models.CharField(max_length=200, default='', help_text="Full Name")
    country = models.ForeignKey('sports.Country', on_delete=models.CASCADE, blank=True, null=True, related_name='country+')
    sports = models.ManyToManyField('sports.Sport', blank=True, related_name='sports+')

    def __str__(self):
        return self.athlete_name
        
class Sport_Images(models.Model):
    title = models.CharField(max_length=200, default='')
    image = models.ImageField()
    alt = models.CharField(max_length=100, default='')
    active = models.BooleanField(default = False, help_text="All active will display.")
    image_attribute = models.CharField(max_length=200, default='', blank=True)
    image_source = models.URLField(max_length=200, blank=True, default='')
    sport = models.ForeignKey('sports.Sport', blank=True, related_name='sport+', on_delete=models.CASCADE,)
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    def __str__(self):
        return self.title
        
