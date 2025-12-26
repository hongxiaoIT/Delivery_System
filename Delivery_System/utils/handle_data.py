from faker import Faker

#1、创建一个faker实例


faker = Faker(locale='zh_CN')
#随机创建姓名
for name in range(0,10):
    print(faker.name())

#随机创建地址
for address in range(0,10):
    print(faker.address())

#随机创建岗位
for code in range(0,10):
    print(faker.job())