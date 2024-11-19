import os
os.system("cls")
import random

opc=0
quantT=0
quantC=0
quantMT=0
quantMC=0
total_corridoT=[]
total_corridoC=[]
T={}
C={}
MDT={}
MDC={}
distanciaM={}
tempoM={}
distanciaPaceT=[]
tempoPaceT=[]
distanciaPaceC=[]
tempoPaceC=[]

def Fadd():
    if addT_C=="T":
        try:
            arquivotxt=open('treinos.txt','w',encoding='utf8')
            try:
                data = input("Digite a data do treino (Formato DD-MM-YYYY): ")
                distancia = float(input("Digite a distância percorrida (Em Km): "))
                distanciaPaceT.append(distancia)
                tempo = float(input("Digite o tempo de duração (Em horas): "))
                tempoPaceT.append(tempo)
                localizacao = input("Digite a localização do treino: ")
                condicoes_climaticas = input("Digite a condição climática (Neve / Chuva / Ensolarado / Nublado): ")
                T[quantT]=(f"{quantT}º TREINO-> |Data: {data}|Distância: {distancia}Km|Tempo de duração: {tempo}h|Localização: {localizacao}|Condição climática: {condicoes_climaticas}\n")
                for i in T:
                    arquivotxt.write(T[i])
                print("Treino registrado com sucesso")
            except ValueError:
                print("Alguma informação digitada é inválida")
            arquivotxt.close()
        except FileNotFoundError:
            print("Arquivo não encontrado")

    elif addT_C=="C":
        try:
            arquivotxt=open('competicoes.txt','w',encoding='utf8')
            try:
                data = input("Digite a data da competição (Formato DD-MM-YYYY): ")
                distancia = float(input("Digite a distância percorrida (Em Km): "))
                distanciaPaceC.append(distancia)
                tempo = float(input("Digite o tempo de duração (Em horas): "))
                tempoPaceC.append(tempo)
                localizacao = input("Digite a localização da competição: ")
                condicoes_climaticas = input("Digite a condição climática (Neve / Chuva / Ensolarado / Nublado): ")
                C[quantC]=(f"{quantC}ª COMPETIÇÃO-> |Data: {data}|Distância: {distancia}Km|Tempo de duração: {tempo}h|Localização: {localizacao}|Condição climática: {condicoes_climaticas}\n")
                for i in C:
                    arquivotxt.write(C[i])
                print("Compeitição registrada com sucesso")
            except ValueError:
                print("Alguma informação digitada é inválida")
            arquivotxt.close()
        except FileNotFoundError:
            print("Arquivo não encontrado")
    
    else:
        print("Opção inválida")

def Fvisu():
    if vizuT_C=="T":
        for i in T:
            print(f"{i}. {T[i]}")
    elif vizuT_C=="C":
        for i in C:
            print(f"{i}. {C[i]}")
    else:
        print("Opção inválida")

