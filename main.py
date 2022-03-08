import os
from telegram import *
from telegram.ext import *
from datetime import datetime
import threading
import queue
import json
import requests
from webdriver import keep_alive
import random
import time
# from replit import db

karanFamily = ["1586900222", "5296205562"]
countDown = 0
# if "subscribers" not in db.keys():
# 	db["subscribers"] = {}
# if "pendings" not in db.keys():
# 	db["pendings"] = {}


def slowMode(start_text):
	print(start_text)
	open("countdown.txt", "w").write("180")
	global countDown
	while True:
		countDown = 180
		for time_count in range(0, 180):
			countDown = int(open("countdown.txt", "r").read())
			time.sleep(60)
			countDown -= 1
			open("countdown.txt", "w").write(str(countDown))
		db["pendings"] = {}


def channelList(disp):
	print(disp)
	while True:
		content = requests.get(
			"https://telegramScrapper.fa17c2ba028iub.repl.co/file").json()
		db["joined"] = content["data"]
		time.sleep(10)


with open('./chegg_cookies.txt', 'r') as cookies:
	chegg_cookies = cookies.read().splitlines()
bot = Bot("5207207122:AAF96gNAG9ZU4SQZE9_8cTnrHYj5w2L0mEc")
user_name = bot.get_me()['username']
print(f">> 🟢 {user_name} IS ONLINE NOW...")
bot_session = Updater(
	"5207207122:AAF96gNAG9ZU4SQZE9_8cTnrHYj5w2L0mEc", use_context=True)
dispatcher = bot_session.dispatcher
# threading.Thread(target=slowMode, args=('>> 🟢 Slow Mode Enabled', )).start()
threading.Thread(target=channelList, args=('>> 🟢 Slow Mode Enabled', )).start()


def HeaderGen():
	SelectedCookie = random.choice(chegg_cookies)
	header = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		'content-type': 'application/json',
		'cookie': SelectedCookie,
		'origin': 'https://www.chegg.com',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
	}
	List = [SelectedCookie, header]
	return List


def newlikeIt(link, cookie):
	# try:
	header = {
	'authority': 'www.chegg.com',
					'cache-control': 'max-age=0',
					'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
					'sec-ch-ua-mobile': '?0',
					'sec-ch-ua-platform': '"macOS"',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'navigate',
					'sec-fetch-user': '?1',
					'sec-fetch-dest': 'document',
					'referer': 'https://www.chegg.com/',
					'accept-language': 'en-US,en;q=0.9',
					'Cookie': f"{cookie}"
		}
	content = requests.get(link.replace(
		' ', "").replace('\n', ""), headers=header).text
	open("testingResults.html", 'w', encoding='utf-8').write(content)
	# print(content)
	askerId = content.split('data-askerId="')[1].split('"')[0]
	entityId = content.split('data-answerId="')[1].split('"')[0]
	# answerDate = content.split(
	#     'data-ansCreateDate="')[1].split('"')[0].replace(':', '%3A')
	questionId = content.split('data-qid="')[1].split('"')[0]
	token = content.split('"token":"')[1].split('"')[0]
	query = 'askerId={}&entityType=ANSWER&entityId={}&reviewType=LIKE_DISLIKE&reviewValue=0&token={}&questionId={}'.format(
			askerId, entityId, token, questionId)
	header = {
					'authority': 'www.chegg.com',
					'cache-control': 'max-age=0',
					'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
					'sec-ch-ua-mobile': '?0',
					'sec-ch-ua-platform': '"macOS"',
					'upgrade-insecure-requests': '1',
					'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'navigate',
					'sec-fetch-user': '?1',
					'sec-fetch-dest': 'document',
					'referer': 'https://www.chegg.com/',
					'accept-language': 'en-US,en;q=0.9',
					'Cookie': f"{cookie}"
					};
	try:
		liked = requests.post('https://www.chegg.com/study/_ajax/contentfeedback/savereview',
							  headers=header, data=query)
		liked = liked.json()["httpCode"]
		return [200]
	except:
		return [400]
	# except:
	# 	return [403]


