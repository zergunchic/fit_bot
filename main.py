import os
import pip
import time

pip.main(['install', 'pytelegrambotapi'])
import telebot
from telebot import types

telegram_api_key = os.environ['TG_API']
bot = telebot.TeleBot(telegram_api_key)


@bot.message_handler(commands=['start'])
def start(message):
  #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  bot.send_photo(message.chat.id,
                 "https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
                 caption="""Привет! С тобой я, Люба Анохина.⁣⁣⠀
                  ⁣⁣⠀
Сейчас ты начнёшь проходить трехдневный воркшоп, который я создала для тебя.⁣⁣⠀
                  ⁣⁣⠀
Во время прохождения ты узнаешь:⁣⁣⠀
                  ⁣⁣⠀
✔️Что нужно для того, чтобы достичь цели;⁣⁣⠀
                  ⁣⁣⠀
✔️Как правильно построить свое питание;⁣⁣⠀
                  ⁣⁣⠀
✔️Как избегать срывов и откатов;⁣⁣⠀
                  ⁣⁣⠀
✔️Причины болей в спине и как от них⠀избавиться;⁣⁣⠀
                  ⁣⁣⠀
И многое другое…""")
  #,
  #               reply_markup=markup)

  button_bar = types.InlineKeyboardButton('Продолжить',
                                          callback_data='begin_expirience_1')
  keyboard = types.InlineKeyboardMarkup()
  keyboard.add(button_bar)
  #sleep 2 sec
  time.sleep(5)

  bot.send_message(message.from_user.id,
                   text="""Модуль 1:

Знакомство и мой путь.

Что нужно, чтобы достичь цели?

Чем опасны сильные дефициты в питании?

*ниже ссылка, она же здесь отобразится видео, видео не прикрепляем""",
                   reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == "begin_expirience_1":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                            callback_data='modul_1')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)
    #bot.answer_callback_query(call.id, "Добро пожаловать в мир тектоника")
    bot.send_message(
        call.message.chat.id,
        """После того, как ты пройдёшь воркшоп, тебя ждет СТРАТЕГИЧЕСКАЯ СЕССИЯ (созвон) лично со мной.⁣⁣⠀
⁣⁣⠀
В ходе неё, мы с полноценно разберем твою ситуацию, непонятные моменты и твои возможные ошибки. ⁣⁣⠀
⁣⁣⠀
А потом вместе доработаем детали твоего будущего плана по достижению желаемой цели.⁣⁣⠀
⁣⁣⠀
Попасть на стратегическую сессию можно, если ты:⁣⁣⠀
✔️прошла все модули,;⁣⁣⠀
✔️сделала это в течение 5 дней с момента начала воркшопа.""",
        reply_markup=keyboard)

  elif call.data == "modul_1":

    button_bar = types.InlineKeyboardButton('Продолжить',
                                            callback_data='modul_2')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)

    bot.send_video(
        call.message.chat.id,
        "http://techslides.com/demos/sample-videos/small.mp4",
        caption="""
Модуль 1:

Знакомство и мой путь.

Что нужно, чтобы достичь цели?

Чем опасны сильные дефициты в питании?

*ниже ссылка, она же здесь отобразится видео, видео не прикрепляем""",
        reply_markup=keyboard)
    #bot.send_message(call.message.chat.id, "This is a message")
  elif call.data == "modul_2":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                            callback_data='modul_3')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)

    bot.send_video(
        call.message.chat.id,
        "http://techslides.com/demos/sample-videos/small.mp4",
        reply_markup=keyboard)
  elif call.data == "modul_3":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                            callback_data='modul_4')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)

    bot.send_photo(call.message.chat.id,
                     "https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
                     caption="""
Твоя формула для расчетов Белков, Жиров и Углеводов:⁣⁣⠀
⁣⁣⠀
✔️Белок: 1.5-2 грамма на килограмм веса.⁣⁣⠀
Например: при весе 50 кг., мне нужно съедать 75-100 грамм белка в день.⁣⁣⠀
⁣⁣⠀
✔️Жиры: 1-1.5 грамм на килограмм веса.⁣⁣⠀
Например: при весе 50 кг., мне нужно съедать 50-75 грамм Жиров в день.⁣⁣⠀
⁣⁣⠀
✔️Углеводы: 2-4 грамм на килограмм веса.⁣⁣⠀
Например: при весе 50 кг., мне нужно съедать 100 грамм (если я хочу худеть), и 150-200 грамм в день, если я хочу набрать.""",
            reply_markup=keyboard)
  elif call.data == "modul_4":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                          callback_data='modul_5')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)
  
    bot.send_photo(call.message.chat.id,
       "https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
       caption="""
    Вариант тренировки, которую
я приготовила для тебя, к выполнению в зале.

Все упражнения в программе кликабельные - нажми на название упражнения и перейти по ссылке на видео

⁣⁣⠀

1. Сплит-приседания. 

• Вес: без веса, либо, в каждой руке по гантеле (2-6 кг каждая). 

• Повторения: по 15 раз на каждую ногу.

• Подходы: 3-4.

⁣⁣⠀
2. Отведение бедра в тренажере. 

⁣⁣⠀
• Вес: выставляем вес в промежутке с 25 до 30 кг.

• Повторения: 20-25.⁣⁣ 

• Подходы: 3.

⁣⁣⠀
3. Вертикальная тяга.⁣⁣⠀

• Вес: выставляем вес на тренажере примерно 12-19 кг.

• Повторения: 15.⁣⁣ 

• Подходы: 4.
⁣⁣⠀

⁣⁣⠀
4. Горизонтальная тяга. ⁣⁣⠀

• Вес: выставляем вес на тренажере 12-20 кг.

• Повторения: 15. ⁣

• Подходы: 4.⁣⁣⠀
⁣⁣⠀

⁣⁣⠀
5. Махи гантелями в стороны. 

• Вес: ⁣⁣гантели  по 2 кг. каждая. 

• Повторения: 15.⁣⁣ 

• Подходы: 4.⁣⁣⠀""",
    reply_markup=keyboard)
    
  elif call.data == "modul_5":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                          callback_data='modul_6')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)

    bot.send_photo(call.message.chat.id,
       "https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
       caption="""
    Вариант тренировки для выполнения дома:⁣⁣

Все упражнения в программе кликабельные - нажми на название упражнения и перейти по ссылке на видео

⁣⁣⠀
⁣⁣⠀
1. Сплит-приседания.

• Вес: без веса, либо, в каждой руке по гантеле (2-6 кг каждая). 

• Повторения: по 15 раз на каждую ногу.

• Подходы: 3-4.

⁣⁣⠀
⁣⁣⠀
2. Шаги в сторону с резинкой.⁣⁣⠀

• Время под нагрузкой:30-40 секунд. 

• Подходы: 3.⁣⁣⠀
⁣⁣⠀
⁣⁣⠀
⁣⁣⠀
3. Тяга гантелей в наклоне. ⁣⁣⠀

• Вес: гантели по 2-6 кг. каждая. 

• Повторения: 20-25.

Подходы: 4. ⁣⁣⠀
⁣⁣⠀

⁣⁣⠀
4. Махи гантелями в стороны. ⁣⁣⠀

• Вес: гантели по 2 кг. каждая. 

• Повторения: 15.⁣⁣⠀

• Подходы: 4.⁣⁣⠀⁣⁣⠀""",
    reply_markup=keyboard)
    
  elif call.data == "modul_6":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                          callback_data='modul_7')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)

    bot.send_photo(call.message.chat.id,
       "https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
       caption="""
    Я поздравляю тебя с прохождением двух модулей нашего воркшопа! ⁣⁣⠀
⁣⁣⠀
Впереди, третий и последний модуль.⁣⁣⠀
Не менее важный, и достаточно объемный.⁣⁣⠀
⁣⁣⠀
🙌Будь готова внимательно прослушать информацию, а также провести самодиагностику на наличие нарушений осанки. ⁣⁣⠀
⁣⁣⠀
А после прохождения этого модуля, я отправлю тебе памятку со своими рекомендациями в текстовом формате.""",
    reply_markup=keyboard)

  elif call.data == "modul_7":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                          callback_data='modul_8')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)

    bot.send_video(
      call.message.chat.id,
      "http://techslides.com/demos/sample-videos/small.mp4",
      reply_markup=keyboard)

  elif call.data == "modul_8":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                          callback_data='modul_9')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)

    bot.send_photo(call.message.chat.id,
       "https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
       caption="""
    Виды нарушений осанки. 
Ты можешь сфотографировать себя сбоку, и сравнить с этими картинками.""",
    reply_markup=keyboard)

  elif call.data == "modul_9":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                          callback_data='modul_10')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)
    
    bot.send_video(
      call.message.chat.id,
      "http://techslides.com/demos/sample-videos/small.mp4",
      reply_markup=keyboard)
  elif call.data == "modul_10":
      button_bar = types.InlineKeyboardButton('Продолжить',
                                            callback_data='modul_11')
      keyboard = types.InlineKeyboardMarkup()
      keyboard.add(button_bar)

      bot.send_photo(call.message.chat.id,
         "https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
         caption="""
      Ну что, как и обещала, высылаю краткие рекомендации по работе с различными нарушениями осанки. ⁣⁣⠀
⁣⁣⠀
✔️Шейный лордоз:⁣⁣⠀
- выполнять гимнастику на расслабление шейного отдела;⁣⁣⠀
- приобрести ортопедическую подушку;⁣⁣⠀
- учиться не перенапрягать шею во время упражнений на пресс, а также во время тренировок на верхнюю часть тела.⁣⁣⠀
⁣⁣⠀
✔️Грудной кифоз:⁣⁣⠀
- выполнять упражнения на раскрытие грудного отдела;⁣⁣⠀
- прокатывать зону грудного отдела позвоночника роллом;⁣⁣⠀
- обязательно добавлять в свои силовые тренировки упражнения на спину (с горизонтальными тягами в том числе).⁣⁣⠀
⁣⁣⠀
✔️Задний наклон таза:⁣⁣⠀
- растягивать и прокатывать заднюю поверхность бедра и ягодицы;⁣⁣⠀
- учиться правильно тренировать ягодичные мышцы.⁣⁣⠀
⁣⁣⠀
✔️Передний наклон таза:⁣⁣⠀
- расслаблять и разгружать поясничный отдел с помощью гимнастки для спины;⁣⁣⠀
- прокатывать и растягивать переднюю поверхность бедра;⁣⁣⠀
- укреплять ягодичные мышцы.⁣⁣⠀""",
      reply_markup=keyboard)
  elif call.data == "modul_11":
    button_bar = types.InlineKeyboardButton('Продолжить',
                                          callback_data='modul_12')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_bar)
    bot.send_message(call.message.chat.id,
       text="""
Хочу отметить, что все эти задачи мы закрываем в нашем закрытом женском клубе, а также на индивидуальном онлайн ведении.""",
       reply_markup=keyboard)
    
  elif call.data == "modul_12":

          bot.send_photo(call.message.chat.id,
             "https://images.unsplash.com/photo-1575936123452-b67c3203c357?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D",
             caption="""
          Благодарю тебя, за проделанную работу! 

На этом наш воркшоп завершен. Ты большая молодец! 

🎁 В конце воркшопа всем участникам я дарю стратегическую сессию лично со мной

Что это такое?

Это видеосозвон, в ходе которого, мы с полноценно разберем твою ситуацию, непонятные моменты и твои возможные ошибки

По результатам созвона я дам тебе полную стратегию и рекомендации

Также для участников воркшопа доступно онлайн-ведение по более выгодному тарифу, это также более подробно могу рассказать на стратегической сессии

Чтобы попасть на разбор, нужно заполнить Гугл-форму по ссылке ниже:
https://forms.gle/rSitYJJ5E5PcpEtc7

До встречи на стратегической сесии!

""")
  

bot.polling(none_stop=True, interval=0)
