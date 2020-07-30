import argparse

parser = argparse.ArgumentParser(description='Transcribe audio file into text')
# Define the arguments
parser.add_argument('--input_file', '-i', type=str, dest='input_file', required=True, help='path of the input audio file')
parser.add_argument('--input_language', '-l', type=str, dest='input_language', required=True,
                    help='language to use to interpret the audio')
parser.add_argument('--output_name', '-o', type=str, dest='output_name', required=True, help='path for output text file')
args = parser.parse_args()


def audio_file_to_text(input_file, input_language, output_name):
    if input_language == None:
        print("choose a language to be used")

    import speech_recognition as sr

    r = sr.Recognizer()

    # use an audio file as input for the data
    audio_file = sr.AudioFile(str(input_file))

    with audio_file as source:
        audio = r.record(source)
        text = r.recognize_google(audio, language=str(input_language))
        print(text)
    audio_file_text_output = open(str(output_name) + '.txt', 'w')
    audio_file_text_output.write(text)
    audio_file_text_output.close()

audio_file_to_text(args.input_file, args.input_language, args.output_name)
