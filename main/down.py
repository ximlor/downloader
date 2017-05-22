# coding: utf-8
import requests
import os


def create_path(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
    return path


def downLoad(item):
    url = 'http://120.52.73.73/data1.cache.directory/media/videos/iphone/%s.mp4' % item
    # url = 'http://120.52.73.73/data1.cache.directory/media/videos/xphone/%s.mp4' % item
    # url = 'http://img1.gtimg.com/cq/pics/hv1/115/52/2204/143328475.jpg'
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        base_path = create_path('/storage/mp4')
        video = '%s/%s.mp4' % (base_path, item)
        # video = '%s/%s.jpg' % (base_path, item)
        try:
            with open(video, 'wb') as code:
                code.write(r.content)
            print(video + ' is down load success!')
        except Exception:
            print('failed!')
            print(Exception.message)
            pass
    else:
        print('Not 200!')
