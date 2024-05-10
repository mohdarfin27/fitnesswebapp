from django.shortcuts import render , redirect
#from django.shortcuts import redirect 

from django.http import HttpResponse, HttpResponseBadRequest
from nltk.chat.util import Chat, reflections
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .nltk_chatbot import chatbot

# Create your views here.
def say_hello(request):
    return render(request,'main.html')
def my_function(request):
    # Your Python function logic goes here
    # For example, let's print a message to the console
    a = "Button clicked!"

    # You can return an HTTP response if needed
    return HttpResponse("<h1>{a}</h1>")  # Or return a rendered template
def bmi(request):
    return render(request,'newform.html')
def videoplay(request):
    return render(request,'videoplayer.html');
def videohome(request):
    return render(request,'index.html');
def ecommerce(request):
    return render(request,'ecom.html');
def ecto(request):
    return render(request,'ectomorph.html');
def endo(request):
    return render(request,'endomorph.html');
def meso(request):
    return render(request,'mesomorph.html');
def vid(request):
    return render(request,'index.html');







# Define pairs of patterns and responses




# Define pairs of patterns and responses

# Define pairs of patterns and responses
"""pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing fine, thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["Apologies for any inconvenience.", "No problem, take your time."],
    ],
    [
        r"quit",
        ["Goodbye, take care!", "Have a great day!"],
    ],
]

# Create a chatbot with pairs and reflections
def chatbot_response(message):
    chat = Chat(pairs, reflections)
    reply = chat.respond(message)
    return reply

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = request.POST
        user_message = data.get('message')
        if user_message:
            bot_reply = chatbot_response(user_message)
            return JsonResponse({'reply': bot_reply})
        else:
            return HttpResponseBadRequest("Message not provided.")
    else:
        return HttpResponseBadRequest("Invalid request method.")
    #from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        bot_response = get_bot_response(user_input)
        return render(request, 'chatbot/home.html', {'user_input': user_input, 'bot_response': bot_response})
    return render(request, 'chatbot/home.html', {})"""


#######################################################################################################







# Define patterns and responses for the chatbot


chat_history = []

#def home(request):
    #return render(request, 'chatbot/home.html', {'chat_history': chat_history})

def chatbot_response(request):
    user_input = request.GET.get('user_input', '')
    chatbot_response = chatbot.respond(user_input)
    # Process user input and generate chatbot response using NLTK or other methods
    head ='You: '
    tail = 'Fitbot: '

    # Add user input and chatbot response to chat history
    chat_history.append((user_input, chatbot_response))

    return render(request, 'chatbot/chatbot.html', {'chat_history': chat_history , 'head':head , 'tail':tail})



def linkedin(request):
   
  return redirect('http://localhost:3000')












"""def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = chatbot.respond(user_input)
        return render(request, 'chatbot/home.html', {'response':"chatbot: "+ response ,'user_input':"You: "+user_input })
    
    return render(request, 'chatbot/home.html')  """


