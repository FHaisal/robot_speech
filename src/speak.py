#!/usr/bin/env python3

import rospy
from robot_speech.srv import String
import pyttsx3

def handle_speak(request):
    text = request.data

    if text:
        engine = pyttsx3.init()

        for voice in engine.getProperty('voices'):
            if voice.name == 'english':
                use_voice = voice

        engine.setProperty('voice', use_voice.id)
        engine.say(text)
        engine.runAndWait()
        return 'Voice spoke'

    return 'Request empty'

def run_server():
    rospy.init_node('robot_speak_server')
    s = rospy.Service('robot_speak', String, handle_speak)
    print('Ready to speak')
    rospy.spin()

if __name__ == '__main__':
    run_server()
