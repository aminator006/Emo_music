from django.db import models

EMOTION_CHOICES = (
    ('fear','FEAR'),
    ('contempt', 'CONTEMPT'),
    ('anger','ANGER'),
    ('sadness','SADNESS'),
    ('surprise','SUPRIZE'),
    ('neutral','NEUTRAL'),
    ('disgust','DISGUST'),
    ('happiness','HAPPINESS'),
)



# Create your models hereself.
class Song(models.Model):
    name = models.CharField(max_length=125)
    audio_file = models.FileField(upload_to='SongsFolder')
    emotionAttached = models.CharField(max_length=20, choices=EMOTION_CHOICES, default='green')

    def __str__(self):
        return self.name
    
