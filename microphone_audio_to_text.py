
import argparse

parser = argparse.ArgumentParser(description='Transcribe microphone input into text')
# Define the arguments
parser.add_argument('--input_language', '-l', type=str, dest='input_language', required=False,
                    help='language to use to interpret the audio')
parser.add_argument('--output_name', '-o', type=str, dest='output_name', required=True, help='path for output text file')
args = parser.parse_args()

def microphone_audio_to_text(input_language,output_name):

    if input_language == None:
        input_language == 'en-US'

    import speech_recognition as sr

    r = sr.Recognizer()
    mic = sr.Microphone()

    # use the microphone as an input for the audio data
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("The microphone is open now.")
        audio = r.listen(source)
        text = r.recognize_google(audio, language=str(input_language))
    print(text)
    microphone_text_output = open(str(output_name)+'.txt', 'w')
    microphone_text_output.write(text)
    microphone_text_output.close()

microphone_audio_to_text(args.input_language, args.output_name)