from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yf
####I will be using the yfinance api to generate news and stock details

def home(request):
    """
    THIS VIEW REPRESENTS THE HOMEPAGE.
    IT RETURNS NEWS ABOUT VARIOUS STOCKS
    """

