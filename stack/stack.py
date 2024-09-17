class Stack:

    def __init__(self):
        """
        Init é o método construtor das classes no python.
        Este método será executado sempre que a classe stack for instanciada

        Ex.:
        stack = Stack()
        """
        self.items = []

    def push(self, item):
        """
        Push é o método de inserção de dados na pilha.
        Este método recebe o argumento 'item', que será adicionado ao inicio da pilha.
        """
        self.items.append(item)

    def size(self):
        """
        Size é o método que retorna a quantidade total de elementos dentro da pilha.
        """
        return len(self.items)

    def peek(self):
        """
        Peek (ou top) é o método que returna o último elemento adicionado na pilha,
        ou seja, o elemento que está no topo dela e será removido primeiro.
        """
        return self.items[-1]

    def pop(self):
        """
        Pop é o método de remoção de items da pilha.
        Este método sempre removerá o último elemento adicionado,
        ou seja, o elemento que está no topo da pilha
        """
        return self.items.pop()

    def is_empty(self):
        """
        is_empty é o método que diz se a pilha está vazia ou não.
        """

        # se o tamanho da pilha for MAIOR que zero
        if self.size() > 0:
            # returne FALSO
            return False

        # se não for maior que zero, ela estará vazia
        else:
            # então retornamos Verdadeiro
            return True
