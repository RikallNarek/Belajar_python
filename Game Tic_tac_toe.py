from tkinter.tix import STATUS

import pygame
import sys
import random
import os

pygame.init()

WIDTH, HEIGHT = 400, 650
OFFSET_Y = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe PRO")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
click_sound = pygame.mixer.Sound(
    os.path.join(BASE_DIR, "click.mp3")
)

click_sound.set_volume(0.5)

FONT = pygame.font.SysFont(None, 40)
BIG_FONT = pygame.font.SysFont(None, 55)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,100,255)
GREEN = (0,200,0)
giliran_text = "Giliran: X"
giliran_color = BLUE
board = [["" for _ in range(3)] for _ in range(3)]
player = "X"
game_over = False
winner_line = None
winner = ""

mode = "MENU"  # MENU / GAME
ai_mode = False
ai_level = "MUDAH"

# ==========================
# AI DELAY
# ==========================
ai_thinking = False
ai_start_time = 0
AI_DELAY = 500

# SOUND (beep sederhana)
def beep():
    click_sound.play()

def draw_menu():

    screen.fill(WHITE)

    mouse = pygame.mouse.get_pos()

    title = FONT.render("TIC TAC TOE PRO", True, BLACK)
    screen.blit(title, (70,60))

    global btn_player
    global btn_ai
    global btn_exit

    btn_player = pygame.Rect(100,150,200,50)
    btn_ai = pygame.Rect(100,230,200,50)
    btn_exit = pygame.Rect(100,310,200,50)

    color1 = BLUE if btn_player.collidepoint(mouse) else BLACK
    color2 = BLUE if btn_ai.collidepoint(mouse) else BLACK
    color3 = RED if btn_exit.collidepoint(mouse) else BLACK

    pygame.draw.rect(screen,color1,btn_player,3)
    pygame.draw.rect(screen,color2,btn_ai,3)
    pygame.draw.rect(screen,color3,btn_exit,3)

    txt1 = FONT.render("2 PLAYER",True,color1)
    txt2 = FONT.render("LAWAN AI",True,color2)
    txt3 = FONT.render("KELUAR",True,color3)

    screen.blit(txt1,(125,160))
    screen.blit(txt2,(130,240))
    screen.blit(txt3,(145,320))

def draw_LEVEL_menu():

    screen.fill(WHITE)

    mouse = pygame.mouse.get_pos()

    title = FONT.render("PILIH LEVEL AI", True, BLACK)
    screen.blit(title, (80, 50))

    global btn_easy
    global btn_medium
    global btn_hard
    global btn_back

    btn_easy = pygame.Rect(100, 130, 200, 50)
    btn_medium = pygame.Rect(100, 220, 200, 50)
    btn_hard = pygame.Rect(100, 310, 200, 50)
    btn_back = pygame.Rect(100, 400, 200, 50)

    color1 = BLUE if btn_easy.collidepoint(mouse) else BLACK
    color2 = BLUE if btn_medium.collidepoint(mouse) else BLACK
    color3 = BLUE if btn_hard.collidepoint(mouse) else BLACK
    color4 = RED if btn_back.collidepoint(mouse) else BLACK

    pygame.draw.rect(screen, color1, btn_easy, 3)
    pygame.draw.rect(screen, color2, btn_medium, 3)
    pygame.draw.rect(screen, color3, btn_hard, 3)
    pygame.draw.rect(screen, color4, btn_back, 3)

    txt1 = FONT.render("MUDAH", True, color1)
    txt2 = FONT.render("SEDANG", True, color2)
    txt3 = FONT.render("SULIT", True, color3)
    txt4 = FONT.render("KEMBALI", True, color4)

    screen.blit(txt1, (135, 140))
    screen.blit(txt2, (125, 230))
    screen.blit(txt3, (140, 320))
    screen.blit(txt4, (120, 410))

def draw_board():
    screen.fill(WHITE)

    # garis
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (0, OFFSET_Y + i*133),(400, OFFSET_Y + i*133),4)
        pygame.draw.line(screen, BLACK, (i*133, OFFSET_Y),(i*133,OFFSET_Y + 400),4)
    # bingkai luar papan
    pygame.draw.rect(screen, BLACK, (0, OFFSET_Y,400,400),4)

    # X O
    for r in range(3):
        for c in range(3):
            if board[r][c] == "X":
                pygame.draw.line(screen, RED, (c*133+20, OFFSET_Y + r*133+20), (c*133+110, OFFSET_Y + r*133+110),6)
                pygame.draw.line(screen, RED, (c*133+110, OFFSET_Y + r*133+20), (c*133+20, OFFSET_Y + r*133+110),6)
            elif board[r][c] == "O":
                pygame.draw.circle(screen, BLUE, (c*133+66, OFFSET_Y + r*133+66),40,6)

    # garis menang
    if winner_line:
        pygame.draw.line(screen, GREEN, winner_line[0], winner_line[1],8)
    
    # ==========================
    # MENU AKHIR PERMAINAN
    # ==========================
    if game_over:

        mouse = pygame.mouse.get_pos()

        global btn_continue, btn_menu, btn_exit_game

        btn_continue = pygame.Rect(20, 535, 110, 45)
        btn_menu = pygame.Rect(145, 535, 110, 45)
        btn_exit_game = pygame.Rect(270, 535, 110, 45)

        color1 = BLUE if btn_continue.collidepoint(mouse) else BLACK
        color2 = BLUE if btn_menu.collidepoint(mouse) else BLACK
        color3 = RED if btn_exit_game.collidepoint(mouse) else BLACK

        pygame.draw.rect(screen, color1, btn_continue, 2)
        pygame.draw.rect(screen, color2, btn_menu, 2)
        pygame.draw.rect(screen, color3, btn_exit_game, 2)

        txt1 = pygame.font.SysFont(None,30).render("LANJUT",True,color1)
        txt2 = pygame.font.SysFont(None,30).render("MENU",True,color2)
        txt3 = pygame.font.SysFont(None,30).render("KELUAR",True,color3)

        screen.blit(txt1,(35,550))
        screen.blit(txt2,(170,550))
        screen.blit(txt3,(285,550))

    # ------------------ AKHIR KODE BARU YANG DITAMBAHKAN ------------------