def TBSHtmlGenerator(Answer, Question):
	Html = '''<html><head></head><body>
	<div class="tg">
		<div onclick="location.href='https://t.me/chegghero';" class="tg_body">
			<div class="obj">Telegram</div>
			<div class="obj_des">Telegram #1 Chegg Unlimited Solutions Provider.</div>
		</div>
	</div>
	<div class="main">
	<h2 class="accordion active"><b>Question</b></h2>
								<div class="question"> 
									
	
	
	<div id="mobile-question-style" style="font-family: 'Helvetica Neue',Helvetica,Arial; color:#333333;">''' + '\n{}\n'.format(
			Question) + '''</div>
	

										</div>
								<h2 class="accordion active"><b>Answer</b></h2><div class="question"> 
										''' + '\n{}\n'.format(Answer) + '''</div>
				<script>
				var acc = document.getElementsByClassName("accordion");
				var i;
				for (i = 0; i < acc.length; i++) {
					acc[i].addEventListener("click", function () {
						this.nextElementSibling.classList.toggle('collapse')
						this.nextElementSibling.classList.toggle('expand')
		
					});
				}
			</script>
				<style>
				
			.img-container-block {
				text-align: center;
			}
			.img-container-inline {
				text-align: center;
				display: block;
			}
			.img-container img {
				width: 92px;
				position: absolute;
				left: 25%;
				top: 6px;
				border: 2px solid #00247;
				border-radius: 50px;
			}
			.step {
				margin: auto;
				margin-top: 7px;
				text-align: center;
				padding: 7px;
				color: #fff;
				font-size: 16px;
				background: #f78112;
				font-weight: bold;
				border-radius: 15px;
			}
			.tg{
					width: 100%;
					display:flex;
					margin-bottom: 10px;
					justify-content: center;
					align-items: center;
				}
				.tg_body{
					width: 38%;
					background:#1284ee;
					border-radius: 30px;
					display: flex;
					justify-content:left;
					align-items:center;
					padding: 5px;
				}
				.tg_body:hover{
					cursor: pointer;
				}
				.obj{
					padding:8px;
					border: 2px solid white;
					border-radius: 30px;
					margin-right: 10px;
					background:#48a7ff;
				}	
			.accordion {
				background-color: #f78112;
				padding: 10px;
				font-size: 15px;
				color: white;
				border-radius: 29px;
				text-align: center;
				text-transform: uppercase;
				width: auto;
				height: auto;
				overflow: hidden;
				filter: brightness(100%);
				transition: filter 0.15s;
			}
	.ad_shadow{
				box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);
				-webkit-box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);
				-moz-box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);

			}
	.ad{
				width: 18%;
				margin-right: 9px;
				border-radius: 10px;
				max-height: 92px;
			}
	.products{
		margin:10px 0px 10px 19px;    
	}
			.question {
				padding: 0 10px;
				margin: 0px 35px 0px 35px;
				border-left: 12px solid;
				border-radius: 20px;
				border-top: 2px solid;
				border-right: 12px solid;
				border-bottom: 2px solid;
				border-color: #f78112;
				text-align: center;
				overflow: hidden;
			}
			.main {
				background-color: white;
			}
			</style></div></body></html>'''
	return Html


