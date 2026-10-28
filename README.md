# Gerenciador Automatizado de Backups - DevOps Simulator 💾

Script em Python que simula um utilitário de infraestrutura e automação (DevOps) para rotinas de cópia de segurança e redundância de dados. O sistema manipula diretórios locais do sistema operacional, gera snapshots temporais (timestamps) dinâmicos e executa o espelhamento completo de arquivos de código de forma segura.

### Tecnologias Utilizadas
- Python 3
- Módulo nativo `os` (Para checagem, validação e gerenciamento de caminhos de arquivos no sistema)
- Módulo nativo `shutil` (Para operações de alto nível sobre coleções de arquivos e diretórios)
- Módulo nativo `datetime` (Para tratamento e formatação de logs de auditoria de tempo real)

### Funcionalidades
- Verificação automatizada e varredura de integridade de pastas locais de códigos-fonte.
- Geração inteligente de snapshots nomeados com data e hora exata da operação para evitar sobreposição de arquivos.
- Mecanismo integrado de tratamento de erros genéricos e logs de confirmação de status da automação.
