import falcon
import json
import mysql.connector
app=falcon.API()
mydb=mysql.connector.connect(host="localhost",user="root",password="Nirmal$31",buffered=True,database="travel")
dbcur=mydb.cursor()
class vechiele(object):
    def on_get(self, req, resp):
        resp.status=falcon.HTTP_200
        resp.content_type='text/html'
        with open('owner.html','r') as fp:
            resp.body=f.read()
    def on_post(self, req, resp):
        odata=json.loads(req.stream.read())
        f=odata['fname']
        l=odata['lname']
        tn=odata['travelsname']
        vehicle=odata['vec']
        permit=odata['permit']
        s1=("insert into vehicle (first_name,last_name,Travels_name,vehcile_count,permit) values(%s, %s, %s, %s,%s)")
        dbcur.execute(s1,(f,l,tn,vehicle,permit,))
        mydb.commit()
app.add_route('/v',vechiele())
class user(object):
    def on_get(self, req, resp):
        resp.status=falcon.HTTP_200
        resp.contend_type='text/html'
        with open("user.html",'r') as fp:
            resp.body=f.read()
    def on_post(self, req, resp):
        udata=json.loads(req.stream.read())
        f=udata["fname"]
        l=udata["lname"]
        vec=udate["count"]
        tn=udata["travelsname"]
        book=udata["booked"]
        s1=("insert into user (first_name,last_name,travels_name,vehcile_count,booked) values(%s, %s, %s, %s, %s)")
        dbcur.execute(s1,(f,l,tn,,vec,book,))
        s2=("update vehicle set book=%s where tn=%s")
        dbcur.execute(s2,(book,tn,))
        mydb.commit()
app.add_route('/u',user())
dbcur.close()
