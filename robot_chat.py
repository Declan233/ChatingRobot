# coding:utf-8
"""
聊天模块
"""

import robot_creat

robot = robot_creat.chatbot

# Get a response to the input text '

#robot.trainer.export_for_training('./my_export.json')

print("你好，请问有什么能帮你")
while True:
    question = input(">>>")
    answer = robot.get_response(question)
    print(answer)

