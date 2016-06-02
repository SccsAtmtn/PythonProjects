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
    personal_info[2], personal_info[3] = personal_info[3], personal_info[2]
    #print personal_info
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

def get_hot_topic_discuss_information():
    global cookie1;
    file = open('D:\\Python Projects\\crawler\\helloJune.txt', 'a')
    fout1 = open('discussant.txt', 'w')
    fout2 = open('discussTime.txt', 'w')
    page = 0
    dtime = []
    uid = []
    while (True):
        time.sleep(5)
        page = page+1
        url = 'http://m.weibo.cn/page/pageJson?containerid=&containerid=2305301008085713f66672bd2cf205b0012655b3ad81__timeline__mobile_info_-_pageapp:23055763d3d983819d66869c27ae8da86cb176&uid=5227568855&featurecode=20000181&luicode=10000011&lfid=1073035713f66672bd2cf205b0012655b3ad81_-_ext_intro&v_p=11&ext=&fid=2305301008085713f66672bd2cf205b0012655b3ad81__timeline__mobile_info_-_pageapp:23055763d3d983819d66869c27ae8da86cb176&uicode=10000011&page=%d' % page
        req = urllib2.Request(url,
                              headers={
                                       'Host': 'm.weibo.cn',
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                                       'cookie': cookie1,
                                       'Connection': 'keep-alive'}
                                      )
        response = urllib2.urlopen(req)
        data = response.read()
    
        head = '{"card_type":9'
        time_head = '"mblog":{"created_at":"'
        uid_head = '"user":{"id":'
        start = data.find(head)

        while (True):
            next = data.find(head, start+1)
            if (next==-1):
                break
            str = data[start:next]
            time_start = str.find(time_head)+len(time_head)
            time_end = str.find('",', time_start)
            now_time = str[time_start:time_end]
            uid_start = str.find(uid_head, time_end)+len(uid_head)
            uid_end = str.find(',', uid_start)
            now_uid = str[uid_start:uid_end]
            if ((not now_uid in uid)or(not now_time in dtime)):
                dtime.append(now_time)
                uid.append(now_uid)
            start = next
        
    for x in dtime:
        fout2.write(x+'\n')
    for x in uid:
        fout1.write(x+'\n')
        
    for i in range(len(uid)):
        try:
            time.sleep(5)
            info = get_user_info_by_id(uid[i])
            file.write(dtime[i]+'    ')
            for j in range(len(info)-1):
                file.write(info[j]+'    ')
            file.write('[ ')
            for x in info[len(info)-1]:
                file.write(x+' ')
            file.write(']\n')
        except Exception as e:
            print uid[i]
            continue
        

cookie1 = 'SUHB=079jeZVSkxgEVW; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; M_WEIBOCN_PARAMS=featurecode%3D20000181%26fid%3D1005052178070944%26uicode%3D10000011; SUB=_2A256S-fVDeTxGeNM6VUU9ibEzjmIHXVZt4mdrDV6PUJbktBeLRSmkW14pPcb5Wvcsv_0VPhauoc51-SyRw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF53ubShYjawnK9F8ki.D._5JpX5o2p5NHD95QfeozNSKqR1h-fWs4Dqcjdi--Ni-i2iK.Ni--4i-2Ei-2Xi--4iKLsi-z0; SSOLoginState=1464833925; gsid_CTandWM=4uN3CpOz5dxNVupK1nk2JlVVCdN; H5_INDEX=2; H5_INDEX_TITLE=%E7%BD%97%E9%A2%A4%E9%9F%B3'

get_hot_topic_discuss_information()
#while (True):
#    try:
#        get_hot_topic_discuss_information()
#        time.sleep(7*60)
#    except Exception as e:
#        time.sleep(30*60)
#        continue
#get_user_info_by_id('3175543542')
#get_user_personal_info('5614427637')
#get_user_friends_by_page_id('1005055091716249')