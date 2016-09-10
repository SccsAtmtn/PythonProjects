# -*- coding:utf-8 -*-  
import urllib2
import time

def get_user_personal_info(uid):
    global cookie1
    url = 'http://m.weibo.cn/users/%s/?' %uid
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
    
    personal_info = []
    if (data.find('微博认证')!=-1):
        personal_info.append('Y')
    else:
        personal_info.append('N')
      
    personal_info.append(uid)
    
    end = data.find('基本信息')
    start = data.find('昵称</span><p>', end)
    if (start!=-1):
        start = start+len('昵称</span><p>')
        end = data.find('</p>', start)
        personal_info.append(data[start:end])
    else:
        personal_info.append('#')
    start = data.find('性别</span><p>', end)
    if (start!=-1):
        start = start+len('性别</span><p>')
        end = data.find('</p>', start)
        personal_info.append(data[start:end])
    else:
        personal_info.append('#')
    start = data.find('所在地</span><p>', end)
    if (start!=-1):
        start = start+len('所在地</span><p>')
        end = data.find('</p>', start)
        personal_info.append(data[start:end])
    else:
        personal_info.append('#')
    start = data.find('生日</span><p>', end)
    if (start!=-1):
        start = start+len('生日</span><p>')
        end = data.find('</p>', start)
        personal_info.append(data[start:end])
    else:
        personal_info.append('#')
    personal_info[3], personal_info[4] = personal_info[4], personal_info[3]
    #print personal_info
    return personal_info
    

def get_user_friends_by_page_id(page_id):
    global cookie1
    page = 0
    friends = []
    while (True):
        time.sleep(7)
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
    

def get_user_info_by_id(uid):
    global cookie1
    url = 'http://m.weibo.cn/u/%s' % uid
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
    
    start = data.find('\'stageId\':\'')
    end = data.find('\'}', start)
    start = start+len('\'stageId\':\'')
    page_id = data[start:end]
    #print page_id
    
    personal_info = get_user_personal_info(uid)
    friends = get_user_friends_by_page_id(page_id)
    personal_info.append(friends)
    return personal_info

def get_hot_topic_fans_information():
    global cookie1;
    file = open('D:\\Python Projects\\crawler\\fans_information6.txt', 'a')
    
    fout1 = open('fans_uid.txt', 'w')
    page = 0
    uid = []
    flag = True
    while (flag):
        flag = False
        time.sleep(5)
        page = page+1
        print page
        url = 'http://m.weibo.cn/page/pageJson?containerid=&containerid=230403_-_1008085713f66672bd2cf205b0012655b3ad81&title=粉丝&uid=5227568855&from=feed&featurecode=20000181&luicode=10000011&lfid=1073035713f66672bd2cf205b0012655b3ad81_-_ext_intro&v_p=11&ext=&fid=230403_-_1008085713f66672bd2cf205b0012655b3ad81&uicode=10000011&page=%d' % page
        req = urllib2.Request(url,
                              headers={
                                       'Host': 'm.weibo.cn',
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                                       'cookie': cookie1,
                                       'Connection': 'keep-alive'}
                                      )
        response = urllib2.urlopen(req)
        data = response.read()
        #f = open('page.html', 'w')
        #f.write(data)
        
        uid_head = '"user":{"id":'
        start = data.find(uid_head)

        while (start!=-1):
            start = start+len(uid_head)
            end = data.find(',', start)
            now_uid = data[start:end]
            if (not now_uid in uid):
                uid.append(now_uid)
                flag = True
            start = data.find(uid_head, end)
        
    for x in uid:
        fout1.write(x+'\n')
    '''
    fin1 = open('fans_uid.txt')
    uid = []
    for i in range(1000):
        str = fin1.readline()
        uid.append(str[0:len(str)-1])
    '''
    for i in range(len(uid)):
        #try:
            time.sleep(7)
            info = get_user_info_by_id(uid[i])
            for j in range(len(info)-1):
                file.write(info[j]+'    ')
            file.write('[ ')
            for x in info[len(info)-1]:
                file.write(x+' ')
            file.write(']\n')
        #except Exception as e:
        #    print uid[i]
        #    continue
        
    
cookie1 = 'SUHB=0pHxD2stUWCfjD; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; SUB=_2A256Ue4YDeTxGeNI71EZ-SjLzjWIHXVZvfJQrDV6PUJbkdBeLVH3kW2Z4oIIU2vgP4A4a6Bn_3us0CMVNQ..; SSOLoginState=1465142453; gsid_CTandWM=4uS9CpOz5N5FskKiVRtIPnGeAcf; M_WEIBOCN_PARAMS=featurecode%3D20000181%26fid%3D1005053721759773_-_FOLLOWERS%26uicode%3D10000012'

get_hot_topic_fans_information()
