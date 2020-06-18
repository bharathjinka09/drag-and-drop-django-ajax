from django.db import models

class Paper(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    description = models.TextField()
    answer = models.TextField()
    papers = models.ManyToManyField(Paper, through='PaperQuestion')

    def __str__(self):
        return f"{self.description}, {self.answer}"    

class PaperQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    paper = models.ForeignKey(Paper, on_delete=models.PROTECT)
    active = models.BooleanField()
    order = models.IntegerField()
    
    class Meta():
        ordering = ['order',]
