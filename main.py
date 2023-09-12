import random
import arcade


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


#_______________________________snake_______________________________

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color = arcade.color.SAND
        self.change_x = 0 #jahat harkat
        self.change_y = 0 #jahat harkat
        self.score = 0
        self.center_x = SCREEN_WIDTH//2 #mokhtasat
        self.center_y = SCREEN_HEIGHT//2 #mokhtasat
        self.speed = 2
        self.body =[] #badan mar

    def move(self):

        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
                
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        
        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y

    def eat(self):
        self.score += 1
        self.body.append([self.center_x,self.center_y])
    
    def pp(self):
        self.score -= 1

    def draw(self): 
        arcade.draw_rectangle_filled(self.center_x , self.center_y , self.width , self.height , self.color)

        for i in range(len(self.body)):
            arcade.draw_rectangle_filled(self.body[i][0] , self.body[i][1] , self.width , self.height , self.color)

#_______________________________apple_______________________________

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 10
        self.color = arcade.color.RED
        self.center_x = random.randint (0 , SCREEN_WIDTH) #mokhtasat
        self.center_y = random.randint (0 , SCREEN_HEIGHT) #mokhtasat
        self.r = 8
    
    def draw(self): 
        arcade.draw_circle_filled(self.center_x , self.center_y , self.r , self.color )



#_______________________________golabi_______________________________

class Golabi(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 10
        self.color = arcade.color.YELLOW
        self.center_x = random.randint (0 , SCREEN_WIDTH) #mokhtasat
        self.center_y = random.randint (0 , SCREEN_HEIGHT) #mokhtasat
        self.r = 8
    
    def draw(self): 
        arcade.draw_circle_filled(self.center_x , self.center_y , self.r , self.color )





#_______________________________poop_______________________________

class Poop(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 10
        self.color = arcade.color.BLACK
        self.center_x = random.randint (0 , SCREEN_WIDTH) #mokhtasat
        self.center_y = random.randint (0 , SCREEN_HEIGHT) #mokhtasat
        self.r = 8
    
    def draw(self): 
        arcade.draw_circle_filled(self.center_x , self.center_y , self.r , self.color )

    



#_______________________________game_______________________________


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH , SCREEN_HEIGHT , title='Snake Game')
        arcade.set_background_color(arcade.color.DARK_OLIVE_GREEN)
        self.snake = Snake()
        self.apple = Apple()
        self.golabi = Golabi()
        self.poop = Poop()
        self.game_over_flag = False

    def on_draw(self): # rasm abject haye tasvir
        arcade.start_render() #neshon dad
        self.snake.draw()
        self.apple.draw()
        self.golabi.draw()
        self.poop.draw()
        score_text = f"Score: {self.snake.score}"
        arcade.draw_text(score_text , 10 , 10 , arcade.color.WHITE, 14)

    def on_update(self , delta_time: float): #tamam mantaq bazi
        if not self.game_over_flag :
            self.snake.move()

            if arcade.check_for_collision(self.snake , self.apple): #barkhord sib va mar
                self.snake.eat()
                self.apple = Apple() #sib jadid

            elif arcade.check_for_collision(self.snake , self.golabi): #barkhord golabi va mar
                self.snake.eat()
                self.snake.eat()
                self.golabi = Golabi() #golabi jadid

            elif arcade.check_for_collision(self.snake , self.poop): #barkhord poop va mar
                self.snake.pp()
                self.poop = Poop() #poop jadid 
                if(self.snake.score>0):
                    self.snake.body.pop(-1)

            if (self.snake.center_x < 0) or (self.snake.center_x > SCREEN_WIDTH) or (self.snake.center_y < 0) or (self.snake.center_y > SCREEN_HEIGHT) or (self.snake.score < 0): 
                    self.snake.score = -1
                    self.game_over()

    def game_over(self):
        self.game_over_flag = True
        arcade.draw_text("Game Over!", 50, 250, arcade.color.RED, 70)
        arcade.finish_render()
        arcade.pause(5)  # توقف بازی به مدت 5 ثانیه
        arcade.close_window()  # بستن پنجره بازی

    def on_key_release(self , key: int , modifiers: int):
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y =-1




my_game = Game()

arcade.run() #barname baste nashe