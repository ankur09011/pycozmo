PyCozmo
=======

`PyCozmo` is a pure-Python [Anki Cozmo](https://anki.com/en-us/cozmo.html) communication library. It allows controlling
a Cozmo robot directly, without having to go through a mobile device, running the Cozmo app.

The library is loosely based on the [Anki Cozmo Python SDK](https://github.com/anki/cozmo-python-sdk) and the
[cozmoclad](https://pypi.org/project/cozmoclad/) library.

This project is a tool for exploring the hardware and software of Anki Cozmo. It is unstable and heavily under
development.


Usage
-----

```python
import time
import pycozmo

cli = pycozmo.Client()
cli.start()
cli.connect()

pkt = pycozmo.protocol_encoder.DriveWheels(lwheel_speed_mmps=50.0, rwheel_speed_mmps=50.0) 
cli.send(pkt)
time.sleep(2.0)
pkt = pycozmo.protocol_encoder.StopAllMotors()
cli.send(pkt)

cli.send_disconnect()
```


Robot Support
-------------

Sensors:
- Camera - work in progress
- Cliff sensor - not supported
- Accelerometers - not supported
- Gyro - not supported
- Battery voltage - not supported
- Cube battery voltage - not supported
- Cube accelerometers - not supported

Actuators:
- Wheel motors - supported
- Head motor - supported
- Lift motor - supported
- Backpack LEDs - supported
- IR LED - supported
- OLED display - work in progress
- Speaker - not supported
- Cube LEDs - not supported

Communication:
- Wi-Fi AP - supported
- Bluetooth LE - not supported


Limitations
-----------

- there is no Wi-Fi control. The library assumes a Wi-Fi connection to Cozmo, established in advance.
- frame retransmission is not implemented
- transmission of multiple packets in a single frame is not implemented


Requirements
------------

- Python 3.5


Installation
------------

Using pip:

```
pip install pycozmo
```

From source:

```
git clone https://github.com/zayfod/pycozmo.git
cd pycozmo
python setup.py install
```


Bugs
----

Bug reports and patches should be sent via GitHub:

https://github.com/zayfod/pycozmo
