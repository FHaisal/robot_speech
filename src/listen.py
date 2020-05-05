#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError

def listen_publisher():
    pub = rospy.Publisher('robot_listen', String, queue_size=10)
    rospy.init_node('robot_listen_publisher')
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        speech = robot_listen()

        if speech['_text']:
            pub.publish(str(speech))
            rate.sleep()

def robot_listen():
    try:
        recogniser = Recognizer()
        microphone = Microphone()

        with microphone as source:
            audio = recogniser.listen(source)

        return recogniser.recognize_wit(audio, key="", show_all=True)
    except (UnknownValueError, RequestError) as e:
        print(e)
        print('\n')
        return {'_text': '', 'entities': {}}
    
if __name__ == '__main__':
    try:
        listen_publisher()
        print('Running')
    except rospy.ROSInterruptException:
        pass