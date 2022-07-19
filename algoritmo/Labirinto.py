import pygame       #usando pygame, usar com pip ou baixar separado
class Labirinto:
    def __init__(self):
        self.posicao = []
        self.posicao.append(50) # posicao horizontal
        self.posicao.append(50) # posicao vertical
        self.linhas = []
        self.grade = 60
        self.novos = []
        self.resolvido = False
        self.nCaminhos = 25
        self.corrigido = False

    def montarLabirinto(self, caminho):
        with open(caminho) as arquivo:
            for linha in arquivo:
                novaLinha = []
                for letra in linha:
                    if letra == "\n":
                        continue
                    novaLinha.append(letra)
                self.linhas.append(novaLinha)
        
    def mostrarCelula(self, caracter, screen, x, y):
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
            case 'P':
                cor = (0,255,0)
            case _:
                cor = (self.prendedor(0,255-(caracter*(255//self.nCaminhos)),255),0,self.prendedor(0,caracter*(255//self.nCaminhos),255))
        celula = pygame.Surface((self.grade, self.grade))
        celula.fill(cor)
        screen.blit(celula, (self.posicao[0]+x*self.grade,self.posicao[1]+y*self.grade))


    def mostrarLab(self, screen):
        for linha in range(len(self.linhas)):
            for coluna in range(len(self.linhas[linha])):
                self.mostrarCelula(self.linhas[linha][coluna], screen, coluna, linha)


    def adicionarInicio(self):
        for linha in range(len(self.linhas)):
            for coluna in range(len(self.linhas[linha])):
                if self.linhas[linha][coluna] == 'C':
                    self.novos.append((coluna,linha))   #adicionar a posicao de inicio em novos (x,y)
                    

    def passoResolver(self):
        if self.corrigido:
            return
        dx=(-1,0,0,1)
        dy=(0,-1,1,0)
        if self.resolvido:
            voltando = self.novos[0]
            valor = self.linhas[voltando[0]][voltando[1]]
            self.linhas[voltando[0]][voltando[1]] = 'P'
            if valor != "C":
                for i in range(4):
                    analisando = self.linhas[voltando[0]+dx[i]][voltando[1]+dy[i]]
                    match analisando:
                        case '.':
                            continue
                        case '#':
                            continue
                        case 'C':
                            for linha in range(len(self.linhas)):
                                for coluna in range(len(self.linhas[linha])):
                                    if self.linhas[linha][coluna] not in {'.','#','C','F','P'}:
                                        self.linhas[linha][coluna] = '.'
                        case 'F':
                            continue
                        case 'P':
                            continue
                        case _:
                            if analisando < valor:
                                valor = analisando
                                self.novos[0] = (voltando[0]+dx[i],voltando[1]+dy[i])
                                return
                return
            else:
                for linha in range(len(self.linhas)):
                    for coluna in range(len(self.linhas[linha])):
                        if coluna not in {'.','#','C','F','P'}:
                            self.linhas[linha][coluna] = '.'
                self.corrigido = True
        if len(self.novos) == 0:
            self.adicionarInicio()
            return
        novoNovos = []
        for ponta in self.novos:
            for i in range(4):
                carac = self.linhas[ponta[0]+dx[i]][ponta[1]+dy[i]]
                if carac == ".":
                    # caminho disponivel
                    if self.linhas[ponta[0]][ponta[1]] == 'C':
                        distancia = 0
                    else:
                        distancia = self.linhas[ponta[0]][ponta[1]]+1
                    self.linhas[ponta[0]+dx[i]][ponta[1]+dy[i]] = distancia
                    novoNovos.append((ponta[0]+dx[i],ponta[1]+dy[i]))
                if carac == "F":
                    self.novos = [(ponta[0],ponta[1])]
                    self.resolvido = True
                    return
        self.novos = novoNovos
                    
    def prendedor(self,minimo,valor,maximo):
        if valor<minimo:
            return minimo
        if valor > maximo:
            return maximo
        return valor
