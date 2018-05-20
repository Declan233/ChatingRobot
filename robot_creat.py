# coding:utf-8
"""
初始创建聊天机器人
"""
from chatterbot import ChatBot


chatbot = ChatBot(
    name='Mybot',

    storage_adapter='chatterbot.storage.SQLStorageAdapter',

    database='./database.sqlite3.db',

    filters=["chatterbot.filters.RepetitiveResponseFilter"],

    logic_adapters=[
    {   # 返回基于已知响应的输入语句最匹配的响应。
        'import_path': 'chatterbot.logic.BestMatch',
        # 'import_path': "chatterbot.logic.MathematicalEvaluation",
        'response_selection_method': 'chatterbot.response_selection.get_most_frequent_response'
    },
    {   # 如果无法以高置信度确定响应，此适配器将返回指定的默认响应。
        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
        'threshold': 0.70,
        'default_response': '抱歉，这个问题暂时无法回答你'
    }],
)
