# 해쉬 테이블(Hash Table)

# 파이썬 Dictionary 타입이 Hash Table의 예

hash_table = list([i for i in range(10)])
print(hash_table)

def hash_func(key):
    return key % 5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

print (ord(data1[0]), ord(data2[0]), ord(data3[0]))

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('Andy', '0105555333')
storage_data('Dave', '0104444333')
storage_data('Trump', '0102222333')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy'))
print(get_data('Dave'))
print(get_data('Trump'))
