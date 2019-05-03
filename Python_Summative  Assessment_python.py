# Import module to generates numbers between 0 and 1
# import datetime from the library
import datetime
import random as rand

# Create a list to generated sensor data
sensor=1
sensorReading32=[]

# Open a file to hold the generated data from each sensor
report = open("Sensors_Reading.txt", "w")

# Loop for 32 arrays of sensors
while sensor<=32:

    sensorData = []

# Generate a list of 16 random float numbers between 0 1nd 1 
    for i in range(16):
            sensorDataNumber = rand.random()
            sensorData.append(sensorDataNumber)
        # Print the generated data from each sensor, date and time stamp the list
            print(sensorData)
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# Write the generated sensor data to the initially opened
    report.write('Readings for sensor {}'.format(sensor) + str(sensorData)+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    report.write("\n")

    sensor=sensor+1


# function to generate new data from the sensors
# The function will identify errors in the generated data
def checkerror(errorvalue):
    import random as rand
    import datetime

    global sensorerror

    sensorerror = 1
    sensorerrordata32 = []
    # open files to hold the sensors data with string errors
    errorReport = open("SensorError2.txt", "w")
    newerrorreport = open('Corrupted_SensorData.txt', 'w')

    while sensorerror <= 32:

        sensorerrordata = []

        for j in range(16):
            sensorerrordatanumber = rand.random()

            sensorerrordata.append(sensorerrordatanumber)

            print(sensorerrordata)
            # print("\n")

        errorReport.write("Reading with error from sensor {}".format(sensorerror) + str(sensorerrordata) + str(
            datetime.datetime.now()))
        errorReport.write("\n")
        errorReport.write("\n")

        errordata = []
        for erroritem in sensorerrordata:
            if erroritem < errorvalue:
                erroritem = 'err'
            errordata.append(erroritem)
        sensorerrordata = errordata

        newerrorreport.write(
            "Reading Errors from sensor {}".format(sensorerror) + str(sensorerrordata) + str(datetime.datetime.now()))
        newerrorreport.write("\n")
        newerrorreport.write("\n")

        sensorerror = sensorerror + 1

checkerror(0.1)

