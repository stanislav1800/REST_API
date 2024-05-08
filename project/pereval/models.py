from django.db import models



class User(models.Model):
    email = models.EmailField()
    phone_nombers = models.TextField(max_length=255, verbose_name='Контактный телефон')
    fam = models.TextField(max_length=255,verbose_name='Фамилия')
    name = models.TextField(max_length=255, verbose_name='Имя')
    otc = models.TextField(max_length=255, verbose_name='Отчество')

class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

class Level(models.Model):
    winter = models.TextField(verbose_name='Зима', null=True, blank=True)
    summer = models.TextField(verbose_name='Лето', null=True, blank=True)
    autumn = models.TextField(verbose_name='Осень', null=True, blank=True)
    spring = models.TextField(verbose_name='Весна', null=True, blank=True)

class Images(models.Model):
    data = models.ImageField(max_length=2000, verbose_name='Изображение', null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)


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

