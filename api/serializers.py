from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from main.models import Quiz, Question, Option, Answer, AnswerDetail

#quiz
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'name', 'correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'name', 'options']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'questions', 'amount']


#answer
class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerDetail
        fields = ['question', 'user_choice']

class AnswerSerializer(serializers.ModelSerializer):
    details = AnswerDetailSerializer(many=True)

    class Meta:
        model = Answer
        fields = ['quiz', 'start_time', 'end_time', 'details']
        
        
#docs
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token