def HtmlGenerator(Answer, Question, Likes, Dislikes, Comments, QuestionHead):
	Html = '''<html><body>
	<div class="tg">
		<div onclick="location.href='https://t.me/chegghero';" class="tg_body">
			<div class="obj">Telegram</div>
			<div class="obj_des">Telegram #1 Chegg Unlimited Solutions Provider.</div>
		</div>
	</div>
	<div class="main">
	<div class="like_dislike">
		<div class="like_dis_like">Likes: '''+Likes+'''</div>
		<div class="like_dis_like">Dislikes: '''+Dislikes+'''</div>
	</div>
	</div></div>
	<h2 class="accordion active"><div class="headline">'''+QuestionHead+'''</div></h2>
								<div class="question"> 
	<div id="mobile-question-style" style="font-family: 'Helvetica Neue',Helvetica,Arial; color:#333333;">''' + '\n{}\n'.format(
			Question) + '''</div>
	

										</div>
								<h2 class="accordion active"><b>Answer</b></h2><div class="question"> 
										''' + '\n{}\n'.format(Answer) + '''</div>
			<div class="comment-box"><div class="comments-header">Comments</div><ul class="comments-list">'''+Comments+'''</ul></div></div></div>
				<script>
				var acc = document.getElementsByClassName("accordion");
				var i;
				for (i = 0; i < acc.length; i++) {
					acc[i].addEventListener("click", function () {
						this.nextElementSibling.classList.toggle('collapse')
						this.nextElementSibling.classList.toggle('expand')
		
					});
				}
			</script>
				<style>
			.img-container-block {
				text-align: center;
			}
			.img{
				max-width: 100%;
				height: 100%;
			}
			.tg{
					width: 100%;
					display:flex;
					margin-bottom: 10px;
					justify-content: center;
					align-items: center;
				}
				.tg_body{
					width: 38%;
					background:#1284ee;
					border-radius: 30px;
					display: flex;
					justify-content:left;
					align-items:center;
					padding: 5px;
				}
				.tg_body:hover{
					cursor: pointer;
				}
				.obj{
					padding:8px;
					border: 2px solid white;
					border-radius: 30px;
					margin-right: 10px;
					background:#48a7ff;
				}
			.Beaster {
				max-width: 100%;
				display: block;
				margin: auto;
			}
			.comment-box{
				border: 2px solid #f78112;
				margin-top: 40px;
				border-radius: 37px;
				border-left: 15px solid #f78112;
			}
	.ad_shadow{
				box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);
				-webkit-box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);
				-moz-box-shadow: 0px 0px 3px 1px rgba(0,0,0,0.75);

			}
	.ad{
				width: 18%;
				margin-right: 9px;
				border-radius: 10px;
				max-height: 92px;
			}
		.products{
			margin:10px 0px 10px 19px;    
		}
			.comments-header{
				background: #f78112;
				width: fit-content;
				margin: auto;
				padding: 9px;
				border-radius: 16px;
				margin-top: -18px;
				padding: 9px;
				color: #fff;
			}
			.comments-markup{
				list-style: none;
				border-left: 10px solid #f78112;
				margin: 0px 10px 5px 10px;
				padding: 7px 0px 0px 10px;
				border-radius: 21px;
			}
			.comment-label{
				color: #f78112;
				font-weight: bold;
			}
			.like_dislike{
				display: flex;
				width: fit-content;
				border: 2px solid #f78112;
				padding: 5px;
				border-radius: 24px;
				margin: auto;
				color: #fff;
			}
			.like_dis_like{
				padding: 8px;
				margin: 0px 5px;
				font-weight: bold;
				border-radius: 17px;
				background: #f78112;
			}
			.headline{
				display: inline;
				color: #ffffff;
				font-size: 15px;
				font-weight: normal;
			}
			.comment-text{
				padding: 0px 25px 0px 25px;
			}
			.comment-header{
				vertical-align: 14px;
			}
			.accordion {
				background-color: #f78112;
				padding: 10px;
				font-size: 15px;
				color: white;
				border-radius: 29px;
				text-align: center;
				text-transform: uppercase;
				width: auto;
				height: auto;
				overflow: hidden;
				filter: brightness(100%);
				transition: filter 0.15s;
			}
			.question {
				padding: 0 10px;
				margin: 0px 35px 0px 35px;
				border-left: 12px solid;
				border-radius: 20px;
				border-top: 2px solid;
				border-right: 12px solid;
				border-bottom: 2px solid;
				border-color: #f78112;
				text-align: center;
				overflow: hidden;
			}
			.main {
				background-color: white;
			}
			</style></body></html>'''
	return Html


def TBS(Question, Cookie, Link):
	ChapterId = str(Question.split('"chapterId":"')[1].split('"')[0])
	Token = str(Question.split('"token":"')[1].split('"')[0])
	ISBN = str(Question.split('"isbn13":"')[1].split('"')[0])
	QID = str(Question.split('problemId":"')[1].split('"')[0])
	try:
		cheggheader = {
			'accept': 'application/json',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
			'content-type': 'application/json',
			'cookie': "{}".format(Cookie),
			'origin': 'https://www.chegg.com',
			'referer': "{}".format(Link),
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
		}
		query = {"query": {"operationName": "getSolutionDetails", "variables": {"isbn13": "{}".format(
			ISBN), "chapterId": "{}".format(ChapterId), "problemId": "{}".format(QID)}}, "token": "{}".format(Token)}
		Content = requests.post('https://www.chegg.com/study/_ajax/persistquerygraphql',
								headers=cheggheader, data=json.dumps(query))
		Content = Content.text.replace("\\", "")
		try:
			Question = Content.split('problemHtml":"')[1].split('","user')[
				0].replace('class="question"', 'class="Kick"')
		except:
			Question = ''
		HTMlIndexes = Content.split('"html":"')
		HTMlIndexes[0] = ''
		count = 0
		Steps = ''
		for i in HTMlIndexes:
			if '<div' in i:
				count += 1
				Steps += '<div class="step">Step# {}</div>{}'.format(
					count, i.split('","link"')[0])
	except:
		Steps = '<p><span style="background-color: #ffffff; color: #ff0000; font-size: 18px;"><strong>Oh No!! No One Has Answered It Yet...</strong></span></p>'
	Html = TBSHtmlGenerator(Steps, Question)
	with open('TextBook_Solution.html', 'w') as TBS:
		TBS.write(Html)
	return


