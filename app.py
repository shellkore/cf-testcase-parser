from flask import Flask,request,render_template
from testcaseParser import parser
import os

app = Flask(__name__)

def makezip(contestNumber):
	BASE_PATH = 'temp'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/download',methods=['POST'])
def download():
	contest = request.form['contest']
	parser(contest)
	# makezip(contest)
	return render_template('download.html',contest = contest)


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)