#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
natural_git.py -
"""
import speech_recognition as sr


# TODO: threading


def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # listen for 5 seconds and create the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=5)
        print("Say something!")
        audio = r.listen(source)
        try:
            speech = r.recognize_sphinx(audio)
            print("Sphinx thinks you said " + speech)
            return speech
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


if __name__ == '__main__':
    listen()
