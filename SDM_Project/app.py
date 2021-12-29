from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('sign_up.html')
@app.route('/validate',methods=['GET','POST'])
def validate():
    if request.method=='POST':
        fname=request.form['fname']
        password=request.form['password']
        if str(fname)=='admin':
            if str(password)=='123':
                return render_template('home.html')
            else:
                result= 'invalid password'
        else:
            result= 'invalid admin'
        return render_template('sign_up.html',result=result)
    else:
        return render_template('sign_up.html')
@app.route('/home', methods=['POST','GET'])
def home():
    # if request.method=='POST':
        return render_template('home.html')
@app.route('/show_table',methods=['GET','POST'])
def show_table():
    if request.method=='POST':
        cname=request.form['cname']
        contact=request.form['contact']
        balance=request.form['balance']
        con = sqlite3.connect('mth.db')
        cur = con.cursor()

        # Create table
        cur.execute('''CREATE TABLE if not exists customer
                    (date date,cname text, contact text, balance VAL)''')

        # Insert a row of data
        cur.execute(f"INSERT INTO customer VALUES(?,?,?,?)", (datetime.date(datetime.now()),str(cname),str(contact),int(balance)))
        rows=cur.execute('select * from customer')
        items=[]
        for i,row in enumerate(rows):
            mydict = {'sr':i+1,'date':row[0],"cname": row[1], "contact": row[2], "balance": str(row[3])+' PKR'}
                
            items.append(mydict) #  appending the comments to the review list

        # Save (commit) the changes
        con.commit()
        return render_template('credit.html',items=items)
    else:
        return render_template('home.html')
@app.route('/credit',methods=['GET'])
def credit():
    con = sqlite3.connect('mth.db')
    cur = con.cursor()
    rows=cur.execute('select * from customer')
    items=[]
    for i,row in enumerate(rows):
        mydict = {'sr':i+1,'date':row[0],"cname": row[1], "contact": row[2], "balance": str(row[3])+' PKR'}
            
        items.append(mydict) #  appending the comments to the review list

    # Save (commit) the changes
        con.commit()
    return render_template('credit.html',items=items)

@app.route('/show_stock',methods=['GET','POST'])
def show_stock():
    if request.method=='POST':
        pname=request.form['pname']
        costp=request.form['cost_price']
        sailp=request.form['sailing_price']
        savail=request.form['stockavail']

        con = sqlite3.connect('stock.db')
        cur = con.cursor()

        # Create table
        cur.execute('''CREATE TABLE if not exists STOCK
                    (pname text,cost_price VAL, sailing_price VAL, stockavail VAL)''')

        # Insert a row of data
        cur.execute(f"INSERT INTO STOCK VALUES(?,?,?,?)",(str(pname),str(costp),str(sailp),int(savail)))
        rows=cur.execute('select * from stock')
        items=[]
        for row in rows:
            mydict = {"pname": row[0], "costp": row[1],'sailp':row[2],"stockavail": str(row[3])+' UNIT'}
                
            items.append(mydict) #  appending the comments to the review list

        # Save (commit) the changes
        con.commit()
        return render_template('stock.html',items=items)
    else:
        return render_template('stock.html')
@app.route('/stock',methods=['GET'])
def stock():
    con = sqlite3.connect('stock.db')
    cur = con.cursor()
    rows=cur.execute('select * from stock')
    items=[]
    for row in rows:
        mydict = {"pname": row[0], "costp": row[1],'sailp':row[2],"stockavail": str(row[3])+' UNIT'}
            
        items.append(mydict) #  appending the comments to the review list

    # Save (commit) the changes
    con.commit()
    return render_template('stock.html',items=items)
    return render_template('Stock.html')

# @app.route('/show_sale',methods=['GET','POST'])
# def show_sale():
#     if request.method=='POST':
#         cname=request.form['cname']
#         total=request.form['total']
#         paid=request.form['paid']
#         status=request.form['status']
#         tax=request.form['tax']
#         con = sqlite3.connect('sale.db')
#         cur = con.cursor()

#         # Create table
#         cur.execute('''CREATE TABLE if not exists customer
#                     (date date,cname text, contact text, balance VAL)''')

#         # Insert a row of data
#         cur.execute(f"INSERT INTO customer VALUES(?,?,?,?)", (datetime.date(datetime.now()),str(cname),str(paid),int(status),str(tax)))
#         rows=cur.execute('select * from customer')
#         items=[]
#         for row in rows:
#             mydict = {'date':row[0],"cname": row[1], "total": row[2], "paid": row[3],"status":row[4],"tax":  str(row[5])}
                
#             items.append(mydict) #  appending the comments to the review list

#         # Save (commit) the changes
#         con.commit()
#         return render_template('add_sale.html',items=items)
#     else:
#         return render_template('sale_list.html')
@app.route('/sale_list',methods=['GET','POST'])
def sale_list():
    return render_template('sale_list.html')
@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    return render_template('add_sale.html')
@app.route('/show_sale',methods=['GET','POST'])
def show_sale():
    if request.method=='POST':
        date=request.form['date']
        cname=request.form['cname']
        tprice=request.form['tprice']
        paid=request.form['paid']
        pstatus=request.form['pstatus']
        print(date,cname,tprice,paid,pstatus)
        con = sqlite3.connect('stock.db')
        cur = con.cursor()

        # Create table
        cur.execute('''CREATE TABLE if not exists sale
                    (date text,cname text, tprice text, paid text,pstatus text)''')

        # Insert a row of data
        cur.execute(f"INSERT INTO sale VALUES(?,?,?,?,?)",(str(date),str(cname),str(tprice),str(paid),str(pstatus)))
        rows=cur.execute('select * from sale')
        items=[]
        for row in rows:
            mydict = {"date": row[0], "cname": row[1],'tprice':row[2],"paid": str(row[3]),'pstatus':str(row[4])}
                
            items.append(mydict) #  appending the comments to the review list

        # Save (commit) the changes
        con.commit()
        return render_template('sale_list.html',items=items)
    return 'GET Method'


if __name__=="__main__":
    app.run(debug=True)