#dungeron_game
import random
import os 

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


CELLS = [(0, 0),(0, 1),(0, 3),(0, 4),
		 (1, 0),(1, 1),(1, 3),(1, 4),
		 (2, 0),(2, 1),(2, 3),(2, 4),		
		 (3, 0),(3, 1),(3, 3),(3, 4),
		 (4, 0),(4, 1),(4, 3),(4, 4),]

player_caractere = "ʕᵔᴥᵔʔ|"
line = ("   " + "-"* 33)
empty = (5,5)

def drawn_grid(element):
	player_location = list(element)
	free_space = "  .  |"
	grid = [[free_space, free_space, free_space, free_space, free_space],
			[free_space, free_space, free_space, free_space, free_space],
			[free_space, free_space, free_space, free_space, free_space],
			[free_space, free_space, free_space, free_space, free_space],
			[free_space, free_space, free_space, free_space, free_space]]
	print("\n\n\n        0  .  1  .  2  .  3  .  4")
	print(line)
	for y in range(5):
		if player_location[1] == y:
			for x in range(5):
				if player_location[0] == x:
					grid[y][x] = player_caractere
				else:
					grid[y][x] = free_space
			print(" {} ||{}{}{}{}{}|".format(y, grid[y][0], grid[y][1], grid[y][2], grid[y][3], grid[y][4]))
			print(line)
		else:
			print(" {} ||{}{}{}{}{}|".format(y, grid[y][0], grid[y][1], grid[y][2], grid[y][3], grid[y][4]))
			print(line) 


clear_screen()  
print("\nConsegue advinhar onde esta o ursinho vai aparecer?") 
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
		drawn_grid(player)
		
		vert = int(vert)
		hori = int(hori)

		if vert == player[0] and hori == player[1]:
			print("\n>>> Uau! Agora me diz o número da loteria...\n>>> Brinks 😋")
		else:
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