import os
from dotenv import load_dotenv
load_dotenv()

sender=os.getenv('sender')
receiver=os.getenv('receiver')
password=os.getenv('password')
from flask import Flask, render_template, request
from requests import get
blog=Flask(__name__)
@blog.route('/')
def home():
    blo=get('https://api.npoint.io/c6bd7919ce3b6779a0f6')
    data=blo.json()
    return render_template('index.html', blog=data)

@blog.route('/about')
def about():
    return render_template('about.html')

@blog.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method=='POST':
        user_name=request.form['uname']
        user_email=request.form['email']
        phone_number=request.form['tel']
        user_feedback=request.form['feedback']
        

        import smtplib
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user='mondaymotivation102@gmail.com', password=password)
            connection.sendmail(from_addr=sender, to_addrs=receiver, 
                                msg=f'Subject:Messaage from {user_name} \n\n{user_feedback}\n\n{user_email}\n\n{phone_number}')
        
        return render_template('contact.html', message='Successfully sent message')

    
        
    return render_template('contact.html')


@blog.route('/post/<int:num>')
def post(num):
    blo=get('https://api.npoint.io/c6bd7919ce3b6779a0f6')
    data=blo.json()
    return render_template('post.html', id=num, blog=data )



if __name__=='__main__':
    blog.run(debug=True)