from bs4 import BeautifulSoup
import requests

#fazer login, inserir cookie##
cookie = 'inserir cookies'
#colocar na var 'z' quantiadde de paginas que possui##
z=5


z+=1
codped = []
for i in range(1,z):
	url = f"https://www.laboranalises.uniexames.srv.br/pedidos/index?page={i}"
	print(url)
	html = requests.get(url , headers={"Cookie": cookie}).content
	soup = BeautifulSoup(html, 'html.parser')
	parent = soup.find("ul", {"id": "resultados"})
	results = parent.findAll("p",{"class":"codped"})
	for i in results:
		codped.append(i.getText())	

print(len(codped))

for i in codped:
	idzes = i[:2]
	contetzes = i[2:]
	print(idzes+"   "+contetzes) 
	url = f"https://www.laboranalises.uniexames.srv.br/pedidos/download-laudo?CCODIPOST={idzes}&CCODIPEDI={contetzes}"
	r = requests.get(url,headers={"Cookie": cookie}, allow_redirects=True)
	open(f"{i}.pdf", 'wb').write(r.content)

 