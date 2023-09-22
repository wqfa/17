
#This bot is developed by Hamoudi AL-Amir 𓅂
#Developer Channel | @MMMFi ✓.

from kvsqlite.sync import Client
import telebot 
from telebot.types import InlineKeyboardButton as but , InlineKeyboardMarkup as key
db = Client('Sq.sqlite')
onwer = int('5191376406') #ID
if not db.get('db'):
    data = {'onwer':[],'admin': [], 'users': [] , 'band':[], 'status': 1}
    db.set('db',data)
if not onwer in db.get('db')['onwer']:
    data = db.get('db')
    data['onwer'].append(onwer)
    db.set('db',data)
bot = telebot.TeleBot('XXX') #TOKEN
@bot.message_handler(commands = ['start'])
def staty(m):
 status = db.get("status")
 channel = db.get("channel")
 userg = len(db.get('db')['users'])
 for i in db.get('db')['onwer']:
     pass
 print(channel)
 data = db.get('db')
 user_id = m.from_user.id
 if user_id in data['band']:
     bot.send_message(m.chat.id,'تم حظرك من البوت 🚫')
 if data['status'] == 2:
     pass
 else:
     if not user_id in data['users']:
         data = db.get('db')
         data['users'].append(user_id)
         db.set('db',data)
         sug = len(db.get("db")["users"])
         text = f' مرحبا بك في البوت\n\nID : {user_id}\nNAME : {m.from_user.first_name}\nUSER : {m.from_user.username}\n\nعدد الاعضاء :{sug}'
         if len(db.get("db")['admin']) > 0:
             for x in data['admin']:
                 print(x)
                 bot.send_message(int(x),text)
             bot.send_message(int(i),text)
         bot.send_message(int(i),text)
 if not db.get('channel'):
     if user_id in data['onwer'] or user_id in data['admin']:
         bot.send_message(m.chat.id,'''This bot is developed by Hamoudi AL-Amir 𓅂
Developer Channel | @MMMFi ✓.''')
 else:
     if not db.get('status'):
         pass
     if db.get('status'):
         member = bot.get_chat_member(f"@{channel}",m.from_user.id)
         if member.status == "member" or member.status == "administartor" or member.status == "creator":
             pass
         else:
             bot.send_message(m.chat.id,f'- يرجى الاشتراك في قناة البوت لـ تتمكن من استخدامة ⚠️	                                                    - قناة البوت | https://t.me/{channel} ✅         • اشترك ثم اضغط /start 🔥')
 v= key()	
 add_adm = but('اضافة ادمن 🕹️',callback_data = 'add')	
 delete_adm = but('تنزيل ادمن 🕹️', callback_data = 'delet')
 rem = but('احصائيات 📊',callback_data = 'statc')
 ban = but('حظر عضو 🚫',callback_data = 'banme')
 bun = but('الغاء حظر عضو 🚫',callback_data = 'baning')
 brod = but('اذاعة 📣',callback_data = 'brod')
 ba = but(f'وضع قناة الاشتراك 🌐',callback_data = 'geti')
 bn =but('فتح الاشتراك الاجباري ✅',callback_data = 'ope')
 tnb = but('فتح التنبيه ✅',callback_data = 'tnb')
 clo = but('تعطيل التنبيه ❌',callback_data = 'clo')
 jio = but('حالة الاشتراك الاجباري 🚸',callback_data = 'ses')
 best = but('تعطيل الاشتراك الاجباري ❌',callback_data = 'gohn')
 dest = but(f'حذف قناة الاشتراك 🗑️',callback_data = 'gets')
 est = but(f'قناة الاشتراك❗',callback_data = 'gs')
 kop = but("حاله التنبيه ⚙️",callback_data = "kop")
 v.add(add_adm,delete_adm)
 v.add(brod)
 v.add(ba,dest)
 v.add(est)
 v.add(tnb,clo)
 v.add(jio)
 v.add(bn,best)
 v.add(rem)
 v.add(bun,ban)
 v.add(kop)
 h = key()
 rem = but('احصائيات 📊',callback_data = 'statc')
 brod = but('اذاعة 📣',callback_data = 'brod')
 h.add(ba,dest)
 h.add(est)
 h.add(tnb,clo)
 h.add(jio)
 h.add(bn,best)
 h.add(rem,brod)
 h.add(kop)
 if user_id in data['onwer'] :
     bot.send_message(m.chat.id,'- مرحبا بك عزيزي المالك يمكنك التحكم في البوت من خلال الأزرار ادناة 👇 							                            • تم تطوير هذة اللوحة من قبل قناة صانع بوتات الأمير | @MMMFi ✅',reply_markup = v)
 if user_id in data['band']:
     pass
 else:
     if user_id in data['admin']:
         bot.send_message(m.chat.id,'- مرحبا بك عزيزي الادمن يمكنك التحكم في البوت من خلال الأزرار ادناة 👇 							                            • تم تطوير هذة اللوحة من قبل قناة صانع بوتات الأمير | @MMMFi ✅',reply_markup = h)
