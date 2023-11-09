def calculate_power(data):
    result = 0
    for chatting in data['chatting']:
        cnt = 0
        for text in chatting['texts']:
            if text.find('mz'):
                cnt += 1
        result += cnt * chatting['idx']
    return result
