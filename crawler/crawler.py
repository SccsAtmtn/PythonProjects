#coding=utf-8
import urllib2

def get_private_info_by_id(uid):
    url = 'http://m.weibo.cn/users/%s' % uid
    req = urllib2.Request(url,
                          headers={
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                              'cookie': 'SUHB=0V5lNqqGfCxXs6; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; H5_INDEX=0_my; H5_INDEX_TITLE=%E6%88%91%E7%9A%84%E5%BE%AE%E5%8D%9A%20; SUB=_2A256Tj4JDeRxGeNI71EZ-SjLzjWIHXVZsUJBrDV6PUJbrdBeLU_AkW1LHesaupiJZCZ4YxLvFh0WjtLD-OrnTg..; SSOLoginState=1464487513; M_WEIBOCN_PARAMS=uicode%3D20000174',
                              'Connection': 'keep-alive'}
                          )
    response = urllib2.urlopen(req)
    data = response.read()
    f = open('D:\\Python Projects\\crawler\\private.html', 'w')
    f.write(data)
    
    private_info = []
    
    start = data.find('性别</span><p>')
    if (start==-1):
        private_info.append('#')
    else:
        start = start+len('性别</span><p>')
        end = data.find('</p></div>', start)
        if (data[start:end]=='男'):
            private_info.append('m')
        else:
            private_info.append('f')
    start = data.find('')

    start = data.find('所在地</span><p>')
    if (start==-1):
        private_info.append('#')
    else:
        start = start+len('所在地</span><p>')
        end = data.find('</p></div>', start)
        private_info.append(data[start:end])

    start = data.find('生日</span><p>')
    if (start==-1):
        private_info.append('#')
    else:
        start = start+len('生日</span><p>')
        end = data.find('</p></div>', start)
        private_info.append(data[start:end])
    return private_info
    
    
def get_friends_by_containerid(containerid):
    url = 'http://m.weibo.cn/page/tpl?containerid=%s_-_FOLLOWERS' % containerid
    req = urllib2.Request(url,
                          headers={
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                              'cookie': 'SUHB=0V5lNqqGfCxXs6; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; H5_INDEX=0_my; H5_INDEX_TITLE=%E6%88%91%E7%9A%84%E5%BE%AE%E5%8D%9A%20; SUB=_2A256Tj4JDeRxGeNI71EZ-SjLzjWIHXVZsUJBrDV6PUJbrdBeLU_AkW1LHesaupiJZCZ4YxLvFh0WjtLD-OrnTg..; SSOLoginState=1464487513; M_WEIBOCN_PARAMS=uicode%3D20000174',
                              'Connection': 'keep-alive'}
                          )
    response = urllib2.urlopen(req)
    data = response.read()
    f = open('D:\\Python Projects\\crawler\\friends.html', 'w')
    f.write(data)
    
    friends = []
    start = 0
    end = 0
    while (True):
        start = data.find('"user":{"id":', end)
        if (start==-1):
            break
        start = start + len('"user":{"id":')
        end = data.find(',', start)
        friends.append(data[start:end])
        
    return friends
        
def get_user_info_by_id(uid):
    url = 'http://m.weibo.cn/u/%s' % uid
    req = urllib2.Request(url,
                          headers={
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                              'cookie': 'SUHB=0V5lNqqGfCxXs6; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; H5_INDEX=0_my; H5_INDEX_TITLE=%E6%88%91%E7%9A%84%E5%BE%AE%E5%8D%9A%20; SUB=_2A256Tj4JDeRxGeNI71EZ-SjLzjWIHXVZsUJBrDV6PUJbrdBeLU_AkW1LHesaupiJZCZ4YxLvFh0WjtLD-OrnTg..; SSOLoginState=1464487513; M_WEIBOCN_PARAMS=uicode%3D20000174',
                              'Connection': 'keep-alive'}
                          )
    response = urllib2.urlopen(req)
    data = response.read()
    f = open('D:\\Python Projects\\crawler\\html.html', 'w')
    f.write(data)
    
    start = data.find('"attNum":"')+len('"attNum":"')
    end = data.find('",', start)
    attNum = data[start:end]
    start = data.find('"mblogNum":"')+len('"mblogNum":"')
    end = data.find('",', start)
    mblogNum = data[start:end]
    start = data.find('"fansNum":"')+len('"fansNum":"')
    end = data.find('",', start)
    fansNum = data[start:end]
    
    info = [uid]
    info.extend(get_private_info_by_id(uid))
    
    start = data.find(',"containerid":"')+len(',"containerid":"')
    end = data.find('",', start)
    containerid = data[start:end]
    info.append(get_friends_by_containerid(containerid))
    return info
    
        
def get_hot_topic_html(url):
    req = urllib2.Request(url,
                          headers={
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                              'cookie': 'SUHB=0V5lNqqGfCxXs6; _T_WM=3272dcaa6c6b3d38a4f9751cefe578cf; H5_INDEX=0_my; H5_INDEX_TITLE=%E6%88%91%E7%9A%84%E5%BE%AE%E5%8D%9A%20; SUB=_2A256Tj4JDeRxGeNI71EZ-SjLzjWIHXVZsUJBrDV6PUJbrdBeLU_AkW1LHesaupiJZCZ4YxLvFh0WjtLD-OrnTg..; SSOLoginState=1464487513; M_WEIBOCN_PARAMS=uicode%3D20000174',
                              'Connection': 'keep-alive'}
                          )
    response = urllib2.urlopen(req)
    data = response.read()
    
    f = open('D:\\Python Projects\\crawler\\ouguan.html', 'w+')
    f.write(data)
    
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
    
    
    file = open('D:\\Python Projects\\crawler\\people.txt', 'w')
    for i in range(len(uid)):
        info = get_user_info_by_id(uid[i])
        file.write(time[i]+'  ')
        for j in range(4):
            file.write(info[j]+'  ')
        for x in info[4]:
            file.write(x+'  ')
        file.write('\n')
        
        
#hot_topic_url = 'http://m.weibo.cn/p/index?containerid=10080819c366f62380fecd399270159fcc2184'
#get_hot_topic_html(hot_topic_url)
info = get_user_info_by_id('2541378475')
print info
#info = get_private_info_by_id('2541378475')
#print info
#get_friends_by_containerid('1005052213170245')