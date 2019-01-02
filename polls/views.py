from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Question, Choice
from rest_framework import viewsets
from polls.serializers import QuestionSerializer, ChoiceSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow users to be viewd or edited
    """
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allow users to be viewed or edited
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
