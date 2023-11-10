import requests
from dotenv import load_dotenv
import os
import time

import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from mz_power_calc import mz_test_everything

load_dotenv()
SERVER_URL = os.getenv('SERVER_URL')

def predict(predict_sentence):
	result = mz_test_everything.mz_power(predict_sentence)
	return sum(result)/len(result), result.index(min(result)) 
	

def analize():
	work = requests.get(SERVER_URL).json()

	if len(work) == 0:
		return False

	raw_chattings = work['rawChatting']
	result = {
		'test_id': work['test_id'],
		'rawChatting': []
	}
	for chatting in raw_chattings:
		chattingResult = {
			'idx': chatting['idx'],
			'contents': []
		}
		for text in chatting['texts']:
			score, feedback = predict(text)
			contents = {
				'texts': text,
				'score': score,
				'feedback': feedback
			}
			chattingResult['contents'].append(contents)
		result['rawChatting'].append(chattingResult)
	
	return result

if __name__ == '__main__':
	work = None
	while True:
		try:
			time.sleep(3)
			print('Fetch Work.')
			result = analize()
			print('Analysis Result: ', result)
			if result:
				requests.post(SERVER_URL, json=result)
		except Exception as e:
			print(e)
