import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='145b047be11f5059687578f4ca85325d23e0cdf8')

file_path = join(dirname(__file__), 'test.jpg')
with open(file_path, 'rb') as image_file:
    text_results = visual_recognition.classify(images_file=image_file,classifier_ids=['WasteType_909361399'])
    print(text_results['images'][0]['classifiers'][0]['classes'][0]['class'])
    print('Confidence:',text_results['images'][0]['classifiers'][0]['classes'][0]['score'])