@bot.callback_query_handler(func=lambda c: True)
def handle_callback(c):
    channel = db.get("channel")
    user_id = c.from_user.id
    data = db.get('db')
    use = len(db.get('db')['users'])
    adm = len(db.get('db')['admin'])
    bans = len(db.get('db')['band'])
    dg = f'''
band  : {bans} 🚫
member : {use} 👥
admin : {adm} 🛃
          '''
    if c.data == 'add': 
        if user_id in data['onwer']:
            m = bot.send_message(c.message.chat.id,'ارسل ايدي الشخص لـرفعة ادمن ✅')
            bot.register_next_step_handler(m,adds)
    if c.data == 'delet': 
        if user_id in data['onwer']:
            ha = bot.send_message(c.message.chat.id,'ارسل ايدي الشخص الذي تريد تنزيلة من الادمنية ✅')
            bot.register_next_step_handler(ha,dgh)
    if c.data == 'banme': 
        if user_id in data['onwer']:
            lita = bot.send_message(c.message.chat.id,'✅ ارسل ايدي الشخص الذي تريد حظره' )
            bot.register_next_step_handler(lita,hhg)
    if c.data == 'baning' : 
        if user_id in data['onwer']:
            li = bot.send_message(c.message.chat.id,'✅ ارسل ايدي الشخص الذي تريد فك الحظر عنه ')
            bot.register_next_step_handler(li,hgf)
    if c.data == 'statc' : 
        if user_id in data['onwer'] or user_id in data['admin']:
            bot.send_message(c.message.chat.id,dg)
    if c.data == 'brod':
        if user_id in data['onwer'] or user_id in data['admin']:
            xc = bot.send_message(c.message.chat.id,'- ارسل النص الذي تريد ارسالة ( نص ، صوره ، ملف ) 💯')
            bot.register_next_step_handler(xc,cx)
    if c.data == 'geti':
        if user_id in data['onwer'] or user_id in data['admin']:
            fiul = bot.send_message(c.message.chat.id,'ارسل يوزر القناة بدون @')
            bot.register_next_step_handler(fiul,setz)
    if c.data == 'gs':
        if user_id in data['onwer'] or user_id in data['admin']:
            if not db.get('channel'):
                bot.send_message(c.message.chat.id,'لم يتم تحديد قناة❗')
            else:
                channel = db.get('channel')
                bot.send_message(c.message.chat.id,f'https://t.me/{channel}')
    if c.data == 'gets':
        if user_id in data['onwer'] or user_id in data['admin']:
            if db.get('channel'):
                db.delete('channel')
                bot.send_message(c.message.chat.id,'تم حذف القناة 🗑️')
            else:
                bot.send_message(c.message.chat.id,'لا توجد قناة مضافه ❌')
    if c.data == 'ope':
        if user_id in data['onwer'] or user_id in data['admin']:
            if not db.get('status'):
                db.set('status',1)
                bot.send_message(c.message.chat.id,'تم تفعيل الاشتراك الاجباري ✅')
            else:
                bot.send_message(c.message.chat.id,'الاشتراك مغعل من قبل❗')
    if c.data == "gohn":
        if user_id in data['onwer'] or user_id in data['admin']:
            if db.get('status'):
                db.delete('status')
                bot.send_message(c.message.chat.id,'تم تعطيل الاشتراك ✅')
            else:
                bot.send_message(c.message.chat.id,'الاشتراك معطل من قبل❗')
    if c.data == "ses":
        if user_id in data['onwer'] or user_id in data['admin']:
            if db.get('status'):
                bot.answer_callback_query(c.id,"الاشتراك الاجباري مفعل ✅",show_alert=True)
            elif not db.get("status"):
                bot.answer_callback_query(c.id,"الاشتراك الاجباري معطل ❌",show_alert=True)
    if c.data == "tnb":
        if user_id in data['onwer'] or user_id in data['admin']:
            if db.get('db')['status'] == 1:
                bot.send_message(c.message.chat.id,"التنبيه مفتوح من قبل❗")
            else:
                data["status"] = 1
                db.set("db",data)
                bot.send_message(c.message.chat.id,"تم فتح التنبيه ✅")
    if c.data == "clo":
        if user_id in data['onwer'] or user_id in data['admin']:
            if data["status"] == 2:
                bot.send_message(c.message.chat.id,"التنبيه معطل من قبل❗")
            else:
                data["status"] = 2
                db.set("db",data)
                bot.send_message(c.message.chat.id,"تم تعطيل التنبيه ✅")
    if c.data == "kop":
        if user_id in data['onwer'] or user_id in data['admin']:
            if data["status"] == 2 :
                bot.answer_callback_query(c.id,"التنبيه معطل ❌",show_alert=True)
            else:
                bot.answer_callback_query(c.id,"التنبيه مفتوح ✅",show_alert=True)
