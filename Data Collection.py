from pathlib import Path  
from csv import writer   
from sense_hat import SenseHat 
from datetime import datetime, timedelta 
import time
from orbit import ISS
from logzero import logger, logfile
import math 
from random import randint 
import os

start_time = datetime.now()

base_folder = Path(__file__).parent.resolve()

data_file = base_folder / "data.csv"

logfile(base_folder / "HHorizons.log")

logger.info(start_time)

sense = SenseHat()

sense.show_message('Hello World')

logger.info('Time Variables & Base Folders Created')

V1_x = float(0)
V2_x = float(0)
A1_x = float(0)
A2_x = float(0)
Dis_x = float(0)

V1_y = float(0)
V2_y = float(0)
A1_y = float(0)
A2_y = float(0)
Dis_y = float(0)

V1_z = float(0)
V2_z = float(0)
A1_z = float(0)
A2_z = float(0)
Dis_z = float(0)

acc = sense.get_accelerometer_raw()
time1_2_x = time.time()
time1_2_y = time1_2_x
time1_2_z = time1_2_x

A2_x = acc["x"]
A2_y = acc["y"]
A2_z = acc["z"]

acc = sense.get_accelerometer_raw()
time1_x = time.time()
time1_y = time1_x
time1_z = time1_x
A1_x = acc["x"]
A1_y = acc["y"]
A1_z = acc["z"]

def get_sense_data():

    global V1_x
    global V2_x
    global A1_x
    global A2_x
    global Dis_x

    global V1_y
    global V2_y
    global A1_y
    global A2_y
    global Dis_y

    global V1_z
    global V2_z
    global A1_z
    global A2_z
    global Dis_z

    global time1_x
    global time1_y
    global time1_z

    global time1_2_x
    global time1_2_y
    global time1_2_z

    try:
        function_calltime = datetime.now()
        logger.info(function_calltime)
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

    try:
        sense_data = []
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

    # Appends to the list the datetime
    try:
        sense_data.append(function_calltime)
        logger.info('Time Added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

    try:
        mag = sense.get_compass_raw()
        logger.info('Mag Variable Created - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(mag["x"])
        logger.info('Mag X added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(mag["y"])
        logger.info('Mag Y added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(mag["z"])
        logger.info('Mag Z added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(math.sqrt((pow(mag["y"], 2)) + (pow(mag["x"], 2)) + (pow(mag["z"], 2))))
        logger.info('Mag Magnitude Calculated And Added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

    try:
        acc = sense.get_accelerometer_raw()
        time2_x = time.time()
        time2_y = time2_x
        time2_z = time2_x
        logger.info('Acc Variable Created - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(acc["x"])
        logger.info('Acc X Added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(acc["y"])
        logger.info('Acc Y added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(acc["z"])
        logger.info('Azz Z added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

    try:
        V1_x = 0.5 * (A1_x + A2_x) * (time1_x - time1_2_x) + V2_x
        Dis_x = 0.25 * (acc["x"] + A1_x) * (time2_x - time1_x) + V1_x * (time2_x - time1_x)
        sense_data.append(Dis_x)
        A2_x = A1_x
        A1_x = acc["x"]
        V2_x = V1_x
        time1_2_x = time1_x
        time1_x = time2_x
        logger.info('Displacement X calculated - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

    try:
        V1_y = 0.5 * (A1_y + A2_y) * (time1_y - time1_2_y) + V2_y
        Dis_y = 0.25 * (acc["y"] + A1_y) * (time2_y - time1_y) + V1_y * (time2_y - time1_y)
        sense_data.append(Dis_y)
        A2_y = A1_y
        A1_y = acc["y"]
        V2_y = V1_y
        time1_2_y = time1_y
        time1_y = time2_y
        logger.info('Displacement Y calculated - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

    try:
        V1_z = 0.5 * (A1_z + A2_z) * (time1_z - time1_2_z) + V2_z
        Dis_z = 0.25 * (acc["z"] + A1_z) * (time2_z - time1_z) + V1_z * (time2_z - time1_z)
        sense_data.append(Dis_z)
        A2_z = A1_z
        A1_z = acc["z"]
        V2_z = V1_z
        time1_2_z = time1_z
        time1_z = time2_z
        logger.info('Displacement Z calculated - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

    try:
        location = ISS.coordinates()
        logger.info('Location Variable Created - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(location.latitude)
        logger.info('Latitude added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(location.longitude)
        logger.info('Longitude added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        sense_data.append(location.elevation.km)
        logger.info('Elevation added - Function')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    return sense_data

with open('data.csv', 'w', buffering=1, newline='') as f:
    try:
        data_writer = writer(f)
        logger.info('Data writer variable created')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    try:
        data_writer.writerow(['DateTime', 'Mag X', 'Mag Y', ' Mag Z', 'Mag Magnitude', 'Acc X', 'Acc Y', 'Acc Z',
                              'Displacement X', 'Displacement Y', 'Displacement Z', 'ISS Latitude', 'ISS Longitude'
                              , 'ISS Elevation'])
        logger.info('Header Added')
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')

now_time = datetime.now()
while now_time < start_time + timedelta(minutes=178):
    try:
        TotalFileSize = os.stat(base_folder/"data.csv").st_size
        TotalFileSize = TotalFileSize + os.stat(base_folder/"HHorizons.log").st_size
        TotalFileSize = TotalFileSize + os.stat(base_folder/"main.py").st_size
        if TotalFileSize >= 2999990000:
            break
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e})')
    with open('data.csv', 'a', buffering=1, newline='') as f:
        try:
            x = randint(0, 7)
            y = randint(0, 7)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            sense.set_pixel(x, y, r, g, b)
            logger.info('Sparkled')
        except Exception as e:
            logger.error(f'{e.__class__.__name__}: {e})')
        try:
            data_writer = writer(f)
            logger.info('Data Writer 2 Created')
        except Exception as e:
            logger.error(f'{e.__class__.__name__}: {e})')
        try:
            data = get_sense_data()
            logger.info('Data Variable created and got the data')
            data_writer.writerow(data)
            logger.info('Data added')
            now_time = datetime.now()
        except Exception as e:
            logger.error(f'{e.__class__.__name__}: {e})')

FinishTime = datetime.now()

logger.info('Finish Time is: ' & FinishTime)

sense.show_message('Finished')

sense.clear()
