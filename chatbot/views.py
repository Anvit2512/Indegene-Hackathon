from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .utils import get_emotional_support

def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        if user_message:
            response = get_emotional_support(user_message)
            return JsonResponse({"response": response})
    return JsonResponse({"error": "Invalid request"}, status=400)
def chatbot_home(request):
    return render(request, "chatbot/chat.html")