def setz(message):
    chn = message.text
    if not db.get('channel'):
        db.delete('channel')
        db.set('channel',chn)
        bot.send_message(message.chat.id,'تم تحديد القناة ✅                                                      • تأكد من أن البوت ادمن في القناة لكي يعمل بشكل صحيح ⚠️                                              Developer Channel | @MMMFi ✓.')
    else:
        bot.send_message(message.chat.id,"❗ يوجد قناة اخري يرجى حذفها لوضع قناة ثانيه")
def cx(message):
    ko = db.get('db')['users']
    for i in ko:
        bot.copy_message(chat_id=i, from_chat_id=message.chat.id, message_id=message.message_id)
def hgf(message):
    data = db.get('db')
    idg = int(message.text)
    if idg in data['band']:
        data['band'].remove(int(f'{idg}'))
        db.set('db',data)
        bot.send_message(message.chat.id,'تم فك الحظر ✅')
    else:
        bot.send_message(message.chat.id,'لم يتم حظر هذا الشخص ❌')
def hhg(message):
    data = db.get('db')
    ids = int(message.text)
    if not ids in data['band']:
        data['band'].append(int(f'{ids}'))
        db.set('db',data)
        bot.send_message(message.chat.id,'تم حظره 🚫')
    else:
        bot.send_message(message.chat.id,'لا يوجد شخص بهذا الايدي❗')
def dgh(message):
    data = db.get('db')
    idd = int(message.text)
    if idd in data['admin']:
        data['admin'].remove(idd)
        db.set('db',data)
        bot.send_message(message.chat.id,'تم تنزيل من الادمن ✅')
    else:
        bot.send_message(message.chat.id,'ليس مرفوع في قائمه الادمنية❗')
def adds(message):
    data = db.get('db')
    id = int(message.text)
    if id in data['admin']:
        bot.send_message(message.chat.id,'مرفوع من قبل❗')
    else:
        data['admin'].append(int(f'{id}'))
        db.set('db',data)
        print(data)
        bot.send_message(message.chat.id,'تم رفع ادمن ✅')
bot.polling(True) #@MMMFi



from telethon import TelegramClient,events,Button
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.auth import CheckPasswordRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from os import path
import asyncio

#فكأنني بالرمح أضرب قائلاً الأرضُ أرضي والزمانُ زماني


