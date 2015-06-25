from flask import (
    render_template, request, jsonify, make_response, abort, redirect, url_for,
    session
    )

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from lhcdb import app
from lhcdb.database import db_session
from lhcdb.models import Input, HardwareConnections
from lhcdb.auth import requires_auth

#def query():
#    #q = db_session.query(HardwareConnections).order_by(HardwareConnections.date_time).first()
#    #q = db_session.query(Input).order_by(Input.name).first()
#    q = HardwareConnections.query.order_by('date_time').first()
#    return q

@app.route('/')
@app.route('/index')
def index():
    query = HardwareConnections.query.order_by('date_time').first()
    query_dict = dict(query.__dict__)
    query_dict.pop('_sa_instance_state', None)
    return render_template('index.html',
                           title='Home',
                           connections=query_dict)

@app.route('/configurations')
def configurations():
    query = HardwareConnections.query.order_by('date_time').all()
    query = Input.query.order_by('name').all()
    print query
    return 'Hello!'

@app.route('/current-config')
def current_config():
    return "Hallo!"

@app.route('/test')
@requires_auth
def test():
    return render_template('test.html', title='Test')

@app.route('/help')
def help():
    return 'I need somebody! Not just anybody!'
