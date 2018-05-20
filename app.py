# -*- coding: utf-8 -*-
# TODO:
# author=xc

import robot_creat
from jieba import analyse
from flask import Flask, request, Response, make_response, g,render_template, send_file, abort
import urllib
import re

robot = robot_creat.chatbot

# 创建Flask实例，即一个web应用/wsgi应用
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_text():
	# Render index.html if request is a GET Request
	if request.method == 'GET':
		return render_template('index.html')
	# Process the form data if request is a POST Request
	elif request.method == 'POST':
		print(request.form)
		if 'question' in request.form:
			question = request.form.get('question')

			answer = cutSentense(question) #分词

			# answer = robot.get_response(question)  # 处理程序的接口函数

			return render_template('index.html', answer=answer)

		return render_template('index.html')  # 抛出403异常


def cutSentense(question):
    q = question
    if len(question)>15:  #问题过长时分词
        keywords = analyse.extract_tags(question)
        print("keywords:")
        # 输出抽取出的关键词
        q = ' '.join(keywords)
        print(q)
        # for keyword in keywords:
        #     print(keyword + "/",)
    elif "翻译" in question:
        question = question.split("：")[1]
        return translateGoogle(question)
    result = robot.get_response(q)
    return result




def translateGoogle(text, f='zh-cn', t='en'):
    url_google = 'http://translate.google.cn'
    reg_text = re.compile(r'(?<=TRANSLATED_TEXT=).*?;')
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    r'Chrome/44.0.2403.157 Safari/537.36'
    values = {'hl': 'zh-cn', 'ie': 'utf-8', 'text': text, 'langpair': '%s|%s' % (f, t)}
    value = urllib.parse.urlencode(values)
    req = urllib.request.Request(url_google + '?' + value)
    req.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    data = reg_text.search(content)
    result = data.group(0).strip(';').strip('\'')
    return result



# Flask封装了一个简单的开发用WSGI服务器，通过调用run()启动服务器运行web应用
if __name__ == '__main__':
	app.run(port=5000)
