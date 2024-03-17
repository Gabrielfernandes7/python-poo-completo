class Erro:
    # não temos acesso aos outros elementos de nossa classe
    @staticmethod
    def protocolo():
        print("Protocolo apresenta erro")

    @staticmethod
    def entrada():
        print("Parâmetros incorretos")

# não preciso instanciar uma classe para ter acesso as funcionalidades
Erro.protocolo()
Erro.entrada()
