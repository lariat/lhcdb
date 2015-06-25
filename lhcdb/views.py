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

@app.route('/inputs')
def inputs():
    query = db_session.query(Input.name).all()
    results = zip(*query)[0]
    return render_template('inputs.html',
                           title='Inputs',
                           inputs=results)

@app.route('/configurations')
def configurations():
    query = HardwareConnections.query.order_by('date_time').all()
    print query
    for result in query:
        query_dict = dict(result.__dict__)
        query_dict.pop('_sa_instance_state', None)
    return 'Hello!'

@app.route('/add-configuration')
@requires_auth
def add_configuration():
    query = HardwareConnections.query.order_by('date_time').first()
    query_dict = dict(query.__dict__)
    query_dict.pop('_sa_instance_state', None)
    return render_template('index.html',
                           title='Add new configuration',
                           connections=query_dict)

@app.route('/test')
@requires_auth
def test():
    return render_template('test.html', title='Test')

@app.route('/help')
def help():
    return 'I need somebody! Not just anybody!'
