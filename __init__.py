from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from wtforms import *

class register(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    mobile = StringField('Mobile Number', [validators.Length(min=10, max=10)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    age = IntegerField('Age', [validators.Length(min=0)])
    gender = BooleanField('gender',[validators.DataRequired()])

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'panace'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM patients")
    data = cur.fetchall()
    cur.close()




    return render_template('index.html', students=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['uname']
        email = request.form['email']
        phone = request.form['mobnumber']
        age = request.form['age']
        gender = request.form['gender']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO patients (name, mobile, email, age, gender) VALUES (%s, %s, %s, %s, %s)", (name,phone,email,age,gender))
        mysql.connection.commit()
        return render_template('General1.html')


@app.route('/gen1', methods = ['POST','GET'])
def gen1():
    if request.method == "POST":
        # cur = mysql.connection.cursor()
        # cur.execute("SELECT id from patients where id = SELECT max(id) from patients")
        sym = []
        obese = request.form['obese']
        cig = request.form['cigarettes']
        chol = request.form['cholesterol']
        hyp = request.form['hypertension']
        diab = request.form['diabetes']
        sym.append(obese)
        sym.append(cig)
        sym.append(chol)
        sym.append(hyp)
        sym.append(diab)
        session["sym"] = sym
        return render_template('General2.html',sym = sym)

@app.route('/gen2', methods = ['POST', 'GET'])
def gen2():
    data = session.get('sym')
    print(data)
    if request.method=='POST':
        print(request.form.getlist('symptoms'))
        syms = request.form.getlist('symptoms')
        if ('Diminished appetite' or 'Fatigue')in syms:
            template = 'Thyroid1.html'
        elif 'Extreme Headache' in syms:
            template = 'headache1.html'
        elif ('Fatigue' or 'Frequent Hunger') in syms:
            template = 'diabetes1.html'
        data = data + syms
        session['data'] = data
        return render_template(template, data = data)

@app.route('/thy1',methods = ['POST','GET'])
def thy1():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['weightgain']
        data.append(wtgn)
        session['data']=data
        return render_template('Thyroid2.html',data=data)

@app.route('/thy2',methods = ['POST','GET'])
def thy2():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['kgs']
        data.append(wtgn)
        session['data']=data
        return render_template('Thyroid3.html',data=data)

@app.route('/thy3',methods = ['POST','GET'])
def thy3():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['eatless']
        data.append(wtgn)
        session['data']=data
        return render_template('Thyroid4.html',data=data)

@app.route('/thy4',methods = ['POST','GET'])
def thy4():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['signs']
        data.append(wtgn)
        session['data']=data
        return render_template('Thyroid5.html',data=data)

@app.route('/thy5',methods = ['POST','GET'])
def thy5():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['TSH']
        data.append(wtgn)
        session['data']=data
        print(data)
        cur = mysql.connection.cursor()
        cur.execute("SELECT max(id) from patients")
        id_data = cur.fetchone()
        print(id_data[0])
        data = '\n'.join(data)
        cur.execute("""
               UPDATE patients
               SET symptoms = %s
               WHERE id = %s
            """, (data, id_data[0]))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return render_template('Thank.html',data=data)

@app.route('/hd1',methods = ['POST','GET'])
def hd1():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['both']
        data.append(wtgn)
        session['data']=data
        return render_template('headache2.html',data=data)

@app.route('/hd2',methods = ['POST','GET'])
def hd2():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['head']
        data.append(wtgn)
        session['data']=data
        return render_template('headache3.html',data=data)

@app.route('/hd3',methods = ['POST','GET'])
def hd3():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['both']
        data.append(wtgn)
        session['data']=data
        return render_template('headache4.html',data=data)

@app.route('/hd4',methods = ['POST','GET'])
def hd4():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['exper']
        data.append(wtgn)
        session['data']=data
        return render_template('headache5.html',data=data)

@app.route('/hd5',methods = ['POST','GET'])
def hd5():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['exper']
        data.append(wtgn)
        session['data']=data
        
        print(data)
        cur = mysql.connection.cursor()
        cur.execute("SELECT max(id) from patients")
        id_data = cur.fetchone()
        print(id_data[0])
        data = '.\n'.join(data)
        cur.execute("""
               UPDATE patients
               SET symptoms = %s
               WHERE id = %s
            """, (data, id_data[0]))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return render_template('Thank.html',data=data)


@app.route('/db1',methods = ['POST','GET'])
def db1():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['hb']
        data.append(wtgn)
        session['data']=data
        return render_template('diabetes2.html',data=data)

@app.route('/db2',methods = ['POST','GET'])
def db2():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['report']
        data.append(wtgn)
        session['data']=data
        return render_template('diabetes3.html',data=data)

@app.route('/db3',methods = ['POST','GET'])
def db3():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['both']
        data.append(wtgn)
        session['data']=data
        return render_template('diabetes4.html',data=data)

@app.route('/db4',methods = ['POST','GET'])
def db4():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['diag']
        data.append(wtgn)
        session['data']=data
        return render_template('diabetes5.html',data=data)

@app.route('/db5',methods = ['POST','GET'])
def db5():
    data = session.get('data')
    if request.method=='POST':
        wtgn = request.form['excess']
        data.append(wtgn)
        session['data']=data
        print(data)
        cur = mysql.connection.cursor()
        cur.execute("SELECT max(id) from patients")
        id_data = cur.fetchone()
        print(id_data[0])
        data = '\n'.join(data)
        cur.execute("""
               UPDATE patients
               SET symptoms = %s
               WHERE id = %s
            """, (data, id_data[0]))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return render_template('Thank.html',data=data)



# @app.route('/delete/<string:id_data>', methods = ['GET'])
# def delete(id_data):
#     flash("Record Has Been Deleted Successfully")
#     cur = mysql.connection.cursor()
#     cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
#     mysql.connection.commit()
#     return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))



@app.route('/view',methods = ['POST'])
def view():
    if request.method == 'POST':
        phone = request.form['mobnumber']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM patients WHERE mobile=%s",(phone,))
        data = cur.fetchall()
        cur.close()
        return render_template('view.html',data = data)




if __name__ == "__main__":
    app.run(debug=True)
