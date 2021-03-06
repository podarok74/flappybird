import pygame, sys, random
width = 288
height = 450
def create_plat(screen, platform, plat_pos):
    """Функция, которая отвечает за создание двух платформ друг за другом
     :param screen: экран
     :param platform: платформа
     :param plat_pos: позиция плтаформы
    """
    screen.blit(platform,(plat_pos,height))
    screen.blit(platform,(plat_pos + width,height))
def create_colone(colone_height, colone):
    """Создаем функцию, которая будет отвечать за создание прямоугольников по контору колон сверху(up colone) и снизу (down_colone) со случайной высотой по центру экрана(внизу или вверху)
    :param colone_height: высота колоны
    :param colone: колонна
    """
    try:
        random_colone = random.choice(colone_height) #выбирает случайную высоту колон
        down_colone = colone.get_rect(midtop = (400,random_colone))
        up_colone = colone.get_rect(midbottom = (400,random_colone - 150))
        return down_colone,up_colone
    except TypeError:
        return None, 'TypeError'
    except AttributeError:
        return None, 'AttributeError'
    except IndexError:
        return None, 'IndexError'

def colone_move(colones):
    """Функция,которая будет отвечать за перемещение прямоугольников по контору колон влево
    :param colones: колоны
    :return: наши колоны
    """
    for colone in colones:
        colone.centerx -= 2.5
    return colones    

def draw_colones(colones, screen, colone):
    """Функция, которая отвечает за вывод колон на экран, при этом проверяется где находится колона. В случае если она находится вверху - она переворачивается на 360 градусов 
    """
    for colon in colones:
        if colon.bottom >= 512:
            screen.blit(colone,colon)
        else:
            flip_pipe = pygame.transform.flip(colone, False, True)
            screen.blit(flip_pipe,colon)

def check_collision(colones, b_rect):
    """ Функция, которая проверяет не сталкивается ли прямоугольник сделанный вокруг птицы с прямоугольников вокруг трубы, а также выходим ли мы за пределы экрана в обоих случаях устанавливаем flag - false
    :param b_rect: прямоугольник вокруг птицы
    """
    for pipe in colones:
        if b_rect.colliderect(pipe):
            return False
    if b_rect.top <= -50 or b_rect.bottom >= 450:
        return False
    return True
         
def rotate_bird(bird, speed):
    """Пишем функцию,которая будет вращать нашу птичку взависимости от направления полета
    :param speed: скорость
    :param bird: птица
    """ 
    new_bird = pygame.transform.rotozoom(bird,-speed * 3,1)
    return new_bird

def score_display(game_state, game_font, score, high_score, screen):
    """ Пишем функцию для подсчета очков
    :param game_state: статус игры
    :param score: текущий счет
    :param high_score: наибольший счет
    """
    if game_state == 'main_game':
        score_surface = game_font.render(f'Time in flight:{int(score)} ', True, (255,255,255))
        score_rect = score_surface.get_rect(center = (144,50))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'High time in flight :{int(high_score)} ', True, (255,255,255))
        score_rect = score_surface.get_rect(center = (144,425))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(str(int(high_score)), True, (255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (144,50))
        screen.blit(high_score_surface, high_score_rect)
 
def update_score(score, high_score):
    """ Пишем функцию для подсчета текущего счета в игре и максимального за период игры
    :param score: текущий счет
    :param high_score: наибольший счет
    """ 
    if score > high_score:
        high_score = score
    return high_score        

def main():
    pygame.init()
    #Задаем размер нашего экрана, путем подбора останавливаемся на 288х512,частоту кадров а также шрифт и его размер
    
    screen = pygame.display.set_mode((288,512))
    clock = pygame.time.Clock()
    game_font = pygame.font.SysFont('microsoftttaile',40)

    #Заранее заданные параметры для нашей игры, устанавливаем статус игры True и значения для счета
    
    gravity = 0.25
    speed = 0
    status = True
    score = 0
    high_score = 0

    #загрузка необходимых фото для игры
    
    fone = pygame.image.load('assets/fone.png').convert()

    platform = pygame.image.load('assets/platform.png').convert()
    plat_pos = 0

    bird = pygame.image.load('assets/bird.png').convert_alpha()
    b_rect = bird.get_rect(center = (50,256))

    colone = pygame.image.load('assets/colone.png').convert()

    colone_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE,1200) # Устанавливаем таймер для появления колон в 1200 милисекунд
    #Список с длинной колон, откуда будет брать модуль random
    colone_height = [200,300,400]
    welcome = pygame.image.load('assets/welcome.png').convert_alpha()
    welcome_rect = welcome.get_rect(center = (144,256))

    # Основной цикл игры, в котором используем sys для выхода из игры, обнуляем наши параметры в случае начала новой игры,а также программируем пробел для управления птицой и начала новой игры в случае проигрыша
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # устанавливаем пробел для уапрвления птицей
                if event.key == pygame.K_SPACE and status:
                    speed = 0
                    speed -= 6
                # Перезапускаем игру в случае если произошло столкновение и обнуляем параметры для коректной работы игры
                if event.key == pygame.K_SPACE and status == False:
                    status = True
                    colone_list.clear()
                    b_rect.center =(50,256)
                    speed = 0
                    score = 0
            if event.type == SPAWNPIPE:
                colone_list.extend(create_colone(colone_height, colone))

        screen.blit(fone,(0,0)) # Выводим наш фон на экран, указывая координата (0,0) т.к совпадает с размерами нашего игрового поля
        
        if status: # в случае true

        #Полет птицы
            speed += gravity
            rotated_bird = rotate_bird(bird, speed)
            b_rect.centery += speed
            screen.blit(rotated_bird,b_rect) # Сама птица и прямоугольник,созданный вокруг неё
            status = check_collision(colone_list, b_rect)

        #Столбы
            colone_list = colone_move(colone_list)
            draw_colones(colone_list, screen, colone)

            score += 0.01
            score_display('main_game', game_font, score, high_score, screen)
        else:
            screen.blit(welcome, welcome_rect) # Выводим на экран приветствие 
            high_score = update_score(score, high_score)
            score_display('game_over', game_font, score, high_score, screen)    
        
        #Выполняем движение платформы на -1 влево, а также когда платформа находится слишком далеко сбрасываем значение до 0,что позволяет нам видеть бесконечно движущуюся платформу
        plat_pos -= 1
        create_plat(screen, platform, plat_pos)
        if plat_pos <= -288:
            plat_pos = 0


        pygame.display.update()
        clock.tick(120)

if __name__ == '__main__':
    main()