class Labirinto:
    def __init__(self):
        self.posicao = []
        self.posicao[0] = 50 # posicao horizontal
        self.posicao[1] = 50 # posicao vertical
        self.linhas = []
        self.grade = 10

    def montarLabirinto(caminho):
        with open(caminho) as arquivo:
            for linha in arquivo:
                novaLinha = []
                for letra in linha:
                    novaLinha.append(letra)
                self.linhas.append(novaLinha)
        
    def mostrarCelula(caracter, screen, x, y):
        cor = (0,0,0)
        match caracter:
            case '.':
                pass
            case '#':
                cor = (255,255,255)
            case 'C':
                cor = (255,0,0)
            case 'F':
                cor = (0,0,255)
        celula = pygame.Surface((grade, grade))
        celula.fill(cor)
        screen.blit(celula, (self.posicao[0]+x*self.grade,self.posicao[1]+y*self.grade))


    def mostrarLab(screen):
        for linha in range(len(self.linhas)):
            for coluna in range(len(self.linhas[linha])):
                mostrarCelula(self.linhas[linha][coluna], screen, coluna, linha)