def Fupdt():    
    if updtT_C=="T":
        try:
            with open('treinos.txt','r',encoding='utf8') as arquivotxt:
                print("Treinos disponíveis para atualização:")
                for i in T:
                    print(f"{i}: {T[i]}")
                try:
                    numUpdt = int(input("Digite o número do treino que você quer atualizar: "))
                    nova_data = input("Digite a nova data do treino (Formato DD-MM-YYYY): ")
                    nova_distancia = float(input("Digite a nova distância percorrida (Em Km): "))
                    distanciaPaceT[numUpdt]=nova_distancia 
                    novo_tempo = float(input("Digite o novo tempo de duração (Em horas): "))
                    tempoPaceT[numUpdt]=novo_tempo
                    nova_localizacao = input("Digite a nova localização do treino: ")
                    nova_condicoes_climaticas = input("Digite a nova condição climática (Neve / Chuva / Ensolarado / Nublado): ")
                except ValueError:
                    print("Alguma informação digitada é inválida")
                    T[numUpdt]=(f"{numUpdt}º TREINO-> |Data: {nova_data}|Distância: {nova_distancia}Km|Tempo de duração: {novo_tempo}h|Localização: {nova_localizacao}|Condição climática: {nova_condicoes_climaticas}\n")
            with open('treinos.txt','w',encoding='utf8') as arquivotxt:
                for i in T:
                    arquivotxt.write(T[i])
            print("Treino atualizado com sucesso")
        except FileNotFoundError:
            print("Arquivo não encontrado")

    elif updtT_C=="C":
        try:
            with open('competicoes.txt','r',encoding='utf8') as arquivotxt:
                print("Competições disponíveis para atualização: ")
                for i in C:
                    print(f"{i}: {C[i]}")
                try:
                    numUpdt = int(input("Digite o número da competição que você quer atualizar: "))
                    nova_data = input("Digite a nova data da competição (Formato DD-MM-YYYY): ")
                    nova_distancia = float(input("Digite a nova distância percorrida (Em Km): "))
                    distanciaPaceC[numUpdt] = nova_distancia
                    novo_tempo = float(input("Digite o novo tempo de duração (Em horas): "))
                    tempoPaceC[numUpdt] = novo_tempo
                    nova_localizacao = input("Digite a nova localização da competição: ")
                    nova_condicoes_climaticas = input("Digite a nova condição climática (Neve / Chuva / Ensolarado / Nublado): ")
                except ValueError:
                    print("Alguma informação digitada é inválida")
                C[numUpdt]=(f"{numUpdt}ª COMPETIÇÃO-> |Data: {nova_data}|Distância: {nova_distancia}Km|Tempo de duração: {novo_tempo}h|Localização: {nova_localizacao}|Condição climática: {nova_condicoes_climaticas}\n")

            with open('competicoes.txt','w',encoding='utf8') as arquivotxt:
                for i in C:
                    arquivotxt.write(C[i])
            print("Competição atualizada com sucesso")
        except FileNotFoundError:
            print("Arquivo não encontrado")
    else:
        print("Opção inválida")

def Fexc():
    if excT_C=="T":
        try:
            with open('treinos.txt','r',encoding='utf8') as arquivotxt:
                print("Treinos disponíveis para excluir: ")
                for i in T:
                    print(f"{i}: {T[i]}")
                try:
                    numExc = int(input("Digite o número do registro de treino que você quer excluir: "))
                except ValueError:
                    print("Digite um valor inteiro")
                if 1<=numExc<=len(T):
                    del T[numExc]
                    del distanciaPaceT[numExc]
                    del tempoPaceT[numExc]
            with open('treinos.txt','w',encoding='utf8') as arquivotxt:
                for i in T:
                    arquivotxt.write(T[i])
        except FileNotFoundError:
            print("Arquivo não encontrado")

        print("Treino excluído com sucesso")

    elif excT_C=="C":
        try:
            with open('competicoes.txt','r',encoding='utf8') as arquivotxt:
                print("Competições disponíveis para exclur: ")
                for i in C:
                    print(f"{i}: {C[i]}")
                try:
                    numExc = int(input("Digite o número do registro de competição que você quer excluir: "))
                except ValueError:
                    print("Digite um valor inteiro")
                if 1<=numExc<=len(C):
                    del C[numExc]
                    del distanciaPaceC[numExc]
                    del tempoPaceC[numExc]
            with open('competicoes.txt','w',encoding='utf8') as arquivotxt:
                for i in C:
                    arquivotxt.writelines(C[i])
        except FileNotFoundError:
            print("Arquivo não encontrado")

        print("Competição excluída com sucesso")

    else:
        print("Opção inválida")

