import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe PRO")

FONT = pygame.font.SysFont(None, 40)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,100,255)
GREEN = (0,200,0)

board = [["" for _ in range(3)] for _ in range(3)]
player = "X"
game_over = False
winner_line = None

mode = "MENU"  # MENU / GAME
ai_mode = False

# SOUND (beep sederhana)
def beep():
    print("🔊 Beep")

def draw_menu():
    screen.fill(WHITE)
    text1 = FONT.render("Klik: 1 = 2 Player", True, BLACK)
    text2 = FONT.render("Klik: 2 = Lawan AI", True, BLACK)
    screen.blit(text1, (50,150))
    screen.blit(text2, (50,220))

def draw_board():
    screen.fill(WHITE)

    # garis
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (0,i*133),(400,i*133),4)
        pygame.draw.line(screen, BLACK, (i*133,0),(i*133,400),4)

    # X O
    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                pygame.draw.line(screen, RED,
                                 (c*133+20,r*133+20),
                                 (c*133+110,r*133+110),6)
                pygame.draw.line(screen, RED,
                                 (c*133+110,r*133+20),
                                 (c*133+20,r*133+110),6)
            elif board[r][c] == "O":
                pygame.draw.circle(screen, BLUE,
                                   (c*133+66,r*133+66),40,6)

    # garis menang
    if winner_line:
        pygame.draw.line(screen, GREEN,
                         winner_line[0],
                         winner_line[1],8)

def check_win():
    global winner_line

    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!="":
            winner_line = ((0,i*133+66),(400,i*133+66))
            return True
        if board[0][i]==board[1][i]==board[2][i]!="":
            winner_line = ((i*133+66,0),(i*133+66,400))
            return True

    if board[0][0]==board[1][1]==board[2][2]!="":
        winner_line = ((0,0),(400,400))
        return True

    if board[0][2]==board[1][1]==board[2][0]!="":
        winner_line = ((400,0),(0,400))
        return True

    return False
def ai_move():
    # 30% AI main random (bisa salah)
    if random.random() < 0.95:
        empty = [(r,c) for r in range(3) for c in range(3) if board[r][c] == ""]
        if empty:
            r,c = random.choice(empty)
            board[r][c] = "-1"
            return

    # 70% tetap pakai minimax (pintar)
    best_score = -100
    best_move = None

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O"
                score = minimax(False)
                board[r][c] = ""

                if score > best_score:
                    best_score = score
                    best_move = (r, c)

    if best_move:
        board[best_move[0]][best_move[1]] = "O"

import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe PRO")

FONT = pygame.font.SysFont(None, 40)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,100,255)
GREEN = (0,200,0)

board = [["" for _ in range(3)] for _ in range(3)]
player = "X"
game_over = False
winner_line = None

mode = "MENU"  # MENU / GAME
ai_mode = False

# SOUND (beep sederhana)
def beep():
    print("🔊 Beep")

def draw_menu():
    screen.fill(WHITE)
    text1 = FONT.render("Klik: 1 = 2 Player", True, BLACK)
    text2 = FONT.render("Klik: 2 = Lawan AI", True, BLACK)
    screen.blit(text1, (50,150))
    screen.blit(text2, (50,220))

def draw_board():
    screen.fill(WHITE)

    # garis
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (0,i*133),(400,i*133),4)
        pygame.draw.line(screen, BLACK, (i*133,0),(i*133,400),4)

    # X O
    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                pygame.draw.line(screen, RED,
                                 (c*133+20,r*133+20),
                                 (c*133+110,r*133+110),6)
                pygame.draw.line(screen, RED,
                                 (c*133+110,r*133+20),
                                 (c*133+20,r*133+110),6)
            elif board[r][c] == "O":
                pygame.draw.circle(screen, BLUE,
                                   (c*133+66,r*133+66),40,6)

    # garis menang
    if winner_line:
        pygame.draw.line(screen, GREEN,
                         winner_line[0],
                         winner_line[1],8)

def check_win():
    global winner_line

    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!="":
            winner_line = ((0,i*133+66),(400,i*133+66))
            return True
        if board[0][i]==board[1][i]==board[2][i]!="":
            winner_line = ((i*133+66,0),(i*133+66,400))
            return True

    if board[0][0]==board[1][1]==board[2][2]!="":
        winner_line = ((0,0),(400,400))
        return True

    if board[0][2]==board[1][1]==board[2][0]!="":
        winner_line = ((400,0),(0,400))
        return True

    return False

def ai_move():
    best_score = -100
    best_move = None

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O"
                score = minimax(False)
                board[r][c] = ""

                if score > best_score:
                    best_score = score
                    best_move = (r, c)

    if best_move:
        board[best_move[0]][best_move[1]] = "O"
def is_full():
    return all(board[r][c] != "" for r in range(3) for c in range(3))


def check_winner():
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!="":
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i]!="":
            return board[0][i]

    if board[0][0]==board[1][1]==board[2][2]!="":
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!="":
        return board[0][2]

    return None


def minimax(is_max):
    winner = check_winner()

    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full():
        return 0

    if is_max:
        best = -100
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "O"
                    score = minimax(False)
                    board[r][c] = ""
                    best = max(best, score)
        return best
    else:
        best = 100
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "X"
                    score = minimax(True)
                    board[r][c] = ""
                    best = min(best, score)
        return best

