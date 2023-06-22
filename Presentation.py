#code for open ai program
#created 06/17/2022
#hackathon
import os
import openai
import colorama
from colorama import Back, Fore, Style

API_KEY = "API_KEY"
openai.api_key = API_KEY

#prompts that the program will use
explorer = "Ask me 3 questions about this idea. (be very creative, exploratory, imaginative, big idea focused)"
refiner = "Ask me 3 questions about the idea. (be detailed, focus on specifics, think out the little things)"
expert = "Ask me 3 questions about the idea. (act like you are an expert in this specific idea and it's field, you have a lot of experience in this area and therefore have helpful feedback about this idea, focus on relevance, integration into this field)"
critic = "Ask me 3 questions about the idea. (be critical, doubting, analytical, find weaknesses, but still polite)"
#the string of conversation
conversation = []

#______________________________________________
#gathers additional details about the idea
#______________________________________________

def consult(perspective):

  consult = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation+[{"role": "system","content": perspective}])
    

  print(
        "\n____________________________________________________\n")
  consult = consult['choices'][0]['message']['content']
  print(consult)
  conversation.append({"role": "assistant", "content": consult})
  print("\n____________________________________________________\n")

  usrResponse = input(Fore.WHITE+ "How will you respond? " + Fore.MAGENTA)
  conversation.append({"role": "user", "content": usrResponse})

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation+[{"role": "system", "content": "The user presents the following response to your question: "}, {"role": "user","content": usrResponse}, {
      "role":
      "system",
      "content":
      "Give a positive and thoughtful response to the user about their answer."
    }])

  print(Style.RESET_ALL +
        "\n____________________________________________________\n")
  response = response['choices'][0]['message']['content']
  print(response)


#______________________________________________
#define summarize function
#______________________________________________


def summarize():
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation + [{"role": "system","content":"Close off your interaction with the user, being polite, then we will go into our 'conclusion' stage"},
      {"role": "system","content":"Summarize what the idea with as concise as possible, make sure your response is correct, explain what you are doing to user."},
      {"role": "system","content":"Put the idea into concise bullet points, explain what you are doing to user."},
      {"role": "system","content":"Come up with a slogan, explain what you are doing to user."},
    ]
  )
  print(Style.RESET_ALL +
        "____________________________________________________\n")
  response = response['choices'][0]['message']['content']
  print(response)
  print(Style.RESET_ALL +
        "____________________________________________________\n")

  while (True):
    run = input("Is this a valid summary? Y/N " + Fore.MAGENTA)

    if (run == "Y"):
      print(Style.RESET_ALL + "Good. Proceeding to next path.")
      
      break
    elif (run == "N"):
      while (True):
        run = input(Style.RESET_ALL +"Is there any other details that you would like to add to your business? Y/N \n" + Fore.MAGENTA)
        if (run == "Y"):
          openai.ChatCompletion.create(
            model="gpt-3.5-turbo",messages=conversation+[{"role":
          "system",
          "content":
          "Someone is adding additional details to their idea."
        }])
          print(Style.RESET_ALL +
            "\n____________________________________________________\n")
          break
        elif (run == "N"):
          break
        else:
          print("Please enter a valid input!")
    else:
      print("Please enter a valid input!")

 

#MAIN**********************************************************************************
#controls execution of program
while (True):
  run = input("Would you like to run the program? Y/N " + Fore.MAGENTA)
  if (run == "N"):
    exit()
  elif (run == "Y"):
    break
  else:
    print(Fore.MAGENTA + "Please enter a valid input!")

#prompts the user for their idea, begins a conversation
conversation.append({"role": "system", "content": input(Fore.WHITE +"\nWhat is your idea? Write as much or as little as you have so far.\n" + Fore.MAGENTA)})

#gets response from AI
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=conversation+[{"role":"system","content":"Someone presents an idea to you and you need to help them with it."}]
)

while (True):
  print(Style.RESET_ALL + "____________________________________________________\n")
  uin = input(
    "\nWho would you like to consult? " + Style.DIM +
    "(press any other key to quit)\n" + Fore.YELLOW +
    "\n1. Explorer"+ Fore.LIGHTGREEN_EX + "\n2. Refiner" + Fore.BLUE +" \n3. Expert" + Fore.RED+ " \n4. Critic\n" + Style.RESET_ALL + "5. Summarize \n\n" +
    Style.DIM + "Choice: " + Style.RESET_ALL)
  print("____________________________________________________\n" + Fore.WHITE)

  if (uin == "1"):
    print(Fore.YELLOW)
    consult(explorer)
  elif (uin == "2"):
    print(Fore.LIGHTGREEN_EX)
    consult(refiner)
  elif (uin == "3"):
    print(Fore.BLUE)
    consult(expert)
  elif (uin == "4"):
    print(Fore.RED)
    consult(critic)
  elif (uin == "5"):
    print(Fore.WHITE)
    summarize()
  else:
    break

