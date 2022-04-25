from django.shortcuts import render

def main_page(request):
    '''
    This is main page. He returned template('index.html')
    '''
    return render(request, 'index.html')

