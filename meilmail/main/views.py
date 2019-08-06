from django.shortcuts import render
import sys
sys.path.append("..")
from account.models import Account

# Create your views here.
def home(request):
  context = {}

  if request.user.is_authenticated:
    account = Account.objects.get(user=request.user)
    context.setdefault('nickname', account.nickname)

  return render(request, "main.html", context)