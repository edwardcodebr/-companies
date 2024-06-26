class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, raiz, chave):
        if not raiz:
            return No(chave)
        elif chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        else:
            raiz.direita = self.inserir(raiz.direita, chave)

        raiz.altura = 1 + max(self.obter_altura(raiz.esquerda), self.obter_altura(raiz.direita))
        equilibrio = self.obter_equilibrio(raiz)

        if equilibrio > 1 and chave < raiz.esquerda.chave:
            return self.rotacao_direita(raiz)
        if equilibrio < -1 and chave > raiz.direita.chave:
            return self.rotacao_esquerda(raiz)
        if equilibrio > 1 and chave > raiz.esquerda.chave:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        if equilibrio < -1 and chave < raiz.direita.chave:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def remover(self, raiz, chave):
        if not raiz:
            return raiz
        elif chave < raiz.chave:
            raiz.esquerda = self.remover(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.remover(raiz.direita, chave)
        else:
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp
            temp = self.obter_no_minimo(raiz.direita)
            raiz.chave = temp.chave
            raiz.direita = self.remover(raiz.direita, temp.chave)

        if raiz is None:
            return raiz

        raiz.altura = 1 + max(self.obter_altura(raiz.esquerda), self.obter_altura(raiz.direita))
        equilibrio = self.obter_equilibrio(raiz)

        if equilibrio > 1 and self.obter_equilibrio(raiz.esquerda) >= 0:
            return self.rotacao_direita(raiz)
        if equilibrio < -1 and self.obter_equilibrio(raiz.direita) <= 0:
            return self.rotacao_esquerda(raiz)
        if equilibrio > 1 and self.obter_equilibrio(raiz.esquerda) < 0:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
        if equilibrio < -1 and self.obter_equilibrio(raiz.direita) > 0:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def buscar(self, raiz, chave):
        if raiz is None or raiz.chave == chave:
            return raiz
        if chave < raiz.chave:
            return self.buscar(raiz.esquerda, chave)
        return self.buscar(raiz.direita, chave)

    def obter_altura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    def obter_equilibrio(self, raiz):
        if not raiz:
            return 0
        return self.obter_altura(raiz.esquerda) - self.obter_altura(raiz.direita)

    def rotacao_direita(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y

    def rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.obter_altura(z.esquerda), self.obter_altura(z.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        return y

    def obter_no_minimo(self, raiz):
        if raiz is None or raiz.esquerda is None:
            return raiz
        return self.obter_no_minimo(raiz.esquerda)

    def imprimir_arvore(self, raiz, nivel=0):
        if raiz is not None:
            self.imprimir_arvore(raiz.direita, nivel + 1)
            print(' ' * 4 * nivel + '->', raiz.chave)
            self.imprimir_arvore(raiz.esquerda, nivel + 1)

    def altura(self):
        return self.obter_altura(self.raiz)

    def esta_balanceada(self):
        return abs(self.obter_equilibrio(self.raiz)) <= 1

    def caminho_para_no(self, raiz, chave):
        if raiz is None:
            return None
        if raiz.chave == chave:
            return [raiz.chave]
        if chave < raiz.chave:
            caminho = self.caminho_para_no(raiz.esquerda, chave)
        else:
            caminho = self.caminho_para_no(raiz.direita, chave)
        if caminho is not None:
            return [raiz.chave] + caminho
        return None

    def inserir_em_lote(self, elementos):
        for elemento in elementos:
            self.raiz = self.inserir(self.raiz, elemento)

    def remover_condicional(self, a, b):
        elementos_para_remover = self._busca_intervalo(self.raiz, a, b)
        for elemento in elementos_para_remover:
            self.raiz = self.remover(self.raiz, elemento)

    def _busca_intervalo(self, raiz, a, b):
        if raiz is None:
            return []
        elementos = []
        if a <= raiz.chave <= b:
            elementos.append(raiz.chave)
        elementos += self._busca_intervalo(raiz.esquerda, a, b)
        elementos += self._busca_intervalo(raiz.direita, a, b)
        return elementos

    def k_esimo_maior(self, k):
        elementos = []
        self._em_ordem(self.raiz, elementos)
        if k <= len(elementos):
            return elementos[-k]
        return None

    def _em_ordem(self, raiz, elementos):
        if raiz is not None:
            self._em_ordem(raiz.esquerda, elementos)
            elementos.append(raiz.chave)
            self._em_ordem(raiz.direita, elementos)

# Exemplo de uso:
arvore_avl = ArvoreAVL()
elementos = [10, 20, 30, 40, 50, 25]
arvore_avl.inserir_em_lote(elementos)
arvore_avl.imprimir_arvore(arvore_avl.raiz)