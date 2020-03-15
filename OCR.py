from aip import AipOcr

model=1

config={
    'appId': '17897236',
    'apiKey': 'pDmRkoOlqUCQliqxm6wwp4sr',
    'secretKey': 'q24kqnZA0dZ1GvnaSAXBc09offm7GjfD',
}

client = AipOcr(**config)

def get_file_bit(file):
    fp = open(file, 'rb')
    return fp.read()

def img_to_str(image_path):
    image_bit=get_file_bit(image_path)
    global model
    if model==1:
        result=client.basicGeneral(image_bit)
    elif model==2:
        result = client.basicAccurate(image_bit)
    elif model==3:
        result = client.handwriting(image_bit)
    str = ''
    for w in result['words_result']:
        str = str.__add__(w['words']).__add__('\n')
    return str
