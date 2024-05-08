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
    img = models.ImageField(max_length=2000, verbose_name='Изображение', null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)



class Pereval(models.Model):
    STATUS_CHOICES = [
        ("new", "новый"),
        ("pending", "в работе"),
        ("accepted", "принят"),
        ("rejected", "отклонен"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.TextField(choices=STATUS_CHOICES)
    beauty_title = models.TextField(blank=True,verbose_name='Основное название вершины', null=True)
    title = models.TextField(blank=True, null=True, verbose_name='Название вершины')
    other_titles = models.TextField(blank=True, null=True,verbose_name='Другое название' )
    connect = models.TextField(blank=True,verbose_name='Связывает', null=True)
    add_time = models.TimeField(auto_now_add=True, blank=True, null=True)

class PerevalImages(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)

