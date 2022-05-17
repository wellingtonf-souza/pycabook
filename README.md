
## [Clean Architectures in Python](https://www.thedigitalcatbooks.com/pycabook-about-the-book/)
***

### Logíca de negócios
A lógica de negócios é o algoritmo ou processo específico que você deseja implementar, a maneira como você transforma dados para fornecer um serviço. É a parte mais importante do sistema.

Os casos de uso implementam as lógicas de negócio.

As partes do sistema que não contêm a lógica de negócios devem ser tratadas como detalhes de implementação. Uma solução ou tecnologia específica é chamada de detalhe quando não é central para o projeto como um todo. A palavra não se refere à complexidade inerente ao assunto, que pode ser maior do que a de partes mais centrais.

### Separação de preocupações
Diferentes partes de um sistema deve gerenciar diferentes partes do processo. Sempre que duas partes separadas de um sistema trabalham nos mesmos dados ou na mesma parte de um processo, elas são acopladas. Embora o acoplamento seja inevitável, quanto maior o acoplamento entre dois componentes, mais difícil é trocar um sem afetar o outro.


*Um sistema de software não é diferente de uma comunidade de trabalho humano, como um escritório ou uma fábrica. Nesses ambientes existem trabalhadores que trocam dados ou objetos físicos para criar e entregar um produto final, seja um objeto ou um serviço. Os trabalhadores precisam de informações e recursos para realizar seu próprio trabalho, mas, acima de tudo, precisam ter uma visão clara de suas responsabilidades.*

### Sistema de armazenamento (storage system)
A abstração representada pelo sistema de armazenamento é: qualquer coisa que o caso de uso possa acessar e que possa fornecer dados é uma fonte. Pode ser um arquivo, um banco de dados (relacional ou não), um endpoint de rede ou um sensor remoto.

### Vantagens de uma arquitetura em camadas
Mudanças exigem modificação em poucos componentes e, principalmente, facilita a **testabilidade**.


### Componentes de uma arquitetura limpa

1. Entidades

    É a camada mais interna, contendo uma representação dos modelos de domínio, que é tudo com que seu sistema precisa interagir e é suficientemente complexa para exigir uma representação específica.

    As entidades possuem conhecimento mútuo, pois vivem na mesma camada, portanto, a arquitetura permite que elas interajam diretamente. Isso significa que uma das classes Python que representam uma entidade pode usar outra diretamente, instanciando-a e chamando seus métodos. As entidades não conhecem nada que viva nas camadas externas, no entanto. Eles não podem chamar o banco de dados, acessar métodos fornecids pela estrutura de apresentação ou instanciar casos de uso.

2. Casos de uso

    A parte mais importante de um sistema limpo são os casos de uso, pois eles implementam as regras de negócios, que são a razão principal da existência do próprio sistema.

    Os casos de uso devem ser os menores possíveis. É muito importante isolar pequenas ações em casos de uso separados, pois isso torna todo o sistema mais fácil de testar, entender e manter. Os casos de uso têm acesso total à camada de entidades, para que possam instanciá-los e usá-los diretamente. Eles também podem chamar uns aos outros, e é comum criar casos de uso complexos compondo casos simples.

3. Entradas (Gateways)

    Esta camada contém componentes que definem interfaces para sistemas externos. Os gateways têm acesso a entidades, portanto a interface pode receber e retornar livremente objetos cujo tipo foi definido naquela camada, pois podem acessar livremente os casos de uso.

4. Sistemas externos

    Esta parte da arquitetura é preenchida por componentes que implementam as interfaces definidas na camada de Gateways. Sistemas externos têm acesso total a gateways, casos de uso e entidades. 

    Quero apontar uma diferença entre sistemas externos que são usados ​​por casos de uso e sistemas externos que querem chamar casos de uso. No primeiro caso a direção da comunicação é para fora, e sabemos que na arquitetura limpa não podemos ir para fora sem interfaces. Assim, quando acessamos um sistema externo a partir de um caso de uso, sempre precisamos de uma interface. Quando o sistema externo quer chamar casos de uso, em vez disso, a direção da comunicação é para dentro, e isso é permitido diretamente, pois as camadas externas têm acesso total às internas.

### Comunicação entre camadas
A Regra de Ouro: fale para dentro com estruturas simples, fale para fora através de interfaces.

### Outras definições
#### repositório: 
* A fonte de informação para o caso de uso.
* Ele pode retornar modelos de domínio
* Pode-se imaginar essa classe sendo o wrapper em torno de um banco de dados real ou qualquer outro tipo de armazenamento