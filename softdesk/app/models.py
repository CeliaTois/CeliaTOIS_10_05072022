from django.db import models

class Users(models.Model):
    user_id = models.fields.IntegerField()
    first_name = models.fields.CharField(max_length=30)
    last_name = models.fields.CharField(max_length=30)
    email = models.fields.EmailField(max_length=254)
    password = models.fields.CharField(max_length=30)


class Projects(models.Model):
    class Type(models.TextChoices):
        BACKEND = 'back-end'
        FRONTEND = 'front-end'
        IOS = 'iOS'
        ANDROID = 'Android'

    project_id = models.fields.IntegerField()
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=254)
    type = models.fields.CharField(choices=Type.choices, max_length=30)
    author_user_id = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)


class Contributors(models.Model):
    class Permission(models.TextChoices):
        AUTHOR = 'author'
        CONTRIBUTOR = 'contributor'
        VISITOR = 'visitor'

    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    permission = models.fields.CharField(choices=Permission.choices, max_length=30)
    role = models.fields.CharField(max_length=30, default='contributor')


class Issues(models.Model):
    class Priority(models.TextChoices):
        FAIBLE = 'FAIBLE'
        MOYENNE = 'MOYENNE'
        ELEVEE = 'ÉLEVÉE'
    
    class Tag(models.TextChoices):
        BUG = 'BUG'
        AMELIORATION = 'AMÉLIORATION'
        TACHE = 'TÂCHE'

    class Status(models.TextChoices):
        A_FAIRE = 'À faire'
        EN_COURS = 'En cours'
        TERMINE = 'Terminé'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=254)
    tag = models.fields.CharField(choices=Tag.choices, max_length=30)
    priority = models.fields.CharField(choices=Priority.choices, max_length=30)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    status = models.fields.CharField(choices=Status.choices, max_length=30)
    author_user_id = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    created_time = models.fields.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment_id = models.fields.IntegerField()
    description = models.fields.CharField(max_length=254)
    author_user_id = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE)
    created_time = models.fields.DateTimeField(auto_now_add=True)
