
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Print the gyro reading out.
"""

from DesignSpark.Pmod.HAT import createPmod
from time import sleep


if __name__ == '__main__':

    gyro = createPmod('Gyro','JA')
    sleep(0.1)

    try:
        while True:
	    voltx = gyro.readX()
	    volty = gyro.readY()
	    voltz = gyro.readZ()
            temp = gyro.readTemp()

	    print(voltx, volty, voltz, temp)
	
            sleep(0.8)
    except KeyboardInterrupt:
        pass
    finally:
        therm.cleanup()

