from django.db import models


class User(models.Model):
    login = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.login
        
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.content

class ChatRoom(models.Model):
    # recoit un unique ID
    id = models.AutoField(primary_key=True)
    # Premier auteur
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    users = models.ManyToManyField(User)
    messages = models.ManyToManyField(Message)

    def __str__(self):
        return self.title