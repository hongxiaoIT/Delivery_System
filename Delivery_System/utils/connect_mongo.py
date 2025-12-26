import pymongo
class MongoDB:
    def __init__(self,user='admin',pwd='sq',ip='192.168.19.149',port=27017):
        '''

        :param user:用户名
        :param pwd: 密码
        :param ip: ip地址
        :param port: 端口号
        '''
        self.user=user
        self.pwd=pwd
        self.ip=ip
        self.port=port
        self.client = pymongo.MongoClient(f"mongodb://{user}:{pwd}@{ip}:{port}/")

    def insert(self,collection,query,db='sq-waimai'):
        '''

        :param db: 使用的数据库
        :param collection: 使用的集合
        :param query: 添加的信息
        :return:
        '''
        db=self.client[db]
        collection=db[collection]
        collection.insert_one(query)

    def find_one(self,collection,query,db='sq-waimai'):
        '''

        :param db: 使用的数据库
        :param collection: 使用的集合
        :param query: 查询的信息
        :return: 查询结果
        '''
        db=self.client[db]
        collection=db[collection]
        result=collection.find_one(query)
        return result

    def find_all(self,collection,query,db='sq-waimai'):
        '''

        :param db: 使用的数据库
        :param collection: 使用的集合
        :param query: 查询的信息
        :return: 查询返回所有结果
        '''
        db=self.client[db]
        collection=db[collection]
        results=collection.find(query)
        return results

    def update_one(self,collection,myquery,newvalues,db='sq-waimai'):
        '''

        :param db: 使用的数据库
        :param collection: 使用的集合
        :param myquery: 查询的信息
        :param newvalues: 修改的信息
        :return:
        '''
        db=self.client[db]
        collection=db[collection]
        collection.update_one(myquery,{'$set':newvalues})
        #collection.update_many(myquery, {'$set': newvalues}) 修改所有的

    def delete_one(self,collection,query,db='sq-waimai'):
        '''

        :param db: 使用数据库
        :param collection: 使用的集合
        :param query: 信息
        :return:
        '''
        db=self.client[db]
        collection=db[collection]
        collection.delete_one(query)

    def delete_all(self,collection,query,db='sq-waimai'):
        '''

        :param db: 使用数据库
        :param collection: 使用的集合
        :param query: 信息
        :return:
        '''
        db=self.client[db]
        collection=db[collection]
        collection.delete_many(query)

if __name__ == '__main__':
    #1-创建mongodb数据库连接
    db=MongoDB()
    # #2- 插入数据
    # db.insert('foods',{'restaurant_id':3269,"category_id":3333,"description":'xx非常好吃',"item_id":6872,'name':'烤肉饭'})
    # #3- 查一条数据
    # res=db.find_one('foods',{'restaurant_id':3269})
    # #4- 打印这一条数据
    # print(res)
    # #5- 删除所有数据
    # # db.delete_all('foods',{'restaurant_id':3269})
    # #6-查所有数据
    # res1=db.find_all('foods',{'restaurant_id':3269})
    # #7-打印所有数据
    # print(res1)
    # for one in res1:
    #     print(one)

    #8- 更新数据
    db.update_one('shops',{'name':'淘汰郎小火锅桐乡店'},{'name':'xintain火锅店'})
    res1 = db.find_one('shops', {'id':1})
    print(res1)