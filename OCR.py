from aip import AipOcr

model=1

def get_file_bit(file_path):
    fp = open(file_path, 'rb')
    return fp.read()

def img_to_str(image_path,APP_ID,API_KEY,SECRET_KEY):
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
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
