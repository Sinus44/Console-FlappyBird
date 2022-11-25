# _Console Engine_
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)

## Classes
|[Classes](https://github.com/Sinus44/CE#classes)               |Description                                           |
|---------------------------------------------------------------|------------------------------------------------------|
|[Window](https://github.com/Sinus44/CE#class-window)           |Класс для рисования                                   |
|[Loop](https://github.com/Sinus44/CE#class-loop)               |Автоматический вызов функции за определенный интервал |
|[Engine](https://github.com/Sinus44/CE#class-engine)           |Различные фишки с консолью                            |
|[Keyboard](https://github.com/Sinus44/CE#class-keyboard)       |Обработка нажатий клавиатуры                          |
|[Vector](https://github.com/Sinus44/CE#class-vector)           |Двумерный вектор (пока что только точка)              |
|[Mmath](https://github.com/Sinus44/CE#class-mmath)             |Математические функции                                |
|[Performance](https://github.com/Sinus44/CE#class-performance) |Тесты производительности                              |
|[Color](https://github.com/Sinus44/CE#class-color)             |Цвет-коды для консоли                                 |
|[Sound](https://github.com/Sinus44/CE#class-sound)             |Работа со звуками                                     |
|[Logging](https://github.com/Sinus44/CE#class-logging)         |Логирование в файл                                    |

## Class Window
|Method                                                                                 |Description                                      |
|---------------------------------------------------------------------------------------|-------------------------------------------------|
|__init__()                                                                             |Метод конструктор                                |
|draw(fast=True)                                       									|Вывод изображения                 				  |
|clear(fast=True)                                   								    |Отчистка консоли								  |
|fill(symbol=" ")                                          								|Полностью заполняет буффер определенным символом |
|point(x=0, y=0, symbol="*")                                                            |Добавить 1 символ 								  |
|rectFill(x=0, y=0, w=1, h=1, symbol="*")                                               |Добавляет в буффер квадрат                       |
|circleFill(x=0, y=0, r=1, symbol="*")                                                  |Добавляет в буффер заполненный круг              |
|line(x1=0, y1=0, x2=0, y2=0, symbol="*")                                               |Добавляет в буффер линию                         |
|paste(frame, x=0, y=0)                                                                 |Вставляет в буффер окна окно                     |
|text(text="TEXT", x=0, y=0, color=Color.WHITE, backgroundColor=Color.Background.BLACK) |Отрисовка текста								  |

# Using exapmle
```python
w = 10 # Width = 30 symbols
h = 10 # height = 10 symbols
window = Window(w,h) # Create Window - object

window.rect(1,1,8,8) # Draw rect on (1,1) size of (8,8) 
window.draw() # Print image in console
```

## Class Loop
|Method     |Description       |
|-----------|------------------|
|__init__() |Метод конструктор |
|start()    |Запуск цикла      |
|stop()     |Остановка цикла   |

## Class Engine
|Method   |Description          |
|---------|---------------------|
|title()  |Установка имени окна |
|resize() |Остановка цикла      |

## Class Keyboard
|Method     |Description                   |
|-----------|------------------------------|
|init()     |Инициализация клавиатуры      |
|addBind()  |Создание действия при нажатии |

## Class Vector
|Method     |Description      |
|-----------|-----------------|
|__init__() |Создание вектора |

## Class Mmath
|Method  |Description                          |
|--------|-------------------------------------|
|round() |Правильное математическое округление |

## Class Performance
|Method  |Description                                      |
|--------|-------------------------------------------------|
|start() |Начинает отсчет времени                          |
|time()  |Возвращает время прошедшее с вызова метода start |

## Class Sound
|Method     |Description                |
|-----------|---------------------------|
|__init__() |Создание звука             |
|play()     |Воспроизвести звук         |
|stop()     |Остановить воспроизведение |

## Class Logging
|Method |Description                |
|-------|---------------------------|
|log()  |Добавить запись в файл-лог |

# Dependencies
* os
* time
* keyboard
* subprocess
* threading
* timeit
* pyaudio
* wave
* ctypes
* datetime

## License
![MIT](https://img.shields.io/badge/license-MIT%20License-green)
**Free Software, Hell Yeah!**
