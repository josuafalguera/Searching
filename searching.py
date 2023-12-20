from mimetypes import init
from platform import node
from re import L
from time import sleep
from turtle import circle, clear, update
import pygame
from pygame.rect import Rect
from pygame_widgets.textbox import TextBox
import pygame_widgets


# colors

node_color = (128,0,128)
num_pos_base = 220
num_pos = [0 , 0  , 0]
# variables 

pos = []
screen_height = 800
screen_width = 1500
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((32,32 , 32))
num = 0
objects = []
nodes = []
edges = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        # self.buttonSurf = smallfont.render(buttonText, True, (20, 20, 20))
        smallfont = pygame.font.SysFont('Corbel',35)
        self.buttonSurf =  smallfont.render(buttonText , True , (20, 20, 20))

        self.alreadyPressed = False
        objects.append(self)

        
    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def breadth_first_search(arr,initial):
    
    visited = []
    processed = []

    for i in range(0 , len(arr)):
        visited.append(0)
    
    queue = [initial]
    visited[initial] = 1

    while len(queue) != 0:

        ev = pygame.event.get()

        node = queue.pop(0)
        pygame.draw.circle(screen , (0 , 255 , 0) , pos[node] , 30 )
        color = (0 , 0 , 0)
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render(str(node) , True , color)
        screen.blit(text , (pos[node][0]-8 , pos[node][1]-20))
        dfs_output(processed=  processed , inqueue=queue , processing=[node]  )
        pygame.display.update()
        pygame.time.wait(1000)

        print(node , end=' ')
        for i in arr[node]:
            
            if visited[i] != 1:
                pygame.draw.circle(screen , (255 , 165 , 0) , pos[i] , 30 )
                smallfont = pygame.font.SysFont('Corbel',35)
                text = smallfont.render(str(i) , True , color)
                screen.blit(text , (pos[i][0]-8 , pos[i][1]-20))
                visited[i] = 1
                queue.append(i)
                dfs_output(processed=  processed , inqueue=queue , processing=[node]  )
                pygame.display.update()
                pygame.time.wait(1000)

        
        processed.append(node)
        pygame.draw.circle(screen , (229, 43, 18) , pos[node] , 30 )
        dfs_output(processed=  processed , inqueue=queue , processing=[node]  )
        color = (0 , 0 , 0)
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render(str(node) , True , color)
        screen.blit(text , (pos[node][0]-8 , pos[node][1]-20))
        pygame.display.update()
        pygame.time.wait(1000)


def depth_first_search(arr,initial):
    
    visited = []

    processed = []
    for i in range(0 , len(arr)):
        visited.append(0)
    
    stack = [initial]
    visited[initial] = 1
    pygame.draw.circle(screen , (0 , 255 , 0) , pos[initial] , 30 )
    color = (0 , 0 , 0)
    smallfont = pygame.font.SysFont('Corbel',35)
    text = smallfont.render(str(initial) , True , color)
    screen.blit(text , (pos[initial][0]-8 , pos[initial][1]-20))
    dfs_output(processed=  processed , inqueue=stack , processing=[initial]  )
    pygame.display.update()
    pygame.time.wait(1000)

    node = 0
 
    while len(stack) != 0:

        ev = pygame.event.get()

        node = stack.pop(0)
        pygame.draw.circle(screen , (0 , 255 , 0) , pos[node] , 30 )
        color = (0 , 0 , 0)
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render(str(node) , True , color)
        screen.blit(text , (pos[node][0]-8 , pos[node][1]-20))
        dfs_output(processed=  processed , inqueue=stack , processing=[node]  )
        pygame.display.update()
        pygame.time.wait(1000)
            
        print(node , end=' ')
        for i in arr[node]:
            
            ev = pygame.event.get()
            if visited[i] != 1:
                pygame.draw.circle(screen , (255 , 165 , 0) , pos[i] , 30 )
                smallfont = pygame.font.SysFont('Corbel',35)
                text = smallfont.render(str(i) , True , color)
                screen.blit(text , (pos[i][0]-8 , pos[i][1]-20))
                visited[i] = 1
                stack.insert(0 , i)
                dfs_output(processed=  processed , inqueue=stack , processing=[node]  )
                pygame.display.update()
                pygame.time.wait(1000)
        
        processed.append(node)
        pygame.draw.circle(screen , (229, 43, 18) , pos[node] , 30 )
        dfs_output(processed=  processed , inqueue=stack , processing=[node]  )
        color = (0 , 0 , 0)
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render(str(node) , True , color)
        screen.blit(text , (pos[node][0]-8 , pos[node][1]-20))
        pygame.display.update()
        pygame.time.wait(1000)

def create_graph():

    for i in range(0 , num):
        nodes.append([])
    for e in edges:
        nodes[e[0]].append(e[1])
        nodes[e[1]].append(e[0])


def myFunction():
    print('Button Pressed')
    create_graph()
    breadth_first_search ( nodes, 0)

def myFunction2():
    print('Button Pressed')
    create_graph()
    depth_first_search ( nodes, 0)