def QuestionHtml(Extracted, q1):
	try:
		Question = str(Extracted[Extracted.index(
			'<div class="ugc-base question-body-text">'):])
		Question = Question[:Question.index('<div class="avatar-comments')]
		Question = Question[:Question.rfind('</div>')] + "</div>"
		Question = Question.replace('"//', '"https://')
		Question = Question.replace('<img ', '<img class="Beaster" ')
	except:
		Question = '<p><span style="color: #ff0000;text-align: center;display: block;"><strong>No one has Answered it yet</strong></span></p>'
	q1.put(Question)


def CommentsHtml(Extracted, q3):
	try:
		Comment = Extracted.split(
			'<div class="comments-markup mod-parent-container">')
		Comment[-1] = Comment[-1].split('<div class="leave-comment ">')[0]
		Comments = ''
		for i in Comment:
			if '<span class="comment-date">' in i:
				Comments += ('<div class="comments-markup mod-parent-container">' + i)
		Comments = Comments.replace('"//', '"https://')
		if Comments == '':
			Comments = '<p><span style="color: #ff0000;text-align: center;display: block;"><strong>No one has commented it yet</strong></span></p>'
	except:
		Comments = '<p><span style="color: #ff0000;text-align: center;display: block;"><strong>No Comments</strong></span></p>'
	q3.put(Comments)


def Like_Dislike(Extracted, header, q4):
	Likes = '0'
	Dislikes = '0'
	try:
		LikID = Extracted.split('"answerId":')[1].split(',')[0]
	except:
		try:
			LikID = Extracted.split('data-answerId="')[1].split('"')[0]
		except:
			LikID = 'None'
	Like_disLike = requests.get(
		'https://www.chegg.com/study/_ajax/contentfeedback/getreview?entityType=ANSWER&entityId={}'.format(LikID), headers=header).text
	if LikID != 'None':
		for i in Like_disLike.split('}},'):
			try:
				Extract = i.split('"result":')[1]
				if len(Extract) > 10:
					for under in Extract.split('"}'):
						if '"reviewValue":"0' in under:
							Likes = under.split('"count":')[1].split(',')[0]
						elif '"reviewValue":"1' in under:
							Dislikes = under.split('"count":')[1].split(',')[0]
			except:
				Likes = '0'
				Dislikes = '0'
	q4.put([Likes, Dislikes])


def QASolution(Extracted, q5):
	try:
		Extracted = str(Extracted[Extracted.index(
			'<div class="answer-given-body ugc-base">'):])
		Solution = str(Extracted[:Extracted.index('<a href="#"')])
		Solution = Solution.replace('"//', '"https://')
		Solution = Solution.replace('<img', '<img class="Beaster"')
	except:
		Solution = "<p><span style='color: #339966;'><strong>This question hasn't been answered yet!</strong></span></p>"
	q5.put(Solution)


def solution(Extracted, header):
	Threads = []
	q1 = queue.Queue()
	q3 = queue.Queue()
	q4 = queue.Queue()
	q5 = queue.Queue()
	Threads.append(threading.Thread(target=QuestionHtml, args=(Extracted, q1)))
	Threads.append(threading.Thread(target=CommentsHtml, args=(Extracted, q3)))
	Threads.append(threading.Thread(
		target=Like_Dislike, args=(Extracted, header, q4)))
	Threads.append(threading.Thread(target=QASolution, args=(Extracted, q5)))
	for i in Threads:
		i.start()
	try:
		QuestionHead = '<em>' + \
			Extracted.split('headline"><em>')[1].split('</h1>')[0]
	except:
		QuestionHead = '<b>Question</b>'
	for i in Threads:
		i.join()
	Question = q1.get()
	Comments = q3.get()
	Likes, Dislikes = q4.get()
	Solution = q5.get()
	Solution = HtmlGenerator(Solution, Question, Likes,
							 Dislikes, Comments, QuestionHead)
	try:
		with open("Q&A_Solution.html", 'w') as FileWrite:
			FileWrite.write(Solution)
	except:
		with open("Q&A_Solution.html", 'w', encoding="utf-8") as FileWrite:
			FileWrite.write(Solution)
	return


