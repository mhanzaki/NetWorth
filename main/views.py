from django.shortcuts import render

# Create your views here.
from main.transactions import ShowNetWorth
import json


def display_net_worth(request):
    net_worth = ShowNetWorth()
    net_worth.calculate_net_worth()
    return render(request, 'net_worth.html',
                  {
                      'net_worth': net_worth.net_worth,
                      'labels': json.dumps(net_worth.created_at)
                  })