api_id = "29510141"
api_hash = "14c074a5aed49dc7752a9f8d54cf4ad4"
alEx = TelegramClient("MBot",api_id,api_hash).start()
@alEx.on(events.NewMessage(pattern=r"^/start$"))
async def StartSourceAlex(message):
	
	await message.reply('''
↯︙اهلا بك عزيزي .
↯︙يمكنني تجميع نقاط بوت [ دعمكم ] .
↯︙اشتراك بالقنوات تلقائي ( الاجباري ، والتجميع ) .''',buttons=([Button.inline('( بدء التجميع )',data='collect')],[Button.inline('( معلوماتي )',data='info')],[Button.inline('( الهدية اليومية )',data='GiftDay'),Button.inline('( استخدام كود )',data='Gift')],[Button.inline('( مغادرة القنوات والمجموعات )', data = 'leave')],[Button.inline('( تسجيل الدخول )',data='login')],[Button.url("[ مبرمج البوت ]",url="https://t.me/DEVEVII")]))

async def CheckChannelsBot(StartCheckChannel,event):
	await StartCheckChannel.send_message('DamKombot','/start')
	await asyncio.sleep(3)
	try:
		Join = await StartCheckChannel.get_messages('DamKombot', limit=1)
	except:
		pass
	
	if str('اشترك') in Join[0].message:
			Url = str(Join[0].message).split('@')[1].split('اشترك')[0]
			try:
				await StartCheckChannel(JoinChannelRequest(Url))
			except Exception as e:
				
				if 'wait' in str(e):
					Second = (str(e).split('of ')[1].split('seconds')[0])
					await alEx.send_message(event.original_update.user_id,f'''
↯︙تم حظرك من الانضمام بالقنوات ❗
↯︙عليك الانتضار ~> {Second} ثانية❕
بعد انتهاء وقت الحظر حاول التجميع مره اخرى ❕
''',buttons=([Button.inline('( رجوع )',data='Back')]))
					StartCheckChannel.disconnect()
			await asyncio.sleep(3)
			await CheckChannelsBot(StartCheckChannel,event)
	elif 'الصيانة'in str(Join[0].message):
				await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙البوت تحت الصيانه 
↯︙الرجاء اعادة المحاولة لاحقاً❕
''',buttons=[Button.inline('( رجوع )',data='Back')])
				StartCheckChannel.disconnect()
	elif str('مرحبا بك في بوت') in str(Join[0].message):
			await CheckChannels(StartCheckChannel,event)
			
			
			
async def CheckChannels(StartCheckChannel,event):
		global alEx
		await asyncio.sleep(4)
		try:
			Tagmea = await StartCheckChannel.get_messages('DamKombot', limit=1)
			if "لا يوجد قنوات حالياً 🤍" in str(Tagmea[0].message):
				await asyncio.sleep(5)
				await CheckChannelsBot(StartCheckChannel,event)
						
			else:
			
				await Tagmea[0].click(1)
				await asyncio.sleep(4)
				Join = await StartCheckChannel.get_messages('DamKombot', limit=1)
				aw = await Join[0].click(0)
				if aw == None:
					for i in range(35):
						
							await coll(StartCheckChannel,event)
						
		except:
					try:
						StartCheckChannel.disconnect()
					except:pass
					
					
async def coll(StartCheckChannel,event):
	global alEx
	await asyncio.sleep(3)
	Tahkok = await StartCheckChannel.get_messages('DamKombot', limit=1)
	
	try:
		Url ="https://t.me/"+str(Tahkok[0].message).split('@')[1]
		await asyncio.sleep(3)
	except:pass
	try:
		await StartCheckChannel(JoinChannelRequest(Url))
	except:
		try:
			await StartCheckChannel(ImportChatInviteRequest(Url))
		except:
			pass
	await asyncio.sleep(2)
	Sub = await StartCheckChannel.get_messages('DamKombot', limit=1)
	if "لا يوجد قنوات حالياً 🤍" in str(Sub):
					await asyncio.sleep(5)
					await CheckChannelsBot(StartCheckChannel,event)
	elif 'الصيانة'in str(Sub):
				await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙البوت تحت الصيانه 
↯︙الرجاء اعادة المحاولة لاحقاً❕
''',buttons=[Button.inline('( رجوع )',data='Back')])
				StartCheckChannel.disconnect()						
						
	else:
			S = await (Sub[0].click(0))
			if str('نقاط') in str(S.message):
				print("- تم اضافة نقاط ✅")
			else:
				print(S.message)				

