SCRN_SIZEX = 1000
SCRN_SIZEY = 600

class Bullet:
    def __init__(self, img, x, y, size_x, size_y):
        self.img = img
        self.size_x = size_x
        self.size_y = size_y
        self.x = x
        self.y = y
    
    def move(self, vel):
        image(self.img, self.x, self.y, self.size_x, self.size_y)
        self.y -= vel

class Enemy:
    def __init__(self, img, x, y, size_x, size_y):
        self.img = img
        self.size_x = size_x
        self.size_y = size_y
        self.x = x
        self.y = y
        self.x_dir = 'r'
    
    def move(self, vel):
        image(self.img, self.x, self.y, self.size_x, self.size_y)
        self.y += vel
        
        # update direction (left or right)
        if self.x+self.size_x > SCRN_SIZEX: self.x_dir = 'l'
        elif self.x < 0: self.x_dir = 'r'
        
        # move
        if self.x_dir == 'r': self.x += 5*vel
        else: self.x -= 5*vel

def generateRandomColor():
    c = color(random(255), random(255), random(255))
    return '#' + hex(c, 6)

def setup():
    size(SCRN_SIZEX, SCRN_SIZEY)
    global player, bullet, bulletExists, enemy
    player = loadImage('Mr._Hankey_transparent.png')
    bullet = Bullet(loadImage('poop_PNG42.png'), 0, 0, 50, 50)
    enemy = Enemy(loadImage('member_berries.png'), random(SCRN_SIZEX), 0, 75, 75)
    bulletExists = False
    
    global bgcolor
    bgcolor = generateRandomColor()
    
    global score, lives
    score = 0
    lives = 5

def draw():
    global player, score, bulletExists, bgcolor, lives
    background(bgcolor)
    image(player, mouseX-(247/2.5)/2, SCRN_SIZEY-200, 247/2.5, 488/2.5)
    textSize(24)
    text("Score: " + str(score), 25, 25) 
    text("Lives: " + str(lives), 25, 50)
    if enemy.y > SCRN_SIZEY: enemy.y = 0
    enemy.move(1.5)
    if bulletExists:
        bullet.move(10)
        
        # test for collision of bullet and enemy
        if dist(bullet.x, bullet.y, enemy.x, enemy.y) < 50: 
            score += 1
            # print(score)
            enemy.y = 0
            bulletExists = False
            bgcolor = generateRandomColor()
    
        # test for collision of bullet and player
        if dist(enemy.x, enemy.y, mouseX-(247/2.5)/2, SCRN_SIZEY-200) < 50:
            lives -= 1
            enemy.y = 0
            bulletExists = False
    
def mouseClicked():
    global bulletExists 
    bulletExists = True
    global bullet
    bullet.x = mouseX-75/2
    bullet.y = SCRN_SIZEY-100
