from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def set_to_default(self):
        """
        Set this note as the default note and unset all other notes.
        """
        Note.objects.exclude(id=self.id).update(is_default=False)
        self.is_default = True
        self.save()
        