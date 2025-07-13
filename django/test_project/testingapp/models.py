from django.db import models
from django.confib.auth.models import User

class survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('surverys:survery_detail', args=[str(self.id)])
    
    class Question(models.Model):
        
        QUESTION_TYPES = [
            ('text', 'Text Answer'),
            ('single', 'Single Choice'),
            ('multiple', 'Multiple Choice'),
        ]
        survery = models.ForeignKey(Survery, on_delete=models.CASCADE,related_name='questions')
        text = models.TextField()
        question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
        is_required = models.BooleanField(default=True)
        order = models.IntegerField(default=0)
        
        class Meta:
            ordering = ['order']
            
            def __str__(self):
                return f"{self.survey.title} - {self.text[50]}"
            
            class Choices(models.Model):
                question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
                text = models.CharField(max_length=200)
                value = models.CharField(max_length=100)
                
                def __str__(self):
                    return self.text
                
                class Response(models.Model):
                    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='response')
                    respondent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
                    created_at = models.DateTimeField(auto_now_add=True)
                    
                    def __str__(self):
                        return f"Response to {self.survey.title} by {self.respondent or'Anonymous'}"
                
                class Answer(models.Model):
                    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='answers')
                    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
                    text_answer = models.TextField(blank=True, null=True)
                    choive_answer = models.ManyToManyField(Choice,blank=True)
                    
                    def __str__(self):
                        return f"Answer to {self.question.text[:50]}"

#create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to-'profile_pictures/', blank=True)
    
    def __str__(self):
        return  self.user.username
    
    
    