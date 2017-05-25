# coding: utf-8
import requests
import os


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


def downLoad(item):
    url = 'http://120.52.73.73/data1.cache.directory/media/filenames/iphone/%s.mp4' % item
    # url = 'http://120.52.73.73/data1.cache.directory/media/filenames/xphone/%s.mp4' % item
    # url = 'http://img1.gtimg.com/cq/pics/hv1/115/52/2204/143328475.jpg'

    log_path = create_path('/storage/log')
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
