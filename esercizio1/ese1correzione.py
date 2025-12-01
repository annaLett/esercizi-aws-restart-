# 1. vedere la domanda X
# 2. vedere le possibili risposte X
# 3. inserire una risposta X
# 4. verificare che la risposta sia esatta X 
# 5. se la risposta che diamo e corretta fai a altrimenti fai b

#per comodità allochiamo le variabili delle risposte e della domanda per avere modo di cambiarle in futuro su tutto il codice
question_1: str = "Qual e' il tuo trapper preferito?"
answer_1 : str = "Gue"
answer_2 : str = "Kid Yogi"
answer_3 : str = "Taxi B"
answer_4 : str = "Dark Polo"

#vedere la domanda X usando le variabili allocate sopra
print(f""" 
      {question_1}
      A. {answer_1} 
      B. {answer_2} 
      C. {answer_3}
      D. {answer_4}
      """)

#prende la risposta
answer: str = input("Inserisci la risposta preferita:")
#.upper() per avere la risposta maiuscola per il confronto
answer_tmp = answer.upper()

# 4. verificare che la risposta sia esatta X col match
match answer_tmp:
    case "A" | "Z":
        result = f"la risposta e: {answer_tmp} - {answer_1}"

    case "B":
        result = f"la risposta e: {answer_tmp} - {answer_2}"

    case "C":
        result = f"la risposta e: {answer_tmp} - {answer_3}"

    case "D":
        result = f"la risposta e: {answer_tmp} - {answer_4}"
    case _:
        result = "Cambia cantante etc. etc."

print(result)



#altro modo col if else
if answer_tmp == "A":
    print(f"la risposta e: {answer_tmp} - Sfera Ebbasta")

elif answer_tmp == "B":
    print(f"la risposta e: {answer_tmp} - Sfera Ebbasta")

elif answer_tmp == "C":
    print(f"la risposta e: {answer_tmp} - Sfera Ebbasta")

elif answer_tmp == "D":
    print(f"la risposta e: {answer_tmp} - Sfera Ebbasta")

else:
    print(f"Cambia cantante, tanto i trapper non cantano")


