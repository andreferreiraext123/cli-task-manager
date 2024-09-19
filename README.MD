# CLI Task Manager

## Descrição
Este programa em Python é um sistema básico de gerenciamento de tarefas via terminal. Ele permite que os usuários gerenciem suas tarefas, oferecendo opções para adicionar, visualizar e excluir tarefas. Simples, mas prático para acompanhar suas pendências.

## Funcionalidades
- **Adicionar**: Usuários podem adicionar múltiplas tarefas ao programa.
- **Excluir**: Usuários podem remover tarefas que foram previamente adicionadas.
- **Mostrar**: Usuários podem visualizar todas as tarefas registradas.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal usada para o desenvolvimento.
- **SQLite**: Banco de dados leve utilizado para armazenar as tarefas.
- **PyInstaller**: Ferramenta usada para compilar o projeto em um executável.

## Download do Executável
Você pode baixar o executável do programa [aqui](https://objects.githubusercontent.com/github-production-release-asset-2e65be/858188710/ccc132a7-78c5-4479-a43e-a108fc6e4771?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240919%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240919T234022Z&X-Amz-Expires=300&X-Amz-Signature=48d8726d5811aac4e28c5ba655eb45e95c9e56555a6db2ba871fb027305f2a98&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B filename%3Dmain.exe&response-content-type=application%2Foctet-stream).

## Imagens do Programa
Aqui estão algumas imagens que mostram o programa em funcionamento:

### Menu do Programa
![Menu do programa](docs/images/menu.PNG)

### Tarefas Salvas
![Tarefas salvas](docs/images/list_with_tasks.PNG)

### Limpando Histórico de Tela
![Limpando histórico de tela](docs/images/cleaning_screen.PNG)

### Programa em Execucao
![Fechando programa](docs/images/gif.mp4)


## Uso
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/andreferreiraext123/cli-task-manager
   cd cli-task-manager
2. **Execute o programa:**
    ```bash
    python task_manager.py

3. **Interaja com o menu:**
    ```bash
    --- Task Manager ---
    1. Mostrar tarefas
    2. Adicionar tarefa
    3. Remover tarefa
    4. Limpar tarefa
    5. Sair


4.**Descricao do menu:**
    - Mostrar tarefas: Exibe todas as tarefas.
    - Adicionar tarefa: Solicita uma descrição da tarefa e a adiciona à lista.
    - Remover tarefa: Solicita o número da tarefa a ser removida.
    - Limpar tela: Remove o histórico de tela
    - Sair: Encerra o programa.

## Diagrama da Estrutura do Projeto
![Diagrama da Estrutura do Projeto](docs/images/der.PNG)
