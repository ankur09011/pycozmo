#!/usr/bin/env python

import time

import pycozmo


def on_camera_image(cli, image):
    del cli
    image.save("camera.png", "PNG")


def pycozmo_program(cli: pycozmo.client.Client):

    angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
    cli.set_head_angle(angle)

    pkt = pycozmo.protocol_encoder.EnableCamera()
    cli.conn.send(pkt)
    pkt = pycozmo.protocol_encoder.EnableColorImages(enable=True)
    cli.conn.send(pkt)

    # Wait for image to stabilize.
    time.sleep(2.0)

    cli.add_handler(pycozmo.event.EvtNewRawCameraImage, on_camera_image, one_shot=True)

    # Wait for image to be captured.
    time.sleep(1)


pycozmo.run_program(pycozmo_program)
