from flask import Flask, render_template, request
from chatTerminator import chatGenerator
app = Flask(__name__)

@app.route('/')
def render_main():
  return render_template('index.html')

@app.route('/', methods = ['POST', 'GET'])
def chat_output():
  if request.method == 'POST':
    result = request.form["chat"]
    num = int(request.form["number"])
    message = chatGenerator(result, num)
    return render_template('index.html',output=message)



if __name__ == '__main__':
  app.run(debug=True, port=54321)

