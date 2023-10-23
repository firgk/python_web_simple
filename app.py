from flask import *
from threading import*


from func import *


app = Flask(__name__,static_folder="", template_folder="")


@app.route('/')
def index():
    # 获取图片文件夹中的文件列表
    content='空'
    # 在index.html后添加传入的参数
    return render_template('index.html',content=content)

    

@app.route('/printhello_flask')
def printhello_flask():
    thread = Thread(target=printhello)
    thread.start()
    return render_template('index.html')



@app.route('/returnhello_flask')
def returnhello_flask():
    content=returnhello()
    return render_template('index.html',content=content)
    



# if you need some args
# @app.route('/re_make_picer/<id>')
# def re_make_picer(id):
#     thread = Thread(target=re_make_pic, args=(id,))
#     thread.start()
#     return redirect(url_for('index'))






if __name__ == '__main__':
    app.run(debug=True)
