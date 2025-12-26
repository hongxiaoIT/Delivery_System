import requests
import threading
HOST = 'http://127.0.0.1:9090'
"""
def test():
    url = f'{HOST}/sq3'
    pyload ={
        "key1":"value1",
        "key2": "value2"
    }
    res = requests.post(url,json=pyload)
    print(res.text)
"""
import time
#-----------------------创建申诉接口-----
def create_order(inData):
    url = f'{HOST}/api/order/create/'
    payload = inData
    res = requests.post(url,json=payload)
    return res.json()

#-----------------查询接口------------
#interval超时5s,超时时间30s
def get_order_result(orderId,interval=5,timeout=30):
    url = f'{HOST}/api/order/get_result1/'
    payload = {'order_id':orderId}
    start_time = time.time()
    print("start_time---->",start_time)
    end_time = start_time + timeout
    print("end_time---->", end_time)
    count = 0#查询次数
    #判断查询是否超时
    while time.time()<end_time:
        print("time.time()",time.time())
        resp = requests.get(url,params=payload)
        count += 1
        if resp.text:
            print(count)
            break
        else:
            print(f"第{count}次查询，没有结果，请耐心等待")
        time.sleep(interval)
    return resp.text

if __name__ == '__main__':
    start_time = time.time()
    testData = {
					"user_id": "sq123456",
					"goods_id": "20200815",
					"num":1,
					"amount":200.6
				}
    id = create_order(testData)['order_id']
    # res = get_order_result(id)
    # print(res)
    #----------------使用多线程操作
    #1、创建子线程
    t1 = threading.Thread(target=get_order_result,args=(id,))

    #-----如果主线程结束了，子线程直接退出
    t1.setDaemon(True)
    t1.start()
    #----------------假如还有其他接口在同时进行测试
    for one in range(40):
        time.sleep(1)
        print("其他接口的测试----",one)


    end_time = time.time()
    print("----------------整个自动化耗时---",end_time - start_time)

