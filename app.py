from flask import *
from textblob import TextBlob

app = Flask(__name__)  
  
@app.route('/')  
def customer():  
   return render_template('page1.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():
	

	if request.method == 'POST':

		result = request.form['name']
		y=TextBlob(result)
		x = y.sentiment.polarity
		# return render_template("page2.html",result = x)
		if x<0:
			res='Sentiment: Negative sentence'
			return render_template('page2.html', result=res, input=result)
			# return res
			
		elif x==0:
			res='Sentiment: Neutral sentence'
			return render_template('page2.html', result=res, input=result)
			
		elif x>0 and x<=1:
			res='Sentiment: Positive sentence'
			return render_template('page2.html', result=res, input=result)
			
		# return x  
   
if __name__ == '__main__':  
   app.run(debug = True)