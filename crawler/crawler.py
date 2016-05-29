import urllib2
import json


def load_data():
    f = open('data.txt')
    data = f.read()
    data = data.split('\n\n')
    cluster = []
    for i in data:
        t = i.split('\n')
        cluster.append({'name': t[1], 'data': t[2:]})
    return cluster


def get_user_info_by_id(uid):
    url = 'http://m.weibo.cn/'
    #url = 'http://m.weibo.cn/u/%s' % uid
    req = urllib2.Request(url,
                          headers={
                              'Host': 'm.weibo.cn',
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                              'Cookie': 'SUB=_2A256TcvsDeRxGeNI71EZ-SjLzjWIHXVZsdWkrDV6PUJbstANLVnxkW1LHettsx5u5nJIWf8uRGWLEAivFCIo8g..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW-m7g_9bU-TmeCUMVwY8-G5JpX5o2p5NHD95QfSoB01h.cS0-4Ws4Dqc_ji--ciKnRiK.pi--ciKnXiKLsi--Ri-2NiKn4i--Xi-i2i-27i--Xi-iFi-8hi--Ri-isiK.Ri--ciK.Ri-8si--Ri-2ciKnpi--fi-82i-2ci--Xi-z4i-27i--Xi-zRiKn7i--Xi-zRi-8W; SUHB=09P9QSO1yqiWVW; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; M_WEIBOCN_PARAMS=uicode%3D20000174; gsid_CTandWM=4u4ECpOz5rnVf9xTqkvL8nGeAcf; H5_INDEX=0_my; H5_INDEX_TITLE=%E6%88%91%E7%9A%84%E5%BE%AE%E5%8D%9A%20',
                              'Connection': 'keep-alive'}
                          )
    response = urllib2.urlopen(req)
    data = response.read()
    try:
        begin = data.find("""[{"mod_type":""")
        end = data.find("""},'common':""")
        body = data[begin:end]
        body = json.loads(body)
        nums = int(body[1]['mblogNum']), int(body[1]['attNum']), int(body[1]['fansNum'])
        print nums
    except Exception as e:
        pass


def get_user_weibo_by_id(uid, page=1):
    url = 'http://m.weibo.cn/page/json?containerid=100505%s_-_WEIBO_SECOND_PROFILE_WEIBO&page=%s' % (uid, page)
    req = urllib2.Request(url,
                          headers={
                              'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 ' +
                                            '(KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
                          )
    response = urllib2.urlopen(req)
    data = response.read()
    try:
        body = json.loads(data)
        weibos = body['cards'][0]['card_group']
        weibolist = [w['mblog'] for w in weibos]
        print weibolist
        return weibolist
    except Exception as e:
        pass

        
get_user_info_by_id('')