Hello, here is a quick setup guide for the Driven Arts Collective Programmers
who wish to develop noises for the EEG OSC instrument. 

The following code runs a client that sends OSC data from an EEG to a selected port.
The data is stored as a csv in /eegdata/

SETUP__________________________/

1. Make a working Directory to clone the code into by typing:
    $ mkdir stream_eegosc

2. Change into that directory by typing:
    $ cd stream_eegosc

3. Create a python virtual environment to run the code in:
    $ python3 -m venv eeg_env

4. Activate the virtual environment
    $ source eeg_env/bin/activate 

    You should now see your command line prefixed by (eeg_osc) like this.
    (eeg_osc) USER$ 

5. Install Requirements
    (eeg_osc) $ pip install python-osc 

6. Check the configuration file and change the IP if sending to another computer.

7. Run a default script
    (eeg_osc) $ python3 stream_eegosc.py test_data.csv

You can run other scripts by using this template:
    (eeg_osc) $ python3 stream_eegosc.py {datafile.csv} {--loop}

Deactivate your virtual environment when done by running:
    $ deactivate 


FUNCTIONS____________________/

LOOP: if you want to loop the csv file forever, which is useful for sound design
    add the loop flag to your command like this.

    $ python3 stream_eegosc.py data.csv --loop True


ADDING DATA_____________________/

To add data for simulated runtime, add cleaned csv files to /eegdata

