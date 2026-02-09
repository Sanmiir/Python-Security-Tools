import sys

class TextLoader:
    def __init__(self, filename):
        self.filename = filename

    def load_text(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.filename}' não encontrado.")
            sys.exit(1)

class WordlistGenerator:
    def __init__(self, text):
        self.text = text
        self.wordlist = []
    
    def generate(self):
        print("Processando texto...")
        self.text = self.text.lower()

        pontuacoes = [".", ",", ";", "!", "?"]
        for p in pontuacoes: 
            self.text = self.text.replace(p, "")
        
        palavras_brutas = self.text.split()
        palavras_unicas = set()

        for palavra in palavras_brutas:
            if len(palavra) >= 3:
                palavras_unicas.add(palavra)
        
        self.wordlist = sorted(list(palavras_unicas))
        return self.wordlist
    def save_to_file(self, filename):
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for palavra in self.wordlist:
                    file.write(palavra + "\n")
            print(f"Sucesso! Wordlist salva em {filename}")
            print(f"Total de palavras geradas: {len(self.wordlist)}")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correto: python wordlist_generator.py <entrada.txt> <saida.txt")
        sys.exit(1)
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]

    loader = TextLoader(arquivo_entrada)
    texto_bruto = loader.load_text()

    gerador = WordlistGenerator(texto_bruto)
    gerador.generate()

    gerador.save_to_file(arquivo_saida)

