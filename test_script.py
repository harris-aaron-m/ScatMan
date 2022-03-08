
#nyqist

import soundfile as sf
import numpy as np

SAMPLE_RATE = 44100
##SAMPLE_RATE = 10 ##Smaller sample rate -> longer audio file

def readAsBinary(fileName):
    with open(fileName, "rb") as file:
        data = file.read()
    return data

def writeAsBinary(fileName, data):
    with open(fileName, "wb") as file:
        file.write(data)

def encode(message, fileName, samplerate=SAMPLE_RATE):
    ## Normalize bytes between -1 and 1
    ## 0 to 256 : (0/128)-1 to (256/128)-1 : -1 to 1
    stream = np.asarray([(byte/128)-1 for byte in message])
    print(stream)
    sf.write(fileName,stream,samplerate)

def decode(fileName):
    data, samplerate = sf.read(fileName)
    return bytes([int(b) for b in (data + 1) * 128])

def encodeDecodeFile(fileName):
    data = readAsBinary(fileName)
    wavFileName = fileName.split(".")[0] + ".wav"
    print("Encoding File to Wav...")
    encode(data, wavFileName)
    print("Decoding File from Wav...")
    byteString = decode(wavFileName)
    writeAsBinary("new_" + fileName, byteString)

encodeDecodeFile("DeepLearningaVisualApproach.pdf")
    
##INPUT   = "maya.txt"
##OUTPUT  = "output"
##OUT_EXT = ""
##ENCODING = "ascii"
##
##
#### Read file in as binary
##with open(INPUT, "rb") as file:
##    data = file.read()
##
#### Iterate over bytes
###for byte in data:
###    print(byte, chr(byte))
##
#### Create a new message and convert to bytes
##newMessage = "Hello world!  I wrote this in binary"
##b = bytes(newMessage, ENCODING)
##print(b)
##
#### Write message to file in binary
##with open(OUTPUT+OUT_EXT, "wb") as file:
##    file.write(b)
