
import random

# Define a list of user agents
user_agents = ["Mozilla/5.0 (Windows; U; Windows NT 10.3;; en-US) AppleWebKit/533.14 (KHTML, like Gecko) Chrome/53.0.1483.219 Safari/601.5 Edge/17.40362", "Mozilla/5.0 (Android; Android 6.0.1; SM-D9350V Build/MDB08I) AppleWebKit/537.14 (KHTML, like Gecko)  Chrome/55.0.1667.324 Mobile Safari/535.5", "Mozilla/5.0 (Linux; Android 6.0.1; HTC One_M8 Build/MRA58K) AppleWebKit/536.30 (KHTML, like Gecko)  Chrome/55.0.2528.318 Mobile Safari/600.1", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_8_1; like Mac OS X) AppleWebKit/535.25 (KHTML, like Gecko)  Chrome/52.0.4000.298 Mobile Safari/536.8", "Mozilla/5.0 (Android; Android 7.1.1; Xperia Build/NDE63X) AppleWebKit/535.8 (KHTML, like Gecko)  Chrome/50.0.1112.347 Mobile Safari/534.8", "Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.0; x64; en-US Trident/4.0)", "Mozilla/5.0 (Windows; U; Windows NT 10.5; Win64; x64) AppleWebKit/603.21 (KHTML, like Gecko) Chrome/54.0.3146.235 Safari/600", "Mozilla/5.0 (U; Linux x86_64; en-US) AppleWebKit/601.6 (KHTML, like Gecko) Chrome/47.0.2779.243 Safari/535", "Mozilla/5.0 (Windows; U; Windows NT 10.4; x64; en-US) AppleWebKit/536.18 (KHTML, like Gecko) Chrome/49.0.1291.214 Safari/601.0 Edge/16.59057", "Mozilla/5.0 (iPhone; CPU iPhone OS 9_9_0; like Mac OS X) AppleWebKit/600.8 (KHTML, like Gecko)  Chrome/48.0.1672.254 Mobile Safari/602.8"," Mozilla/5.0 (iPhone; CPU iPhone OS 9_4_5; like Mac OS X) AppleWebKit/537.47 (KHTML, like Gecko)  Chrome/49.0.3706.320 Mobile Safari/534.7", "Mozilla/5.0 (Linux; Linux x86_64) Gecko/20100101 Firefox/61.8", "Mozilla/5.0 (Android; Android 5.0.1; SM-A800H Build/LRX22G) AppleWebKit/535.37 (KHTML, like Gecko)  Chrome/53.0.3834.373 Mobile Safari/535.3", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; en-US) AppleWebKit/534.22 (KHTML, like Gecko) Chrome/49.0.2157.322 Safari/534.4 Edge/10.88427", "Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64) AppleWebKit/603.49 (KHTML, like Gecko) Chrome/54.0.1608.144 Safari/600.8 Edge/17.49536",]

# Generate as many as random user agents you'd like.
user_agents_list = []
for i in range(3):
    user_agents_list.append(random.choice(user_agents))

print("User Agents:")
for user_agent in user_agents_list:
    print(user_agent)
