from django.shortcuts import render
from .models import person
from django.http import JsonResponse
from django.db.models import Count
from ..models import Survey ,Question,Choice,Response as SurveyResponse, Answer
from .serializers import (
    SurveySerializer,
    QuestionSerializer,
    ChoiceSerializer,
    ResponseSerializer,
    AnswerSerializer,
    SurveyCreateSerializer
    
)

from .models import Survey, Question,Choice,Response,Answer
from .forms import SurveyForm, QuestionFormSet
from .permission import IsOwnerOrReadOnly
from rest_framework.decorators import action

class SurveyListView(ListView):
    model = Survey
    template_name = 'surveys/survey_list.html'
    context_object_name = 'surveys'
    
    def get_queryset(self):
        return Survey.object.filter(is_active=True) 
    
    class SurveyCreateViewSet(viewsets.ModelViewSet):
        queryset = Survey.objection.all()
        serializer_class = SurveyCreateSerializer
        permission_classes = [IsAuthenticated]
        
        def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
        
        class SurveyViewSet(viewsets.ModelViewSet):
       
         class QuestionViewSet(viewset.ModelViewSet):
       
           class ChoiceAnswer(viewset.ModelViewSet):
               
               class ResponseViewset(viewset.ModelViewSet):
       
                 class AnswerViewset(viewset.ReadOnlyModelViewSet):
        
        ""
        read only endpoint for viewing answers
        ""
        serializer_class = AnswerSerializer
        permission_classes = [permissions. IsAuthenticated]
        
        def get_query(self):
            return Answer.object.filter(
                response__respondent=self.request.user
            ).select_related('question', 'response')
            
    

        
    



    
