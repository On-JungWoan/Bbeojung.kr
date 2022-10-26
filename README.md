# 뻐정 : 정류장 혼잡도 예측 ML Model 개발 및 서비스

<br>
버스를 타러 정류장에 갔는데 예상치 못하게 사람이 너무 많아 곤욕을 치르셨던 경험 한 번쯤 있으실겁니다.<br>
그렇다면 **미리 정류장에 사람이 얼마나 있을지 알 수는 없을까?** 하여 시작된 것이 뻐정 프로젝트입니다.

특히 22년 5월 2일부터 **실외 마스크 착용 의무화가 해제**됨으로써 정류장처럼 사람이 정적으로 많이 모여있는 곳에 가기를 불안해 하시는 분들이 늘어나고 있습니다.

**뻐정은 이러한 문제점들을 완화**하고 사용자에게 기타 다양한 정보를 제공하기 위해 탄생한 프로젝트입니다.

**Developer : 온정완**

<br>
<br>

# 1. URL 주소 & Web 화면 구성

## 1) URL 주소 (운영 종료)

> **URL : http://bbeojung.kr**

아직은 지원 받는 곳이 없어서 해당 프로젝트 비용은 모두 **개인 사비**로 진행하고 있습니다. 서버는 AWS 3개월 무료 플랜을 사용하고 있어 **22년 8**월부터는 **해당 URL 접속이 불가**할 수도 있습니다.

## 2) Web 화면 구성

 1. **메인 화면**
 
![main_jpg](https://user-images.githubusercontent.com/84084372/174231183-6f34ce39-f180-480c-a075-0678677bf190.jpg)
**소재지**와 **정류장명**을 입력하고 **노선명**(생략 가능)을 입력하면 선택 된 정보에 대한 상세페이지로 이동합니다.

<br>


 2. **상세 화면**
 
![detail](https://user-images.githubusercontent.com/84084372/174231536-f2c2078c-7c75-4c77-9ef5-d993620c9854.jpg)
선택된 정보에 대한 **통계량**을 출력합니다.

<br>
<br>

# 2. Model

사용 DataSet 및 Feature, 학습 방법에 대한 간략한 정보입니다.

## 1) DataSet
|                |출처                          |내용                         |
|----------------|-------------------------------|-----------------------------|
|`광주_버스_이용객.csv`|공공데이터 포털|광주광역시 3~4월 버스 이용객            |
|`광주광역시_정류장_위치정보.csv`          |공공데이터 포털|정류장의 경도, 위도 데이터|
|`Google Geocoding API`          |Google Maps|해당 경/위도의 주소 정보를 반환해 줌.|
|`광주광역시_행정지역_인구.csv`          |KOSIS|광주광역시의 행정지역(똥)별 인구 데이터셋|
|`법정동_행정동_맵핑.csv`          |공공데이터 포털|전국 법정동과 행정동 맵핑 데이터|
|`2018~2022_공휴일_정보.csv`          |공공데이터 포털|2018~2022 공휴일 정보|
|`기상청_기상_데이터.csv`          |기상자료개방포털|기온, 습도, 강수량, 풍속|


## 2) Train Feature

 - Distance
	 - 광주광역시 주요 정류장에 대한 거리정보
 - Population
	 - 해당 소재지(동)의 인구 정보
 - Weekday
	 - 요일 One-Hot Encoding)
 - Mean & Sum
	 - 주요 변수의 요약 통계량
 - Congestion
	 - 주요 변수별 탑승객 Min-Max Scaling
 - Weekday & Holiday
	 - 주말 및 공휴일 여부
 - Weather data
	 - 온도, 습도, 강수량, 풍속 데이터
 - Label Encoding
	 - 주요 변수 Label Encoding 값

## 3) Train Model
모델 학습 과정은 반자동 ML 라이브러리인 Pycaret을 이용하였습니다.
<br>

#### I. Find Best Model
	R square 값을 기준으로 지도 학습 라이브러리의 성능 계산 Best 3 Model을 선택함

#### II. HyperParameter Tuning
	Best 3 Model에 대해서 Random Search 방식으로 하이퍼 파라미터 튜닝 진행

#### III. Model Blending
	Best 3 Model Blending

#### IV. Model Ensemble
	배깅 방식으로 앙상블 진행

## 4) Model 성능 평가
fold 값을 10으로 하여 k-fold 교차검증을 해주었습니다.

![image](https://user-images.githubusercontent.com/84084372/174237056-c7c61f6a-51d8-40c6-8205-0c0e41e47b9e.png)


<br>
<br>


# 3. Web

## 1) 사용 Server 및 DB

| 서버/DB | 내용 |
|--|--|
| 클라우드 시스템 | AWS Lightsail |
| Web Server | Nginx |
| WSGI Server | Gunicorn |
| DB | PostgreSQL |
| Application | Django |

우선, **클라우드 시스템**으로는 **AWS Lightsail**을 사용해 주었습니다. AWS가 비싸기도 하고 사용 방법이 어렵다는 단점이 있지만, **LightSail**이 이 단점들을 모두 보완해 줄 수 있기에 클라우드 서버로는 AWS의 라이트 세일을 채택하였습니다.
한 달 **5달러** 요금의 서버를 구입하였는데 AWS에서 **3개월 무료 플랜**을 지원해줘서 지금은 무료로 사용하고 있습니다.

**웹 서버**로는 일반적으로 Django와 많이 사용하는 **Nginx**를 사용하였습니다.

또한, 동적 웹페이지를 처리할 **WSGI 서버**로는 **gunicorn**을 채택하였습니다.

위스키 서버 어플리케이션으로는 사용하기 편리한 완성형 프레임워크 **Django**를 사용하였습니다.

**Nginx**가 정적 요청을 처리하고 동적 요청은 **gunicorn**이 장고에 넘겨줘서 처리하는 방식으로 웹이 동작하고 있습니다.


## 2) Back-End Flow Chart

![image](https://user-images.githubusercontent.com/84084372/174237817-a7e9fb91-9fdc-47e8-b5f3-f1efaea05290.png)

우선, 파이썬 환경에서 학습을 마친 모델을 **pickle파일**로 저장하여 서버에 저장해둡니다.

이후 Django 환경의 **View함수**에, pickle 파일을 불러와 **predict**하는 알고리즘을 미리 작성해두고, 사용자가 url을 요청하면 **View함수**를 호출하여 **html**로 넘겨주는 형태로 웹이 동작합니다.


<br>
<br>


# 4. 활용 방안


앞서 보여드렸던 웹은 제가 제시하는 모델 활용 방안의 일부이고, 이외에도 해당 모델을 활용할 수 있는 방안은 많이 있을 것입니다.

모델을 **버스 전광판 시스템**과 연동하여 전광판에 정류장 혼잡도를 제공할 수도 있고,

사용자가 접근하기 편리하도록 **앱**이나 **챗봇**을 출시하는 방향도 생각중에 있습니다.
