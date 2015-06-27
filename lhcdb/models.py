from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY

from lhcdb.database import Base

class Input(Base):
    """ Inputs. """

    __tablename__ = 'lhcdb_input_names'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Input %r>' % (self.name)

class HardwareConnections(Base):
    """ Hardware connections. """

    __tablename__ = 'lhcdb_hardware_connections'

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime(timezone=False), unique=True, nullable=False)
    date_time_added = Column(
        DateTime(timezone=False), unique=True, nullable=False)
    date_time_updated = Column(
        DateTime(timezone=False), unique=True, nullable=False)

    # CAEN board 7: CAEN V1740, 64 channels, channels 32 to 63
    caen_board_7_channel_32 = Column(String, unique=False)
    caen_board_7_channel_33 = Column(String, unique=False)
    caen_board_7_channel_34 = Column(String, unique=False)
    caen_board_7_channel_35 = Column(String, unique=False)
    caen_board_7_channel_36 = Column(String, unique=False)
    caen_board_7_channel_37 = Column(String, unique=False)
    caen_board_7_channel_38 = Column(String, unique=False)
    caen_board_7_channel_39 = Column(String, unique=False)
    caen_board_7_channel_40 = Column(String, unique=False)
    caen_board_7_channel_41 = Column(String, unique=False)
    caen_board_7_channel_42 = Column(String, unique=False)
    caen_board_7_channel_43 = Column(String, unique=False)
    caen_board_7_channel_44 = Column(String, unique=False)
    caen_board_7_channel_45 = Column(String, unique=False)
    caen_board_7_channel_46 = Column(String, unique=False)
    caen_board_7_channel_47 = Column(String, unique=False)
    caen_board_7_channel_48 = Column(String, unique=False)
    caen_board_7_channel_49 = Column(String, unique=False)
    caen_board_7_channel_50 = Column(String, unique=False)
    caen_board_7_channel_51 = Column(String, unique=False)
    caen_board_7_channel_52 = Column(String, unique=False)
    caen_board_7_channel_53 = Column(String, unique=False)
    caen_board_7_channel_54 = Column(String, unique=False)
    caen_board_7_channel_55 = Column(String, unique=False)
    caen_board_7_channel_56 = Column(String, unique=False)
    caen_board_7_channel_57 = Column(String, unique=False)
    caen_board_7_channel_58 = Column(String, unique=False)
    caen_board_7_channel_59 = Column(String, unique=False)
    caen_board_7_channel_60 = Column(String, unique=False)
    caen_board_7_channel_61 = Column(String, unique=False)
    caen_board_7_channel_62 = Column(String, unique=False)
    caen_board_7_channel_63 = Column(String, unique=False)

    # CAEN board 8: CAEN V1751, 8 channels
    caen_board_8_channel_0 = Column(String, unique=False)
    caen_board_8_channel_1 = Column(String, unique=False)
    caen_board_8_channel_2 = Column(String, unique=False)
    caen_board_8_channel_3 = Column(String, unique=False)
    caen_board_8_channel_4 = Column(String, unique=False)
    caen_board_8_channel_5 = Column(String, unique=False)
    caen_board_8_channel_6 = Column(String, unique=False)
    caen_board_8_channel_7 = Column(String, unique=False)

    # CAEN board 9: CAEN V1751, 8 channels
    caen_board_9_channel_0 = Column(String, unique=False)
    caen_board_9_channel_1 = Column(String, unique=False)
    caen_board_9_channel_2 = Column(String, unique=False)
    caen_board_9_channel_3 = Column(String, unique=False)
    caen_board_9_channel_4 = Column(String, unique=False)
    caen_board_9_channel_5 = Column(String, unique=False)
    caen_board_9_channel_6 = Column(String, unique=False)
    caen_board_9_channel_7 = Column(String, unique=False)

    # CAEN board 24: CAEN V1740, 64 channels
    caen_board_24_channel_0 = Column(String, unique=False)
    caen_board_24_channel_1 = Column(String, unique=False)
    caen_board_24_channel_2 = Column(String, unique=False)
    caen_board_24_channel_3 = Column(String, unique=False)
    caen_board_24_channel_4 = Column(String, unique=False)
    caen_board_24_channel_5 = Column(String, unique=False)
    caen_board_24_channel_6 = Column(String, unique=False)
    caen_board_24_channel_7 = Column(String, unique=False)
    caen_board_24_channel_8 = Column(String, unique=False)
    caen_board_24_channel_9 = Column(String, unique=False)
    caen_board_24_channel_10 = Column(String, unique=False)
    caen_board_24_channel_11 = Column(String, unique=False)
    caen_board_24_channel_12 = Column(String, unique=False)
    caen_board_24_channel_13 = Column(String, unique=False)
    caen_board_24_channel_14 = Column(String, unique=False)
    caen_board_24_channel_15 = Column(String, unique=False)
    caen_board_24_channel_16 = Column(String, unique=False)
    caen_board_24_channel_17 = Column(String, unique=False)
    caen_board_24_channel_18 = Column(String, unique=False)
    caen_board_24_channel_19 = Column(String, unique=False)
    caen_board_24_channel_20 = Column(String, unique=False)
    caen_board_24_channel_21 = Column(String, unique=False)
    caen_board_24_channel_22 = Column(String, unique=False)
    caen_board_24_channel_23 = Column(String, unique=False)
    caen_board_24_channel_24 = Column(String, unique=False)
    caen_board_24_channel_25 = Column(String, unique=False)
    caen_board_24_channel_26 = Column(String, unique=False)
    caen_board_24_channel_27 = Column(String, unique=False)
    caen_board_24_channel_28 = Column(String, unique=False)
    caen_board_24_channel_29 = Column(String, unique=False)
    caen_board_24_channel_30 = Column(String, unique=False)
    caen_board_24_channel_31 = Column(String, unique=False)
    caen_board_24_channel_32 = Column(String, unique=False)
    caen_board_24_channel_33 = Column(String, unique=False)
    caen_board_24_channel_34 = Column(String, unique=False)
    caen_board_24_channel_35 = Column(String, unique=False)
    caen_board_24_channel_36 = Column(String, unique=False)
    caen_board_24_channel_37 = Column(String, unique=False)
    caen_board_24_channel_38 = Column(String, unique=False)
    caen_board_24_channel_39 = Column(String, unique=False)
    caen_board_24_channel_40 = Column(String, unique=False)
    caen_board_24_channel_41 = Column(String, unique=False)
    caen_board_24_channel_42 = Column(String, unique=False)
    caen_board_24_channel_43 = Column(String, unique=False)
    caen_board_24_channel_44 = Column(String, unique=False)
    caen_board_24_channel_45 = Column(String, unique=False)
    caen_board_24_channel_46 = Column(String, unique=False)
    caen_board_24_channel_47 = Column(String, unique=False)
    caen_board_24_channel_48 = Column(String, unique=False)
    caen_board_24_channel_49 = Column(String, unique=False)
    caen_board_24_channel_50 = Column(String, unique=False)
    caen_board_24_channel_51 = Column(String, unique=False)
    caen_board_24_channel_52 = Column(String, unique=False)
    caen_board_24_channel_53 = Column(String, unique=False)
    caen_board_24_channel_54 = Column(String, unique=False)
    caen_board_24_channel_55 = Column(String, unique=False)
    caen_board_24_channel_56 = Column(String, unique=False)
    caen_board_24_channel_57 = Column(String, unique=False)
    caen_board_24_channel_58 = Column(String, unique=False)
    caen_board_24_channel_59 = Column(String, unique=False)
    caen_board_24_channel_60 = Column(String, unique=False)
    caen_board_24_channel_61 = Column(String, unique=False)
    caen_board_24_channel_62 = Column(String, unique=False)
    caen_board_24_channel_63 = Column(String, unique=False)

    def __init__(self, date_time, date_time_added):
        self.date_time = date_time
        self.date_time_added = date_time_added
        self.date_time_updated = date_time_added

    def __repr__(self):
        return '<HardwareConnections %r>' % (self.date_time)

