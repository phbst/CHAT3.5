from flask import Flask, request
from flask_cors import CORS
import requests
import jwt
from functools import wraps

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ""}})                          //网站跨域//
CORS(app, resources={r"/*": {"origins": "http://localhost:8081"}})

SECRET_KEY = ''                     //token key
openai_api_key = ''                 //openai key
openai_url = 'https://api.openai.com/v1/chat/completions'

# 对话历史列表，初始化为空
dialogue_history = []

def check_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            error_message = 'Token is missing.'
            return {'error': error_message,'code':'401'}

        try:
            decoded = jwt.decode(token, key=SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.DecodeError:
            error_message = 'Invalid token.'
            return {'error': error_message,'code':'401'}

        # 如果token验证通过，则调用被装饰的函数
        return func(*args, **kwargs)

    return wrapper


@app.route('/', methods=['POST'])
@check_token
def chat():
    global dialogue_history  # 声明为全局变量

    data = request.get_json()
    question = data['question']

    # 将问题和对话历史组合为新的对话历史
    dialogue_history.append({"role": "user", "content": question})

    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'messages': [
            {'role': 'system', 'content': ''},
            *dialogue_history
        ],
        'max_tokens': 2000,
        'model': 'gpt-3.5-turbo',
        'temperature': 0.8,
        'frequency_penalty': 1.0,
        'presence_penalty': 0.0
    }

    try:
        response = requests.post(openai_url, headers=headers, json=payload)
        response_data = response.json()

        # 获取模型的回答
        answer = response_data['choices'][0]['message']['content']

        # 将回答添加到对话历史
        dialogue_history.append({"role": "assistant", "content": answer})

        if len(dialogue_history) >= 6:
            # 保留最后两条数据并重置为初始状态
            dialogue_history = dialogue_history[-2:]

        return {'answer': answer,'code':'200'}

    except Exception as e:
        return {'error': str(e)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=)//port