from django.db import models

import json

# Create your models here.
class Dictionary(models.Model):
    title = models.CharField(null=False, unique=True, max_length=255)
    revision = models.CharField(null=True, max_length=255)
    sequenced = models.BooleanField(null=True, default=False)
    format = models.SmallIntegerField(null=True)
    version = models.SmallIntegerField(null=True)
    author = models.CharField(null=True, max_length=255)
    url = models.URLField(null=True)
    description = models.TextField(null=True)
    attribution = models.TextField(null=True)

    def __str__(self):
        return self.title


class Term(models.Model):
    term = models.CharField(max_length=255)
    reading = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    ruleIdentifiers = models.CharField(max_length=255)
    popularity = models.IntegerField()
    definitions = models.TextField() # JSON
    @property
    def separated_definitions(self):
        return json.loads(self.definitions)

    sequence = models.IntegerField()
    
    dictionary = models.ForeignKey(Dictionary, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.term} ({self.reading}) - {self.definitions}"