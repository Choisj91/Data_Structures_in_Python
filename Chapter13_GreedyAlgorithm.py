coin_list = [1, 100, 50, 500]
print(coin_list)
coin_list.sort(reverse=True) # sort는 실체 본체 조합의 index순서가 바뀜 reverse의 true로 하면 큰 것부터 반대로 정렬됨
print(coin_list)


coin_list = [1, 100, 50, 500]

def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)          #500만 고려하고 나머지 동전에 대해서는 고려하지 않아, 온전히 최적의 500만 고려!
    for coin in coin_list:
        coin_num = value // coin          #나눌 수 있는 데까지 나누고 몫을 구한다 「500원 9개까지 채워진다」
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])   #어떤 종류의 동전이 몇개 쓰였는지를 표시해주기 위해서! 리스트문으로 append로 붙이기
        
    return total_coin_count, details

print(min_coin_count(4720, coin_list))


