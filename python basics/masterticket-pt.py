SERVICE_CHARGE = 2
TICKET_PRICE = 10
tickets_remaining = 100  

def cauculate_price(numb):
  return (TICKET_PRICE * numb) + SERVICE_CHARGE
  
while tickets_remaining > 0: 
  print("\nAinda existem {} disponíveis. Corra para comprar!".format(tickets_remaining))
  client_name = input("> Olá, qual seu nome? ")
  ticket_quantity = input("> Quantos ingressos você quer comprar, {}? ".format(client_name))
  
  try:
    ticket_quantity = int(ticket_quantity)
    if ticket_quantity > tickets_remaining:
            raise ValueError("Você só pode comprar até {} ingressos.".format(tickets_remaining))
  except ValueError as limites:
    print("Caramba, você digitou algo incorretamente. {}".format(limites))
  else: 
    purchase_value = cauculate_price(ticket_quantity)
    
    if ticket_quantity > 1:
      print("{}, {} ingressos custam {} reais.".format(client_name, ticket_quantity, purchase_value))
    elif ticket_quantity == 1:
      print("{}, cada ingresso custa {} reais.".format(client_name, purchase_value))
    else: 
      print("Hey {}, vc não pode comprar ingressos negativos!!!".format(client_name))
  
    answer = input('> Quer comprar os ingressos? (Responda: "sim" ou "não") ')
  
    if answer.lower() == "sim":
      print("Parabéns, você acaba de comprar {} ingressos por R$ {}. Aproveite!".format(ticket_quantity, purchase_value))
      tickets_remaining -= ticket_quantity
    else:
      print("Tudo bem. Fica pra próxima.")

#avisar que vendemos todos os ingressos    
print("Vendemos todos os ingressos. Volte novamente semana que vem.")
