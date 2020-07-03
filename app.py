from flask import Flask,request,render_template,url_for
from testcaseParser import parser
import os
import shutil

app = Flask(__name__)

def makezip(contestNumber):
	current_dir = os.getcwd()
	source_dir = os.path.join(current_dir,'temp',contestNumber)
	output_filename = os.path.join(current_dir,'static','zipfiles',contestNumber)
	shutil.make_archive(output_filename, 'zip', source_dir)
	print("Zip File Made")


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/download',methods=['POST'])
def download():
	contest = request.form['contest']
	if not os.path.exists(f'static/zipfiles/{contest}.zip'):
		parser(contest)
		makezip(contest)
	return render_template('download.html',contest = contest)


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)