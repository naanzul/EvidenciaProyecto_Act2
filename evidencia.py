from random import randrange, choice
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ["blue", "green", "yellow", "purple", "orange"] 

patch-1
snake_color = choice(colors)
food_color = choice([c for c in colors if c != snake_color])


main
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

# Nueva función para checar colisión solo con el cuerpo
def collides_with_body(head, snake):
    for segment in snake[:-1]:  # excluir la cabeza
        if head.x == segment.x and head.y == segment.y:
            return True
    return False

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
    

    if not inside(head) or collides_with_body(head, snake):
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Verificamos si la serpiente comió la comida
    if head == food:
        print('Snake:', len(snake))
        # Reubicar comida aleatoriamente
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Primer cambio: Mover la comida un paso al azar 
    dx = choice([-10, 0, 10])
    dy = choice([-10, 0, 10])

    new_x = food.x + dx
    new_y = food.y + dy

    if head != food:
        if -200 < new_x < 190:
            food.x = new_x
        if -200 < new_y < 190:
            food.y = new_y

    clear()

    # Aquí se dibuja la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)

patch-1
    square(food.x, food.y, 9, food_color)

    # Aquí dibujamos la comida
    square(food.x, food.y, 9, 'green')
main
    update()
    ontimer(move, 100)

# Esta es la configuración inicial de la ventana
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()


