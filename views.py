from django.shortcuts import render
from django.http import HttpResponse   #追加
from django.shortcuts import render
from datetime import datetime      # 追加
from .models import item        #追加
 
# Create your views here.
###以下追加###
def index(request):
    html = "<h1>myappのウェルカムページです</h1>"
    return HttpResponse(html)
 
def foo(request):
    html = "<h1>fooが指定されたときのページです</h1>"
    return HttpResponse(html)
    
#def hello(request):                       #新たにhello( )関数を追加
#    return render(request, 'index.html')  #追加


#ここから追加
def hello(request):
    context = {
        'datetime': datetime.now(),
        'message': 'Templateを使ってみよう！',
    }
    return render(request, 'index.html', context)


def show_item(request,item_code):
    # item_codeで指定された商品コードでデータベースを検索しデータを取得
    Item = item.objects.get(code=item_code)
    context = {'item':Item, }
    return render(request, 'item.html', context)