def ContentGrabber(url):
	Cookie, header = HeaderGen()
	Responce = requests.get(url, headers=header)
	return([Cookie, header, Responce])


def SolutionFinalizer(Extracted, header, Cookie, url):
	if 'TBS Solution Page' in Extracted:
		SolutionType = 'TextBook_Solution'
		TBS(Extracted, Cookie, url)
	else:
		SolutionType = 'Q&A_Solution'
		solution(Extracted, header)
	return(SolutionType)


def new_user(update, context):
	# if f'{update.message.from_user.id}' not in db["subscribers"].keys():
	# db["subscribers"][str(update.message.from_user.id)] = 50
	# update.message.reply_text(
	# 	'<b>🤖 FREE CHEGG SOLUTION UNBLUR 🤖</b>\n\n <b>Gift: 50 Free unlocks.\n\n🔸 Paste the link and get your solution.</b>\n<b>🔸 Free unblur.</b>\n\n<i><b>Join Our Main Channel: @chegghero</b></i>', parse_mode=ParseMode.HTML)
	bot.send_message(
		'1586900222', f'USERNAME: {update.message.from_user.username}\nSCREEN NAME: {update.message.from_user.first_name} {update.message.from_user.last_name}\nID: {update.message.from_user.id}')
	# else:
	# 	plx_unlocks = db["subscribers"][str(update.message.from_user.id)]
	# 	update.message.reply_text(
	# 		f'<b>🤖 FREE CHEGG SOLUTION UNBLUR 🤖</b>\n\n <b>Remaining Unlocks: {plx_unlocks}.\n\n🔸 Paste the link and get your solution.</b>\n<b>🔸 Free unblur.</b>\n\n<i><b>Join Our Main Channel: @chegghero</b></i>', parse_mode=ParseMode.HTML)


