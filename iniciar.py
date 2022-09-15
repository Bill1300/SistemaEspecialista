# pip install tk
from tkinter import *
import tkinter as tk
from tkinter import Canvas
import datetime
from pathlib import Path
import os
import csv
import re
from tkinter import filedialog as file
import linecache
from sistemaEspecialista import main


def algoritmoEspecialista():
    txtRetorno = main()
    txtRetorno = txtRetorno.split('#')
    txtRetorno.pop()
    print(txtRetorno)
    return txtRetorno


def criarTela():

    def apagarSaida(lbl):
        return 0

    def salvarDados():

        def escreverArquivo():

            dataArquivo = datetime.datetime.now().strftime('%d-%m-%Y')
            horario = datetime.datetime.now().strftime('%H:%M:%S')
            nomeArquivoTXT = 'dados.txt'
            arquivoTXT = Path(nomeArquivoTXT)

            info = [str(vazao_val), str(temperatura_val), str(umidade_val), str(pureza_val),
                    str(pressaoP_val), str(pressaoR_val), str(ch4_val), str(co_val), str(h2s_val)]

            print(info)

            with open(arquivoTXT, 'w') as f:
                for linha in info:
                    f.write(linha)
                    f.write('\n')

            if chk.get() == 1:

                nomeArquivoCSV = 'dados-'+dataArquivo+'.csv'

                # CABEÇALHO
                cabecalho = ['data', 'horario', 'vazao', 'temperatura',
                             'umidade', 'pureza', 'pressaoP', 'pressaoR', 'ch4', 'co', 'h2s']

                linha = [
                    {
                        'data': dataArquivo,
                        'horario': horario,
                        'vazao': vazao_val,
                        'temperatura': temperatura_val,
                        'umidade': umidade_val,
                        'pureza': pureza_val,
                        'pressaoP': pressaoP_val,
                        'pressaoR': pressaoR_val,
                        'ch4': ch4_val,
                        'co': co_val,
                        'h2s': h2s_val
                    }
                ]

                arquivoCSV = os.path.join("./planilhas", nomeArquivoCSV)
                
                modoEscrever = 'a' if os.path.exists(arquivoCSV) else 'w'
                with open(arquivoCSV, modoEscrever, encoding='UTF8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=cabecalho)
                    if modoEscrever == 'w':
                        writer.writeheader()
                    writer.writerows(linha)

        def mudarCorEntrada():
            if vazao_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', vazao_val)):
                vazao_txtIn.config(bg='red')
            else:
                vazao_txtIn.config(bg='white')

            if temperatura_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', temperatura_val)):
                temperatura_txtIn.config(bg='red')
            else:
                temperatura_txtIn.config(bg='white')

            if umidade_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', umidade_val)):
                umidade_txtIn.config(bg='red')
            else:
                umidade_txtIn.config(bg='white')

            if pureza_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', pureza_val)):
                pureza_txtIn.config(bg='red')
            else:
                pureza_txtIn.config(bg='white')

            if pressaoP_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', pressaoP_val)):
                pressaoP_txtIn.config(bg='red')
            else:
                pressaoP_txtIn.config(bg='white')

            if pressaoR_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', pressaoR_val)):
                pressaoR_txtIn.config(bg='red')
            else:
                pressaoR_txtIn.config(bg='white')

            if ch4_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', ch4_val)):
                ch4_txtIn.config(bg='red')
            else:
                ch4_txtIn.config(bg='white')

            if co_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', co_val)):
                co_txtIn.config(bg='red')
            else:
                co_txtIn.config(bg='white')

            if h2s_val == '' or not (re.match(r'(\+|\-)?\d+(.\d+)?$', h2s_val)):
                h2s_txtIn.config(bg='red')
            else:
                h2s_txtIn.config(bg='white')

        vazao_val = vazao_txtIn.get()
        h2s_val = h2s_txtIn.get()
        ch4_val = ch4_txtIn.get()
        temperatura_val = temperatura_txtIn.get()
        pressaoR_val = pressaoR_txtIn.get()
        umidade_val = umidade_txtIn.get()
        co_val = co_txtIn.get()
        pureza_val = pureza_txtIn.get()
        pressaoP_val = pressaoP_txtIn.get()

        # ERRO: FLOAT NÃO INSERIDO
        if not (re.match(r'(\+|\-)?\d+(.\d+)?$', vazao_val) and re.match(r'(\+|\-)?\d+(.\d+)?$', temperatura_val) and re.match(r'(\+|\-)?\d+(.\d+)?$', umidade_val) and re.match(r'(\+|\-)?\d+(.\d+)?$', pureza_val) and re.match(r'(\+|\-)?\d+(.\d+)?$', pressaoP_val) and re.match(r'(\+|\-)?\d+(.\d+)?$', pressaoR_val) and re.match(r'(\+|\-)?\d+(.\d+)?$', ch4_val) and re.match(r'(\+|\-)?\d+(.\d+)?$', co_val) and re.match(r'(\+|\-)?\d+(.\d+)?$', h2s_val)):
            # ERRO: TODOS OS CAMPOS DEVEM ESTAR PREENCHIDOS.
            if (vazao_val and h2s_val and ch4_val and temperatura_val and pressaoR_val and umidade_val and co_val and pureza_val and pressaoP_val) == '':
                mudarCorEntrada()
                alg_saida = -1

            # ERRO: O TIPO DE ENTRADA DEVE SER UM NÚMERO.
            else:
                mudarCorEntrada()
                alg_saida = -2
        else:
            mudarCorEntrada()
            escreverArquivo()
            alg_saida = algoritmoEspecialista()

        lblRetorno = Label(janela)
        lblRetorno.place(x=colLabel, y=450)

        # ERRO: TODOS OS CAMPOS DEVEM ESTAR PREENCHIDOS.
        if alg_saida == -1:
            lblRetorno.config(text='ERRO: Todos os campos devem estar preenchidos.', font=(
                'Helvetica', tamFonte, 'bold'), fg='white', bg='red')
        # ERRO: O TIPO DE ENTRADA DEVE SER UM NÚMERO.
        elif alg_saida == -2:
            lblRetorno.config(text='ERRO: O tipo de entrada deve ser um número.', font=(
                'Helvetica', tamFonte, 'bold'), fg='white', bg='red')
        # CASOS:
        else:
            yLista = 450
            for i in alg_saida:
                lblR = Label(janela)
                #VERMELHO
                if re.match('CUIDADO', str(i)):
                    lblR.config(text=str(i), font=('Helvetica', tamFonte+1, 'bold'), bg='red')
                else:
                    lblR.config(text=str(i), font=('Helvetica', tamFonte+1, 'bold'), bg='white')
                lblR.place(x=colLabel, y=yLista)
                yLista = yLista + 25

    def importarArquivo():
        nomeArquivoImportado = file.askopenfilename()
        print(nomeArquivoImportado)

        lbl = Label(janela)

        if Path(nomeArquivoImportado).suffix == '.txt':
            lbl.config(text='Arquivo: '+nomeArquivoImportado, font=(
                'Helvetica', tamFonte-2), bg='white')
            lbl.place(x=colLabel, y=janelaY-25)

            vazao_val = float(linecache.getline(nomeArquivoImportado, 1))
            h2s_val = float(linecache.getline(nomeArquivoImportado, 2))
            ch4_val = float(linecache.getline(nomeArquivoImportado, 3))
            temperatura_val = float(linecache.getline(nomeArquivoImportado, 4))
            pressaoR_val = float(linecache.getline(nomeArquivoImportado, 5))
            umidade_val = float(linecache.getline(nomeArquivoImportado, 6))
            co_val = float(linecache.getline(nomeArquivoImportado, 7))
            pureza_val = float(linecache.getline(nomeArquivoImportado, 8))
            pressaoP_val = float(linecache.getline(nomeArquivoImportado, 9))

            vazao_txtIn.delete(0, END)
            vazao_txtIn.insert(0, str(vazao_val))

            temperatura_txtIn.delete(0, END)
            temperatura_txtIn.insert(0, str(temperatura_val))

            umidade_txtIn.delete(0, END)
            umidade_txtIn.insert(0, str(umidade_val))

            pureza_txtIn.delete(0, END)
            pureza_txtIn.insert(0, str(pureza_val))

            pressaoP_txtIn.delete(0, END)
            pressaoP_txtIn.insert(0, str(pressaoP_val))

            pressaoR_txtIn.delete(0, END)
            pressaoR_txtIn.insert(0, str(pressaoR_val))

            ch4_txtIn.delete(0, END)
            ch4_txtIn.insert(0, str(ch4_val))

            co_txtIn.delete(0, END)
            co_txtIn.insert(0, str(co_val))

            h2s_txtIn.delete(0, END)
            h2s_txtIn.insert(0, str(h2s_val))

        else:
            lbl.config(text='ERRO: O tipo de arquivo deve ser do tipo texto.', font=(
                'Helvetica', tamFonte, 'bold'), fg='white', bg='red')
            lbl.place(x=colLabel, y=450)

    tamFonte = 11
    colLabel = 25
    colInput = 230
    colUnd = 400
    janelaX = 500
    janelaY = 700

    janela = tk.Tk()

    lbl = Label(janela, text='Vazão', font=('Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=25)
    vazao_txtIn = Entry(janela, text='', bd=1, bg='white')
    vazao_txtIn.place(x=colInput, y=25)
    lbl = Label(janela, text='ml/s',
                font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=25)

    lbl = Label(janela, text='Temperatura', font=(
        'Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=50)
    temperatura_txtIn = Entry(janela, text='', bd=1, bg='white')
    temperatura_txtIn.place(x=colInput, y=50)
    lbl = Label(janela, text='ºC', font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=50)

    lbl = Label(janela, text='Umidade', font=(
        'Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=75)
    umidade_txtIn = Entry(janela, text='', bd=1, bg='white')
    umidade_txtIn.place(x=colInput, y=75)
    lbl = Label(janela, text='%', font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=75)

    lbl = Label(janela, text='Pureza', font=(
        'Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=100)
    pureza_txtIn = Entry(janela, text='', bd=1, bg='white')
    pureza_txtIn.place(x=colInput, y=100)
    lbl = Label(janela, text='%', font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=100)

    lbl = Label(janela, text='Pressão em Pulmão',
                font=('Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=125)
    pressaoP_txtIn = Entry(janela, text='', bd=1, bg='white')
    pressaoP_txtIn.place(x=colInput, y=125)
    lbl = Label(janela, text='bar', font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=125)

    lbl = Label(janela, text='Pressão em Reforma',
                font=('Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=150)
    pressaoR_txtIn = Entry(janela, text='', bd=1, bg='white')
    pressaoR_txtIn.place(x=colInput, y=150)
    lbl = Label(janela, text='bar', font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=150)

    lbl = Label(janela, text='Elementos',
                font=('Helvetica', tamFonte, 'bold'), bg='white')
    lbl.place(x=colLabel, y=190)

    lbl = Label(janela, text='CH4 (metano)', font=(
        'Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=225)
    ch4_txtIn = Entry(janela, text='', bd=1, bg='white')
    ch4_txtIn.place(x=colInput, y=225)
    lbl = Label(janela, text='%', font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=225)

    lbl = Label(janela, text='CO (monóxido de carbono)',
                font=('Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=250)
    co_txtIn = Entry(janela, text='', bd=1, bg='white')
    co_txtIn.place(x=colInput, y=250)
    lbl = Label(janela, text='%', font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=250)

    lbl = Label(janela, text='H2S (sulfeto de hidrogênio)',
                font=('Helvetica', tamFonte), bg='white')
    lbl.place(x=colLabel, y=275)
    h2s_txtIn = Entry(janela, text='', bd=1, bg='white')
    h2s_txtIn.place(x=colInput, y=275)
    lbl = Label(janela, text='ppm', font=('Helvetica', tamFonte-2), bg='white')
    lbl.place(x=colUnd, y=275)

    horizontal = Frame(janela, bg='black', height=2, width=450)
    horizontal.place(x=colLabel, y=400)

    btn = Button(janela, text='INICIAR', command=salvarDados,  width=8, height=2,
                 bd=1, font=('Helvetica', tamFonte, 'bold'), bg='black', foreground='white')
    btn.place(x=colLabel, y=370)

    btn = Button(janela, text='IMPORTAR ARQUIVO', command=importarArquivo,  width=16, height=2,
                 bd=1, font=('Helvetica', tamFonte-3, 'bold'), bg='black', foreground='white')
    btn.place(x=355, y=400)

    chk = IntVar()
    checkboxCSV = Checkbutton(janela, text='Salvar informações em planilha',
                              variable=chk, onvalue=1, offvalue=0, bg='white', font=('Helvetica', 9))
    checkboxCSV.place(x=colLabel, y=325)

    imagemPNGufpr = PhotoImage(file='./imagens/ufpr.png')
    imgemLabel = Label(janela, image=imagemPNGufpr, bd=0)
    imgemLabel.place(x=370, y=325)

    imagemPNGlcomp = PhotoImage(file='./imagens/lcomp.png')
    imgemLabel = Label(janela, image=imagemPNGlcomp, bd=0)
    imgemLabel.place(x=253, y=325)

    janela.title(
        'Sistema Especialista - Produção de energia a partir do biogás')
    janela['bg'] = 'white'
    janela.geometry(str(janelaX)+'x'+str(janelaY))
    janela.resizable(False, False)
    janela.mainloop()


criarTela()
