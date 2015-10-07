import sys
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from lhcdb.database import init_db, db_session
from lhcdb.models import Input, HardwareConnections

init_db()

lhc = HardwareConnections(
    date_time=datetime.strptime('2015-06-17 02:16 PM', '%Y-%m-%d %I:%M %p'),
    date_time_added=datetime.now(),
    )

# CAEN board 8
lhc.caen_board_8_channel_0 = 'TOFUS1'
lhc.caen_board_8_channel_1 = 'TOFUS2'
lhc.caen_board_8_channel_2 = 'TOFDS1'
lhc.caen_board_8_channel_3 = 'TOFDS1'
lhc.caen_board_8_channel_4 = 'AGUSE'
lhc.caen_board_8_channel_5 = 'AGUSW'
lhc.caen_board_8_channel_6 = 'AGDSE'
lhc.caen_board_8_channel_7 = 'AGDSW'

# CAEN board 9
lhc.caen_board_9_channel_0 = 'CRYOPMT1'
lhc.caen_board_9_channel_1 = 'CRYOPMT2'
lhc.caen_board_9_channel_2 = 'CRYOSIPM3'
lhc.caen_board_9_channel_3 = 'CRYOSIPM2'
lhc.caen_board_9_channel_4 = 'CRYOSIPM1'
lhc.caen_board_9_channel_5 = 'VETO1'
lhc.caen_board_9_channel_6 = 'VETO2'
lhc.caen_board_9_channel_7 = 'AGCOSMIC1'

# CAEN board 24
lhc.caen_board_24_channel_0 = 'HSCUS1'
lhc.caen_board_24_channel_1 = 'HSCUS2'
lhc.caen_board_24_channel_2 = 'HSCUS3'
lhc.caen_board_24_channel_3 = 'HSCUS4'
lhc.caen_board_24_channel_4 = 'HSCUS5'
lhc.caen_board_24_channel_5 = 'HSCUS6'
lhc.caen_board_24_channel_6 = None
lhc.caen_board_24_channel_7 = None
lhc.caen_board_24_channel_8 = None
lhc.caen_board_24_channel_9 = None
lhc.caen_board_24_channel_10 = None
lhc.caen_board_24_channel_11 = None
lhc.caen_board_24_channel_12 = None
lhc.caen_board_24_channel_13 = None
lhc.caen_board_24_channel_14 = None
lhc.caen_board_24_channel_15 = None
lhc.caen_board_24_channel_16 = None
lhc.caen_board_24_channel_17 = None
lhc.caen_board_24_channel_18 = None
lhc.caen_board_24_channel_19 = None
lhc.caen_board_24_channel_20 = None
lhc.caen_board_24_channel_21 = None
lhc.caen_board_24_channel_22 = None
lhc.caen_board_24_channel_23 = None
lhc.caen_board_24_channel_24 = None
lhc.caen_board_24_channel_25 = None
lhc.caen_board_24_channel_26 = None
lhc.caen_board_24_channel_27 = None
lhc.caen_board_24_channel_28 = None
lhc.caen_board_24_channel_29 = None
lhc.caen_board_24_channel_30 = None
lhc.caen_board_24_channel_31 = None
lhc.caen_board_24_channel_32 = 'MURS1'
lhc.caen_board_24_channel_33 = 'MURS2'
lhc.caen_board_24_channel_34 = 'MURS3'
lhc.caen_board_24_channel_35 = 'MURS4'
lhc.caen_board_24_channel_36 = 'MURS5'
lhc.caen_board_24_channel_37 = 'MURS6'
lhc.caen_board_24_channel_38 = 'MURS7'
lhc.caen_board_24_channel_39 = 'MURS8'
lhc.caen_board_24_channel_40 = 'MURS9'
lhc.caen_board_24_channel_41 = 'MURS10'
lhc.caen_board_24_channel_42 = 'MURS11'
lhc.caen_board_24_channel_43 = 'MURS12'
lhc.caen_board_24_channel_44 = 'MURS13'
lhc.caen_board_24_channel_45 = 'MURS14'
lhc.caen_board_24_channel_46 = 'MURS15'
lhc.caen_board_24_channel_47 = 'MURS16'
lhc.caen_board_24_channel_48 = 'WC1'
lhc.caen_board_24_channel_49 = 'WC2'
lhc.caen_board_24_channel_50 = 'WC3'
lhc.caen_board_24_channel_51 = 'WC4'
lhc.caen_board_24_channel_52 = 'BEAMON'
lhc.caen_board_24_channel_53 = 'TOFUS'
lhc.caen_board_24_channel_54 = 'TOFDS'
lhc.caen_board_24_channel_55 = 'PUNCH'
lhc.caen_board_24_channel_56 = 'HALO'
lhc.caen_board_24_channel_57 = 'PULSER'
lhc.caen_board_24_channel_58 = 'COSMICON'
lhc.caen_board_24_channel_59 = 'COSMIC'
lhc.caen_board_24_channel_60 = 'PILEUP'
lhc.caen_board_24_channel_61 = 'MICHEL'
lhc.caen_board_24_channel_62 = 'LARSCINT'
lhc.caen_board_24_channel_63 = 'MURS'

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

