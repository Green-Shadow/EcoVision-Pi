import json
from os.path import join, dirname
from os import environ
import time
from watson_developer_cloud import VisualRecognitionV3
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1024, 768)
time.sleep(2)
file_path = join(dirname(__file__), str(time.time()) + '.jpg')
camera.capture(file_path)

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='9f67d912993f80609db8173387e7b32b8d1776c8')

with open(file_path, 'rb') as image_file:
    text_results = visual_recognition.classify(images_file=image_file,classifier_ids=['EcoVision_2039938386'],threshold=0.001)
    print(text_results['images'][0]['classifiers'][0]['classes'][0]['class'])
    print('Confidence:',text_results['images'][0]['classifiers'][0]['classes'][0]['score'])


