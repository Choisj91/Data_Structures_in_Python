# 꼭 알아둬야 할 자료 구조: 배열 (Array)
# 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# 파이썬에서는 리스트 타입이 배열 기능을 제공함

# 1차원 배열: 리스트로 구현시
data_list = [1, 2, 3, 4, 5]

print(data_list)

# 2차원 배열: 리스트로 구현시
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(data_list)

print (data_list[0])
print (data_list[0][0])
print (data_list[0][1])
print (data_list[0][2])
print (data_list[1][0])
print (data_list[1][1])

# 위의 dataset 리스트에서 전체 이름 안에 M 은 몇 번 나왔는지 빈도수 출력하기

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

m_count = 0;

for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count += 1

print(m_count)