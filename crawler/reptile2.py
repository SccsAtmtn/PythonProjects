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

def get_hot_topic_discuss_information():
    print 'round'
    global cookie1;
    url = 'http://m.weibo.cn/p/index?containerid=2305301008087d777c3c3b736359711495f34dbd4d24__timeline__mobile_info_-_pageapp%3A23055763d3d983819d66869c27ae8da86cb176&containerid=2305301008087d777c3c3b736359711495f34dbd4d24__timeline__mobile_info_-_pageapp%3A23055763d3d983819d66869c27ae8da86cb176&uid=5643896759'
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
    time = []
    uid = []
    while (start!=-1):
        next = data.find(head, start+1)
        str = data[start:next]
        time_start = str.find(time_head)+len(time_head)
        time_end = str.find('",', time_start)
        time.append(str[time_start:time_end])
        uid_start = str.find(uid_head, time_end)+len(uid_head)
        uid_end = str.find(',', uid_start)
        uid.append(str[uid_start:uid_end])
        start = next
    
    
    file = open('D:\\Python Projects\\crawler\\discuss_information.txt', 'a')
    for i in range(len(uid)):
        #print uid[i]
        info = get_user_info_by_id(uid[i])
        file.write(time[i]+'    ')
        for j in range(len(info)-1):
            file.write(info[j]+'    ')
        file.write('[ ')
        for x in info[len(info)-1]:
            file.write(x+' ')
        file.write(']\n')
        
        
cookie = 'UOR=blog.csdn.net,widget.weibo.com,login.sina.com.cn; SINAGLOBAL=8910301221166.844.1463715027234; ULV=1464597848129:9:9:3:6655188481325.942.1464597848122:1464568924612; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW-m7g_9bU-TmeCUMVwY8-G5JpX5K2hUgL.Fo-cSheR1KqNSK.2dJLoIc7LxKqL1hnL1K2LxKqL1hBL1-qLxKnLBKML1h.LxKBLB.BLBK5LxKBLB.zLB-eLxKnLB.qL1KnLxKqL1KnLB-qLxKnLBKqL1h2LxK-LB-BLBKqLxKBLBo.LBK5LxKBLBonL1h5LxKBLBonLB-2t; SUHB=0pHxD2stUWFo-P; un=17710305576; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; SUB=_2A256SVLHDeRxGeNI71EZ-SjLzjWIHXVZP8MPrDV8PUNbuNBeLWjWkW9LHes7Krks7l15zDpGmglQvxGYswlSIw..; YF-V5-G0=b59b0905807453afddda0b34765f9151; _s_tentry=login.sina.com.cn; Apache=6655188481325.942.1464597848122; YF-Page-G0=35f114bf8cf2597e9ccbae650418772f; WBStore=8ca40a3ef06ad7b2|undefined; myuid=5227568855; WBtopGlobal_register_version=f81ab92b992b2688; appkey=; WB_register_version=f81ab92b992b2688; SUS=SID-5643896759-1464672919-GZ-ru3f6-7d8b5c41420dc7330dfcc356945a0889; SUE=es%3Dbed35c14f535c9eddc8d6ef0dc4a5cdc%26ev%3Dv1%26es2%3D6d8afe34cf17101ea5651f45710b8960%26rs0%3DMCzuqVnvW4eC1f9kcz03xLS8DfKzEvrATzNBux23IFHJSNGlH%252FX9i6YX9qP4o5MR9VY5H0zNFMzWBW4mRYgJ0nWsOO%252BnT6nLhWDPJca%252FRX4Aa1%252F2DDt6lNTvjbOU0gmwOiEwZGUEMaldZ7LbsFP%252F2pXHfX6VaoV0GlyeisVj2Vo%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1464672919%26et%3D1464759319%26d%3Dc909%26i%3D0889%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D5643896759%26name%3D17710305576%26nick%3D%25E7%2594%25A8%25E6%2588%25B75643896759%26fmp%3D%26lcp%3D2015-10-01%252018%253A41%253A01; ALF=1465277718; SSOLoginState=1464672919; wvr=6'
cookie1 = 'SUHB=0N21quxm9-PknS; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; SUB=_2A256SVQNDeRxGeNI71EZ-SjLzjWIHXVZsnxFrDV6PUJbrdBeLRfRkW1LHes3ONaUA2lcYDagK4FFwzwqRTvG6g..; SSOLoginState=1464673373; M_WEIBOCN_PARAMS=uicode%3D20000174; H5_INDEX=2; H5_INDEX_TITLE=%E6%88%91%E6%84%9F%E8%A7%89%E4%BD%A0%E4%BB%AC%E8%BF%98%E6%98%AF%E8%A6%81%E5%AD%A6%E4%B9%A0%E4%B8%80%E4%B8%AA; gsid_CTandWM=4uI5CpOz5aj7lWhwQqF26nGeAcf'
#get_hot_topic_fans_information()
while (True):
    try:
        get_hot_topic_discuss_information()
        time.sleep(7*60)
    except Exception as e:
        time.sleep(30*60)
        continue
#print get_user_info_by_id('609884564')
#get_user_personal_info('5091716249', '1006065921499921')
#get_user_friends_by_page_id('1005055091716249')