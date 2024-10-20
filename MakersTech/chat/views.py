from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatSerializer
from .main import start_chat

class ChatBotAPIView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            
            response = start_chat(prompt)

            if response:
                return Response({'response': response}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Error al generar respuesta.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)