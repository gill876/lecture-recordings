def transcribe_model_selection(speech_file, model):
    """Transcribe the given audio file synchronously with
    the selected model."""
    from google.cloud import speech

    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code="en-US",
        model=model,
    )

    response = client.recognize(config=config, audio=audio)

    output = ""
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        output+= ("-" * 20 + "\n")
        print("First alternative of result {}".format(i))
        output+= "First alternative of result {}\n".format(i)
        print(u"Transcript: {}".format(alternative.transcript))
        output+= u"Transcript: {}\n".format(alternative.transcript)

    with open(speech_file + ".txt", "w") as f:
        f.write(output)

transcribe_model_selection("gs://lecture-recordings-c/HIST2408-7.mp3", "video")