@alEx.on(events.CallbackQuery)
async def CallBackAlex(event):
	global StartCheckChannel
	if event.data == b'collect':
		if path.exists('MySessionAlex.session') == False:
			await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,'''
↯︙انت غير مسجل بحساب تليكرام ❗
↯︙عليك تسجيل الدخول ليعمل البوت بشكل صحيح ❗''',buttons=[Button.inline('( رجوع )', data='Back')])
		else:
			await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,'''
↯︙جارِ التجميع ....
↯︙الرجاء عدم ضغط اي زر لان كل الازرار تعتمد على ( عمل الحساب في البوت ) . 
↯︙عند الضغط على اي زر سيتم ايقاف التجميع ❗
		''',buttons=[Button.inline('( ايقاف التجميع ) ', data='stop')])
			StartCheckChannel = await TelegramClient('MySessionAlex',api_id,api_hash).start()
			await CheckChannelsBot(StartCheckChannel,event)
	elif event.data == b'info':
		if path.exists('MySessionAlex.session') == False:
			await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,'''
↯︙انت غير مسجل بحساب تليكرام ❗
↯︙عليك تسجيل الدخول ليعمل البوت بشكل صحيح ❗''',buttons=[Button.inline('( رجوع )', data='Back')])
		else:
				
			StartCheckChannel = await TelegramClient('MySessionAlex',api_id,api_hash).start()
			await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
انتظر قليلاً ....
''',buttons=[Button.url("[ مبرمج البوت ]",url="https://t.me/DevEviI")])
			async def check():
				await StartCheckChannel.send_message('DamKombot','/start')
				await asyncio.sleep(3)
				Join = await StartCheckChannel.get_messages('DamKombot', limit=1)
				if str('اشترك') in str(Join[0].message):
					
						await asyncio.sleep(3)
						Url = str(Join[0].message).split('@')[1].split('اشترك')[0]
						try:
							await StartCheckChannel(JoinChannelRequest(Url))
							await check()
						except Exception as e:
							if 'wait' in str(e):
								Second = (str(e).split('of ')[1].split('seconds')[0])
								await alEx.send_message(event.original_update.user_id,f'''
↯︙تم حظرك من الانضمام بالقنوات ❗
↯︙عليك الانتضار ~> {Second} ثانية❕
بعد انتهاء وقت الحظر حاول التجميع مره اخرى ❕
''',buttons=([Button.inline('( رجوع )',data='Back')]));StartCheckChannel.disconnect()
							else:
								print(e)
					
				elif str('مرحبا بك في بوت') in str(Join[0].message):
					await Join[0].click(2)
					Infor = await StartCheckChannel.get_messages('DamKombot',limit=1)
					Info = str(Infor[0].message)
					Coin = str(Info.split('نقاطك : ')[1].split('النقاط')[0].split('نقطة')[0])
					Used = str(Info.split('المستخدمة :')[1].split('لقد')[0].split('نقطة')[0])
					Invit = str(Info.split('لقد دعوت : ')[1].split('المتبقي للهدية : ')[0].split('✳️')[0])
					Status_Gift= str(Info.split('المتبقي للهدية : ')[1])
					await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙نقاطك ~> {Coin}
↯︙النقاط المستخدمة ~> {Used}
↯︙شاركت رابطك ~> {Invit}
↯︙المتبقي للهدية ~> {Status_Gift}
''',buttons=[Button.inline('( رجوع ) ',data='Back')])
					await StartCheckChannel.disconnect()
				elif 'الصيانة'in str(Join[0].message):
					await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙البوت تحت الصيانه 
↯︙الرجاء اعادة المحاولة لاحقاً❕
''',buttons=[Button.inline('( رجوع )',data='Back')]);StartCheckChannel.disconnect()
				else:
					print(Join[0].message)
			await check()
	elif event.data == b'Back':
				try:
					StartCheckChannel.disconnect()
				except:
					pass
				await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,'''
