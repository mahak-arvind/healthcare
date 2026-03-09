from django.db import models



class Test(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="tests/")


    def __str__(self):
        return self.name


class Collector(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='collectors/')
    phone = models.CharField(max_length=15)
    rating = models.FloatField(default=4.5)

    def __str__(self):
        return self.name


class Booking(models.Model):

    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    visit_time = models.CharField(max_length=50)
    visit_date = models.DateField()


    collector = models.ForeignKey(
        Collector,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)