def FaddMeta():
    if addMetaT_C=="T":
        medida_tempo_meta=input("Sua meta será uma meta semanal, mensal ou anual? (S / M / A): ").upper()
        try:
            if medida_tempo_meta=="S":
                tempo_meta=int(input("Digite em quantas semanas você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="semanas"
                else:
                    s_m_a="semana"
            elif medida_tempo_meta=="M":
                tempo_meta=int(input("Digite em quantos meses você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="meses"
                else:
                    s_m_a="mês"
            elif medida_tempo_meta=="A":
                tempo_meta=int(input("Digite em quantos anos você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="anos"
                else:
                    s_m_a="ano"
            else:
                print("Opção inválida")
        except ValueError:
            print("Digite um valor inteiro")

        distancia_meta = input(f"Digite a distância que você quer correr em {tempo_meta} {s_m_a} (Em KM): ")
        distanciaM[quantMT] = distancia_meta
        MDT[quantMT]=(f"{quantMT}ª META DE TREINO-> {distancia_meta}Km em {tempo_meta} {s_m_a}")
        print("Meta de treino registrada com sucesso!")

    elif addMetaT_C=="C":
        medida_tempo_meta = input("Sua meta será uma meta semanal, mensal ou anual? (S / M / A): ").upper()
        try:
            if medida_tempo_meta=="S":
                tempo_meta = int(input("Digite em quantas semanas você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="semanas"
                else:
                    s_m_a="semana"
            elif medida_tempo_meta=="M":
                tempo_meta = int(input("Digite em quantos meses você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="meses"
                else:
                    s_m_a="mês"
            elif medida_tempo_meta=="A":
                tempo_meta = int(input("Digite em quantos anos você quer bater a meta: "))
                if tempo_meta>1:
                    s_m_a="anos"
                else:
                    s_m_a="ano"
            else:
                print("Opção inválida")
        except ValueError:
            print("Digite um valor inteiro")
   
        distancia_meta = input(f"Digite a distância que você quer correr em {tempo_meta} {s_m_a} (Em KM): ")
        distanciaM[quantMC] = distancia_meta
        MDT[quantMC] = (f"{quantMC+1}ª META DE COMPETIÇÃO-> {distancia_meta}Km em {tempo_meta} {s_m_a}")
        print("Meta de competição registrada com sucesso!")

    else:
        print("Opção inválida")

def FupdtMeta():
    if updtMetaT_C=="T":
        total_corridoT=0
        print("Metas e desafios de treino disponíveis para atualização: ")
        for i in MDT:
            print(f"{i}: {MDT[i]}")
        try:
            numUpdtMeta = int(input("Digite o número da meta de treino que você quer atualizar o progresso: "))
            km_corridos = float(input("Digite a distância já corrida (Em Km): "))
        except ValueError:
            print("Alguma informação digitada é inválida")
        total_corridoT+=km_corridos
        distancia_faltando = int(distanciaM[numUpdtMeta])-total_corridoT
        distanciaM[numUpdtMeta] = distancia_faltando
        if (distancia_faltando)>0:
            print("Progresso em meta de treino atualizado com sucesso!")
            print(f"Ainda faltam {distancia_faltando}Km para bater a meta")
        else:
            print(f"Parabéns! Você bateu a {numUpdtMeta}ª meta de treinos!")
            del MDT[numUpdtMeta]
    
    elif updtMetaT_C=="C":
        total_corridoC=0
        print("Metas e desafios de competição disponíveis para atualização: ")
        for i in MDT:
            print(f"{i}: {MDT[i]}")
        try:
            numUpdtMeta = int(input("Digite o número da meta de competição que você quer atualizar o progresso: "))
            km_corridos = float(input("Digite a distância já corrida (Em Km): "))
        except ValueError:
            print("Alguma informação digitada é inválida")
        total_corridoC+=km_corridos
        distancia_faltando = int(distanciaM[numUpdtMeta])-total_corridoC
        distanciaM[numUpdtMeta-1] = distancia_faltando
        if (distancia_faltando)>0:
            print("Progresso de meta de competição atualizado com sucesso!")
            print(f"Ainda faltam {distancia_faltando}Km para bater a meta")
        else:
            print(f"Parabéns! Você bateu a {numUpdtMeta}ª meta de competições!")
            del MDC[numUpdtMeta]
    
    else:
        print("Opção inválida")

def Fextra():
    if paceT_C=="T":
        print("Treinos registrados: ")
        for i in T:
            print(f"{i}. {T[i]}")
        try:
            numPace = int(input("Digite o número do treino que você quer calcular o pace: "))
            if tempoPaceT[numPace-1]!=0:
                pace = int(distanciaPaceT[numPace-1])/int(tempoPaceT[numPace-1])
        except ValueError:
            print("Alguma informação digitada é inválida")
        print(f"O pace do {numPace}º treino é {pace}Km/h")

    elif paceT_C=="C":
        print("Competições registradas: ")
        for i in C:
            print(f"{i}. {C[i]}")
        try:     
            numPace = int(input("Digite o número da competição que você quer calcular o pace: "))
            if tempoPaceC[numPace-1]!=0:
                pace = int(distanciaPaceC[numPace-1])/int(tempoPaceC[numPace-1])
        except ValueError:
            print("Alguma informação digitada é inválida")
        print(f"O pace da {numPace}ª competição é {pace}Km/h") 

    else:
        print("Opção inválida")  

def Ffiltrar():
    if filtT_C == "T":  
        try:
            print("Treinos disponíveis para filtragem: ")
            for i in T:
                print(f"{i}. {T[i]}")
                dis_ou_temp = input("Quer filtrar por distância ou tempo? (D / T): ").upper()
            if dis_ou_temp == "D":
                distancia = float(input("Digite a distância que será filtrada (Em Km): "))
                filtrados = [treino for treino in T if str(distancia) in treino]
                if filtrados:
                    print("Treinos filtrados por distância:")
                    for treino in filtrados:
                        print(treino)
                else:
                    print("Não foram encontrados treinos para serem filtrados")
            elif dis_ou_temp == "T":
                tempo = float(input("Digite o tempo que será filtrado (Em horas): "))
                filtrados = [treino for treino in T if str(tempo) in treino]
                if filtrados:
                    print("Treinos filtrados por tempo:")
                    for treino in filtrados:
                        print(treino)
                    else:
                        print("Não foram encontrados treinos para serem filtrados")
            else:
                print("Opção inválida")
        except ValueError:
            print("Alguma informação digitada é inválida")

    elif filtT_C == "C":
        try:
            print("Competições disponíveis para filtragem: ")
            for i in C:
                print(f"{i}. {C[i]}")
                dis_ou_temp = input("Quer filtrar por distância ou tempo? (D / T): ").upper()
            if dis_ou_temp == "D":
                distancia = float(input("Digite a distância que será filtrada (Em Km): "))
                filtrados = [competicao for competicao in C if str(distancia) in competicao]
                if filtrados:
                    print("Competições filtradas por distância: ")
                    for competicao in filtrados:
                        print(competicao)
                else:
                    print("Não foram encontradas competições para serem filtradas")
            elif dis_ou_temp == "T":
                tempo = float(input("Digite o tempo que será filtrado (Em horas): "))
                filtrados = [competicao for competicao in C if str(tempo) in competicao]
                if filtrados:
                    print("Competições filtradas por tempo: ")
                    for competicao in filtrados:
                        print(competicao)
                    else:
                        print("Não foram encontradas competições para serem filtradas")
            else:
                print("Opção inválida")

        except ValueError:
            print("Alguma informação digitada é inválida")

    else:
        print("Opção inválida")

def Falea():
    treino_aleatorio=random.choice(T)
    print(f"TREINO SUGERIDO->{treino_aleatorio}")

while opc!=10:
    print("1. Fazer um registro")
    print("2. Visualizar os registros")
    print("3. Atualizar os registros")
    print("4. Excluir um registro")
    print("5. Registrar metas e desafios")
    print("6. Atualizar o progresso das metas e desafios")
    print("7. Calcular o seu pace")
    print("8. Filtrar os registros")
    print("9. Sugestão de treino aleatório")
    print("10. Parar")
    opc=int(input("Digite o que você quer fazer: "))
    
    if opc==1:
        addT_C = input("Quer registrar um treino ou uma competição?: (T \ C): ").upper()
        if addT_C=="T":
            quantT+=1
        elif addT_C=="C":
            quantC+=1
        Fadd()
        
    elif opc==2:
        vizuT_C = input("Quer vizualizar os registros dos treinos ou das competições? (T \ C): ").upper()
        Fvisu()

    elif opc==3:
        updtT_C = input("Quer atualizar os registros dos treinos ou das competições? (T \ C): ").upper()
        Fupdt()

    elif opc==4:
        excT_C = input("Quer excluir um registro de treino ou de competição? (T \ C): ").upper()
        Fexc()
    
    elif opc==5:
        addMetaT_C = input("Quer registrar uma meta de treino ou de competição? (T \ C): ").upper()
        if addMetaT_C=="T":
            quantMT+=1
        elif addMetaT_C=="C":
            quantMC+=1
        FaddMeta()

    elif opc==6:
        updtMetaT_C = input("Quer atualizar o progresso uma meta de treino ou de competição? (T \ C): ").upper()
        FupdtMeta()
        
    elif opc==7:
        paceT_C = input("Quer calcular o pace de um treino ou de uma competição? (T \ C): ").upper()
        Fextra()

    elif opc==8:
        filtT_C = input("Quer filtrar um registro de treino ou de competição? (T \ C): ").upper()
        Ffiltrar()

    elif opc==9:
        Falea()

    elif opc==10:
        print("Encerrando...")

            
