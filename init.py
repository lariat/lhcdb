import sys
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from lhcdb.database import init_db, db_session
from lhcdb.models import Input, HardwareConnections

init_db()

#tpc_induction_input_names = [
#    'IND{}'.format(wire) for wire in xrange(0+1, 240+1)
#    ]
#
#tpc_collection_input_names = [
#    'COL{}'.format(wire) for wire in xrange(0+1, 240+1)
#    ]

input_names = [
    'CRYOPMT1',
    'CRYOPMT2',
    'CRYOSIPM1',
    'CRYOSIPM2',
    'CRYOSIPM3',
    'TOFUS1',
    'TOFUS2',
    'TOFUS3',
    'TOFUS4',
    'TOFDS1',
    'TOFDS2',
    'AGUSW',
    'AGUSE',
    'AGDSE',
    'AGDSW',
    'AGCOSMIC1',
    'VETO1',
    'VETO2',
    'SC1',
    'SC2',
    'SC3',
    'MURS1',
    'MURS2',
    'MURS3',
    'MURS4',
    'MURS5',
    'MURS6',
    'MURS7',
    'MURS8',
    'MURS9',
    'MURS10',
    'MURS11',
    'MURS12',
    'MURS13',
    'MURS14',
    'MURS15',
    'MURS16',
    'HSCUS1',
    'HSCUS2',
    'HSCUS3',
    'HSCUS4',
    'HSCUS5',
    'HSCUS6',
    ]

trigger_input_names = [
    'WC1',
    'WC2',
    'WC3',
    'WC4',
    'BEAMON',
    'TOFUS',
    'TOFDS',
    'PUNCH',
    'HALO',
    'PULSER',
    'COSMICON',
    'COSMIC',
    'PILEUP',
    'MICHEL',
    'LARSCINT',
    'MURS',
    ]

input_lists = [
    #tpc_induction_input_names,
    #tpc_collection_input_names,
    input_names,
    trigger_input_names,
]

for input_list in input_lists:
    for input_name in input_list:
        db_session.add(
            Input(name=input_name)
            )

lhc = HardwareConnections(
    date_time=datetime.strptime('2015-06-17 02:16 PM', '%Y-%m-%d %I:%M %p'),
    date_time_added=datetime.now(),
    )

