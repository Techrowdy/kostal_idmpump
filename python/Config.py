#!/usr/bin/env python

import configparser
import os
from datetime import datetime

# read config
config = configparser.ConfigParser()


def read():
    try:
        # read config
        config.read("kostal-idm.ini")

        values = {}

        values["idm_ip"] = config["IdmSection"]["idm_ip"]
        values["idm_port"] = int(config["IdmSection"]["idm_port"])
        values["feed_in_limit"] = int(config["IdmSection"]["feed_in_limit"])
        if os.getenv("IDM_IP", "None") != "None":
            values["idm_ip"] = os.getenv("IDM_IP")
            # print ("using env: IDM_IP")
        if os.getenv("IDM_PORT", "None") != "None":
            values["idm_port"] = int(os.getenv("IDM_PORT"))
            # print ("using env: IDM_PORT")
        if os.getenv("FEED_IN_LIMIT", "None") != "None":
            values["feed_in_limit"] = int(os.getenv("FEED_IN_LIMIT"))
            # print ("using env: FEED_IN_LIMIT")

        values["inverter_ip"] = config["KostalSection"]["inverter_ip"]
        values["inverter_port"] = int(config["KostalSection"]["inverter_port"])
        if os.getenv("INVERTER_IP", "None") != "None":
            values["inverter_ip"] = os.getenv("INVERTER_IP")
            # print ("using env: INVERTER_IP")
        if os.getenv("INVERTER_PORT", "None") != "None":
            values["inverter_port"] = int(os.getenv("INVERTER_PORT"))
            # print ("using env: INVERTER_PORT")

        # print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " config: ", values)

        return values
    except Exception as ex:
        print("ERROR Config: ", ex)
