import requests

oluheaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
url_olu='http://dict.eudic.net/Home/TranslationAjax'

def trans(content,from_,to_):
    data={'to':to_,'from':from_,'text':content}
    response=requests.post(url_olu,data=data,headers=oluheaders)
    return response.text