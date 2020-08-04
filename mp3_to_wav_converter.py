#!/usr/bin/env python
#establish arguments
import argparse
parser = argparse.ArgumentParser('Convert audio files into wav files')
#define the arguments
parser.add_argument(--input_file, -i, type=str, dest='input_file', required=True,
                    help='audio file to be converted')
parser.add_argument('--output_name', '-o', type=str, dest='output_name', required=True, help='path for output wav file')
args = parser.parse_args()

def audio_wav_converter(input_file, output_name):

    from os import path
    from pydub import AudioSegment

    # files
    src = str(input_file)
    dst = str(output_name)+'.wav'

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

#function with the arguments
audio_wav_converter(args.input_file, args.output_name)


