# 배열(array)

> 데이터를 나열하고 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조

배열에는 인덱스(index) 사용가능

index - 데이터 즉 공간의 위치를 알려주는 거

python - list 타입이 배열을 제공하고 있음

### 배열이 필요한 이유

- 같은 종류의 데이터를 효율적으로 관리하기 위해 사용
- 같은 종류의 데이터를 순차적으로 저장

### 배열 장점

- 빠른 접근 가능(인덱스를 통한 접근)

### 배열의 단점

- 추가 / 삭제가 쉽지 않음(가운데 부분이 삭제되면 뒷부분에 있는걸 앞으로 당겨오기 때문에), 아니면 새로운 공간에 추가

## 파이썬

```python
country = 'US'
print (country)
```

## C언어

```c
#include <stdio.h>

int main(int argc, char * argv[])
{
    char country[3] = "US"; //최대 길이 3으로 설정
    printf ("%c%c\n", country[0], country[1]); //해당데이터 출력
    printf ("%s\n", country);    //출력
    return 0;
}
```

# 파이썬과 배열

파이썬에서는 리스트로 배열 구현 가능

1차원 배열 : 리스트로 구현

```python
data_list = [1, 2, 3, 4, 5]
data_list
```

2차원 배열 : 리스트안에 리스트로 구현

```python
data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_list
```

2차원 배열 출력 방법

```python
print (data_list[0])

print (data_list[0][0]) # 1
print (data_list[0][1]) # 2
print (data_list[0][2]) # 3
print (data_list[1][0]) # 4
print (data_list[1][1]) # 5
```

프로그래밍 연습

**연습2: 위의 dataset 리스트에서 전체 이름 안에 M 은 몇 번 나왔는지 빈도수 출력하기**

```python
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
```

정답

```python
m_count = 0
for data in dataset:
    for index in range(len(data)):
        if data[index] == 'M':
            m_count += 1
print (m_count)
```
