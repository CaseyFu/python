from queue import PriorityQueue
"""
twitter的关注设计
时间线, 其中用到优先级队列
"""


class Tweet:
    """推文类"""
    tweetId = None
    tweetContent = None
    tweetTime = None
    next = None

    def __init__(self, tweetId: int, tweetContent: str):
        self.tweetId = tweetId
        self.tweetContent = tweetContent

    def setTweetTime(self, time: int):
        self.tweetTime = time

    def __lt__(self, other):  # operator <
        return self.tweetTime > other.tweetTime
    # def __cmp__(self,other):
    #     #call global(builtin) function cmp for int
    #     return cmp(self.priority,other.priority)

    def __str__(self):
        return "id:"+str(self.tweetId)+"content:"+str(self.tweetContent)+"time:"+str(self.tweetTime)


class User:
    """用户类"""
    userId = None
    followed = None   # 已经关注的人
    head = None

    def __init__(self, userId: int):
        self.followed = set()
        self.userId = userId
        self.head = Tweet(0, "头")
        self.follow(userId)     # 关注自己, 为了获取自己的动态

    def follow(self, followeeId: int):
        # 关注, 加入set
        self.followed.add(followeeId)

    def unfollow(self, followeeId: int):
        # 取关
        if(self.userId == followeeId):  # 自己不能取关自己
            return
        self.followed.remove(followeeId)

    def post(self, tweet: Tweet):
        # 发推
        tweet.next = self.head.next
        self.head.next = tweet


class Twitter:
    userMap = None  # 模拟数据库
    time = None    # 模拟时间

    def __init__(self):
        self.userMap = {}
        self.time = 0

    def postTweet(self, userId: int, tweet: Tweet):
        # 发推
        if(not self.userMap.get(userId)):
            user = User(userId)
            self.userMap[userId] = user
        tweet.setTweetTime(self.time)
        self.time += 1
        self.userMap.get(userId).post(tweet)

    def getNews(self, userId: int):
        # 根据userId获取推文
        # 每一次都是从优先级队列中取time最大的(最近发表)
        pq = PriorityQueue()
        result = []
        followed: set = self.userMap.get(userId).followed
        for i in followed:
            tweet = self.userMap.get(i).head
            if(tweet.next):
                pq.put(tweet.next)

        while(not pq.empty() ):
            if(len(result) == 10):
                break
            t = pq.get()
            result.append(t)
            if(t.next):
                pq.put(t.next)
        return result
        # if(not user):
        #     print("userId无效")
        #     return
        # p = user.head.next
        # print(userId, "的朋友圈:")
        # while(p):
        #     print("""tweetId:%d\ntweetContent:%s\ntweetTime:%d\n==================""" %
        #           (p.tweetId, p.tweetContent, p.tweetTime))
        #     p = p.next

    def follow(self, followerId: int, followeeId: int):
        # 关注
        if(not self.userMap.get(followerId)):
            user: User = User(followerId)
            self.userMap[follower] = user
        if(not self.userMap.get(followeeId)):
            user: User = User(followeeId)
            self.userMap[followeeId] = user
        self.userMap.get(followerId).follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int):
        # 取消关注
        if(not self.userMap.get(followerId)):
            return
        self.userMap.get(followerId).unfollow(followeeId)


twitter = Twitter()
twitter.postTweet(1, Tweet(5, "这是推特5"))  # 用户1发推5
twitter.postTweet(1, Tweet(6, "今天天气好好啊, 我又发一条推"))  # 用户1发推6
# for i in twitter.getNews(1):      # 获取用户1的推文 [6, 5]
#     print(i)
# print("===================")
twitter.postTweet(2, Tweet(7, "我注册了推"))  # 用户2发推7
twitter.follow(1, 2)    # 用户1关注用户2
twitter.postTweet(2, Tweet(8, "哈哈哈1还关注了我"))  # 用户2发推8
twitter.postTweet(1, Tweet(9, "他他他他他"))  # 用户2发推8

# for i in twitter.getNews(1):      # 是[8, 6, 5] 还是[8, 7, 6, 5], 应该是[8, 6, 5]
#     print(i)

# print("===================")
# twitter.unfollow(1, 2)  # 取关
for i in twitter.getNews(1):      # [6, 5]
    print(i)
# print("===================")


# b = BiHeap()
# b.test()
# t1 = Tweet(1, "hhh")
# t2 = Tweet(2, "yyy")
# b.exchObj(t1, t2)
# print(t1)
# print(t2)
