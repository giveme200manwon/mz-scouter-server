import requests
from dotenv import load_dotenv
import os
import time

import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from mz_power_calc import mz_test_everything
# from mz_power_ai import mz_classify

load_dotenv()
SERVER_URL = os.getenv('SERVER_URL')

def predict(predict_sentence):
	result_power = mz_test_everything.mz_power(predict_sentence)
	# result_class = mz_classify.predict(predict_sentence)

	# result_power_mean = sum(result)/len(result)

	# if result_power_mean >= 40 and result_power_mean <= 50 and result_class == 1:
	# 	result_power = 60
	# elif result_power_mean >= 50 and result_power_mean <= 60 and result_class == 0:
	# 	result_power = 40

	return result_power, result.index(min(result))
	

def analize():
	work = requests.get(SERVER_URL).json()

	if len(work) == 0:
		return False

	raw_chattings = work['chatting']
	result = {
		'test_id': work['test_id'],
		'chatting': []
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
		result['chatting'].append(chattingResult)
	
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
