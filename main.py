import pygame as pg
from pygame import mixer
import time
def main():
    p = (255,255,255)
    k = p
    pg.init()
    height = 600
    surface = pg.display.set_mode((height,height))
    pg.display.set_caption("Tic Tac Toe - Atharva Vaze")
    run = True
    turn = 0
    tool = ''
    class button:
        hover = False
        pressed = False
        def __init__(button, rect, color):
            button.rect = rect
            button.color = color
        def draw(button, surface):
            pg.draw.rect(surface, button.color, button.rect)
    def is_grid_full(grid):
        for row in grid:
            for box in row:
                if box == '':
                    return False
        return True
    def three(grid):
        pos1 = grid[0][0]
        pos2 = grid[0][1]
        pos3 = grid[0][2]
        pos4 = grid[1][0]
        pos5 = grid[1][1]
        pos6 = grid[1][2]
        pos7 = grid[2][0]
        pos8 = grid[2][1]
        pos9 = grid[2][2]
        if pos1 == pos2 == pos3 and len(pos1) != 0:
            return True
        elif pos4 == pos5 == pos6 and len(pos4) != 0:
            return True
        elif pos7 == pos8 == pos9 and len(pos7) != 0:
            return True
        elif pos1 == pos4 == pos7 and len(pos4) != 0:
            return True
        elif pos2 == pos5 == pos8 and len(pos2) != 0:
            return True
        elif pos3 == pos6 == pos9 and len(pos3) != 0:
            return True
        elif pos1 == pos5 == pos9 and len(pos1) != 0:
            return True
        elif pos3 == pos5 == pos7 and len(pos5) != 0:
            return True
        else:
            return False
    grid  = [['','',''],
            ['','',''],
            ['','','']]
    clock = pg.time.Clock()
    def ex(coords):
            tup1 = coords
            # first line coords
            x = tup1[0]-75
            y = tup1[1] + 75
            a = tup1[0] + 75
            b = tup1[1] - 75
            # secnd line coords
            i = tup1[0]-75
            k = tup1[1] - 75
            j = tup1[0] + 75
            l = tup1[1] + 75
            pg.draw.line(surface, (255,0,0), (x,y), (a,b), 20)
            pg.draw.line(surface, (255,0,0), (i,k), (j,l), 20)
    surface.fill((100,100,255))
    tpcheck = False
    c = (255,255,255)
    d = (255,255,255)
    pg.mixer.pre_init(44100, -16,2,512)
    mixer.init()
    while run:
        hover1 = False
        hover2 = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        if not tpcheck:
            counter = 0
            execute = False
            pg.draw.rect(surface, (220,220,220), (100,200, 400, 200))
            pg.draw.line(surface, (0,0,0), (100,200), (500,200), 10)
            pg.draw.line(surface, (0,0,0), (100,400), (500,400), 10)
            pg.draw.line(surface, (0,0,0), (100,200), (100,400), 20)
            pg.draw.line(surface, (0,0,0), (500,200), (500,400), 20)
            tpm = button((230,230,150,50),c)
            opm = button((230,300,150,50),d)
            tpm.draw(surface)
            opm.draw(surface)
            font = pg.font.Font(None, 25)
            text = font.render("Two-Player Mode", 1, (255,0,0))
            surface.blit(text, (235,250))
            n1text = font.render("Another Mode", 1, (255,0,0))
            surface.blit(n1text, (235, 320))
            nfont = pg.font.Font(None, 40)
            ntext = nfont.render("Tic-Tac-Toe Menu: Choose Game Modes.", 1, (0,0,0))
            surface.blit(ntext, (35,100))
            pg.display.flip()
        p1 = pg.mouse.get_pos()[0]
        p2 = pg.mouse.get_pos()[1]
        hover = False
        if (230 <= p1 <= 380) and (230<= p2 <= 280) and not (pg.mouse.get_pressed()[0]):
            hover = True
        if hover:
            c = (141,145,141)
        else:
            c = (255,255,255)
        if (230 <= p1 <= 380) and (230<= p2 <= 280) and (pg.mouse.get_pressed()[0]):
            tpcheck = True
            if not counter > 0:
                w = pg.mixer.Sound('chime.wav')
                w.play()
            counter +=1
            continue
        if (tpcheck):
            surface.fill((255,255,255))
            if pg.mouse.get_pressed()[0] and not execute:
                if turn % 2 == 0:
                    tool = 'X'
                else:
                    tool = 'O'
                if 0 <= pg.mouse.get_pos()[0] <= 200 and 0 <= pg.mouse.get_pos()[1] <= 200:
                    if len(grid[0][0]) == 0:
                        grid[0][0] = tool
                        turn += 1
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                elif 200 < pg.mouse.get_pos()[0] <= 400 and 0 <= pg.mouse.get_pos()[1] <= 200:
                    if len(grid[0][1]) == 0:
                        grid[0][1] = tool
                        turn+=1
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                elif 400 < pg.mouse.get_pos()[0] <= 600 and 0 <= pg.mouse.get_pos()[1] <= 200:
                    if len(grid[0][2]) == 0:
                        grid[0][2] = tool
                        turn += 1
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                elif 0 <= pg.mouse.get_pos()[0] <= 200 and 200 < pg.mouse.get_pos()[1] <= 400:
                    if len(grid[1][0]) == 0:
                        grid[1][0] = tool
                        turn +=1 
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                elif 200 < pg.mouse.get_pos()[0] <= 400 and 200 < pg.mouse.get_pos()[1] <= 400:
                    if len(grid[1][1]) == 0:
                        grid[1][1] = tool
                        turn +=1
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                elif 400 < pg.mouse.get_pos()[0] <= 600 and 200 < pg.mouse.get_pos()[1] <= 400:
                    if len(grid[1][2]) == 0:
                        grid[1][2] = tool
                        turn +=1
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                elif 0 <= pg.mouse.get_pos()[0] <= 200 and 400 < pg.mouse.get_pos()[1] <= 600:
                    if len(grid[2][0]) == 0:
                        grid[2][0] = tool
                        turn +=1
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                elif 200 < pg.mouse.get_pos()[0] <= 400 and 400 < pg.mouse.get_pos()[1] <= 600:
                    if len(grid[2][1]) == 0:
                        grid[2][1] = tool
                        turn += 1
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                elif 400 < pg.mouse.get_pos()[0] <= 600 and 400 < pg.mouse.get_pos()[1] <= 600:
                    if len(grid[2][2]) == 0:
                        grid[2][2] = tool
                        turn += 1
                        w1 = pg.mixer.Sound('wood.wav')
                        w1.play()
                coords = [(100,100),(300,100),(500,100),(100,300),(300,300),(500,300),(100,500),(300,500),(500,500)]
            i = 0
            for row in grid:
                for pos in row:
                    if pos == 'X':
                        ex(coords[i])
                    elif pos == 'O':
                        pg.draw.circle(surface, (0,0,255), coords[i], 75, 20)
                    elif pos == '':
                        pass
                    i += 1
            pg.draw.line(surface, (0,0,0), (200,0),(200,600),20)
            pg.draw.line(surface, (0,0,0), (400,0), (400,600), 20)
            pg.draw.line(surface, (0,0,0), (0,200), (600,200), 20)
            pg.draw.line(surface, (0,0,0), (0,400), (600, 400), 20)
            if not three(grid) and is_grid_full(grid):
                if execute:
                    time.sleep(0.25)
                    surface.fill((100,100,225))
                    ta = button((90,100,400,100),(255,255,255))
                    ta.draw(surface)
                    font = pg.font.Font(None, 145)
                    text = font.render('TIE!',1,(0,255,0))
                    surface.blit(text, (190,100))
                    fonty = pg.font.Font(None, 100)
                    ta1 = button((90,300,420,75),p)
                    ta2 = button((90,450,400,100),k)
                    ta1.draw(surface)
                    ta2.draw(surface)
                    ta1text = fonty.render('Play Again?',1,(0,0,0))
                    ta2text = font.render('Exit', 1, (255,0,0))
                    surface.blit(ta1text, (110,300))
                    surface.blit(ta2text, (190,450))
                    p3 = pg.mouse.get_pos()[0]
                    p4 = pg.mouse.get_pos()[1]
                    if (90 <= p3 <= 510) and (300<= p4 <= 375):
                        hover1 = True
                        if pg.mouse.get_pressed()[0]:
                            surface.fill((100,100,255))
                            grid  = [['','',''],['','',''],['','','']]
                            tpcheck = False
                            atharva = pg.mixer.Sound('chime.wav')
                            atharva.play()
                    elif (90 <= p3<= 490) and (450<=p4<=550):
                        hover2 = True
                        if pg.mouse.get_pressed()[0]:
                            run = False
                    if hover1:
                        p = (220,220,220)
                    else:
                        p = (255,255,255)
                    if hover2:
                        k = (220,220,220)
                    else:
                        k = (255,255,255)
                else:
                    time.sleep(0.1)
                    execute = True
            elif three(grid):
                if execute:
                    time.sleep(0.25)
                    grid = [['x','x','x'],['x','x','x'],['x','x','x']]
                    surface.fill((100,100,225))
                    ta = button((90,100,400,100),(255,255,255))
                    ta.draw(surface)
                    font = pg.font.Font(None, 145)
                    if tool == 'X':
                        text = font.render("X WON!",1,(255,0,0))
                    else:
                        text = font.render('O WON!',1, (0,0,255) )
                    surface.blit(text, (110,100))
                    fonty = pg.font.Font(None, 100)
                    ta1 = button((90,300,420,75),p)
                    ta2 = button((90,450,400,100),k)
                    ta1.draw(surface)
                    ta2.draw(surface)
                    ta1text = fonty.render('Play Again?',1,(0,0,0))
                    ta2text = font.render('Exit', 1, (255,0,0))
                    surface.blit(ta1text, (110,300))
                    surface.blit(ta2text, (190,450))
                    p3 = pg.mouse.get_pos()[0]
                    p4 = pg.mouse.get_pos()[1]
                    if (90 <= p3 <= 510) and (300<= p4 <= 375):
                        hover1 = True
                        if pg.mouse.get_pressed()[0]:
                            surface.fill((100,100,255))
                            grid  = [['','',''],['','',''],['','','']]
                            tpcheck = False
                            atharva = pg.mixer.Sound('chime.wav')
                            atharva.play()
                    elif (90 <= p3<= 490) and (450<=p4<=550):
                        hover2 = True
                        if pg.mouse.get_pressed()[0]:
                            run = False
                    if hover1:
                        p = (220,220,220)
                    else:
                        p = (255,255,255)
                    if hover2:
                        k = (220,220,220)
                    else:
                        k = (255,255,255)
                else:
                    time.sleep(0.1)
                    execute = True
            pg.display.flip()
            clock.tick(60)
    pg.quit()
if __name__ == "__main__":
    main()