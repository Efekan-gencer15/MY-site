from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()
    twitter = models.URLField(blank=True)

    def __str__(self):
        return self.email
