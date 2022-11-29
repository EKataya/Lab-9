import random
import logging

# Работаем с логированием
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)

# Создаем файл для логирования
file_handler = logging.FileHandler("log.log")
# Создаем форматер, отображающий дату, время, имя логгера, уровень и сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


#Диалог с пользователем 
name=input('Введите свое имя:')
print('Привет,', name, 'Давай поиграем в игру. Я загадаю число, попробуй его отгадать!')


while True:
    logger.info('program started')
    try:
        n=int(input('Какое максимальное число я могу тебе загадать? '))
        assert n > 1 
        logger.info('n={}'.format(n))
        break
       
    except ValueError:
        print('Данные введены неверно, попробуй еще раз')
        logger.error('Incorrect value')    
    except AssertionError:
        print('Число должно быть больше 1')
        logger.error('Incorrect value.')

while True:
     logger.info('program started')
     try:
         k=int(input('Какое количество попыток я могу тебе дать?'))
         assert k > 0
         logger.info('k={}'.format(k))
         break

     except ValueError:
         print('Данные введены неверно, попробуй еще раз')
         logger.error('Incorrect value')
     except AssertionError:
         print('Число должно быть больше 0.')
         logger.error('Incorrect value.')
     
rand=random.randint(1,n)
logger.info('rand={}')

while k > 0:
    print('Твое количество попыток - {}'.format(k))
    try:
        ans = int(input('Попробуй отгадать число:   '))
        logger.info('input ans = {}'.format(ans))
        assert 1 <= ans <= n
        logger.info('suitable')
        if ans == rand:
            print('Поздравляю, ты выиграл!\n')
            logger.info('right answer')
            break
        else:
            k -= 1
            print('Ты проиграл!:(')
            logger.info('цкщтп фтыцук')
            if ans < rand:
                print('Число {} меньше загаданного'.format(ans))
            else:
                print('Число {} больше загаданного'.format(ans))
            if k == 0:
                print('Попытки закончились:(\n')
                logger.info('no attemps')
    except AssertionError:
        print('Число не в диапазоне'.format(n))
        logger.error('incorrect value')
    except ValueError:
        print('Ошибка ввода, попробуйте ещё раз')
        logger.error('incorrect value')
logger.info('progrram done')

                    
  
                    
                
                    
                
                 
                
           




    
         


