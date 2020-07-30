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
        text = r.recognize_google(audio, language=input_language)
    print(text)
    microphone_text_output = open("microphone_audio_transcript.txt", 'w')
    microphone_text_output.write(text)
    microphone_text_output.close()