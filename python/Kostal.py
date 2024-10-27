#!/usr/bin/env python

from datetime import datetime
from pymodbus.client import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder


# -----------------------------------------
# Routine to read a float
def readfloat(client, myadr_dec, unitid):
    r1 = client.read_holding_registers(myadr_dec, 2, slave=unitid)
    FloatRegister = BinaryPayloadDecoder.fromRegisters(
        r1.registers, byteorder=Endian.BIG, wordorder=Endian.LITTLE
    )
    result_FloatRegister = round(FloatRegister.decode_32bit_float(), 2)
    return result_FloatRegister


def read(inverter_ip, inverter_port):
    try:
        # connection Kostal
        client = ModbusTcpClient(inverter_ip, port=inverter_port)
        client.connect()

        result = {}

        powerToGrid = -readfloat(client, 252, 71)
        # print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " powerToGrid: ", powerToGrid)
        result["powerToGrid"] = powerToGrid

        return result
    except Exception as ex:
        print("ERROR Kostal: ", ex)
    finally:
        client.close()
