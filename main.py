import asyncio
from telegram.ext import CommandHandler, MessageHandler, Application, CallbackContext, filters
from telegram import Update, ReplyKeyboardMarkup, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton





application = Application.builder().token(Token).build()


async def start(update: Update, context: CallbackContext):
    message = """
<b>Добро пожаловать в наш техцентр, где ваш грузовик в надежных руках! 🚛</b>  
Мы заботимся о каждом автомобиле, ведь для нас важен <strong>каждый километр</strong> вашего пути. Наши эксперты всегда готовы обеспечить качественное обслуживание и ремонт для вашего надежного спутника на дороге.🔧👨‍🔧  
<b>Обслуживание вашего грузовика в нашем сервисе — это всегда качественно и своевременно ⏱️</b>
"""

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message, parse_mode="HTML"
    )

   
    await asyncio.sleep(3)

    custom_keybord = [
        ['🛠️ Услуги', '💸 Выкуп'],
        ['🤝 Наши партнёры', '📜 Сертификаты'],
        ['💲 Прайс-лист', '📞 Контакты'],
    ]

    
    reply_keybord = ReplyKeyboardMarkup(custom_keybord, resize_keyboard=True, one_time_keyboard=True)

    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Для удобства выберите одну из категорий на клавиатуре, и мы предоставим вам всю нужную информацию о наших услугах и компании!',
        reply_markup=reply_keybord
    )


