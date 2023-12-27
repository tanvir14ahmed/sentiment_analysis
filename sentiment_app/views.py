from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .utils import get_sentiment_label
from pymongo import MongoClient
from .serializers import SentimentSerializer


class SentimentAnalysisAPIView(APIView):
    def post(self, request, format=None):
        serializer = SentimentSerializer(data=request.data)
        
        if serializer.is_valid():
            sentence = serializer.validated_data['sentence']
            sentiment_label = get_sentiment_label(sentence)

            # MongoDB connection and insertion
            with MongoClient('mongodb+srv://tanvir14ahmed:tanviR%4054321@tanvir.vtl6awx.mongodb.net/') as client:
                db = client['sentiment_analysis']
                collection = db['review_data']
                post = {"sentence": sentence, "sentiment": sentiment_label}
                post_id = collection.insert_one(post).inserted_id

            return Response({"sentence": sentence, "sentiment": sentiment_label}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def index(request):
    sentence = None
    sentiment_label = None

    if request.method == 'POST':
        sentence = request.POST.get('sentence')
        sentiment_label = get_sentiment_label(sentence)

        # MongoDB connection and insertion
        with MongoClient('mongodb+srv://tanvir14ahmed:tanviR%4054321@tanvir.vtl6awx.mongodb.net/') as client:
            db = client['sentiment_analysis']
            collection = db['review_data']
            post = {"sentence": sentence, "sentiment": sentiment_label}
            post_id = collection.insert_one(post).inserted_id

    return render(request, 'index.html', {'sentence': sentence, 'sentiment': sentiment_label})