↯︙اهلا بك عزيزي .
↯︙يمكنني تجميع نقاط بوت [ دعمكم ] .
↯︙اشتراك بالقنوات تلقائي ( الاجباري ، والتجميع ) .''',buttons=([Button.inline('( بدء التجميع )',data='collect')],[Button.inline('( معلوماتي )',data='info')],[Button.inline('( الهدية اليومية )',data='GiftDay'),Button.inline('( استخدام كود )',data='Gift')],[Button.inline('( مغادرة القنوات والمجموعات )', data = 'leave')],[Button.inline('( تسجيل الدخول )',data='login')],[Button.url("[ مبرمج البوت ]",url="https://t.me/DEVEVII")]))

	elif event.data == b'stop':
		try:
			await StartCheckChannel.disconnect()
		except:
			try:
				StartCheckChannel = await TelegramClient('MySessionAlex',api_id,api_hash).start()
			except:
				try:
					await StartCheckChannel.disconnect()
				except:pass
		await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙تم إيقاف التجميع ....
↯︙تستطيع التحكم بالازرار الان بحرية ❕
''',buttons=[Button.inline('( رجوع ) ', data='Back')])
	elif event.data == b'Gift':
		StartCheckChannel = await TelegramClient('MySessionAlex',api_id,api_hash).start()
		await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙انتضر قليلاً من فضلك ... ❕
''',buttons=[Button.url("[ مبرمج البوت ]",url="https://t.me/DEVEVII")])
		async def check():
				await StartCheckChannel.send_message('DamKombot','/start')
				await asyncio.sleep(3)
				Join = await StartCheckChannel.get_messages('DamKombot', limit=1)
				if str('اشترك') in str(Join[0].message):
					
						await asyncio.sleep(3)
						Url = str(Join[0].message).split('@')[1].split('اشترك')[0]
						try:
							await StartCheckChannel(JoinChannelRequest(Url))
							await check()
						except Exception as e:
							if 'wait' in str(e):
								Second = (str(e).split('of ')[1].split('seconds')[0])
								await alEx.send_message(event.original_update.user_id,f'''
↯︙تم حظرك من الانضمام بالقنوات ❗
↯︙عليك الانتضار ~> {Second} ثانية❕
بعد انتهاء وقت الحظر حاول التجميع مره اخرى ❕
''',buttons=([Button.inline('( رجوع )',data='Back')]))
								StartCheckChannel.disconnect()
				elif str('مرحبا بك في بوت') in str(Join[0].message):
					await Join[0].click(3)
					Gifter = await StartCheckChannel.get_messages('DamKombot',limit=1)
					gift = str(Gifter[0].message)
					if 'ارسل الكود ' in gift:
						await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙ارسل الكود من فضلك :
''',buttons=[Button.url("[ مبرمج البوت ]",url="https://t.me/DEVEVII")])
						@alEx.on(events.NewMessage)
						async def ForId(eve):
							if type(eve.original_update.message.message) == str:
								msg = await eve.reply(f'''
↯︙جار فحص الكود  ...
''',buttons=[Button.url("[ مبرمج البوت ]",url="https://t.me/DEVEVII")])
								await StartCheckChannel.send_message('DamKombot',f'{eve.original_update.message.message}')
								Status = await StartCheckChannel.get_messages('DamKombot',limit=1)
								if 'تم اضافة'in str(Status[0].message):
									Status = await StartCheckChannel.get_messages('DamKombot',limit=1)
									await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''{Status[0].message}
''',buttons=[Button.inline('( رجوع ) ',data='Back')])
								else:
									Status = await StartCheckChannel.get_messages('DamKombot',limit=1)
									await alEx.delete_messages(event.original_update.user_id,[msg])
									await eve.reply(f'''{Status[0].message}
''',buttons=[Button.inline('( رجوع ) ',data='Back')])
									await StartCheckChannel.disconnect()
		if path.exists('MySessionAlex.session') == False:
			await asyncio.sleep(2)
			await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,'''
↯︙انت غير مسجل بحساب تليكرام ❗
↯︙عليك تسجيل الدخول ليعمل البوت بشكل صحيح ❗''',buttons=[Button.inline('( رجوع )', data='Back')])
		else:
			await check()
	elif event.data==b'leave':
		global Msg
		leavg,Leav=0,0
		if path.exists('MySessionAlex.session') == False:
			await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,'''
