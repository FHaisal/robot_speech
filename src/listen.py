#!/usr/bin/env python

import rospy
from robot_speech.srv import String, Listen
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError


def robot_listen(request):
    try:
        recogniser = Recognizer()
        microphone = Microphone()

        print('Listening')

        with microphone as source:
            audio = recogniser.listen(source)

        return str(recogniser.recognize_wit(audio, key='2F35S7KRNBLUIIFEVKC2PLFQ2XPGA45L', show_all=True))
    except (UnknownValueError, RequestError) as e:
        print(e)
        print('\n')
        return str({'_text': '', 'entities': {}})

def run_server():
    rospy.init_node('robot_listen_server')
    service = rospy.Service('robot_listen', Listen, robot_listen)
    rospy.spin()


if __name__ == '__main__':
    run_server()