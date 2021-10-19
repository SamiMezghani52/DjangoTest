from django.db import models


class School(models.Model):
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Level(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE) 
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.level

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return self.classroom

class Lines(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description
