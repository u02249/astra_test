from django.shortcuts import render
from .models import Message
from .forms import MessageForm

# Create your views here.
def messages(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            m = Message.objects.create(message=form.cleaned_data.get("message"))
            m.save()

    all_messages = Message.objects.order_by('-createdon')
    ctx = { 'messages': all_messages, 'form': MessageForm() }
    return render(request, 'messages.html', context=ctx)
