# Python Security Tools - Atividades Pós-Graduação

Este repositório contém os scripts desenvolvidos como parte das atividades práticas da disciplina de Python para Cibersegurança.

## Arquivos do Projeto

### 1. `wordlist_generator.py` (Gerador de Wordlists)
Uma ferramenta CLI robusta para criação de wordlists direcionadas (Targeted Wordlists) baseadas em engenharia social.
- **Funcionalidades:**
  - Leitura de arquivo de entrada.
  - Normalização de texto (minúsculo/maiúsculo).
  - Geração de permutações com datas e caracteres especiais.
  - Implementação de lógica **Leetspeak** (ex: `admin` -> `4dm1n`).
  - Remoção automática de duplicatas.

**Uso:**
```bash
python wordlist_generator.py
```

# Siga as instruções interativas no terminal
2. recon.py (Arquitetura de Scanner)
Um exercício focado na estrutura de Classes e Orientação a Objetos (POO) para ferramentas de reconhecimento.


Objetivo: Demonstrar a lógica de estruturação de um scanner de portas.

Funcionalidades:

Classes Target e Recon.

Tratamento de argumentos via linha de comando (sys.argv).

Simulação de detecção de serviços baseada em portas padrão.

Uso:

Bash
python recon.py <host> <porta>
# Exemplo: python recon.py 192.168.0.1 80
Desenvolvido por: Sanmir
