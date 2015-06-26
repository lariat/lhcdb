from flask import (
    render_template, request, jsonify, make_response, abort, redirect, url_for,
    session
    )

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from lhcdb import app
from lhcdb.database import db_session
from lhcdb.models import Input, HardwareConnections
from lhcdb.auth import requires_auth

@app.route('/')
@app.route('/index')
def index():
    result = HardwareConnections.query.order_by('date_time').first()
    result_dict = dict(result.__dict__)
    result_dict.pop('_sa_instance_state', None)
    return render_template('index.html',
                           title='Home',
                           connections=result_dict)

@app.route('/configurations')
@app.route('/configurations/<int:page>')
def configurations(page=1):
    #query = HardwareConnections.query.order_by('date_time').all()
    #query = HardwareConnections.query.with_entities(
    #    HardwareConnections.id,
    #    HardwareConnections.date_time,
    #    HardwareConnections.date_time_added,
    #    HardwareConnections.date_time_updated,
    #    ).order_by('date_time').all()
    configs = HardwareConnections.query.order_by('date_time').paginate(
        page, 10
        )
    return render_template('configurations.html',
                           configurations=configs,
                           title='Configurations')
    return 'Hello!'

@app.route('/inputs')
def inputs():
    query = db_session.query(Input.name).all()
    #query = Input.query.with_entities(Input.name).all()
    results = zip(*query)[0]
    return render_template('inputs.html',
                           title='Inputs',
                           inputs=results)

@app.route('/config')
def config():
    id_ = request.args.get('id', 1)
    query = HardwareConnections.query.filter(HardwareConnections.id==id_)
    result = query.first_or_404()
    return render_template('config.html',
                           title='Configurations',
                           connections=result)

@app.route('/add-config')
#@requires_auth
def add_config():
    result = HardwareConnections.query.order_by('date_time').first()
    result_dict = dict(result.__dict__)
    result_dict.pop('_sa_instance_state', None)
    return render_template('add-config.html',
                           title='Add new configuration',
                           connections=result_dict)

@app.route('/submit-config', methods=['GET', 'POST'])
#@requires_auth
def submit_config():
    if request.method == 'POST':
        print request.form
        #print request.form.get('caen-board-7-channel-32', None)
        response = make_response(redirect(url_for('add_config')))
        return response
    return 'Error!'

@app.route('/help')
def help():
    return 'I need somebody! Not just anybody!'
