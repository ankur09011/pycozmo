#!/usr/bin/env python

from threading import Event

import pycozmo


e = Event()


def on_nv_storage_op_result(cli: pycozmo.client.Client, pkt: pycozmo.protocol_encoder.NvStorageOpResult):
    del cli
    print(pkt.result)
    print(pkt.data)

    if pkt.result != pycozmo.protocol_encoder.NvResult.NV_MORE:
        e.set()


def pycozmo_program(cli: pycozmo.client.Client):
    cli.conn.add_handler(pycozmo.protocol_encoder.NvStorageOpResult, on_nv_storage_op_result)

    pkt = pycozmo.protocol_encoder.NvStorageOp(
        tag=pycozmo.protocol_encoder.NvEntryTag.NVEntry_CameraCalib,
        length=1,
        op=pycozmo.protocol_encoder.NvOperation.NVOP_READ)
    cli.conn.send(pkt)

    e.wait(timeout=20.0)


pycozmo.run_program(pycozmo_program, log_level="DEBUG")