## CAEN board 0
#lhc.caen_board_0_channel_0 = 'IND240'
#lhc.caen_board_0_channel_1 = 'IND239'
#lhc.caen_board_0_channel_2 = 'IND238'
#lhc.caen_board_0_channel_3 = 'IND237'
#lhc.caen_board_0_channel_4 = 'IND236'
#lhc.caen_board_0_channel_5 = 'IND235'
#lhc.caen_board_0_channel_6 = 'IND234'
#lhc.caen_board_0_channel_7 = 'IND233'
#lhc.caen_board_0_channel_8 = 'IND232'
#lhc.caen_board_0_channel_9 = 'IND231'
#lhc.caen_board_0_channel_10 = 'IND230'
#lhc.caen_board_0_channel_11 = 'IND229'
#lhc.caen_board_0_channel_12 = 'IND228'
#lhc.caen_board_0_channel_13 = 'IND227'
#lhc.caen_board_0_channel_14 = 'IND226'
#lhc.caen_board_0_channel_15 = 'IND225'
#lhc.caen_board_0_channel_16 = 'IND224'
#lhc.caen_board_0_channel_17 = 'IND223'
#lhc.caen_board_0_channel_18 = 'IND222'
#lhc.caen_board_0_channel_19 = 'IND221'
#lhc.caen_board_0_channel_20 = 'IND220'
#lhc.caen_board_0_channel_21 = 'IND219'
#lhc.caen_board_0_channel_22 = 'IND218'
#lhc.caen_board_0_channel_23 = 'IND217'
#lhc.caen_board_0_channel_24 = 'IND216'
#lhc.caen_board_0_channel_25 = 'IND215'
#lhc.caen_board_0_channel_26 = 'IND214'
#lhc.caen_board_0_channel_27 = 'IND213'
#lhc.caen_board_0_channel_28 = 'IND212'
#lhc.caen_board_0_channel_29 = 'IND211'
#lhc.caen_board_0_channel_30 = 'IND210'
#lhc.caen_board_0_channel_31 = 'IND209'
#lhc.caen_board_0_channel_32 = 'IND208'
#lhc.caen_board_0_channel_33 = 'IND207'
#lhc.caen_board_0_channel_34 = 'IND206'
#lhc.caen_board_0_channel_35 = 'IND205'
#lhc.caen_board_0_channel_36 = 'IND204'
#lhc.caen_board_0_channel_37 = 'IND203'
#lhc.caen_board_0_channel_38 = 'IND202'
#lhc.caen_board_0_channel_39 = 'IND201'
#lhc.caen_board_0_channel_40 = 'IND200'
#lhc.caen_board_0_channel_41 = 'IND199'
#lhc.caen_board_0_channel_42 = 'IND198'
#lhc.caen_board_0_channel_43 = 'IND197'
#lhc.caen_board_0_channel_44 = 'IND196'
#lhc.caen_board_0_channel_45 = 'IND195'
#lhc.caen_board_0_channel_46 = 'IND194'
#lhc.caen_board_0_channel_47 = 'IND193'
#lhc.caen_board_0_channel_48 = 'IND192'
#lhc.caen_board_0_channel_49 = 'IND191'
#lhc.caen_board_0_channel_50 = 'IND190'
#lhc.caen_board_0_channel_51 = 'IND189'
#lhc.caen_board_0_channel_52 = 'IND188'
#lhc.caen_board_0_channel_53 = 'IND187'
#lhc.caen_board_0_channel_54 = 'IND186'
#lhc.caen_board_0_channel_55 = 'IND185'
#lhc.caen_board_0_channel_56 = 'IND184'
#lhc.caen_board_0_channel_57 = 'IND183'
#lhc.caen_board_0_channel_58 = 'IND182'
#lhc.caen_board_0_channel_59 = 'IND181'
#lhc.caen_board_0_channel_60 = 'IND180'
#lhc.caen_board_0_channel_61 = 'IND179'
#lhc.caen_board_0_channel_62 = 'IND178'
#lhc.caen_board_0_channel_63 = 'IND177'
#
## CAEN board 1
#lhc.caen_board_1_channel_0 = 'IND176'
#lhc.caen_board_1_channel_1 = 'IND175'
#lhc.caen_board_1_channel_2 = 'IND174'
#lhc.caen_board_1_channel_3 = 'IND173'
#lhc.caen_board_1_channel_4 = 'IND172'
#lhc.caen_board_1_channel_5 = 'IND171'
#lhc.caen_board_1_channel_6 = 'IND170'
#lhc.caen_board_1_channel_7 = 'IND169'
#lhc.caen_board_1_channel_8 = 'IND168'
#lhc.caen_board_1_channel_9 = 'IND167'
#lhc.caen_board_1_channel_10 = 'IND166'
#lhc.caen_board_1_channel_11 = 'IND165'
#lhc.caen_board_1_channel_12 = 'IND164'
#lhc.caen_board_1_channel_13 = 'IND163'
#lhc.caen_board_1_channel_14 = 'IND162'
#lhc.caen_board_1_channel_15 = 'IND161'
#lhc.caen_board_1_channel_16 = 'IND160'
#lhc.caen_board_1_channel_17 = 'IND159'
#lhc.caen_board_1_channel_18 = 'IND158'
#lhc.caen_board_1_channel_19 = 'IND157'
#lhc.caen_board_1_channel_20 = 'IND156'
#lhc.caen_board_1_channel_21 = 'IND155'
#lhc.caen_board_1_channel_22 = 'IND154'
#lhc.caen_board_1_channel_23 = 'IND153'
#lhc.caen_board_1_channel_24 = 'IND152'
#lhc.caen_board_1_channel_25 = 'IND151'
#lhc.caen_board_1_channel_26 = 'IND150'
#lhc.caen_board_1_channel_27 = 'IND149'
#lhc.caen_board_1_channel_28 = 'IND148'
#lhc.caen_board_1_channel_29 = 'IND147'
#lhc.caen_board_1_channel_30 = 'IND146'
#lhc.caen_board_1_channel_31 = 'IND145'
#lhc.caen_board_1_channel_32 = 'IND144'
#lhc.caen_board_1_channel_33 = 'IND143'
#lhc.caen_board_1_channel_34 = 'IND142'
#lhc.caen_board_1_channel_35 = 'IND141'
#lhc.caen_board_1_channel_36 = 'IND140'
#lhc.caen_board_1_channel_37 = 'IND139'
#lhc.caen_board_1_channel_38 = 'IND138'
#lhc.caen_board_1_channel_39 = 'IND137'
#lhc.caen_board_1_channel_40 = 'IND136'
#lhc.caen_board_1_channel_41 = 'IND135'
#lhc.caen_board_1_channel_42 = 'IND134'
#lhc.caen_board_1_channel_43 = 'IND133'
#lhc.caen_board_1_channel_44 = 'IND132'
#lhc.caen_board_1_channel_45 = 'IND131'
#lhc.caen_board_1_channel_46 = 'IND130'
#lhc.caen_board_1_channel_47 = 'IND129'
#lhc.caen_board_1_channel_48 = 'IND128'
#lhc.caen_board_1_channel_49 = 'IND127'
#lhc.caen_board_1_channel_50 = 'IND126'
#lhc.caen_board_1_channel_51 = 'IND125'
#lhc.caen_board_1_channel_52 = 'IND124'
#lhc.caen_board_1_channel_53 = 'IND123'
#lhc.caen_board_1_channel_54 = 'IND122'
#lhc.caen_board_1_channel_55 = 'IND121'
#lhc.caen_board_1_channel_56 = 'IND120'
#lhc.caen_board_1_channel_57 = 'IND119'
#lhc.caen_board_1_channel_58 = 'IND118'
#lhc.caen_board_1_channel_59 = 'IND117'
#lhc.caen_board_1_channel_60 = 'IND116'
#lhc.caen_board_1_channel_61 = 'IND115'
#lhc.caen_board_1_channel_62 = 'IND114'
#lhc.caen_board_1_channel_63 = 'IND113'
#
## CAEN board 2
#lhc.caen_board_2_channel_0 = 'IND112'
#lhc.caen_board_2_channel_1 = 'IND111'
#lhc.caen_board_2_channel_2 = 'IND110'
#lhc.caen_board_2_channel_3 = 'IND109'
#lhc.caen_board_2_channel_4 = 'IND108'
#lhc.caen_board_2_channel_5 = 'IND107'
#lhc.caen_board_2_channel_6 = 'IND106'
#lhc.caen_board_2_channel_7 = 'IND105'
#lhc.caen_board_2_channel_8 = 'IND104'
#lhc.caen_board_2_channel_9 = 'IND103'
#lhc.caen_board_2_channel_10 = 'IND102'
#lhc.caen_board_2_channel_11 = 'IND101'
#lhc.caen_board_2_channel_12 = 'IND100'
#lhc.caen_board_2_channel_13 = 'IND99'
#lhc.caen_board_2_channel_14 = 'IND98'
#lhc.caen_board_2_channel_15 = 'IND97'
#lhc.caen_board_2_channel_16 = 'IND96'
#lhc.caen_board_2_channel_17 = 'IND95'
#lhc.caen_board_2_channel_18 = 'IND94'
#lhc.caen_board_2_channel_19 = 'IND93'
#lhc.caen_board_2_channel_20 = 'IND92'
#lhc.caen_board_2_channel_21 = 'IND91'
#lhc.caen_board_2_channel_22 = 'IND90'
#lhc.caen_board_2_channel_23 = 'IND89'
#lhc.caen_board_2_channel_24 = 'IND88'
#lhc.caen_board_2_channel_25 = 'IND87'
#lhc.caen_board_2_channel_26 = 'IND86'
#lhc.caen_board_2_channel_27 = 'IND85'
#lhc.caen_board_2_channel_28 = 'IND84'
#lhc.caen_board_2_channel_29 = 'IND83'
#lhc.caen_board_2_channel_30 = 'IND82'
#lhc.caen_board_2_channel_31 = 'IND81'
#lhc.caen_board_2_channel_32 = 'IND80'
#lhc.caen_board_2_channel_33 = 'IND79'
#lhc.caen_board_2_channel_34 = 'IND78'
#lhc.caen_board_2_channel_35 = 'IND77'
#lhc.caen_board_2_channel_36 = 'IND76'
#lhc.caen_board_2_channel_37 = 'IND75'
#lhc.caen_board_2_channel_38 = 'IND74'
#lhc.caen_board_2_channel_39 = 'IND73'
#lhc.caen_board_2_channel_40 = 'IND72'
#lhc.caen_board_2_channel_41 = 'IND71'
#lhc.caen_board_2_channel_42 = 'IND70'
#lhc.caen_board_2_channel_43 = 'IND69'
#lhc.caen_board_2_channel_44 = 'IND68'
#lhc.caen_board_2_channel_45 = 'IND67'
#lhc.caen_board_2_channel_46 = 'IND66'
#lhc.caen_board_2_channel_47 = 'IND65'
#lhc.caen_board_2_channel_48 = 'IND64'
#lhc.caen_board_2_channel_49 = 'IND63'
#lhc.caen_board_2_channel_50 = 'IND62'
#lhc.caen_board_2_channel_51 = 'IND61'
#lhc.caen_board_2_channel_52 = 'IND60'
#lhc.caen_board_2_channel_53 = 'IND59'
#lhc.caen_board_2_channel_54 = 'IND58'
#lhc.caen_board_2_channel_55 = 'IND57'
#lhc.caen_board_2_channel_56 = 'IND56'
#lhc.caen_board_2_channel_57 = 'IND55'
#lhc.caen_board_2_channel_58 = 'IND54'
#lhc.caen_board_2_channel_59 = 'IND53'
#lhc.caen_board_2_channel_60 = 'IND52'
#lhc.caen_board_2_channel_61 = 'IND51'
#lhc.caen_board_2_channel_62 = 'IND50'
#lhc.caen_board_2_channel_63 = 'IND49'
#
## CAEN board 3
#lhc.caen_board_3_channel_0 = 'IND48'
#lhc.caen_board_3_channel_1 = 'IND47'
#lhc.caen_board_3_channel_2 = 'IND46'
#lhc.caen_board_3_channel_3 = 'IND45'
#lhc.caen_board_3_channel_4 = 'IND44'
#lhc.caen_board_3_channel_5 = 'IND43'
#lhc.caen_board_3_channel_6 = 'IND42'
#lhc.caen_board_3_channel_7 = 'IND41'
#lhc.caen_board_3_channel_8 = 'IND40'
#lhc.caen_board_3_channel_9 = 'IND39'
#lhc.caen_board_3_channel_10 = 'IND38'
#lhc.caen_board_3_channel_11 = 'IND37'
#lhc.caen_board_3_channel_12 = 'IND36'
#lhc.caen_board_3_channel_13 = 'IND35'
#lhc.caen_board_3_channel_14 = 'IND34'
#lhc.caen_board_3_channel_15 = 'IND33'
#lhc.caen_board_3_channel_16 = 'IND32'
#lhc.caen_board_3_channel_17 = 'IND31'
#lhc.caen_board_3_channel_18 = 'IND30'
#lhc.caen_board_3_channel_19 = 'IND29'
#lhc.caen_board_3_channel_20 = 'IND28'
#lhc.caen_board_3_channel_21 = 'IND27'
#lhc.caen_board_3_channel_22 = 'IND26'
#lhc.caen_board_3_channel_23 = 'IND25'
#lhc.caen_board_3_channel_24 = 'IND24'
#lhc.caen_board_3_channel_25 = 'IND23'
#lhc.caen_board_3_channel_26 = 'IND22'
#lhc.caen_board_3_channel_27 = 'IND21'
#lhc.caen_board_3_channel_28 = 'IND20'
#lhc.caen_board_3_channel_29 = 'IND19'
#lhc.caen_board_3_channel_30 = 'IND18'
#lhc.caen_board_3_channel_31 = 'IND17'
#lhc.caen_board_3_channel_32 = 'IND16'
#lhc.caen_board_3_channel_33 = 'IND15'
#lhc.caen_board_3_channel_34 = 'IND14'
#lhc.caen_board_3_channel_35 = 'IND13'
#lhc.caen_board_3_channel_36 = 'IND12'
#lhc.caen_board_3_channel_37 = 'IND11'
#lhc.caen_board_3_channel_38 = 'IND10'
#lhc.caen_board_3_channel_39 = 'IND9'
#lhc.caen_board_3_channel_40 = 'IND8'
#lhc.caen_board_3_channel_41 = 'IND7'
#lhc.caen_board_3_channel_42 = 'IND6'
#lhc.caen_board_3_channel_43 = 'IND5'
#lhc.caen_board_3_channel_44 = 'IND4'
#lhc.caen_board_3_channel_45 = 'IND3'
#lhc.caen_board_3_channel_46 = 'IND2'
#lhc.caen_board_3_channel_47 = 'IND1'
#lhc.caen_board_3_channel_48 = 'COL240'
#lhc.caen_board_3_channel_49 = 'COL239'
#lhc.caen_board_3_channel_50 = 'COL238'
#lhc.caen_board_3_channel_51 = 'COL237'
#lhc.caen_board_3_channel_52 = 'COL236'
#lhc.caen_board_3_channel_53 = 'COL235'
#lhc.caen_board_3_channel_54 = 'COL234'
#lhc.caen_board_3_channel_55 = 'COL233'
#lhc.caen_board_3_channel_56 = 'COL232'
#lhc.caen_board_3_channel_57 = 'COL231'
#lhc.caen_board_3_channel_58 = 'COL230'
#lhc.caen_board_3_channel_59 = 'COL229'
#lhc.caen_board_3_channel_60 = 'COL228'
#lhc.caen_board_3_channel_61 = 'COL227'
#lhc.caen_board_3_channel_62 = 'COL226'
#lhc.caen_board_3_channel_63 = 'COL225'
#
## CAEN board 4
#lhc.caen_board_4_channel_0 = 'COL224'
#lhc.caen_board_4_channel_1 = 'COL223'
#lhc.caen_board_4_channel_2 = 'COL222'
#lhc.caen_board_4_channel_3 = 'COL221'
#lhc.caen_board_4_channel_4 = 'COL220'
#lhc.caen_board_4_channel_5 = 'COL219'
#lhc.caen_board_4_channel_6 = 'COL218'
#lhc.caen_board_4_channel_7 = 'COL217'
#lhc.caen_board_4_channel_8 = 'COL216'
#lhc.caen_board_4_channel_9 = 'COL215'
#lhc.caen_board_4_channel_10 = 'COL214'
#lhc.caen_board_4_channel_11 = 'COL213'
#lhc.caen_board_4_channel_12 = 'COL212'
#lhc.caen_board_4_channel_13 = 'COL211'
#lhc.caen_board_4_channel_14 = 'COL210'
#lhc.caen_board_4_channel_15 = 'COL209'
#lhc.caen_board_4_channel_16 = 'COL208'
#lhc.caen_board_4_channel_17 = 'COL207'
#lhc.caen_board_4_channel_18 = 'COL206'
#lhc.caen_board_4_channel_19 = 'COL205'
#lhc.caen_board_4_channel_20 = 'COL204'
#lhc.caen_board_4_channel_21 = 'COL203'
#lhc.caen_board_4_channel_22 = 'COL202'
#lhc.caen_board_4_channel_23 = 'COL201'
#lhc.caen_board_4_channel_24 = 'COL200'
#lhc.caen_board_4_channel_25 = 'COL199'
#lhc.caen_board_4_channel_26 = 'COL198'
#lhc.caen_board_4_channel_27 = 'COL197'
#lhc.caen_board_4_channel_28 = 'COL196'
#lhc.caen_board_4_channel_29 = 'COL195'
#lhc.caen_board_4_channel_30 = 'COL194'
#lhc.caen_board_4_channel_31 = 'COL193'
#lhc.caen_board_4_channel_32 = 'COL192'
#lhc.caen_board_4_channel_33 = 'COL191'
#lhc.caen_board_4_channel_34 = 'COL190'
#lhc.caen_board_4_channel_35 = 'COL189'
#lhc.caen_board_4_channel_36 = 'COL188'
#lhc.caen_board_4_channel_37 = 'COL187'
#lhc.caen_board_4_channel_38 = 'COL186'
#lhc.caen_board_4_channel_39 = 'COL185'
#lhc.caen_board_4_channel_40 = 'COL184'
#lhc.caen_board_4_channel_41 = 'COL183'
#lhc.caen_board_4_channel_42 = 'COL182'
#lhc.caen_board_4_channel_43 = 'COL181'
#lhc.caen_board_4_channel_44 = 'COL180'
#lhc.caen_board_4_channel_45 = 'COL179'
#lhc.caen_board_4_channel_46 = 'COL178'
#lhc.caen_board_4_channel_47 = 'COL177'
#lhc.caen_board_4_channel_48 = 'COL176'
#lhc.caen_board_4_channel_49 = 'COL175'
#lhc.caen_board_4_channel_50 = 'COL174'
#lhc.caen_board_4_channel_51 = 'COL173'
#lhc.caen_board_4_channel_52 = 'COL172'
#lhc.caen_board_4_channel_53 = 'COL171'
#lhc.caen_board_4_channel_54 = 'COL170'
#lhc.caen_board_4_channel_55 = 'COL169'
#lhc.caen_board_4_channel_56 = 'COL168'
#lhc.caen_board_4_channel_57 = 'COL167'
#lhc.caen_board_4_channel_58 = 'COL166'
#lhc.caen_board_4_channel_59 = 'COL165'
#lhc.caen_board_4_channel_60 = 'COL164'
#lhc.caen_board_4_channel_61 = 'COL163'
#lhc.caen_board_4_channel_62 = 'COL162'
#lhc.caen_board_4_channel_63 = 'COL161'
#
## CAEN board 5
#lhc.caen_board_5_channel_0 = 'COL150'
#lhc.caen_board_5_channel_1 = 'COL159'
#lhc.caen_board_5_channel_2 = 'COL158'
#lhc.caen_board_5_channel_3 = 'COL157'
#lhc.caen_board_5_channel_4 = 'COL156'
#lhc.caen_board_5_channel_5 = 'COL155'
#lhc.caen_board_5_channel_6 = 'COL154'
#lhc.caen_board_5_channel_7 = 'COL153'
#lhc.caen_board_5_channel_8 = 'COL152'
#lhc.caen_board_5_channel_9 = 'COL151'
#lhc.caen_board_5_channel_10 = 'COL150'
#lhc.caen_board_5_channel_11 = 'COL149'
#lhc.caen_board_5_channel_12 = 'COL148'
#lhc.caen_board_5_channel_13 = 'COL147'
#lhc.caen_board_5_channel_14 = 'COL146'
#lhc.caen_board_5_channel_15 = 'COL145'
#lhc.caen_board_5_channel_16 = 'COL144'
#lhc.caen_board_5_channel_17 = 'COL143'
#lhc.caen_board_5_channel_18 = 'COL142'
#lhc.caen_board_5_channel_19 = 'COL141'
#lhc.caen_board_5_channel_20 = 'COL140'
#lhc.caen_board_5_channel_21 = 'COL139'
#lhc.caen_board_5_channel_22 = 'COL138'
#lhc.caen_board_5_channel_23 = 'COL137'
#lhc.caen_board_5_channel_24 = 'COL136'
#lhc.caen_board_5_channel_25 = 'COL135'
#lhc.caen_board_5_channel_26 = 'COL134'
#lhc.caen_board_5_channel_27 = 'COL133'
#lhc.caen_board_5_channel_28 = 'COL132'
#lhc.caen_board_5_channel_29 = 'COL131'
#lhc.caen_board_5_channel_30 = 'COL130'
#lhc.caen_board_5_channel_31 = 'COL129'
#lhc.caen_board_5_channel_32 = 'COL128'
#lhc.caen_board_5_channel_33 = 'COL127'
#lhc.caen_board_5_channel_34 = 'COL126'
#lhc.caen_board_5_channel_35 = 'COL125'
#lhc.caen_board_5_channel_36 = 'COL124'
#lhc.caen_board_5_channel_37 = 'COL123'
#lhc.caen_board_5_channel_38 = 'COL122'
#lhc.caen_board_5_channel_39 = 'COL121'
#lhc.caen_board_5_channel_40 = 'COL120'
#lhc.caen_board_5_channel_41 = 'COL119'
#lhc.caen_board_5_channel_42 = 'COL118'
#lhc.caen_board_5_channel_43 = 'COL117'
#lhc.caen_board_5_channel_44 = 'COL116'
#lhc.caen_board_5_channel_45 = 'COL115'
#lhc.caen_board_5_channel_46 = 'COL114'
#lhc.caen_board_5_channel_47 = 'COL113'
#lhc.caen_board_5_channel_48 = 'COL112'
#lhc.caen_board_5_channel_49 = 'COL111'
#lhc.caen_board_5_channel_50 = 'COL110'
#lhc.caen_board_5_channel_51 = 'COL109'
#lhc.caen_board_5_channel_52 = 'COL108'
#lhc.caen_board_5_channel_53 = 'COL107'
#lhc.caen_board_5_channel_54 = 'COL106'
#lhc.caen_board_5_channel_55 = 'COL105'
#lhc.caen_board_5_channel_56 = 'COL104'
#lhc.caen_board_5_channel_57 = 'COL103'
#lhc.caen_board_5_channel_58 = 'COL102'
#lhc.caen_board_5_channel_59 = 'COL101'
#lhc.caen_board_5_channel_60 = 'COL100'
#lhc.caen_board_5_channel_61 = 'COL99'
#lhc.caen_board_5_channel_62 = 'COL98'
#lhc.caen_board_5_channel_63 = 'COL97'
#
## CAEN board 6
#lhc.caen_board_6_channel_0 = 'COL96'
#lhc.caen_board_6_channel_1 = 'COL95'
#lhc.caen_board_6_channel_2 = 'COL94'
#lhc.caen_board_6_channel_3 = 'COL93'
#lhc.caen_board_6_channel_4 = 'COL92'
#lhc.caen_board_6_channel_5 = 'COL91'
#lhc.caen_board_6_channel_6 = 'COL90'
#lhc.caen_board_6_channel_7 = 'COL89'
#lhc.caen_board_6_channel_8 = 'COL88'
#lhc.caen_board_6_channel_9 = 'COL87'
#lhc.caen_board_6_channel_10 = 'COL86'
#lhc.caen_board_6_channel_11 = 'COL85'
#lhc.caen_board_6_channel_12 = 'COL84'
#lhc.caen_board_6_channel_13 = 'COL83'
#lhc.caen_board_6_channel_14 = 'COL82'
#lhc.caen_board_6_channel_15 = 'COL81'
#lhc.caen_board_6_channel_16 = 'COL80'
#lhc.caen_board_6_channel_17 = 'COL79'
#lhc.caen_board_6_channel_18 = 'COL78'
#lhc.caen_board_6_channel_19 = 'COL77'
#lhc.caen_board_6_channel_20 = 'COL76'
#lhc.caen_board_6_channel_21 = 'COL75'
#lhc.caen_board_6_channel_22 = 'COL74'
#lhc.caen_board_6_channel_23 = 'COL73'
#lhc.caen_board_6_channel_24 = 'COL72'
#lhc.caen_board_6_channel_25 = 'COL71'
#lhc.caen_board_6_channel_26 = 'COL70'
#lhc.caen_board_6_channel_27 = 'COL69'
#lhc.caen_board_6_channel_28 = 'COL68'
#lhc.caen_board_6_channel_29 = 'COL67'
#lhc.caen_board_6_channel_30 = 'COL66'
#lhc.caen_board_6_channel_31 = 'COL65'
#lhc.caen_board_6_channel_32 = 'COL64'
#lhc.caen_board_6_channel_33 = 'COL63'
#lhc.caen_board_6_channel_34 = 'COL62'
#lhc.caen_board_6_channel_35 = 'COL61'
#lhc.caen_board_6_channel_36 = 'COL60'
#lhc.caen_board_6_channel_37 = 'COL59'
#lhc.caen_board_6_channel_38 = 'COL58'
#lhc.caen_board_6_channel_39 = 'COL57'
#lhc.caen_board_6_channel_40 = 'COL56'
#lhc.caen_board_6_channel_41 = 'COL55'
#lhc.caen_board_6_channel_42 = 'COL54'
#lhc.caen_board_6_channel_43 = 'COL53'
#lhc.caen_board_6_channel_44 = 'COL52'
#lhc.caen_board_6_channel_45 = 'COL51'
#lhc.caen_board_6_channel_46 = 'COL50'
#lhc.caen_board_6_channel_47 = 'COL49'
#lhc.caen_board_6_channel_48 = 'COL48'
#lhc.caen_board_6_channel_49 = 'COL47'
#lhc.caen_board_6_channel_50 = 'COL46'
#lhc.caen_board_6_channel_51 = 'COL45'
#lhc.caen_board_6_channel_52 = 'COL44'
#lhc.caen_board_6_channel_53 = 'COL43'
#lhc.caen_board_6_channel_54 = 'COL42'
#lhc.caen_board_6_channel_55 = 'COL41'
#lhc.caen_board_6_channel_56 = 'COL40'
#lhc.caen_board_6_channel_57 = 'COL39'
#lhc.caen_board_6_channel_58 = 'COL38'
#lhc.caen_board_6_channel_59 = 'COL37'
#lhc.caen_board_6_channel_60 = 'COL36'
#lhc.caen_board_6_channel_61 = 'COL35'
#lhc.caen_board_6_channel_62 = 'COL34'
#lhc.caen_board_6_channel_63 = 'COL33'
#
## CAEN board 7
#lhc.caen_board_7_channel_0 = 'COL32'
#lhc.caen_board_7_channel_1 = 'COL31'
#lhc.caen_board_7_channel_2 = 'COL30'
#lhc.caen_board_7_channel_3 = 'COL29'
#lhc.caen_board_7_channel_4 = 'COL28'
#lhc.caen_board_7_channel_5 = 'COL27'
#lhc.caen_board_7_channel_6 = 'COL26'
#lhc.caen_board_7_channel_7 = 'COL25'
#lhc.caen_board_7_channel_8 = 'COL24'
#lhc.caen_board_7_channel_9 = 'COL23'
#lhc.caen_board_7_channel_10 = 'COL22'
#lhc.caen_board_7_channel_11 = 'COL21'
#lhc.caen_board_7_channel_12 = 'COL20'
#lhc.caen_board_7_channel_13 = 'COL19'
#lhc.caen_board_7_channel_14 = 'COL18'
#lhc.caen_board_7_channel_15 = 'COL17'
#lhc.caen_board_7_channel_16 = 'COL16'
#lhc.caen_board_7_channel_17 = 'COL15'
#lhc.caen_board_7_channel_18 = 'COL14'
#lhc.caen_board_7_channel_19 = 'COL13'
#lhc.caen_board_7_channel_20 = 'COL12'
#lhc.caen_board_7_channel_21 = 'COL11'
#lhc.caen_board_7_channel_22 = 'COL10'
#lhc.caen_board_7_channel_23 = 'COL9'
#lhc.caen_board_7_channel_24 = 'COL8'
#lhc.caen_board_7_channel_25 = 'COL7'
#lhc.caen_board_7_channel_26 = 'COL6'
#lhc.caen_board_7_channel_27 = 'COL5'
#lhc.caen_board_7_channel_28 = 'COL4'
#lhc.caen_board_7_channel_29 = 'COL3'
#lhc.caen_board_7_channel_30 = 'COL2'
#lhc.caen_board_7_channel_31 = 'COL1'
#lhc.caen_board_7_channel_32 = None
#lhc.caen_board_7_channel_33 = None
#lhc.caen_board_7_channel_34 = None
#lhc.caen_board_7_channel_35 = None
#lhc.caen_board_7_channel_36 = None
#lhc.caen_board_7_channel_37 = None
#lhc.caen_board_7_channel_38 = None
#lhc.caen_board_7_channel_39 = None
#lhc.caen_board_7_channel_40 = None
#lhc.caen_board_7_channel_41 = None
#lhc.caen_board_7_channel_42 = None
#lhc.caen_board_7_channel_43 = None
#lhc.caen_board_7_channel_44 = None
#lhc.caen_board_7_channel_45 = None
#lhc.caen_board_7_channel_46 = None
#lhc.caen_board_7_channel_47 = None
#lhc.caen_board_7_channel_48 = None
#lhc.caen_board_7_channel_49 = None
#lhc.caen_board_7_channel_50 = None
#lhc.caen_board_7_channel_51 = None
#lhc.caen_board_7_channel_52 = None
#lhc.caen_board_7_channel_53 = None
#lhc.caen_board_7_channel_54 = None
#lhc.caen_board_7_channel_55 = None
#lhc.caen_board_7_channel_56 = None
#lhc.caen_board_7_channel_57 = None
#lhc.caen_board_7_channel_58 = None
#lhc.caen_board_7_channel_59 = None
#lhc.caen_board_7_channel_60 = None
#lhc.caen_board_7_channel_61 = None
#lhc.caen_board_7_channel_62 = None
#lhc.caen_board_7_channel_63 = None

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

