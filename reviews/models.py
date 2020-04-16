from django.db import models
from core import models as core_models


class Reviews(core_models.TimeStampedModel):

    ''' Review Model Definition '''

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name='reviews', on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name='reviews', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.review} - {self.room}'
    
    def rating_average(self):
        avg = (
            self.accuracy,
            self.communication,
            self.location,
            self.check_in,
            self.value
        )
        return round(sum(avg)/6, 2)
    rating_average.short_description = 'Avg'