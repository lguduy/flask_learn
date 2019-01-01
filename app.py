from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to liangyu\'s app!'


@app.route('/user/<name>')
def user_page(name):
    return 'hello, {}'.format(name)


@app.route('/test')
def test_url_for():
    """
    url_for: 输入视图函数名返回绑定的url
    """
    print(url_for('home'))                       # 视图函数：home, 输出：/
    print(url_for('user_page', name='liangyu'))  # 视图函数：user_page, 输出：/user/greyli
    print(url_for('user_page', name='xuting'))   # 视图函数：user_page, 输出：/user/peter
    print(url_for('test_url_for'))               # 视图函数：test_url_for, 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))        # 输出：/test?num=2
    return 'test page'
