from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def fed_for_today(self):
      return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
    def __str__(self):
       return f'{self.name}'
    
    def get_absolute_url(self):
       return reverse('detail', kwargs={'dog_id': self.id})

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
	      choices=MEALS,
	      default=MEALS[0][0]
  )
    
  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
      return f"Photo for dog_id: {self.dog_id} @{self.url}"