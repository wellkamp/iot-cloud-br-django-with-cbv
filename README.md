<h1> Projeto iot cloud br com Django Class Based Views </h1> 
<h2> Continuação do projeto de sistemas embarcados </h2>
<p>Este projeto é semelhante ao projeto: https://github.com/wellkamp/iot_cloud_br. 
A diferença é a implementação do framework Django para criação da estrutura do projeto.</p>

<p align="center">
 <a href="#objetivo">Objetivo</a> •
 <a href="#roadmap">Roadmap e Features</a> • 
 <a href="#tecnologias">Pré-requisitos</a> • 
 <a href="#contribuicao">Tecnologias</a> • 
 <a href="#licenc-a">Autor</a> • 
 <a href="#autor">Licença</a>
</p>

<h2>Objetivo</h2>
<p>Este projeto tem como objetivo principal de auxiliar os estudos do autor</p>
<h3>Objetivos especificos</h3>
<p>Os objetivos especificos deste projeto é implementar tecnologias de front-end e back-end para criar 
uma página que possa demonstrar registros de valores de um sensor DHT11 enviados para o banco de dados
através de um embarcado que no caso desse projeto é uma esp32.</p>

<h2>Roadmap e Features</h2>
<ul>
<li>[x] Criar um app dos usuarios no Django
<ul>
<li>[x] Cadastro do usuário</li>
<li>[x] Login e logout usuário</li>
</ul>
</li>

<li>[x] Criar um app do perfil dos usuarios no Django
<ul>
<li>[x] Criar/Editar Nome e Sobrenome</li>
<li>[ ] Criar/Editar Foto/Avatar</li>
<li>[ ] Criar/Editar Endereço</li>
<li>[ ] Criar/Editar Documentos</li>
</ul>
</li>

<li>[x] Criar um app dos sensores DHT11 dos usuários no Django
<ul>
<li>[ ] Criar/Deletar Nome de identificação do sensor</li>
<li>[x] Retornar o nome de identificação dos sensosres DHT11 criados do usuário em um template</li>
<li>[x] Retornar os valores do sensor do usuário em uma tabela</li>
<li>[x] Construir um gráfico dos últimos valores de temperatura e umidade do sensor</li>
<li>[x] Deletar o registro de um valor do sensor</li>
<li>[ ] Criar/Deletar servidor MQTT com o nome do tópico escolhido pelo usuário</li>
</ul>
</li>

<li>[x] Implementar os Templates.
<ul>
<li>[x] Construir os templates básicos.</li>
<li>[x] Utilizar o bootstrap para estilizar os tempaltes.</li>
<li>[ ] Avançar na construção de design dos templates.</li>
<li>[ ] Responsividade.</li>
</ul>

<li>[ ] Script servidor MQTT.
<ul>
<li>[ ] Tópico deve ser criado pelo usuário no frontend.</li>
<li>[ ] Usuário deve acionar o momento que quer rodar o servidor.</li>
<li>[ ] Script deve aceitar vários tópicos em um client</li>
</ul>
</li>

<li>[ ] Implementar um módulo em micropython para interagir com a esp32 e o sistema.
<ul>
<li>[ ] Enviar as mensagens por MQTT</li>
</ul>
</li>

<li>[ ] Implementar um bot no telegram para interagir com o sistema.
</li>

</ul>

<h2>Pré-requisitos</h2>
<p> Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
<a href="www.github.com">Git,</a> <a href="https://www.python.org/">Python</a>.
</p>

<p>Além disto é bom ter um editor ou IDE para trabalhar com o código. Este projeto foi utilizado a IDE 
<a href="https://www.jetbrains.com/pt-br/pycharm/">Pycharm</a>.</p>

~~~python
# Rodar o ambiente Virtual do Python
python -m venv ./venv

# Ativar o ambiente virtual do python
venv\Scripts\activate.bat

# Clonar o repositorio
git clone https://github.com/wellkamp/iot-cloud-br-django-with-cbv.git

# Acessar a pasta do projeto no terminal/cmd
cd .\iot-cloud-br-django-with-cbv\

# Instalar o requirements.txt
pip install -r requirements.txt

# Rodar no cmd migrações necessarias para o funcionamento do projeto.
python manage.py migrate

# Criar um super usuário no Django.
python manage.py createsuperuser
~~~

<p>Atualmente a criação do sensor e população dos valores devem ser feitos pelo
admin do Django através do super usuário.</p>

<h2>Tecnologias</h2>
<p>As seguintes Tecnologias foram usadas</p>
<ul>
<li><a href="https://www.python.org/">Python</a></li>
<li><a href="https://www.djangoproject.com/">Django</a></li>
<li><a href="https://pt.wikipedia.org/wiki/HTML">HTML</a></li>
<li><a href="https://pt.wikipedia.org/wiki/Cascading_Style_Sheets">CSS</a></li>
<li><a href="https://pt.wikipedia.org/wiki/JavaScript">Javascript</a></li>
<li><a href="https://getbootstrap.com/">Bootstrap</a></li>
</ul>

<h2>Autor</h2>
<p>
 <img style="border-radius: 50%;" src="https://github.com/wellkamp.png " width="100px;" alt=""/>
 <br />
 <sub><b>Wellington Porto</b></sub></p>

[![Linkedin Badge](https://img.shields.io/badge/-Wellington-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wellington-weikamp-porto-8a00b295/)](https://www.linkedin.com/in/wellington-weikamp-porto-8a00b295/) 
[![Gmail Badge](https://img.shields.io/badge/-wellkamp@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:wellkamp@gmail.com)](mailto:wellkamp@gmail.com)
