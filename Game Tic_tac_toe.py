import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe PRO")
click_sound = pygame.mixer.Sound("click.mp3")
click_sound.set_volume(0.5)

FONT = pygame.font.SysFont(None, 40)

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

mode = "MENU"  # MENU / GAME
ai_mode = False
ai_level = "MUDAH"
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
    text1 = FONT.render("MUDAH", True, BLACK)
    text2 = FONT.render("SEDANG", True, BLACK)
    text3 = FONT.render("SULIT", True, BLACK)
    screen.blit(text1, (130,120))
    screen.blit(text2, (130,200))
    screen.blit(text3, (130,280))

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
                pygame.draw.line(screen, RED, (c*133+20,r*133+20), (c*133+110,r*133+110),6)
                pygame.draw.line(screen, RED, (c*133+110,r*133+20), (c*133+20,r*133+110),6)
            elif board[r][c] == "O":
                pygame.draw.circle(screen, BLUE, (c*133+66,r*133+66),40,6)

    # garis menang
    if winner_line:
        pygame.draw.line(screen, GREEN, winner_line[0], winner_line[1],8)
    
    # ------------------ AWAL KODE BARU YANG DITAMBAHKAN ------------------
    global btn_back
    mouse = pygame.mouse.get_pos()
    
    # Membuat area kotak tombol (x=240, y=430, lebar=140, tinggi=45)
    btn_back = pygame.Rect(240, 430, 140, 45)
    
    # Efek Hover: warna merah jika dilewati mouse, hitam jika tidak
    color_back = RED if btn_back.collidepoint(mouse) else BLACK
    pygame.draw.rect(screen, color_back, btn_back, 2)
    
    # Cetak tulisan "KEMBALI" di dalam kotak tombol
    txt_back = pygame.font.SysFont(None, 30).render("KEMBALI", True, color_back)
    screen.blit(txt_back, (265, 442))

    # Teks info status game di sebelah kiri bawah layar
    status_str = f"LVL: {ai_level}" if ai_mode else "2 PLAYER"
    if game_over:
        status_str = "SERI!" if not winner_line else "SELESAI!"
        
    level_text = FONT.render(status_str, True, BLACK)
    screen.blit(level_text, (10, 440))
    # ------------------ AKHIR KODE BARU YANG DITAMBAHKAN ------------------
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
                x,y = event.pos
                if 100 < y < 170:
                    ai_level = "EASY"
                    mode = "GAME"
                    click_sound.play()
                elif 180 < y < 250:
                    ai_level = "MEDIUM"
                    mode = "GAME"
                    click_sound.play()
                elif 260 < y < 330:
                    ai_level = "HARD"
                    mode = "GAME"
                    click_sound.play()

        elif mode == "GAME":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1. CEK DULU: Apakah yang diklik adalah tombol kembali?
                if btn_back.collidepoint(event.pos):
                    click_sound.play()
                    reset()       # Bersihkan papan sebelum kembali
                    mode = "MENU" # Pindah ke Menu Utama
                
                # 2. JIKA BUKAN tombol kembali, jalankan logika papan game seperti biasa
                # (Hanya berjalan jika game belum selesai DAN klik berada di area papan y < 400)
                elif not game_over and event.pos[1] < 400:
                    x, y = event.pos
                    r = y // 133
                    c = x // 133

                    if board[r][c] == "":
                        board[r][c] = player
                        beep()

                        if check_win():
                            print("MENANG:", player)
                            game_over = True
                        else:
                            player = "O" if player == "X" else "X"
                            if player == "X":
                                   giliran_text = "Giliran: X"
                                   giliran_color = BLUE 
                            else:
                                    giliran_text = "Giliran: O"
                                    giliran_color = RED
                        # AI jalan
                        if ai_mode and player == "O" and not game_over:
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
    elif mode == "LEVEL":
        draw_LEVEL_menu()
    else:
        draw_board()

    text_surface = FONT.render(giliran_text, True, giliran_color)
    screen.blit(text_surface, (20,20))

    pygame.display.update()
