# -*- coding:utf-8 -*-  
import urllib2
import time

def get_user_personal_info(uid, page_id):
    global cookie
    url = 'http://weibo.com/p/%s/info?mod=pedit_more' %page_id
    req = urllib2.Request(url,
                          headers={
                              'Host': 'weibo.com',
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                              'cookie': cookie,
                              'Connection': 'keep-alive'}
                            )
    response = urllib2.urlopen(req)
    data = response.read()
    #f = open('user.html', 'w')
    #f.write(data)
    
    personal_info = [uid]
    
    end = data.find('基本信息')
    start = data.find('昵称：<\\/span><span class=\\"pt_detail\\">', end)
    if (start!=-1):
        start = start+len('昵称：<\\/span><span class=\\"pt_detail\\">')
        end = data.find('<\\/span>', start)
        personal_info.append(data[start:end])
    else:
        personal_info.append('#')
    start = data.find('所在地：<\\/span><span class=\\"pt_detail\\">', end)
    if (start!=-1):
        start = start+len('所在地：<\\/span><span class=\\"pt_detail\\">')
        end = data.find('<\\/span>', start)
        personal_info.append(data[start:end])
    else:
        personal_info.append('#')
    start = data.find('性别：<\\/span><span class=\\"pt_detail\\">', end)
    if (start!=-1):
        start = start+len('性别：<\\/span><span class=\\"pt_detail\\">')
        end = data.find('<\\/span>', start)
        personal_info.append(data[start:end])
    else:
        personal_info.append('#')
    start = data.find('生日：<\\/span><span class=\\"pt_detail\\">', end)
    if (start!=-1):
        start = start+len('生日：<\\/span><span class=\\"pt_detail\\">')
        end = data.find('<\\/span>', start)
        personal_info.append(data[start:end])
    else:
        personal_info.append('#')
    return personal_info


def get_user_friends_by_page_id(page_id):
    global cookie1
    page = 0
    friends = []
    while (True):
        time.sleep(5)
        page = page+1
        url = 'http://m.weibo.cn/page/json?containerid=%s_-_FOLLOWERS&page=%d' % (page_id, page)
        req = urllib2.Request(url,
                              headers={
                                  'Host': 'm.weibo.cn',
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                                  'cookie': cookie1,
                                  'Connection': 'keep-alive'}
                              )
        response = urllib2.urlopen(req)
        data = response.read()
        #f = open('user.html', 'w')
        #f.write(data)
        end = data.find('"card_group":')
        tot = 0
        while (True):
            start = data.find('"user":{"id":', end)
            if (start==-1):
                break
            start = start+len('"user":{"id":')
            end = data.find(',', start)
            uid = data[start:end]
            if (not uid in friends):
                tot = tot+1
                friends.append(data[start:end])
        if (tot==0):
            break
    #print friends
    return friends    
    
'''
def get_user_friends_by_page_id(page_id):
    global cookie
    page = 0
    friends = []
    while (True):
        time.sleep(5)
        page = page+1
        url = 'http://weibo.com/p/%s/follow?page=%d#Pl_Official_HisRelation__64' % (page_id, page)
        req = urllib2.Request(url,
                              headers={
                                  'Host': 'weibo.com',
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                                  'cookie': cookie,
                                  'Connection': 'keep-alive'}
                              )
        response = urllib2.urlopen(req)
        data = response.read()
        #f = open('user.html', 'w')
        #f.write(data)
        end = data.find('<!--关注\\/粉丝列表-->\\r\\n')
        tot = 0
        while (True):
            start = data.find('usercard=\\"id=', end)
            if (start==-1):
                break
            start = start+len('usercard=\\"id=')
            end = data.find('&', start)
            uid = data[start:end]
            if (not uid in friends):
                tot = tot+1
                friends.append(data[start:end])
        if (tot==0):
            break
    return friends
 '''

def get_user_info_by_id(uid):
    global cookie
    url = 'http://weibo.com/u/%s?refer_flag=100808&is_hot=1' % uid
    req = urllib2.Request(url,
                          headers={
                              'Host': 'weibo.com',
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                              'cookie': cookie,
                              'Connection': 'keep-alive'}
                          )
    response = urllib2.urlopen(req)
    data = response.read()
    #f = open('user.html', 'w')
    #f.write(data)
    
    personal_info = []
    start = data.find('current=fans#place\\" ><strong class=\\"')+len('current=fans#place\\" ><strong class=\\"W_f18\\">')
    end = data.find('<\\/strong>', start)
    #print data[start:end]
    if (end-start>5):
        personal_info.append('Y')
    else:
        personal_info.append('N')
        
    start = data.find('$CONFIG[\'page_id\']=\'')
    end = data.find('\';', start)
    start = start+len('$CONFIG[\'page_id\']=\'')
    page_id = data[start:end]
    #print page_id
    
    personal_info.extend(get_user_personal_info(uid, page_id))
    friends = get_user_friends_by_page_id(page_id)
    personal_info.append(friends)
    return personal_info