def reset():
    global board, player, game_over, winner_line
    board = [["" for _ in range(3)] for _ in range(3)]
    player = "X"
    game_over = False
    winner_line = None

# LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if mode == "MENU":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if 100 < y < 200:
                    mode = "GAME"
                    ai_mode = False
                elif 200 < y < 300:
                    mode = "GAME"
                    ai_mode = True

        elif mode == "GAME":
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x,y = event.pos
                if y < 400:
                    r = y // 133
                    c = x // 133

                    if board[r][c] == "":
                        board[r][c] = player
                        beep()

                        if check_win():
                            print("MENANG:", player)
                            game_over = True
                        else:
                            player = "O" if player=="X" else "X"

                        # AI jalan
                        if ai_mode and player=="O" and not game_over:
                            ai_move()
                            beep()

                            if check_win():
                                print("AI MENANG")
                                game_over = True
                            else:
                                player = "X"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()

    if mode == "MENU":
        draw_menu()
    else:
        draw_board()

    pygame.display.update()        
    import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe PRO")

FONT = pygame.font.SysFont(None, 40)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,100,255)
GREEN = (0,200,0)

board = [["" for _ in range(3)] for _ in range(3)]
player = "X"
game_over = False
winner_line = None

mode = "MENU"  # MENU / GAME
ai_mode = False

# SOUND (beep sederhana)
def beep():
    print("🔊 Beep")

def draw_menu():
    screen.fill(WHITE)
    text1 = FONT.render("Klik: 1 = 2 Player", True, BLACK)
    text2 = FONT.render("Klik: 2 = Lawan AI", True, BLACK)
    screen.blit(text1, (50,150))
    screen.blit(text2, (50,220))

def draw_board():
    screen.fill(WHITE)

    # garis
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (0,i*133),(400,i*133),4)
        pygame.draw.line(screen, BLACK, (i*133,0),(i*133,400),4)

    # X O
    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                pygame.draw.line(screen, RED,
                                 (c*133+20,r*133+20),
                                 (c*133+110,r*133+110),6)
                pygame.draw.line(screen, RED,
                                 (c*133+110,r*133+20),
                                 (c*133+20,r*133+110),6)
            elif board[r][c] == "O":
                pygame.draw.circle(screen, BLUE,
                                   (c*133+66,r*133+66),40,6)

    # garis menang
    if winner_line:
        pygame.draw.line(screen, GREEN,
                         winner_line[0],
                         winner_line[1],8)

def check_win():
    global winner_line

    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!="":
            winner_line = ((0,i*133+66),(400,i*133+66))
            return True
        if board[0][i]==board[1][i]==board[2][i]!="":
            winner_line = ((i*133+66,0),(i*133+66,400))
            return True

    if board[0][0]==board[1][1]==board[2][2]!="":
        winner_line = ((0,0),(400,400))
        return True

    if board[0][2]==board[1][1]==board[2][0]!="":
        winner_line = ((400,0),(0,400))
        return True

    return False

def ai_move():
    empty = [(r,c) for r in range(3) for c in range(3) if board[r][c]==""]

    if empty:
        r,c = random.choice(empty)
        board[r][c] = "O"

def reset():
    global board, player, game_over, winner_line
    board = [["" for _ in range(3)] for _ in range(3)]
    player = "X"
    game_over = False
    winner_line = None

# LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if mode == "MENU":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if 100 < y < 200:
                    mode = "GAME"
                    ai_mode = False
                elif 200 < y < 300:
                    mode = "GAME"
                    ai_mode = True

        elif mode == "GAME":
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x,y = event.pos
                if y < 400:
                    r = y // 133
                    c = x // 133

                    if board[r][c] == "":
                        board[r][c] = player
                        beep()

                        if check_win():
                            print("MENANG:", player)
                            game_over = True
                        else:
                            player = "O" if player=="X" else "X"

                        # AI jalan
                        if ai_mode and player=="O" and not game_over:
                            ai_move()
                            beep()

                            if check_win():
                                print("AI MENANG")
                                game_over = True
                            else:
                                player = "X"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()

    if mode == "MENU":
        draw_menu()
    else:
        draw_board()

    pygame.display.update()

def reset():
    global board, player, game_over, winner_line
    board = [["" for _ in range(3)] for _ in range(3)]
    player = "X"
    game_over = False
    winner_line = None

# LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if mode == "MENU":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if 100 < y < 200:
                    mode = "GAME"
                    ai_mode = False
                elif 200 < y < 300:
                    mode = "GAME"
                    ai_mode = True

        elif mode == "GAME":
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x,y = event.pos
                if y < 400:
                    r = y // 133
                    c = x // 133

                    if board[r][c] == "":
                        board[r][c] = player
                        beep()

                        if check_win():
                            print("MENANG:", player)
                            game_over = True
                        else:
                            player = "O" if player=="X" else "X"

                        # AI jalan
                        if ai_mode and player=="O" and not game_over:
                            ai_move()
                            beep()

                            if check_win():
                                print("AI MENANG")
                                game_over = True
                            else:
                                player = "X"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()

    if mode == "MENU":
        draw_menu()
    else:
        draw_board()

    pygame.display.update()