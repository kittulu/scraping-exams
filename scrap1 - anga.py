from bs4 import BeautifulSoup
import requests
import json

#logar na conta
#inserir cookies de sessão e headers
cookies = {
    #ISERIR COOKIES#
    'inserir cookie':'valor cookie',
    'inserir cookie':'valor cookie',
}

headers = {
    'inserir header':'valor header',
    'inserir header':'valor header',
    #INSERIR HEADER#
    }

#modificar data de inicio e fim do filtro de busca no url#
initialDate = '01/01/2017'
finalDate = '01/01/2020'


response = requests.get(f"https://pixeon.clickvita.com.br/api/delivery/persistence/dashboard/protocols/patient?initialDate={initialDate}&finalDate={finalDate}&institutionCode=null", cookies=cookies, headers=headers)

a=[]
b=[]

for i in json.loads(response.content):
	a.append(i['requestId'])

for i in a:
	url = f"https://pixeon.clickvita.com.br/api/delivery/persistence/dashboard/protocols/exams?requestId={i}&tag=0"
	response = json.loads(requests.get(url, cookies=cookies, headers=headers).content)	
	b.append(response[0]['resource']['identifier'])

#print (b)

#Salva os arquivos em pdf

for i in b:
	url = f"https://pixeon.clickvita.com.br/api/delivery/resource?resourceId={i}"
	r = requests.get(url, cookies=cookies, headers=headers).content	
	open(f"{i}.pdf", 'wb').write(r)