↯︙انت غير مسجل بحساب تليكرام ❗
↯︙عليك تسجيل الدخول ليعمل البوت بشكل صحيح ❗''',buttons=[Button.inline('( رجوع )', data='Back')])
		else:
			StartCheckChannel = await TelegramClient('MySessionAlex',api_id,api_hash).start()
			D = await StartCheckChannel.get_dialogs()
			for dialog in D:
				entity = dialog.entity
				try:
					if entity.megagroup == True:
						Leav+=1
						All = Leav+leavg
						a = await StartCheckChannel(LeaveChannelRequest(entity))
						await asyncio.sleep(2)
						Msg = await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙جار المغادرة ...
↯︙عليك الانتضار الى ان تتم المغادرة بالكامل ❗

''',buttons=([Button.inline(f'القنوات ~> {Leav}',data='leaving'),Button.inline(f'المجموعات ~> {leavg}',data='leaving')],[Button.inline(f'الاجمالي ~> {All}',data='alaa')]))
						a.disconnect()
					elif entity.megagroup == False:
						leavg+=1
						All = Leav+leavg
						a = await StartCheckChannel(LeaveChannelRequest(entity))
						await asyncio.sleep(2)
						Msg = await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙جار المغادرة ...
↯︙عليك الانتضار الى ان تتم المغادرة بالكامل ❗
''',buttons=([Button.inline(f'القنوات ~> {Leav}',data='leaving'),Button.inline(f'المجموعات ~> {leavg}',data='leaving')],[Button.inline(f'الاجمالي ~> {All}',data='alaa')]))
						a.disconnect()
				except Exception as e:
					pass
		
			await alEx.delete_messages(event.original_update.user_id,[Msg])
			await alEx.send_message(event.original_update.user_id,'↯︙تم مغادرة جميع القنوات والمجموعات .',buttons=[
			Button.inline('( رجوع )',data='Back')])
			StartCheckChannel.disconnect()
	elif event.data==b'GiftDay':
			try:
				StartCheckChannel.disconnect()
			except:
				pass
			StartCheckChannel = await TelegramClient('MySessionAlex',api_id,api_hash).start()
			await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙جار سحب الهدية اليومية ... ❕
''',buttons=[Button.url("[ مبرمج البوت ]",url="https://t.me/DEVEVII")])
			async def check():
				await StartCheckChannel.send_message('DamKombot','/start')
				await asyncio.sleep(3)
				Join = await StartCheckChannel.get_messages('DamKombot', limit=1)
				if str('اشترك') in str(Join[0].message):
					
						await asyncio.sleep(3)
						Url = str(Join[0].message).split('@')[1].split('اشترك')[0]
						try:
							await StartCheckChannel(JoinChannelRequest(Url))
							await check()
						except Exception as e:
							if 'wait' in str(e):
								Second = (str(e).split('of ')[1].split('seconds')[0])
								await alEx.send_message(event.original_update.user_id,f'''
↯︙تم حظرك من الانضمام بالقنوات ❗
↯︙عليك الانتضار ~> {Second} ثانية❕
بعد انتهاء وقت الحظر حاول التجميع مره اخرى ❕
''',buttons=([Button.inline('( رجوع )',data='Back')]));StartCheckChannel.disconnect()
				elif str('مرحبا بك في بوت') in str(Join[0].message):
					await Join[0].click(1)
					await asyncio.sleep(3)
					GetMessage = await StartCheckChannel.get_messages('DamKombot', limit=1)
					Gift = await GetMessage[0].click(2)
					await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,f'''
↯︙{Gift.message}
		''',buttons=[Button.inline('( رجوع ) ', data='Back')])
			if path.exists('MySessionAlex.session') == False:
				await asyncio.sleep(2)
				await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,'''
↯︙انت غير مسجل بحساب تليكرام ❗
↯︙عليك تسجيل الدخول ليعمل البوت بشكل صحيح ❗''',buttons=[Button.inline('( رجوع )', data='Back')])
			else:
				await check()
	elif event.data == b'login' or event.data == b'again':
			await alEx.edit_message(event.original_update.user_id,event.original_update.msg_id,'''
↯︙تسجيل الدخول 📥
↯︙علماً انه اذا كنت قد سجلت دخول سابقاً بالبوت فـ سيتم حذف الجلسه السابقة ❗
↯︙وايضا البوت سيتمم مهامة من خلال الحساب الذي ستسجل به الان ❕

↯︙ارسل رقمك مع رمز الدولة مثال ( ********964+)

''',buttons=[Button.inline('( رجوع )', data='Back')])
			@alEx.on(events.NewMessage)
			async def MyPhone(event):
				LoginAlex= TelegramClient('MySessionAlex',api_id,api_hash)
				if str('+') in event.original_update.message.message:
							await LoginAlex.connect()
							try:
								SendCode = await LoginAlex.send_code_request(event.original_update.message.message)
								if str("phone_code_hash") in str(SendCode) or str('Telegram is having') in str(SendCode):
									await event.reply('''
↯︙الرقم صحيح ❕
↯︙تم ارسال كود التحقق 🔘
↯︙ارسل لي كود التحقق ❗
''',buttons=[Button.inline('( رجوع )',data='Back'),Button.inline('( حاول مجدداً )',data='again')])
									phone = event.original_update.message.message
									Hash = (SendCode.phone_code_hash)
									alEx.remove_event_handler(MyPhone)
									await CheckCode(event,LoginAlex,phone,Hash)
									
			
									
							except Exception as e:
								
								if "The phone number is invalid" in str(e):
									alEx.remove_event_handler(MyPhone)
									await event.reply('''
↯︙الرقم الذي ارسلتة ليس بالشكل المطلوب ❗
↯︙عليك ارسال الرقم بهذا الشكل ( ****96475+)
''',buttons=[Button.inline('( رجوع )',data='Back'),Button.inline('( حاول مجدداً )',data='again')])
									
								else:
									print(e)
									
			
				else:
								alEx.remove_event_handler(MyPhone)
								await event.reply('''
↯︙الرقم الذي ارسلتة ليس بالشكل المطلوب ❗
↯︙عليك ارسال الرقم بهذا الشكل ( ****96475+)
''',buttons=[Button.inline('( رجوع )',data='Back'),Button.inline('( حاول مجدداً )',data='again')])

			
			async def CheckCode(event,LoginAlex,phone,Hash):
				@alEx.on(events.NewMessage)
				async def c(event):
					print(event.original_update.message.message)
					try:
						Login = await LoginAlex.sign_in(phone=phone,code=event.original_update.message.message, phone_code_hash=Hash)
						if str('User') in str(Login):
							await Login.send_message('me',f'{Login.session.save()}')
							await alEx.send_message(event.original_update.message.peer_id.user_id,'''
↯︙تم تسجيل الدخول للحساب ❕
↯︙سيتم الان استخدام هذا الحساب للتجميع ❕
''',buttons=[Button.inline('( رجوع )', data='Back')])
					except SessionPasswordNeededError as e:
						alEx.remove_event_handler(c)
						await event.reply('''
↯︙الان ارسل كلمة السر ❗''',buttons=[Button.inline('( رجوع )',data='Back')])
						@alEx.on(events.NewMessage)
						async def p(event):
							password = event.original_update.message.message
							try:
								LoginPassword = await LoginAlex.sign_in(password=password)
								if str('User') in str(LoginPassword):
									await LoginAlex.disconnect()
									await alEx.send_message(event.original_update.message.peer_id.user_id,'''
↯︙تم تسجيل الدخول للحساب ❕
↯︙سيتم الان استخدام هذا الحساب للتجميع ❕
''',buttons=[Button.inline('( رجوع )', data='Back')])
								else:
									print(LoginPassword)
							except:
								alEx.remove_event_handler(p)
								await alEx.send_message(event.original_update.message.peer_id.user_id,'''
↯︙كلمة السر خطأ ❗
↯︙تجنباً لحظر حسابك يمكنك المحاوله مره واحده❗
↯︙تأكد من كلمة السر واعد تسجيل الدخول مره اخرى ❕
''',buttons=[Button.inline('( رجوع )', data='Back'),Button.inline('( رجوع )',data='again')])



																
#فكأنني بالرمح أضرب قائلاً الأرضُ أرضي والزمانُ زماني


alEx.run_until_disconnected()