def handle_message(update, context):
	try:
		if str(update.message.text).split('www.')[1].split('.')[0].lower() == 'chegg':
			if str(update.message.from_user.id) in karanFamily:
				cookie = random.choice(chegg_cookies)
				response = newlikeIt(update.message.text, cookie)
				print(response)
				if response[0] == 200:
					update.message.reply_text(
						f"<strong>Upvoted Successfully</strong>\n\n<strong>Link:</strong>\n\n<i><b>{update.message.text}</b></i>", parse_mode=ParseMode.HTML)
			else:
				update.message.reply_text(
					"<strong>🚫Channel Join Error🚫</strong>\n\n<strong>Unfortunately, you haven't joined our main channel yet. Join our channel to unblur chegg solution.</strong>\n\n<i><b>My Channel: @chegghero</b></i>", parse_mode=ParseMode.HTML)
			return
	except:
		print('TRY 1')
	try:
		if str(update.message.text).split(' ')[0] == 'add':
			if len(update.message.text.split(' ')) == 3:
				if update.message.from_user.id == 1586900222:
					try:
						user_id = int(str(update.message.text).split(' ')[1])
						if str(update.message.text).split(' ')[1] in db["subscribers"].keys():
							db["subscribers"][str(user_id)] = db["subscribers"][str(
								update.message.text).split(' ')[1]] + int(str(update.message.text).split(' ')[2])
							update.message.reply_text('<b>USER: {}\n</b>\nUnlocks Availible: {}'.format(str(update.message.text).split(
								' ')[1], db["subscribers"][str(update.message.text).split(' ')[1]]), parse_mode=ParseMode.HTML)
						else:
							db["subscribers"][str(update.message.text).split(' ')[1]] = int(
								str(update.message.text).split(' ')[2])
							update.message.reply_text('<b>USER: {}\n</b>\nUnlocks Availible: {}'.format(str(
								update.message.text).split(' ')[1], str(update.message.text).split(' ')[2]), parse_mode=ParseMode.HTML)
					except:
						update.message.reply_text(
							'<i><b>ERROR!\n\n Invalid USER ID.</b></i>', parse_mode=ParseMode.HTML)
				elif update.message.from_user.id == 1006156248:
					try:
						user_id = int(str(update.message.text).split(' ')[1])
						username_ram = str(update.message.text).split(' ')[1]
						unlocks_ram = str(update.message.text).split(' ')[2]
						if str(update.message.text).split(' ')[1] in db["subscribers"].keys():
							db["subscribers"][str(user_id)] = db["subscribers"][str(
								update.message.text).split(' ')[1]] + int(str(update.message.text).split(' ')[2])
							update.message.reply_text('<b>USER: {}\n</b>\nUnlocks Availible: {}'.format(str(update.message.text).split(
								' ')[1], db["subscribers"][str(update.message.text).split(' ')[1]]), parse_mode=ParseMode.HTML)
							bot.send_message(
								'1586900222', f'Ramlala Added:\n\nUSERNAME: {username_ram}\nUnlocks: {unlocks_ram}')
						else:
							db["subscribers"][str(update.message.text).split(' ')[1]] = int(
								str(update.message.text).split(' ')[2])
							update.message.reply_text('<b>USER: {}\n</b>\nUnlocks Availible: {}'.format(str(
								update.message.text).split(' ')[1], str(update.message.text).split(' ')[2]), parse_mode=ParseMode.HTML)
							bot.send_message(
								'1586900222', f'Ramlala Added:\n\nUSERNAME: {username_ram}\nUnlocks: {unlocks_ram}')
					except:
						update.message.reply_text(
							'<i><b>ERROR!\n\n Invalid USER ID.</b></i>', parse_mode=ParseMode.HTML)
				else:
					update.message.reply_text(
						'<i><b>This is an admin command.</b></i>', parse_mode=ParseMode.HTML)
				return
			else:
				update.message.reply_text(
					'<i><b>Invalid Command</b></i>', parse_mode=ParseMode.HTML)
	except:
		print('TRY 2')
	try:
		if str(update.message.text).split(' ')[0] == 'rmv':
			if update.message.from_user.id == 1586900222:
				if str(update.message.text).split(' ')[1] in db["subscribers"].keys():
					del db["subscribers"][str(
						update.message.text).split(' ')[1]]
					update.message.reply_text('USER : {}, has been Unsubscribed.'.format(
						str(update.message.text).split(' ')[1]))
				else:
					update.message.reply_text('<b>USER: {}\n</b>\nIs not in our SUbscription Database'.format(
						str(update.message.text).split(' ')[1]), parse_mode=ParseMode.HTML)
			else:
				update.message.reply_text(
					'<i><b>This is an admin command.</b></i>', parse_mode=ParseMode.HTML)
			return
	except:
		print('TRY 3')
	# try:
	if str(update.message.text) == 'paid':
		if update.message.from_user.id in [1586900222, 1006156248]:
			descriptionText = "<b>Users Unlocks:</b>\n\n"
			for eachPiad in db["subscribers"].keys():
				try:
					descriptionText += "{}  --  {} unlocks.\n".format(
						eachPiad, db["subscribers"][eachPiad])
				except:
					pass
			update.message.reply_text(
				descriptionText, parse_mode=ParseMode.HTML)
		else:
			update.message.reply_text(
				'<i><b>This is an admin command.</b></i>', parse_mode=ParseMode.HTML)
		return
	# except:
	# 	print('TRY 4')
	try:
		if str(update.message.text) == 'my':
			if str(update.message.from_user.id) in db["subscribers"].keys():
				display_text = "<i><b>{} Unlocks Availible</b></i>".format(
					(db["subscribers"][str(update.message.from_user.id)]))
				update.message.reply_text(
					display_text, parse_mode=ParseMode.HTML)
			else:
				display_text = "<i><b>You are not a pro members of ours.</b></i>"
				update.message.reply_text(
					display_text, parse_mode=ParseMode.HTML)
			return
	except:
		print('TRY 4')


dispatcher.add_handler(CommandHandler("start", new_user))
# dispatcher.add_handler(CommandHandler("price", price))
# dispatcher.add_handler(CommandHandler("info", info))
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
bot_session.start_polling()
keep_alive()
bot_session.idle()
