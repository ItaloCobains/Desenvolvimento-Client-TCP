# Clienttcp.py
## Como instalar ?
` git clone https://github.com/ItaloCobains/Desencolvimento-Client-TCP `
## Como usar ?
` python3 clienttcp.py `

### Explicação do programa:
#### Feito com Socket e sys com dois inputs Host e Port, Tenta um conexão tcp no Host informado caso algum erro acontece ele mostrara na tela o erro e fechara o programa, pois a conexão com o comando `s.shutdown(2)` ele ficará 2 segundo conectado e depois se disconectará para que não fique em loop.
