from django.db import models



class User(models.Model):
    email = models.EmailField()
    phone_nombers = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

class Level(models.Model):
    winter = models.CharField(max_length=128)
    summer = models.CharField(max_length=128)
    autumn = models.CharField(max_length=128)
    spring = models.CharField(max_length=128)

class Images(models.Model):
    data = models.ImageField()
    title = models.CharField(max_length=255, null=True)
    date_added = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with open('static/image', 'rb') as f:
            self.data.save(f)



class Pereval(models.Model):
    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        ("NW", "new"),
        ("PN", "pending"),
        ("AC", "accepted"),
        ("RJ", "rejected"),
)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.ManyToManyField(Images, through='PerevalImages')
    coords_id = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level_id = models.OneToOneField(Level, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='NEW')
    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)

class PerevalImages(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)

