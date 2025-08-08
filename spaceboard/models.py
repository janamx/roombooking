from django.db import models

class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return str(self.id)

    @classmethod
    def book(cls, room, user_id, start, end):
        booking = cls.objects.create(
            room=room,
            user_id=user_id,
            start=start,
            end=end,
        )
        booking.save()
        return booking
    