async def handler_services(update: Update, context: CallbackContext):
    text = update.message.text

    if text == '🛠️ Услуги':
        custom_keybord = [
            ['🔧 ТО и регламентное обслуживание грузовых автомобилей и полуприцепов'],
            ['⚙️ Слесарный Цех'],
            ['🚗 Ремонт ходовой'],
            ['💻 Компьютерная диагностика'],
            ['🔌 Ремонт электрооборудования'],
            ['🚛 Ремонт полуприцепов'],
            ['⬅️ Назад']
        ]

        reply_keybord = ReplyKeyboardMarkup(custom_keybord, resize_keyboard=True, one_time_keyboard=True)

        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Мы предоставим полную информацию по данным услугам',
            reply_markup=reply_keybord
        )

    elif text == '🔧 ТО и регламентное обслуживание грузовых автомобилей и полуприцепов':
        maintenance = """
1️⃣ ТО грузовых автомобилей  
🛠️ ТО1 — Регламентное обслуживание для поддержания надежности вашего грузовика.  
🔧 ТО2 — Расширенное обслуживание с учетом всех технических нюансов и диагностики.  
📸 Фото: ТО грузовых автомобилей  

2️⃣ ТО прицепной техники  
🚚 ТО1 — Обслуживание прицепов для безопасной эксплуатации.  
🔩 ТО2 — Комплексное ТО для прицепной техники, включая диагностику и профилактику.  
📸 Фото: ТО прицепной техники  

3️⃣ Профилактические работы  
🛠️ Профилактическое обслуживание для предотвращения поломок и продления срока службы транспортного средства.  
📸 Фото: Профилактика автомобилей  

4️⃣ Сезонные работы  
❄️ Зимнее ТО — Подготовка к холодному сезону: проверка отопителей, тормозных систем и аккумулятора.  
🌞 Летнее ТО — Обслуживание для летних условий: проверка кондиционеров, подвески и охлаждающей системы.  
📸 Фото: Сезонное обслуживание
"""

        
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo='img/mechanical-engineering.jpg',  # Замените на путь к изображению или URL
            caption=maintenance,
            parse_mode="HTML"
        )

    elif text == '⚙️ Слесарный Цех':
        metalworkingShop_part1 = '''
1️⃣ Ремонт двигателей  
🔧 Ремонт и восстановление работы двигателей для обеспечения долгосрочной службы и надежности.  
📸 Фото: Ремонт двигателей

2️⃣ Ремонт топливных систем  
⛽ Профессиональный ремонт топливных систем для обеспечения бесперебойной работы и эффективности двигателя.  
📸 Фото: Ремонт топливных систем

3️⃣ Ремонт КПП, редукторов, ГУР  
🔧 Обслуживание и ремонт коробок передач, редукторов и гидроусилителей руля для точности и надежности работы.  
📸 Фото: Ремонт КПП и редукторов

4️⃣ Ремонт ходовой  
🚗 Восстановление и замена деталей ходовой части для плавного и безопасного движения.  
📸 Фото: Ремонт ходовой

5️⃣ Ремонт суппортов и тормозных механизмов  
🛠️ Замена и ремонт тормозных систем для безопасности вашего транспортного средства.  
📸 Фото: Ремонт тормозных механизмов
'''

        metalworkingShop_part2 = '''
6️⃣ Ремонт пневматических систем  
💨 Обслуживание и ремонт пневматических систем для надежной работы тормозов и других систем.  
📸 Фото: Ремонт пневматических систем

7️⃣ Ремонт гидравлических систем  
💧 Профессиональный ремонт гидравлических систем для обеспечения работы грузовиков и прицепов.  
📸 Фото: Ремонт гидравлических систем

8️⃣ Регулировка схождения/соосности  
🔧 Регулировка углов схождения и соосности для оптимальной работы подвески и колес.  
📸 Фото: Регулировка схождения

9️⃣ Слесарные работы  
🛠️ Широкий спектр слесарных работ для восстановления и улучшения деталей и систем вашего автомобиля.  
📸 Фото: Слесарные работы

🔟 Ремонт автономных отопителей  
🔥 Ремонт и настройка автономных отопителей для комфортной работы в холодное время года.  
📸 Фото: Ремонт отопителей

1️⃣1️⃣ Замена лобовых стекол автомобилей  
🛠️ Замена стекол с гарантией качества и безопасности.  
📸 Фото: Замена лобовых стекол
'''

        
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo='img/metalworking.jpg',  # Замените на путь к изображению или URL
            caption=metalworkingShop_part1,
            parse_mode="HTML"
        )

        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=metalworkingShop_part2,
            parse_mode="HTML"
        )

    elif text == '🚗 Ремонт ходовой':
        ChassisRepair = '''
1️⃣ Диагностика ходовой и подвески  
🔧 Полная диагностика ходовой части и подвески для обеспечения безопасности и комфорта на дороге.  
📸 Фото: Диагностика ходовой и подвески

2️⃣ Проверка и измерение люфтов  
🔍 Тщательная проверка на наличие люфтов в подвеске, для выявления ранних признаков износа и предотвращения поломок.  
📸 Фото: Проверка люфтов

3️⃣ Проверка и регулировка схождения/соосности  
⚙️ Точная регулировка углов схождения и соосности для уменьшения износа шин и улучшения управляемости.  
📸 Фото: Регулировка схождения

4️⃣ Замена сайлентблоков и втулок  
🔩 Замена изношенных сайлентблоков и втулок для уменьшения вибраций и улучшения плавности хода.  
📸 Фото: Замена сайлентблоков

5️⃣ Замена пневморессор  
💨 Замена пневморессор для обеспечения комфортной работы подвески и правильной амортизации груза.  
📸 Фото: Замена пневморессор

6️⃣ Замена стоек стабилизаторов  
⚖️ Замена стоек стабилизаторов для улучшения стабильности на поворотах и предотвращения кренов.  
📸 Фото: Замена стоек стабилизаторов
'''

        
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo='img/chassisrepair.jpg', 
            caption=ChassisRepair,
            parse_mode="HTML"
        )


    elif text == '💻 Компьютерная диагностика':
        diagnostic_services_part1 = '''
1️⃣ 🖥️ Диагностика Volvo  
🔧 Использование системы VTT/VTT2 для диагностики и устранения неисправностей на грузовиках Volvo.  
📸 Фото: Диагностика Volvo

2️⃣ 🖥️ Диагностика Renault  
🔧 Диагностика с использованием системы Renault Diag (RTT) для точного определения проблем в автомобилях Renault.  
📸 Фото: Диагностика Renault

3️⃣ 🖥️ Диагностика Mercedes-Benz  
🔧 Использование системы Xentry Diagnostics (SPconnect) для диагностики автомобилей Mercedes-Benz.  
📸 Фото: Диагностика Mercedes-Benz

4️⃣ 🖥️ Диагностика MAN  
🔧 Диагностика с использованием MAN Cats 2 для точного выявления неисправностей в автомобилях MAN.  
📸 Фото: Диагностика MAN

5️⃣ 🖥️ Диагностика DAF  
🔧 Использование системы DAVIE для диагностики автомобилей DAF и устранения неисправностей.  
📸 Фото: Диагностика DAF
'''

        diagnostic_services_part2 = '''
6️⃣ 🖥️ Диагностика Iveco  
🔧 Диагностика с использованием системы EASy Diag (ECTRAC) для обеспечения точности и надежности.  
📸 Фото: Диагностика Iveco

7️⃣ 🖥️ Диагностика Scania  
🔧 Использование системы SDP3 для диагностики автомобилей Scania и устранения возможных проблем.  
📸 Фото: Диагностика Scania

8️⃣ 🖥️ Диагностика Wabco; Knorr-Bremse; Haldex  
🔧 Диагностика систем тормозов и пневматики с использованием проверенных решений Wabco, Knorr-Bremse, Haldex.  
📸 Фото: Диагностика тормозных систем

9️⃣ 🖥️ Диагностика электронной системы автомобиля  
🔧 Диагностика всех электронных компонентов для выявления неисправностей.  
📸 Фото: Диагностика электронных систем
'''

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo='img/computer-diagnostics.jpg',
            caption=diagnostic_services_part1,
            parse_mode="HTML"
        )

        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=diagnostic_services_part2,
            parse_mode="HTML"
        )

    elif text == '🔌 Ремонт электрооборудования': 
        electrical_equipment_repair = '''
1️⃣ ⚡️ Электротехнические работы на грузовых автомобилях и прицепах  
🔧 Профессиональные электротехнические работы для грузовых автомобилей и прицепов.  
📸 Фото: Электротехнические работы

2️⃣ 🔧 Ремонт и установка дополнительного оборудования  
🔌 Установка и ремонт электроприборов, включая дополнительное оборудование для грузовиков.  
📸 Фото: Установка дополнительного оборудования

3️⃣ 🌡 Ремонт и установка автономных отопителей (Webasto, Eberspacher)  
🔧 Ремонт и установка автономных отопителей для обеспечения комфортной температуры в холодное время года.  
📸 Фото: Установка отопителей

4️⃣ 💡 Восстановление электронных блоков  
🔧 Восстановление электронных блоков для обеспечения стабильной работы электрооборудования.  
📸 Фото: Восстановление блоков

5️⃣ 👨‍🔧 Квалифицированный персонал  
🔧 Работы выполняются высококвалифицированными специалистами с большим опытом работы.  
📸 Фото: Квалифицированный персонал
'''
        

        
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo='img/electrical.jpg',
            caption=electrical_equipment_repair,
            parse_mode="HTML"
        )
        
        
    elif text == '🚛 Ремонт полуприцепов':
        semitrailerpart1 = '''
1️⃣ ⚙️ Ремонт полуприцепов и прицепного оборудования  
🔧 Профессиональный ремонт самосвальных полуприцепов и прицепов различных марок: Grunwald, Koegel, Krone, SCHMITZ, Wielton.  
📸 Фото: Ремонт полуприцепов

2️⃣ 🛠 Ремонт осей полуприцепов  
🔧 Комплексный ремонт и восстановление осей полуприцепов для обеспечения их надежной работы.  
📸 Фото: Ремонт осей

3️⃣ 🚗 Ремонт гидробортов  
🔧 Выполнение всех видов ремонта гидробортов для грузовиков и прицепов.  
📸 Фото: Ремонт гидроборта

4️⃣ ⚡️ Диагностика электрооборудования (ABS, EBS)  
🔧 Профессиональная диагностика и настройка электрооборудования, включая системы ABS и EBS, для улучшения безопасности на дороге.  
📸 Фото: Диагностика электрооборудования
'''

        semitrailerpart2 = '''
5️⃣ 🔩 Ремонт пневматических систем  
🔧 Ремонт пневматических систем от ведущих производителей Wabco, Knorr-Bremse, Haldex.  
📸 Фото: Ремонт пневматических систем

6️⃣ 🚚 Ремонт тормозных систем  
🔧 Наклёпка накладок, замена колодок, восстановление тормозных валов, замена ремкомплектов.  
📸 Фото: Ремонт тормозных систем

7️⃣ 🛠 Капитальный ремонт суппортов  
🔧 Полный капитальный ремонт суппортов для обеспечения долговечности тормозной системы.  
📸 Фото: Капитальный ремонт суппортов

8️⃣ 🔧 Замена подшипников и сайлентблоков  
🔧 Замена подшипников и сайлентблоков для восстановления устойчивости и комфорта работы техники.  
📸 Фото: Замена подшипников

9️⃣ 🔥 Сварочные работы  
🔧 Качественные сварочные работы для ремонта и восстановления конструкций различных типов.  
📸 Фото: Сварочные работы
'''

        
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo='img/semitrailerrepair.jpg',
            caption=semitrailerpart1,
            parse_mode="HTML"
        )

        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=semitrailerpart2,
            parse_mode="HTML"
        )

    elif text == '⬅️ Назад':
        custom_keybord = [
            ['🛠️ Услуги', '💸 Выкуп'],
            ['🤝 Наши партнёры', '📜 Сертификаты'],
            ['💲 Прайс-лист', '📞 Контакты'],
        ]

        reply_keybord = ReplyKeyboardMarkup(custom_keybord, resize_keyboard=True, one_time_keyboard=True)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Для удобства выберите одну из категорий на клавиатуре, и мы предоставим вам всю нужную информацию о наших услугах и компании!',
            reply_markup=reply_keybord
        )

    elif text == '💸 Выкуп':
        ransom_caption = """
🌟 <b>Выкуп техники — быстро и удобно!</b> 🌟

Продажа техники самостоятельно — <b>много времени и усилий</b>, отвлекая вас от важной работы. Больше не нужно тратить дни на демонстрацию! Мы готовы <b>выкупить вашу технику</b> прямо сейчас по <b>справедливой рыночной цене</b>! 💰

📝 <b>Быстрая оценка и осмотр</b>  
Мы грамотно <b>оценим ваше оборудование</b>, проведём <b>осмотр</b> и предложим честную цену. Всё это займёт <b>минимум вашего времени</b>.

🛋 <b>Комфортное ожидание</b>  
Во время осмотра вы сможете <b>отдохнуть</b> в уютной зоне, не беспокоясь о процессе.

🚗 Дайте нам свою технику — а мы позаботимся обо всём остальном!
"""
        traidin_caption = """
🚗 <b>Трейд ИН — быстро, выгодно и удобно!</b> 🚗

Вы хотите не просто <b>продать</b>, но ещё и <b>купить новую технику</b>? Мы готовы предложить <b>комплексное решение</b> по схеме <b>Трейд Ин</b>. Всё это <b>быстро</b>, <b>выгодно</b> и <b>удобно</b>! 

🔧 За один день вы уже уедете на новом <b>полуприцепе</b> от ведущих <b>европейских производителей</b> в своём сегменте. 🌍

💼 <b>Продажа и покупка техники</b> в одном пакете — это идеальный выбор для вашего бизнеса!
"""
        sales_platform_caption = """
💼 <b>Продажа через площадку — комиссия</b> 💸

Если по каким-то причинам нам не удалось с вами договориться о выкупе техники, мы готовы предложить <b>продажу через нашу стоянку</b>. Доверив команде профессионалов свой любимый грузовик, вы всегда можете быть уверены, что с ним <b>ничего не случится</b> на нашей <b>24/7 охраняемой стоянке</b> 🛡️.

🛠️ <b>Техника всегда будет готова к показу</b> как в <b>летнее</b>, так и в <b>зимнее время</b> 🌞❄️. На территории техцентра есть <b>мойка</b> 🚿 и возможность оперативно исправить любую неполадку, препятствующую оперативной продаже.

💼 <b>Продажа с нашей помощью для вас</b> <b>абсолютно бесплатна</b>!
"""

        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=ransom_caption, parse_mode="HTML")
        
        await asyncio.sleep(4)

        await context.bot.send_message(chat_id=update.effective_chat.id, text=traidin_caption, parse_mode="HTML")

        await asyncio.sleep(5)

        await context.bot.send_message(chat_id=update.effective_chat.id, text=sales_platform_caption, parse_mode="HTML")

        await context.bot.send_message(chat_id=update.effective_chat.id, text='<b>Мы экономим Ваши силы и нервы. Приезжайте в наш техцентр.</b>', parse_mode="HTML")

    elif text == '🤝 Наши партнёры':
        media=[
            InputMediaPhoto(open('img/hyva.jpg','rb')),
            InputMediaPhoto(open('img/wabco.jpg','rb')),
            InputMediaPhoto(open('img/bpw.jpg','rb')),
            InputMediaPhoto(open('img/binotto.jpg','rb')),
            InputMediaPhoto(open('img/jmkipper.jpg','rb')),
            InputMediaPhoto(open('img/gazprom.jpg','rb')),
            InputMediaPhoto(open('img/dongfeng.jpg','rb')),
            InputMediaPhoto(open('img/faw.jpg','rb')),
            InputMediaPhoto(open('img/sitrak.jpg','rb')),
            InputMediaPhoto(open('img/chengloong.jpg','rb')),
            InputMediaPhoto(open('img/tonar.jpg','rb')),
            InputMediaPhoto(open('img/wielton.jpg','rb')),
    ]
        
        group1 = media[:6]
        group2 = media[6:]

        await context.bot.send_media_group(chat_id=update.effective_chat.id, media=group1)
        await context.bot.send_media_group(chat_id=update.effective_chat.id, media=group2)


    elif text == '💲 Прайс-лист':   
        price_list_caption = """
    💰 <b>Прайс-лист на основные услуги</b> 🔧

    🛠️ Слесарные работы — <b>2 500 ₽</b>
    🛠️ Слесарные работы (со своими запчастями) — <b>3 000 ₽</b>

    ⚡ Работа автоэлектрика — <b>2 800 ₽</b>
    ⚡ Работа автоэлектрика (со своими запчастями) — <b>3 500 ₽</b>
    """
        await context.bot.send_message(chat_id=update.effective_chat.id,     text=price_list_caption, parse_mode="HTML")


    elif text ==  '📞 Контакты':
        description = """ 
<b>СВЯЖИТЕСЬ С НАМИ — МЫ ВСЕГДА НА СВЯЗИ!</b> 📞

Наша команда всегда готова помочь вам с <b>любым вопросами</b> и <b>уточнениями</b>. Мы ценим ваше время ⏳ и стремимся предоставить вам <b>точную</b> и <b>оперативную информацию</b>. ✅

<b>Позвоните нам</b>, и мы с радостью ответим на все ваши вопросы. 📱 У нас есть <b>специалисты</b> по <b>продажам</b>, <b>сервису</b> и <b>запчастям</b>, которые всегда готовы оказать необходимую помощь. 🛠️

<b>Свяжитесь с нами прямо сейчас</b>, и мы сделаем все, чтобы ваш опыт с нами был максимально <b>удобным и результативным</b>. 🌟
"""
        await context.bot.send_message(chat_id=update.effective_chat.id,text=description, 
        parse_mode="HTML")

        await asyncio.sleep(3)


        numbers = '''
📞 <b>ОБЩИЙ</b>:      +74951428194

💼 <b>ПРОДАЖИ</b>:    +79015003343

🔧 <b>Cервис</b>:     +79775453344

🔩  <b>ОТДЕЛ ЗАПЧАСТЕЙ</b>: +79915948006
'''


        await context.bot.send_message(chat_id=update.effective_chat.id,text=numbers, 
        parse_mode="HTML")

        await asyncio.sleep(4)
       
        yandex_map_url = "https://yandex.com.ge/maps/-/CHqRMVk2"
        await update.message.reply_text(f'<a href="{yandex_map_url}"><b>📍Московская область, городской округ Чехов, территориальный отдел Баранцевский, точка на карте 55.135484, 37.516621🗺️</b></a>', parse_mode='HTML')

        await asyncio.sleep(5)

          
        keyboard = [
        [InlineKeyboardButton(text="Наш сайт 🌐", url='https://kts77.ru/')],
        [InlineKeyboardButton(text="Напишите нам на почту 💌", url='https://mail.yandex.ru/compose?to=info@kts77.ru')],
        #[InlineKeyboardButton(text="Позвоните нам", url='tel:+7999999999')]
        #telegram.error.BadRequest: Inline keyboard button url 'tel:+7999999999' is invalid: wrong port number specified in the url
        ]



        description_end = '''
Посетите наш <b>сайт</b> 🌐 или напишите нам на <b>почту</b> 💌 — мы всегда готовы предложить вам <b>лучшие решения</b> 💡!
'''

        markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=description_end, reply_markup=markup, parse_mode="HTML")



button_handler = CommandHandler('start', start)
application.add_handler(button_handler)
handler_button_message = MessageHandler(filters.TEXT & ~filters.COMMAND, handler_services)
application.add_handler(handler_button_message)
application.run_polling()
