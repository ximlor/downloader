# coding: utf-8
import requests
import os
from time import sleep

def create_path(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
    return path


def write(filename, content):
    with open(filename, 'wb') as file:
        file.write(content)


def log(filename, content):
    with open(filename, 'a+') as file:
        file.write(content)


log_path = create_path('/storage/logs')


# url = 'http://img1.gtimg.com/cq/pics/hv1/115/52/2204/143328475.jpg'

def downLoad(item):
    url = 'http://120.52.73.73/data1.cache.directory/media/videos/iphone/%s.mp4' % item
    log_file = '%s/mp4.log' % log_path
    base_path = create_path('/storage/mp4')
    filename = '%s/%s.mp4' % (base_path, item)
    if os.path.exists(filename):
        print('exist')
        pass
    else:
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            try:
                write(filename, r.content)
                log(log_file, '%s-0\n' % item)
            except Exception:
                log(log_file, 'failed!')
                print(Exception.message)
                pass
        else:
            log(log_file, '%s-404\n' % item)


def downLoad2(item):
    url = 'http://media2.ccxx99.com/remote_control.php'
    log_file = '%s/ccxx99.log' % log_path

    base_path = create_path('/storage/mp4/ccxx99')
    filename = '%s/%s.mp4' % (base_path, item)
    if os.path.exists(filename):
        print('exist')
        pass
    else:
        r = requests.get(url, params={
            'time': '1495864713',
            'cv': 'a038f0b5f4c0accf6bfb0f3a2e2dee00',
            'lr': '0',
            'cv2': '28ddaeccb7119a0e24879d04473f9de9',
            'cv3': '3384243a1593581e105bed356b1a1383',
            'file': '/videos/0/%s/%s.mp4' % (item, item),
        }, headers={'Connection': 'closeMax retries exceeded'})
        if r.status_code == requests.codes.ok:
            try:
                print('ok')
                write(filename, r.content)
                log(log_file, '%s-0\n' % item)
            except Exception:
                log(log_file, 'failed!')
                print(Exception.message)
                pass
        else:
            print('not')
            log(log_file, '%s-404\n' % item)
    sleep(30)
