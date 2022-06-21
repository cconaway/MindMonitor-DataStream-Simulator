
#Import Standard Libraries
import time
import csv
import argparse
from collections import deque
import sys

#Import 3rd Party Libraries 
from pythonosc import udp_client

#Import Constants
import configuration

def main():
    #Defining Constants
    CLIENT_IP = configuration.CLIENT_IP
    CLIENT_PORT = configuration.CLIENT_PORT
    RATE = configuration.RATE

    #Command Line Arg Parse
    parser = argparse.ArgumentParser()
    parser.add_argument('datafile', type=str, help='The csv filename in eegdata you would like to use. ex: accelerometer.csv')
    parser.add_argument('--loop', type=bool, help="Put True if you want the stream to loop." )
    args = parser.parse_args()

    #Read CSV file
    filename = args.datafile
    with open('./eegdata/{}'.format(filename), 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    #Init Client
    client = udp_client.SimpleUDPClient(CLIENT_IP, CLIENT_PORT)

    #For Row in Data, convert to sendable format and send at Rate
    if args.loop == True:
        print('Looping Forever')
        print('To Stop Stream press CTRL-C.')
        dq = deque(data)

        while True:
            row = dq[0]
            args = [float(x) for x in row[1:]]
            client.send_message(row[0], args)
            time.sleep(RATE)
            sent_value = dq.popleft()
            dq.append(sent_value)

    else:
        print('To Stop Stream press CTRL-C.')
        for row in data:
            args = [float(x) for x in row[1:]]
            client.send_message(row[0], args)
            time.sleep(RATE)
        
        print('DataSet Streamed, Closing Application.\n\n')
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nClosing Application.\n\n')