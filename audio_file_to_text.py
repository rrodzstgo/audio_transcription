def audio_file_to_text(input_language,output_name):

    if input_language == None:
    input_language == 'en-US'

    import speech_recognition as sr

    r = sr.Recognizer()

#use an audio file as input for the data
    audio_file = sr.AudioFile('voicemail-23.wav')

    with audio_file as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        print(text)
    audio_file_text_output = open("audio_file_transcript.txt",'w')
    audio_file_text_output.write(text)
    audio_file_text_output.close()
