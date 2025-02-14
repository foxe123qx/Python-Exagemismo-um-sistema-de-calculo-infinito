import re

class Exagemismo:
    def __init__(self, estado_inicial="EE"):
        self.estado = self.converter_para_numero(estado_inicial)
        self.historico = []  # Guarda as operações feitas

    def registrar(self, operacao):
        self.historico.append(f"{operacao} → {self.exibir_estado()}")

    def converter_para_numero(self, estado):
        # Conta quantos 'E' existem antes do ".E"
        match = re.match(r"(E+)\.E", estado)
        if match:
            return len(match.group(1))  # Número de Es antes do ".E"
        else:
            return 2  # Se não houver ".E", assume termetria nula (EE = 2)

    def converter_para_exagemismo(self):
        return f"{'E' * self.estado}.E ({self.estado}.1)"  # Exibe Es e o número associado!

    def somar(self):
        self.estado += 8  # Somar 8 ao valor numérico
        self.registrar("+8")

    def subtrair(self):
        if self.estado > 8:
            self.estado -= 8
            self.registrar("-8")
        else:
            print("Operação inválida! Não pode ter menos de 2 Es.")

    def multiplicar(self):
        self.estado *= 2
        self.registrar("x2")

    def estado_auxiliar(self):
        self.estado += 8
        self.registrar("⨀8")

    def auxiliar_positivo(self):
        self.estado += 8
        self.registrar("⨁8")

    def exibir_estado(self):
        return self.converter_para_exagemismo()

    def finalizar(self):
        return f"Fim do cálculo: {self.exibir_estado()}\nHistórico: " + " | ".join(self.historico)

    def modo_interativo(self):
        estado_inicial = input("Digite o estado inicial (ex: EE, EEEE.E): ").strip()
        self.estado = self.converter_para_numero(estado_inicial)
        print("Estado inicial:", self.exibir_estado())

        print("Comandos disponíveis: +8, -8, x2, ⨀8, ⨁8, [E] para finalizar")

        while True:
            comando = input("Digite um comando: ").strip()

            if comando == "+8":
                self.somar()
            elif comando == "-8":
                self.subtrair()
            elif comando == "x2":
                self.multiplicar()
            elif comando == "⨀8":
                self.estado_auxiliar()
            elif comando == "⨁8":
                self.auxiliar_positivo()
            elif comando == "[E]":
                print(self.finalizar())
                break
            else:
                print("Comando inválido! Use +8, -8, x2, ⨀8, ⨁8 ou [E].")

            print("Estado atual:", self.exibir_estado())

# Iniciando o sistema interativo
exagem = Exagemismo()
exagem.modo_interativo()

