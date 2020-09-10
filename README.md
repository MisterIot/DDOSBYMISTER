# slowloris.py - Slowloris simples em Python

 ## O que é Slowloris?
 Slowloris é basicamente um ataque de negação de serviço HTTP que afeta servidores encadeados.  Funciona assim:

 1. Começamos a fazer muitas solicitações HTTP.
 2. Enviamos cabeçalhos periodicamente (a cada 15 segundos) para manter as conexões abertas.
 3. Nunca fechamos a conexão a menos que o servidor o faça.  Se o servidor fecha uma conexão, criamos uma nova e continuamos fazendo a mesma coisa.

 Isso esgota o pool de threads do servidor e o servidor não pode responder a outras pessoas.

 ## Como instalar e executar?

 Você pode clonar o repositório git ou instalar usando ** pip **.  Veja como você o executa.

 * `sudo pip3 install slowloris`
 * `slowloris example.com`

 Isso é tudo o que é preciso para instalar e executar slowloris.py.


 ### Suporte a proxy SOCKS5

 No entanto, se você planeja usar a opção `-x` para usar um proxy SOCKS5 para conectar em vez de uma conexão direta sobre o seu endereço IP, você precisará instalar a biblioteca` PySocks` (ou qualquer outra implementação do `  biblioteca de meias) também.  [`PySocks`] (https://github.com/Anorov/PySocks) é um fork de [` SocksiPy`] (http://socksipy.sourceforge.net/) do usuário GitHub @Anorov e pode ser facilmente instalado por  adicionar `PySocks` ao comando` pip` acima ou executá-lo novamente assim:

 * `sudo pip3 install PySocks`

 Você pode então usar a opção `-x` para ativar o suporte SOCKS5 e as opções` --proxy-host` e `--proxy-port` para especificar o host proxy SOCKS5 e sua porta, se eles forem diferentes do padrão`  127.0.0.1: 8080`.

 ## Opções de configuração
 É possível modificar o comportamento do slowloris com a linha de comando
 argumentos.  Para obter um documento de ajuda atualizado, basta executar
 `slowloris -h`.

 * -p, --port
 * * Porta do servidor web, geralmente 80
 * -s, --sockets
 * * Número de soquetes para usar no teste
 * -v, --verbose
 * * Aumenta o registro (saída no terminal)
 * -ua, --randuseragents
 * * Randomiza os agentes do usuário com cada solicitação
 * -x, --useproxy
 * * Use um proxy SOCKS5 para conectar
 * --https
 * * Use HTTPS para as solicitações
 * --hora de dormir
 * * Tempo para dormir entre cada cabeçalho enviado

 ## Licença
 O código está licenciado sob a Licença MIT.
