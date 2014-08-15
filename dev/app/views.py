from flask import render_template
from flask import jsonify
from app import app
import MySQLdb as mdb

#db = mdb.connect(user="root", password="password",host="localhost", db="world_innodb", charset='utf8')
db= mdb.connect('localhost', 'root', 'password', 'school');

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route("/schools_json")
def schools_json():
    with db:
        cur = db.cursor()
        cur.execute("SELECT School, School_Type, 2013_14_GRADE_PRED, \
            2012_13_GRADE, 2011_12_GRADE, 2010_11_GRADE, 2009_10_GRADE, 2008_09_GRADE, 2007_08_GRADE, 2006_07_GRADE, \
            2012_13_PERF_PERC, 2011_12_PERF_PERC, 2010_11_PERF_PERC, 2009_10_PERF_PERC, 2008_09_PERF_PERC, 2007_08_PERF_PERC, 2006_07_PERF_PERC \
            FROM Final")
        query_results = cur.fetchall()
    schools = []
    for result in query_results:
        schools.append(dict(school=result[0], schooltype=result[1], grade2014=result[2], \
            grade2013=result[3], grade2012=result[4], grade2011=result[5], grade2010=result[6], grade2009=result[7], grade2008=result[8], grade2007=result[9],\
            perc2013=result[10], perc2012=result[11], perc2011=result[12], perc2010=result[13], perc2009=result[14], perc2008=result[15], perc2007=result[16])), 
    return jsonify(dict(schools=schools))
	
@app.route("/dev")
def index_jquery():
    return render_template('index_dev.html') 

@app.route("/db_json")
def cities_json():
    with db:
        cur = db.cursor()
        cur.execute("SELECT SCHOOL_NAME, 2012_2013, 2011_2012, 2010_11, 2009_10, 2008_09, 2007_08, 2006_07 FROM Multiyear WHERE SCHOOL_NAME = 'P.S. 190 Sheffield'")
        query_results = cur.fetchall()
    cities = []
    for result in query_results:
        cities.append(dict(school=result[0], grade2013=result[1], grade2012=result[2], grade2011=result[3], grade2010=result[4], \
            grade2009=result[5], grade2008=result[6], grade2007=result[7])), 
    return jsonify(dict(cities=cities))



@app.route('/db')
def cities_page():
	with db: 
		cur = db.cursor()
		cur.execute("SELECT Name FROM city LIMIT 15;")
		query_results = cur.fetchall()
	cities = ""
	for result in query_results:
		cities += result[0]
		cities += "<br>"
	return cities

@app.route("/db_fancy")
def cities_page_fancy():
	with db:
		cur = db.cursor()
		cur.execute("SELECT Name, CountryCode, \
			Population FROM city ORDER BY Population LIMIT 15;")

		query_results = cur.fetchall()
	cities = []
	for result in query_results:
		cities.append(dict(name=result[0], country=result[1], population=result[2]))
	return render_template('cities.html', cities=cities)