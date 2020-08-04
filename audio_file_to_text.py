#!/usr/bin/env python
#establish arguments
import argparse
from wit import Wit
parser = argparse.ArgumentParser(description='Transcribe audio file into text')
# Define the arguments
parser.add_argument('--input_file', '-i', type=str, dest='input_file', required=True, help='path of the input audio file')
#parser.add_argument('--input_language', '-l', type=str, dest='input_language', required=False,
#                    help='language to use to interpret the audio')
parser.add_argument('--output_name', '-o', type=str, dest='output_name', required=True, help='path for output text file')
args = parser.parse_args()

#function to take the audio file and transcribe it using google
def audio_file_to_text(input_file, output_name):
    client = Wit('G5B355BBFZBLVXKYQSOABXUCB7G5Q6DY')
    resp = None
    with open(str(input_file), 'rb') as f:
        resp = client.speech(f, {'Content-Type': 'audio/wav'})
    audio_file_text_output = open(str(output_name) + '.txt', 'w')
    audio_file_text_output.write(str(resp))
    audio_file_text_output.close()

#function with the corresponding arguments
audio_file_to_text(args.input_file, args.output_name)
