from experta import *
from numpy import loadtxt  # numpy==1.22.1
import linecache


class ValoresInicializacao(Fact):
    pass


class ComposicaoGas(Fact):
    pass


class Reforma(Fact):
    pass


class Pulmao(Fact):
    pass


aviso = '\n'


class Prototipo(KnowledgeEngine):
    @Rule(ValoresInicializacao(vazao=MATCH.vazao),
          TEST(lambda vazao: vazao == 0))
    def iniciarSistema(self):
        global aviso
        aviso = 'Vazão desligada, por favor iniciar sistema#' + aviso

    @Rule(ComposicaoGas(h2s=MATCH.h2s),
          TEST(lambda h2s: h2s >= 50))
    def reduzirVazaoH2S(self, h2s):
        global aviso
        aviso = 'H2S em '+str(h2s) + \
            '. ATENÇÃO: Reduzindo vazão em 25%#' + aviso
        escreverArquivo()

    @Rule(ComposicaoGas(ch4=MATCH.ch4),
          TEST(lambda ch4: ch4 >= 55))
    def reduzirVazaoCH4(self, ch4):
        global aviso
        aviso = 'CH4 em '+str(ch4) + \
            '%. ATENÇÃO: Reduzindo vazão em 25%#' + aviso
        escreverArquivo()

    @Rule(ComposicaoGas(co=MATCH.co),
          TEST(lambda co: co >= 58))
    def reduzirVazao(self, co):
        global aviso
        aviso = 'CO em '+str(co) + \
            '%. ATENÇÃO: Reduzindo vazão em 25%#' + aviso
        escreverArquivo()

    @Rule(ComposicaoGas(pureza=MATCH.pureza),
          TEST(lambda pureza: pureza < 99))
    def valvulaPSA(self, pureza):
        global aviso
        aviso = 'Pureza em '+str(pureza) + \
            '%. Abrindo válvula para PSA#' + aviso

    @Rule(Reforma(temperatura=MATCH.temperatura),
          TEST(lambda temperatura: temperatura < 600))
    def aumentarTemperatura(self):
        global aviso
        aviso = 'Aumentando temperatura#' + aviso

    @Rule(Reforma(temperatura=MATCH.temperatura),
          TEST(lambda temperatura: temperatura >= 820))
    def alertaTemperatura(self, temperatura):
        global aviso
        aviso = 'CUIDADO: Temperatura em '+str(temperatura)+'°C#' + aviso

    @Rule(Reforma(temperatura=MATCH.temperatura),
          TEST(lambda temperatura: temperatura >= 850))
    def pararProcesso(self):
        global aviso
        aviso = 'Parando processo#' + aviso

    @Rule(Pulmao(pressao=MATCH.pressao),
          TEST(lambda pressao: pressao == 2))
    def vazaoCelulaCombustivel(self):
        global aviso
        aviso = 'Iniciar vazão para Célula Combustível#' + aviso

    @Rule(Reforma(pressao=MATCH.pressao),
          TEST(lambda pressao: pressao >= 2.5))
    def reduzirVazaoPressao(self, pressao):
        global aviso
        aviso = 'Pressão na reforma em ' + \
            str(pressao) + ' bar. ATENÇÃO: Reduzindo vazão em 25%#' + aviso
        escreverArquivo()

    @Rule(Reforma(umidade=MATCH.umidade),
          TEST(lambda umidade: umidade > 2))
    def reduzirVazaoUmidade(self, umidade):
        global aviso
        aviso = 'Umidade em '+str(umidade) + \
            '%. ATENÇÃO: Reduzindo vazão em 25%#' + aviso
        escreverArquivo()

vazao = float(linecache.getline('dados.txt', 1))
VAZAORAIZ = vazao * 0.25

def escreverArquivo():
    global VAZAORAIZ
    vazao = float(linecache.getline('dados.txt', 1))
    vazao = vazao - VAZAORAIZ

    lines = open('dados.txt', 'r').readlines()
    lines[0] = str(vazao)+ '\n'
    out = open('dados.txt', 'w')
    out.writelines(lines)
    out.close()


def main():

    lines = loadtxt('dados.txt', delimiter='\n')
    p = Prototipo()
    p.reset()
    p.declare(ValoresInicializacao(vazao=lines[0]), ComposicaoGas(h2s=lines[8]),
              ComposicaoGas(ch4=lines[6]), Reforma(temperatura=lines[1]),
              Reforma(pressao=lines[5]), Reforma(umidade=lines[2]),
              ComposicaoGas(co=lines[7]), ComposicaoGas(pureza=lines[3]),
              Pulmao(pressao=lines[4]))
    p.run()
    return aviso
