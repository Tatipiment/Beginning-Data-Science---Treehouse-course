#dungeron_game
import random
import os 

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


CELLS = [(0, 0),(0, 1),(0, 3),
		 (1, 0),(1, 1),(1, 3),
		 (2, 0),(2, 1),(2, 3),		
		 (3, 0),(3, 1),(3, 3),]

player_caractere = "ʕ•ᴥ•ʔ|"
line = ("   " + "-"* 26)
empty = (5,5)

def drawn_grid(element):
	player_location = list(element)
	free_space = "  .  |"
	grid = [[free_space, free_space, free_space, free_space],
			[free_space, free_space, free_space, free_space],
			[free_space, free_space, free_space, free_space],
			[free_space, free_space, free_space, free_space],]
	print("\n\n\n        0  .  1  .  2  .  3")
	print(line)
	for y in range(4):
		if player_location[1] == y:
			for x in range(4):
				if player_location[0] == x:
					grid[y][x] = player_caractere
				else:
					grid[y][x] = free_space
			print(" {} ||{}{}{}{}|".format(y, grid[y][0], grid[y][1], grid[y][2], grid[y][3]))
			print(line)
		else:
			print(" {} ||{}{}{}{}|".format(y, grid[y][0], grid[y][1], grid[y][2], grid[y][3]))
			print(line) 


clear_screen()  
print("\nAdivinhe onde o Ursinho vai aparecer") 
while True:
	drawn_grid(empty)
	vert = input("\nEm que coluna?\n> ")
	if vert.lower() == "n":
		break
	hori = input("Em que linha?\n> ")
	if hori.lower() == "n":
		break 

	try:
		clear_screen()
		print("\n>>> Resultado: ")
		player = random.choice(CELLS)
		
		
		vert = int(vert)
		hori = int(hori)

		if vert == player[0] and hori == player[1]:
			player_caractere = "ʕᵔᴥᵔʔ|"
			drawn_grid(player)
			print("\n>>> Uau! Agora me diz o número da loteria...\n>>> Brinks 😋")

		else:
			player_caractere = "ʕ˘̩-˘̩ʔ|"
			drawn_grid(player)
			print("\n>>> Ahh! Fica pra próxima. 🙏")
			print("Seu palpite: ({}, {}) \nResultado:   {}".format(vert, hori, player))
	
		more = input("\n>>> Quer continuar? (S/N)\n> ")

		if more.lower() == "s":
			clear_screen()
			print("\n>>> Tente novamente:")
			continue

		else:
			if more.lower() == "n":
				clear_screen()
				break 

		clear_screen()
		print("\n>>> Desculpa, não entendi... Mas toma aqui mais uma rodada:")

	except :
		clear_screen()
		print("\n>>> Digite números de 0 à 4, certo?")
		continue