def reset():

    for node in range(0 , len(pos)):
        pygame.draw.circle(screen , node_color , pos[node] , 30 )
        color = (255 , 255 , 255)
        smallfont = pygame.font.SysFont('Corbel',35)
        text = smallfont.render(str(node) , True , color)
        screen.blit(text , (pos[node][0]-8 , pos[node][1]-20))
    


def output():
    # Get text in the textbox
    print("points - "+ str(type(textbox.getText())))
    print(textbox.getText())
    p1 , p2 = map( int , textbox.getText().split(' '))
    pygame.draw.line(screen , (255 , 255 , 255) ,pos[p1] ,pos[p2] , width=3)
    edges.append((p1 , p2))
    print(textbox.getText())
    textbox.setText('')

def reset_edges():
    
    global pos 
    global num
    number = num
    p = pos
    clearall()
    pos = p
    reset()
    num = number
    print(pos)
    print(num)
    print(edges)
    print(nodes)

 
def clearall():

    global num
    global edges
    global pos
    global nodes
    num = 0
    edges = []
    nodes= []
    pos = []
    screen.fill((32,32 , 32))
    text = font.render('Enter the edges', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (120 ,  190)
    screen.blit(text, textRect)
    textbox
    pygame.draw.line(screen , (255, 255, 255) , (250 , 0) , ( 250 , 600) , 2)
    pygame.draw.line(screen , (255, 255, 255) , (0 , 600) , ( 1500 , 600) , 5)
    # pygame.draw.line(screen , (255, 255, 255) , (0 , 460) , ( 250 , 460) , 5)
    pygame.display.update()
    


customButton = Button(30, 30, 200, 50, 'Run BFS', myFunction)
customButton2 = Button(30, 90, 200, 50, 'Run DFS', myFunction2)
rese = Button(30, 270, 200, 50, 'Reset', reset)
cl = Button(30, 330, 200, 50, 'Clear All', clearall)
reset_ed = Button(30, 390, 200, 50, 'Reset Edges', reset_edges)

font = pygame.font.Font(None, 32)
text = font.render('Enter the Edges', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (120 ,  190)
screen.blit(text, textRect)
textbox = TextBox(screen, 30 , 210 , 180, 40, fontSize=30,
                  borderColour=(0, 0, 0), textColour=(0, 0, 0),
                  onSubmit=output, radius=0, borderThickness=1)

line1 = pygame.draw.line(screen , (255, 255, 255) , (250 , 0) , ( 250 , 600) , 2)
# line2 = pygame.draw.line(screen , (255, 255, 255) , (0 , 460) , ( 250 , 460) , 5)
line2 = pygame.draw.line(screen , (255, 255, 255) , (0 , 600) , ( 1500 , 600) , 5)

def dfs_output(processed , inqueue , processing):

   
    screen.fill((32,32 , 32) , pygame.Rect(0 , 600 ,  1500 , 200))

    margin = 120
    position_t = 650

    texts = ['Processed : ' , 'In Queue : ' , 'Processing : ']
    colrs = [(229, 43, 18) , (255 , 165 , 0) , (0 , 255 , 0)]
    parms = [processed , inqueue , processing]

    font = pygame.font.Font(None, 32)

    for i in range(0 , len(texts)):

        text = font.render(texts[i], True, colrs[i])
        textRect = text.get_rect()
        textRect.center = (margin ,  position_t)
        screen.blit(text, textRect)
        global num_pos
        global num_pos_base

        for j in range(len(parms[i])):
            text = font.render( str (parms[i][j]), True, colrs[i])
            textRect = text.get_rect()
            textRect.center = (num_pos_base + num_pos[i] ,  position_t)
            screen.blit(text, textRect)
            num_pos[i] += 30

        position_t += 50
        num_pos[i] = 0
        pygame.display.update()

    

     

def run_game():

    user_text = ''
    input_rect = pygame.Rect(200, 200, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False
    running = True
    color = (255 , 255 , 255)
    smallfont = pygame.font.SysFont('Corbel',35)
    global num
    pygame.display.flip()
    while running:
        
        circ = pygame.mouse.get_pos()
        
        events = pygame.event.get()
        for event in events:


            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse click : " , circ)

                if (circ[0] >= 250 ):
                    

                    res = 1
                    i = 0
                    # for po in pos:
                    #     print(i , po)
                    #     i += 1
                    #     if( (abs( po[0] - circ[0] ) > 20) and (abs(po[1] - circ[1]) > 20) ):
                    #         res = 1
                    #     else : 
                    #         res = 0
                    #         break

                    if( res == 1):    
                        pygame.draw.circle(screen , node_color , circ , 30)
                        pos.append(circ)
                        text = smallfont.render(str(num) , True , color)
                        screen.blit(text , (circ[0]-8 , circ[1]-20))
                        num += 1
                        res = 0

                pygame.display.update()
                        # pygame.draw.circle(screen , (0 , 255 , 0) ,circ , 30 )
                

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False


            for object in objects:
                object.process()

            
        pygame_widgets.update(events)

        pygame.display.flip()
        


run_game()