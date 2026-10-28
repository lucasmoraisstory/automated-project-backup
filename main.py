# Gerenciador Automatizado de Backups - DevOps Simulator
import os
import shutil
from datetime import datetime

def executar_backup():
    print("=" * 55)
    print("💾 GERENCIADOR DE BACKUP AUTOMATIZADO (DevOps System) 💾")
    print("=" * 55)
    
    # Simulação de diretórios locais
    pasta_projeto = "meu_projeto_ti"
    pasta_backup_diretorio = "backups_sistema"
    
    # Cria as pastas na máquina se elas não existirem para o teste rodar limpo
    if not os.path.exists(pasta_projeto):
        os.makedirs(pasta_projeto)
        # Cria um arquivo fictício de código apenas para ter o que copiar
        with open(f"{pasta_projeto}/main.c", "w") as f:
            f.write("// Codigo fonte protegido pelo sistema de backup\n")
            
    if not os.path.exists(pasta_backup_diretorio):
        os.makedirs(pasta_backup_diretorio)
        
    print(f"\n🔍 Verificando arquivos no diretório: '{pasta_projeto}'...")
    arquivos = os.listdir(pasta_projeto)
    print(f"📦 Arquivos encontrados prontos para salvar: {arquivos}")
    
    # Gera o nome da pasta de backup com a data e hora exata da execução
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destino_final = os.path.join(pasta_backup_diretorio, f"backup_snapshot_{timestamp}")
    
    confirmacao = input("\n🔄 Deseja iniciar a automação do backup agora? (s/n): ").strip().lower()
    
    if confirmacao == 's':
        try:
            # Executa a cópia completa do diretório de forma automatizada
            shutil.copytree(pasta_projeto, destino_final)
            print("\n" + "📊 RELATÓRIO DE SUCESSO DO LOG ".center(45, "="))
            print(f" Status do Job: CONCLUÍDO SEM ERROS")
            print(f" Destino do Snapshot: {destino_final}")
            print(f" Registro salvo no Banco de Logs do Sistema.")
            print("=" * 45)
        except Exception as e:
            print(f"\n❌ Erro crítico no Job de automação: {e}")
    else:
        print("\n⚠️ Operação abortada pelo administrador do sistema.")

if __name__ == "__main__":
    executar_backup()
