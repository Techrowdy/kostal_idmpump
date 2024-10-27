#!/usr/bin/env python

from datetime import datetime

import IdmPump
import Kostal
import Config


# idm heat pump
def idm(idm_ip, idm_port, powerToGrid, feed_in_limit):
    try:
        # feed in must be above our limit
        feed_in = powerToGrid
        if feed_in > feed_in_limit:
            # print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " iDM feed-in reached: ", feed_in)
            feed_in = feed_in / 1000
        else:
            # print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " iDM send ZERO: ", feed_in)
            feed_in = 0

        # connection iDM
        return IdmPump.writeandread(idm_ip, idm_port, feed_in)
    except Exception as ex:
        print("ERROR idm: ", ex)


if __name__ == "__main__":
    # print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " START #####")
    try:
        conf = Config.read()

        # read Kostal
        kostalvalues = Kostal.read(conf["inverter_ip"], conf["inverter_port"])

        # send idm
        idmval = idm(
            conf["idm_ip"],
            conf["idm_port"],
            kostalvalues["powerToGrid"],
            conf["feed_in_limit"],
        )

        print(
            datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            + " Kostal: "
            + str(kostalvalues["powerToGrid"])
            + ", IDM: "
            + str(idmval)
        )

        # print (datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " END #####")

    except Exception as ex:
        print("ERROR: ", ex)
