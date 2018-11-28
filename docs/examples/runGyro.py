from DesignSpark.Pmod.HAT import createPmod
from time import sleep


if __name__ == '__main__':

    gyro = createPmod('Gyro','JA')

    while True:
    #        if (gyro.readInt2()==1):
        if True:
	    voltx = gyro.readX()
	    volty = gyro.readY()
	    voltz = gyro.readZ()
            temp = gyro.readTemp()

	    print(voltx, volty, voltz, temp)
	
        sleep(0.8)
