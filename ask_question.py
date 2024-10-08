import os

def clear_console():
  if os.name == 'nt':  
    os.system('cls')
  else:  
    os.system('clear')


def ask_question(question, answers):
  answered = False
  message2show = ""
  
  while not answered:
    clear_console()
    
    if message2show:
      print(message2show)
      
    print(question)
    for index in range(len(answers)):
      print(str(index+1) + ". " + answers[index])
    
    print("\n")
    answer = input("Votre réponse: \n")
    try:
      answerIndex = int(answer) - 1
      if answerIndex < 0 or answerIndex > len(answers) - 1:
        message2show = "Veuillez entrer un numéro correct"
      else:
        answered = True
    except ValueError:
      message2show = "Ce n'est pas un chiffre. Veuillez entrer le numéro de la réponse"

  clear_console()
  return answerIndex

  
  
reponse1 = ask_question("Quelle est la capitale de la France", ["Paris", "Disneyland", "Ta mère", "Michel"])
reponse2 = ask_question("Quelle est la capitale de la Belgique", ["Paris", "Disneyland", "Ta mère", "Belgique"])

print(reponse1)
print(reponse2)