def get_hot_topic_fans_information():
    '''
    global cookie
    page = 0
    user_id = []
    while (True):
        time.sleep(5)
        page = page+1
        print page
        url = 'http://weibo.com/p/1008088343a0acaca8d63795b22a9c53d8494d/followlist?page=%d#Pl_Core_F4RightUserList__34' % page
        req = urllib2.Request(url,
                              headers={
                                  'Host': 'weibo.com',
                                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                                  'cookie': cookie,
                                  'Connection': 'keep-alive'}
                             )
        response = urllib2.urlopen(req)
        data = response.read()
        #f = open('a.html', 'w')
        #f.write(data)
    
        start = 0
        end = 0
        tot = 0
        while (True):
            start = data.find('usercard=\\"id=', end)
            if (start==-1):
                break
            start = start +len('usercard=\\"id=')
            end = data.find('&', start)
            uid = data[start:end]
            if (not uid in user_id):
                tot = tot+1
                user_id.append(uid)
        if (tot==0):
            break
    print len(user_id)
    
    fans_uid = open('fans_uid.txt', 'w')
    for uid in user_id:
        fans_uid.write(uid+'\n')
    '''
    file = open('fans_info.txt', 'a')
    fin = open('fans_uid.txt')
    user_id = []
    for i in range(4420):
        s = fin.readline()
        user_id.append(s[0:len(s)-1])
    for uid in user_id:
        try:
            time.sleep(5)
            #print uid
            info = get_user_info_by_id(uid)
            for i in range(len(info)-1):
                file.write(info[i]+'    ')
            file.write('[ ')
            for x in info[len(info)-1]:
                file.write(x+' ')
            file.write(']\n')
        except Exception as e:
            print uid
            continue
    file.close()
    
cookie = 'UOR=blog.csdn.net,widget.weibo.com,login.sina.com.cn; SINAGLOBAL=8910301221166.844.1463715027234; ULV=1464597848129:9:9:3:6655188481325.942.1464597848122:1464568924612; SUHB=0N21quxm9-PtPa; un=17710305576; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; YF-V5-G0=b59b0905807453afddda0b34765f9151; _s_tentry=login.sina.com.cn; Apache=6655188481325.942.1464597848122; YF-Page-G0=35f114bf8cf2597e9ccbae650418772f; WBStore=8ca40a3ef06ad7b2|undefined; myuid=5643896759; WBtopGlobal_register_version=f81ab92b992b2688; appkey=; WB_register_version=f81ab92b992b2688; wb_bub_hot_5643896759=1; wb_bub_hot_5227568855=1; wvr=6; ALF=1467371521; SUS=SID-5227568855-1464779521-GZ-8a1oy-d5f68e9be122cebd80d2d32808c70889; SUE=es%3Db9d2b73696a1f66bb1c041ed15b01e78%26ev%3Dv1%26es2%3Da0e0d7e7178615d8a9b6e05365e81374%26rs0%3DVTNgBgYsRk16ZFdmjHd9p8Xxwjswigx0CYATsl8uyxnFJp3qJH9n5hTF%252BuK3j0UM8gMqhE%252F6uGXe8ltjnKwwyYTj9lFSMN5bTVFrtJ0T%252F%252BxL8K5ZVMD52FT36u44BAK5XINvs3GpgMmR%252FfPWeyMbExuaC0qNRZhouewY%252FLWXGSE%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1464779521%26et%3D1464865921%26d%3Dc909%26i%3D0889%26us%3D1%26vf%3D%26vt%3D%26ac%3D%26st%3D0%26uid%3D5227568855%26name%3D18810913874%26nick%3D%25E7%25BD%2597%25E9%25A2%25A4%25E9%259F%25B3%26fmp%3D%26lcp%3D2014-09-01%252010%253A18%253A36; SUB=_2A256SrNRDeTxGeNM6VUU9ibEzjmIHXVZtN0ZrDV8PUJbkNBeLXfskW0Lm615I6h-IvwFNr3xaO4HhXxYRw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF53ubShYjawnK9F8ki.D._5NHD95QfeozNSKqR1h-fWs4Dqcjdi--Ni-i2iK.Ni--4i-2Ei-2Xi--4iKLsi-z0'
cookie1 = 'SUHB=0wn1-2Coo52I7X; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; SUB=_2A256SrNQDeTxGeNM6VUU9ibEzjmIHXVZtN0YrDV6PUJbkdBeLXmnkW0IGa9W9NJ2mF1LJmrejboOT23nlg..; SSOLoginState=1464779520; gsid_CTandWM=4uv5CpOz5LpAngbVW5JwYlVVCdN; H5_INDEX=2; H5_INDEX_TITLE=%E7%BD%97%E9%A2%A4%E9%9F%B3; M_WEIBOCN_PARAMS=featurecode%3D20000181%26luicode%3D10000012%26lfid%3D1005053090120397_-_FOLLOWERS%26fid%3D1005053090120397_-_FOLLOWERS%26uicode%3D10000012'
get_hot_topic_fans_information()
#print get_user_info_by_id('609884564')
#get_user_personal_info('5091716249', '1006065921499921')
#get_user_friends_by_page_id('1005055091716249')