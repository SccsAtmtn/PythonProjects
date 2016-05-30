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
    
    start = data.find('current=fans#place\\" ><strong class=\\"W_f18\\">')
    start = start + len('current=fans#place\\" ><strong class=\\"W_f18\\">')
    end = data.find('<\\/strong>', start)
    fans_num = data[start:end]
    if (len(fans_num)>5):
        personal_info.append('Y')
    else:
        personal_info('N')
    
    
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
    
    start = data.find('$CONFIG[\'page_id\']=\'')
    end = data.find('\';', start)
    start = start+len('$CONFIG[\'page_id\']=\'')
    page_id = data[start:end]
    #print page_id
    
    personal_info = get_user_personal_info(uid, page_id)
    friends = get_user_friends_by_page_id(page_id)
    personal_info.append(friends)
    return personal_info

def get_hot_topic_fans_information():
    global cookie
    page = 0
    user_id = []
    while (True):
        page = page+1
        print page
        url = 'http://weibo.com/p/100808cd410514b09851a9ec3bdbb3e87b858f/followlist?page=%d#Pl_Core_F4RightUserList__34' %page
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
    
    file = open('fans_info.txt', 'w')
    for uid in user_id:
        try:
            time.sleep(5)
            info = get_user_info_by_id(uid)
            for i in range(len(info)-1):
                file.write(info[i]+'    ')
            file.write('[ ')
            for x in info[len(info)-1]:
                file.write(x+' ')
            file.write(']\n')
        except Exception as e:
            continue
            
cookie = 'UOR=blog.csdn.net,widget.weibo.com,login.sina.com.cn; SINAGLOBAL=8910301221166.844.1463715027234; ULV=1464568924612:8:8:2:9000646499887.074.1464568923925:1464488985943; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW-m7g_9bU-TmeCUMVwY8-G5JpX5K2hUgL.Fo-cSheR1KqNSK.2dJLoIc7LxKqL1hnL1K2LxKqL1hBL1-qLxKnLBKML1h.LxKBLB.BLBK5LxKBLB.zLB-eLxKnLB.qL1KnLxKqL1KnLB-qLxKnLBKqL1h2LxK-LB-BLBKqLxKBLBo.LBK5LxKBLBonL1h5LxKBLBonLB-2t; SUHB=0C1CX_sCYuADrK; un=17710305576; SUB=_2A256T_5SDeRxGeNI71EZ-SjLzjWIHXVZPWiarDV8PUNbuNAMLRHHkW9LHesp4ReWlUYQNzQ_R4zX5ghK-0p7bw..; YF-Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; YF-V5-G0=2a21d421b35f7075ad5265885eabb1e4; _s_tentry=weibo.com; Apache=9000646499887.074.1464568923925; YF-Page-G0=f27a36a453e657c2f4af998bd4de9419; WBStore=8ca40a3ef06ad7b2|undefined; WBtopGlobal_register_version=f81ab92b992b2688; SUS=SID-5643896759-1464569346-JA-9pmhn-c6d551136fc58f29df13a85ba5279470; SUE=es%3D40da1b29684c4ad718e5c7cf720e0c39%26ev%3Dv1%26es2%3D4496dfb3a1dce247141110ea185a644f%26rs0%3DA4U%252BSIsCDXBanMojdLJbdVN8ikxSd9PH%252FFu5dDo%252BplGo4Lps5gPvoNgLiAw3DBN35uMp0kOzoXZRUZ9ISyb6DF9LW82WKAdouLXzqvHOziUVREXFFSEXKxig6BmgaBuv1G7hn2AeVxW8%252FFLGmvJEAQBZpX3xoBbFhpiBf6Y65ek%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1464569346%26et%3D1464655746%26d%3Dc909%26i%3D9470%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D5643896759%26name%3D17710305576%26nick%3D%25E7%2594%25A8%25E6%2588%25B75643896759%26fmp%3D%26lcp%3D2015-10-01%252018%253A41%253A01; ALF=1465174146; SSOLoginState=1464569346; wvr=6'
get_hot_topic_fans_information()
#get_user_info_by_id(2748017985)
#get_user_personal_info('5091716249', '1005055091716249')
#get_user_friends_by_page_id('1005055091716249')