import sys

'''
--------------1.
mostra_menu() (senza return)
Non prende parametri
Stampa la domanda e le 4 opzioni
Non restituisce nulla

'''

def mostra_domanda(domanda: str) -> None: 
    """
    Questa funzione restituisce la domanda e le opzioni della riposta. 
    """
    print(domanda)
    


"""
--------------2.
raccogli_risposta() (con return)
Non prende parametri
Chiede l'input all'utente
Converte in int
Restituisce la scelta

"""
def raccogli_risposta() -> str :
    """
    Questa funzione si occupa solamente di prendere l'input dell'utente.
    Il controllo di tale valore avverrà attraverso una funzione dedicata
    """
    return input("----> Inserisci la tua scelta:")


"""
--------------3.
valida_scelta(scelta) (con return)
prende come parametro il numero scelto
Verifica se è tra A e D usando if
Restituisce True se valida, False altrimenti

"""
def valida_scelta(scelta: str) -> bool:
    """
    Questa funzione prendere un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A,B,C o D .
    Se la risposta è una stringa vuota, restituisce false, lo stesso per altre letter oltre quelle elencate.
    """
    scelta_tmp = scelta.upper()
    if  scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else:
        return False
    

"""
--------------4.
genera_feedback(scelta) (con return)
Prende come parametro la lettera scelta (A-D)
Usa if/elif/else per determinare il messaggio
Restituisce la stringa con il feedback personalizzato

"""
def genera_feedback(is_corretta:bool) -> str :
    """
    Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
    Questa funzione viene eseguita solo se la funzione di validazione restituisce true. 
    """
    if is_corretta == True:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato. Ritenta!"

"""
--------------5.
mostra_feedback(messaggio) (senza return)
Prende come parametro una stringa
Stampa il feedback in modo formattato
Non restituisce nulla

"""
def mostra_feedback(messaggio:str) -> None:
    """
    Restituisce il feedback formattato nella maniera desiderata
    """
    simbol: str = "*"*30
    print(f"""
          
{simbol}
{messaggio}
{simbol}
          
          """)
    
"""
--------------6.
is_risposta_esatta(scelta:str) (con return)
Prende come parametro una stringa
restituisce il feedback come bool. 
Utilizziamo questa funzione per il ciclo while
"""  
def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    """
    Restituisce true o false a differenza che la risposta sia esatta("A") o meno
    """
    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False
    

def leggi_file(filepath:str) -> str:
    with open(filepath, "r") as file:
        content = file.read()
        return content

def estrai_index(content: str) -> int: 
    return content.index("£")

def estrai_domanda(content: str, index: int) -> str:
    return content[0:index]

def estrai_risposta(content: str, index: int) -> str:
    return content[index+1:]  #per prendere il valore dopo £ che è A

def main():
    domande_list: list[str] = []
    qa:dict[str,str]={
        "domanda":None,
        "risposta":None
    }
    with open("domande.txt","r") as f:
        for i in f:
            domande_list.append(i.strip())
    #with open(domande_list[0],"r") as f:
     #   for i in f:
      #      print(i)
            
    content: str = leggi_file(f"domande_risposte/{domande_list[0]}")
    index:int = estrai_index(content)
    qa["domanda"] = estrai_domanda(content, index)
    qa["risposta"]= estrai_risposta(content, index)
    print(qa)

    
    
    
    """
    filepath : str = sys.argv[1] # comando per lanciare python3 main.py domanda-1.txt
    content: str = leggi_file(filepath)
    index: int = estrai_index(content)
    domanda: str = estrai_domanda(content, index)
    risposta: str = estrai_risposta(content, index)

    is_risposta_corretta: bool = False
    while True:
        mostra_domanda(domanda)
        risposta_da_validare: str = raccogli_risposta()
        risposta_validata: bool = valida_scelta(risposta_da_validare)
        feedback: str = ""

        if risposta_validata == True:
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare, risposta)
            feedback = genera_feedback(is_risposta_corretta)
        else: 
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        mostra_feedback(feedback)
        if is_risposta_corretta == True: 
            break
            """

# Entry point del nostro programma
main()