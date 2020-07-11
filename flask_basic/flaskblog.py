from flask import Flask, render_template
app = Flask(__name__)

#this is basic template for flask 

posts = [
    {'author':'user1',
    'title':'Blog Post 1',
    'content': 'First Post Content',
    'date_posted': 'June 01 2020'
    },
    {'author':'user2',
    'title':'Blog Post 2',
    'content': 'second Post Content',
    'date_posted': 'June 02 2020'
    }
    ]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title='About')




if __name__=='__main__':
    app.run(debug=True)