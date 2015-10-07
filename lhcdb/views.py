from datetime import datetime

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

    # get latest configuration
    result = HardwareConnections.query.order_by(
        HardwareConnections.date_time.desc()
        ).first()

    # cast result as dictionary
    result_dict = dict(result.__dict__)

    # remove '_sa_instance_state' key
    result_dict.pop('_sa_instance_state', None)

    # render page with the latest configuration
    return render_template('index.html',
                           title='Home',
                           connections=result_dict)

@app.route('/configurations')
@app.route('/configurations/<int:page>')
def configurations(page=1):

    # list 10 configurations, paginate with 10 per page
    configs = HardwareConnections.query.order_by(
        HardwareConnections.date_time.desc()
        ).paginate(
            page, 10
            )

    # render page
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

    # get id from URL: /config?id=id_
    id_ = request.args.get('id', 1)

    # query database for configuration using id
    query = HardwareConnections.query.filter(HardwareConnections.id==id_)

    # use the first result from query
    result = query.first_or_404()

    # render page to display configuration
    return render_template('config.html',
                           title='Configurations',
                           connections=result)

@app.route('/add-config')
#@requires_auth
def add_config():

    # get latest configuration
    result = HardwareConnections.query.order_by(
        HardwareConnections.date_time.desc()
        ).first()

    # cast result as a dictionary
    result_dict = dict(result.__dict__)

    # remove '_sa_instance_state' key
    result_dict.pop('_sa_instance_state', None)

    # render form for adding a new configuration using the
    # latest configuration as template
    return render_template('add-config.html',
                           title='Add new configuration',
                           connections=result_dict)

@app.route('/remove-config')
#@requires_auth
def remove_config():
    
    # get id from URL: /config?id=id_
    id_ = request.args.get('id', -1)

    # get confirmation for removal
    confirm = request.args.get('confirm', 0)

    # cast confirm as int
    try:
        confirm = int(confirm)
    except:
        confirm = 0

    if confirm > 0:

        # remove configuration
        HardwareConnections.query.filter_by(id=id_).delete()

        # commit change to database
        try:
            db_session.commit()
        except IntegrityError as e:
            db_session.rollback()
            print str(e)
        except SQLAlchemyError as e:
            db_session.rollback()
            print str(e)

    # redirect to configurations page
    return redirect(url_for('configurations'))

@app.route('/submit-config', methods=['GET', 'POST'])
#@requires_auth
def submit_config():

    if request.method == 'POST':

        keys = []
        submission = request.form
        id_ = submission.get('id_', '')
        date_time = submission.get('date-time', '')

        if date_time == '':
            response = make_response(redirect(url_for('add_config')))
            return response

        date_time = datetime.strptime(date_time, '%m/%d/%Y %I:%M %p')

        for key, value in submission.iteritems():
            if value:
                keys.append(key)
                #print key, value

        result = HardwareConnections.query.get(id_)

        if not result:
            response = make_response(redirect(url_for('add_config')))
            return response

        lhc_dict = dict(result.__dict__)
        lhc_dict.pop('_sa_instance_state', None)
        lhc_dict.pop('id', None)
        lhc_dict.pop('date_time', None)
        lhc_dict.pop('date_time_added', None)
        lhc_dict.pop('date_time_updated', None)

        db_session.remove()

        for key in keys:
            lhc_dict[key] = submission.get(key)
            #print key, submission.get(key)

        keys.extend(lhc_dict.keys())
        keys = list(set(keys))

        lhc = HardwareConnections(
            date_time=date_time, date_time_added=datetime.now()
            )

        for key, value in lhc_dict.iteritems():
            if value == 'None':
                setattr(lhc, key, None)
            else:
                setattr(lhc, key, value)

        db_session.add(lhc)

        try:
            db_session.commit()
        except IntegrityError as e:
            db_session.rollback()
            print str(e)
        except SQLAlchemyError as e:
            db_session.rollback()
            print str(e)

        db_session.remove()

        response = make_response(redirect(url_for('configurations')))

        return response

    return 'Error!'

@app.route('/help')
def help():
    return 'I need somebody! Not just anybody!'