def check_win():
    global winner_line

    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!="":
            winner_line = ((0, OFFSET_Y + i*133+66),(400, OFFSET_Y + i*133+66))
            return True
        if board[0][i]==board[1][i]==board[2][i]!="":
            winner_line = ((i*133+66, OFFSET_Y),(i*133+66, OFFSET_Y + 400))
            return True

    if board[0][0]==board[1][1]==board[2][2]!="":
        winner_line = ((0, OFFSET_Y),(400, OFFSET_Y + 400))
        return True

    if board[0][2]==board[1][1]==board[2][0]!="":
        winner_line = ((400, OFFSET_Y),(0, OFFSET_Y + 400))
        return True

    return False

def ai_easy():
    empty = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                empty.append((r,c))

    if empty:
        r,c = random.choice(empty)
        board[r][c] = "O"


def ai_hard():

    best_score = -100
    move = None

    for r in range(3):
        for c in range(3):

            if board[r][c] == "":

                board[r][c] = "O"
                score = minimax(False)

                board[r][c] = ""

                if score > best_score:
                    best_score = score
                    move = (r,c)

    if move:
        board[move[0]][move[1]] = "O"


def ai_medium():

    if random.random() < 0.5:
        ai_easy()
    else:
        ai_hard()


def ai_move():

    if ai_level == "EASY":
        ai_easy()

    elif ai_level == "MEDIUM":
        ai_medium()

    elif ai_level == "HARD":
        ai_hard()

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
    global board, player, game_over, winner_line, winner, draw_game
    board = [["" for _ in range(3)] for _ in range(3)]
    player = "X"
    game_over = False
    winner_line = None
    winner = ""
    draw_game = False
# LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if mode == "MENU":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if btn_player.collidepoint(event.pos):
                    mode = "GAME"
                    ai_mode = False
                    click_sound.play()

                elif btn_ai.collidepoint(event.pos):
                    mode = "LEVEL"
                    ai_mode = True
                    click_sound.play()

                elif btn_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        elif mode == "LEVEL":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_easy.collidepoint(event.pos):
                    ai_level = "EASY"
                    mode = "GAME"
                    click_sound.play()
                elif btn_medium.collidepoint(event.pos):
                    ai_level = "MEDIUM"
                    mode = "GAME"
                    click_sound.play()
                elif btn_hard.collidepoint(event.pos):
                    ai_level = "HARD"
                    mode = "GAME"
                    click_sound.play()
                elif btn_back.collidepoint(event.pos):
                    mode = "MENU"
                    click_sound.play()

        elif mode == "GAME":
            if event.type == pygame.MOUSEBUTTONDOWN:

                # ==========================
                # JIKA GAME SUDAH SELESAI
                # ==========================
                if game_over:

                    if btn_continue.collidepoint(event.pos):
                        click_sound.play()
                        reset()

                    elif btn_menu.collidepoint(event.pos):
                        click_sound.play()
                        reset()
                        mode = "MENU"

                    elif btn_exit_game.collidepoint(event.pos):
                        click_sound.play()
                        pygame.quit()
                        sys.exit()

                # ==========================
                # JIKA GAME BELUM SELESAI
                # ==========================
                elif OFFSET_Y <= event.pos[1] < OFFSET_Y + 400: # type: ignore

                    x, y = event.pos
                    r = (y - OFFSET_Y) // 133 # type: ignore
                    c = x // 133

                    if board[r][c] == "":
                        board[r][c] = player
                        beep()

                    if check_win():
                        winner = player
                        print("MENANG:", player)
                        game_over = True

                    else:
                        player = "O" if player == "X" else "X"
                        draw_game = True

                    if draw_game and not game_over:
                        if all(board[i][j] != "" for i in range(3) for j in range(3)):
                            game_over = True
                            winner = "seri"
                            print("seri")
                    if ai_mode and player == "O" and not game_over:
                        ai_thinking = True
                        ai_start_time = pygame.time.get_ticks()
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
    # =========================
    # AI BERPIKIR
    # =========================
    if ai_thinking:

        sekarang = pygame.time.get_ticks()

        if sekarang - ai_start_time >= AI_DELAY:

            ai_move()
            beep()

            if check_win():
                winner = "O"
                print("AI MENANG")
                game_over = True
            else:
                player = "X"

            ai_thinking = False

    if mode == "MENU":
        draw_menu()
    elif mode == "LEVEL":
        draw_LEVEL_menu()
    else:
        draw_board()

    # ==========================
    # STATUS GILIRAN
    # ==========================
        
    if player == "X":

        giliran_text = "Giliran : X"
        giliran_color = BLUE

    else:

        giliran_text = "Giliran : O"
        giliran_color = RED

    if mode == "GAME" and not game_over:
        text_surface = FONT.render(giliran_text, True, giliran_color)
        screen.blit(text_surface, (20,485))

    if game_over:
        
        if winner == "seri":
            text = BIG_FONT.render("Seri!", True, RED)
            screen.blit(text, (140, 15))
        else:
            text = BIG_FONT.render(f"Pemenang: {winner}", True, GREEN)
            screen.blit(text, (45, 15))

    pygame.display.update()
