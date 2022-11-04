# Bbeojung PROJECT REPORT
## Contents

- [**Ⅰ. BASIC DATA**](#ⅰ-basic-data)

- [**Ⅱ. OPENING REMARKS**](#ⅱ-opening-remarks)

- [**Ⅲ . IMPLEMENTATION DETAILS**](#ⅲ--implementation-details)

  1. [Real-time obj. detection](#1-real-time-obj-detection)

      [1.1 Inference process](#11-inference-process)

      [1.2 Visualization inference performance](#12-visualization-inference-performance)

      [1.3 Using multi angle of view (예정)](#13-using-multi-angle-of-view-%EC%98%88%EC%A0%95)

  2. [Bus demand predicting model](#2-bus-demand-predicting-model)

      [2.1 Using data](#21-using-data)

      [2.2 Train feature](#22-train-feature)


      [2.3 Ensemble algorithm](#23-ensemble-algorithm)

      [2.4 Hyperparameter tuning](#24-hyperparameter-tuning)

  3. [Web](#3-web)


- [**Ⅳ. TEST**](#ⅳ-test)

  1. [Real-time object detection](#1-real-time-object-detection)

  2. [Web](#2-web)

<br>

## Ⅰ. BASIC DATA

<p align="center"><img src="https://user-images.githubusercontent.com/84084372/199860610-1a075e3f-267b-4314-bdb8-2b224f55c426.png" style="border: 1px solid black"></p>

- **Project Title**

  - 뻐정 (Bbeojung.kr)

- **Participation**

  - 개발 : 온정완

  - 기획/ppt/발표 : 진유승

- **Project Dates**

  - 1차 프로토타입 (Jun. 2022 ~ Jul.2022)

  - 2차 개선버전 (Oct. 2022 ~ Nov. 2022)

- **Detail description link**

  - Summary : <https://on-jungwoan.github.io/bbeojung/bbeojung/>

  - full description : <https://on-jungwoan.github.io/categories/bbeojung>


<br>

## Ⅱ. OPENING REMARKS

- **Summary**

```
뻐정은 obj detection 모델과 버스 수요 예측 ML 모델 및 광주광역시 BIS가 결합하여 탄생한 통합 플랫폼입니다.
기존에 광주광역시가 제공한 버스 출발, 도착 예정 정보와 더불어 정류장별 수요 예측을 통해 시민들의 버스 이용 편의를 극대화하고
배차간격, 노선 체계 등의 결정과 같은 의사결정에 도움을 주는 플랫폼입니다.
```

- **Objectives/Skills**

  - LGBM

  - SSD Network Model (TRT Engine)

  - CUDA Stream

- **Overview**

<p align="center"><img src="https://user-images.githubusercontent.com/84084372/199863866-1200ae81-2230-40b6-a0bb-ef9d77731324.png" width="50%" style="border: 1px solid black"></p>


cctv와의 rtsp 통신을 바탕으로 특정 정류장의 real-time 객체 인식을 진행합니다. 또한, 이 인원 중 특정한 버스에 탑승할 인원이 몇 명이나 되는지 예측합니다. 사용자에게는 위 결과를 원활 / 보통 / 혼잡으로 나누어 제공합니다.

<br>

## Ⅲ . IMPLEMENTATION DETAILS

### 1. Real-time obj. detection

#### 1.1 Inference process

<p align="center"><img src="https://user-images.githubusercontent.com/84084372/199865040-079bacef-9d0a-4a0a-8bb4-0ae64ce1603e.png"></p>

- Description

```
coco 데이터셋으로 pre-train 된 SSD 모델을 obj detection 모델로 채택하였습니다. 또한, real-time 추론을 위해 2가지 최적화를 해주었습니다.

1. TensorRT로 변환 후 Engine 모듈 분리
2. CUDA Stream을 사용한 Memory copy
```

#### 1.2 Visualization inference performance

<p align="center"><img src="https://user-images.githubusercontent.com/84084372/199866075-81556b2c-1d10-4648-865b-e955d2b1e090.png"></p>

- Description

```
1. 기존 ssd 모델 대비 연산속도 약 24배 향상
2. Precision Reduction에 따른 confidence loss는 거의 없음
```

#### 1.3 Using multi angle of view (예정)

<p align="center"><img src="https://user-images.githubusercontent.com/84084372/199866542-09fcacb0-54aa-4489-90f4-5e8a9ca6c50c.png" width="80%"></p>

- Description

```
객체가 장애물 또는 사람에 가려져서 인식되지 않는 문제를 해결하기 위해 다음과 같은 해결책을 제시합니다.

1. 시범 정류장에 다양한 화각의 cctv를 설치하여 각 화각의 데이터셋을 확보
2. 해당 데이터셋에 대해 모델 파인튜닝 및 블랜딩
```

### 2. Bus demand predicting model

#### 2.1 Using data

<p align="center"><img src="https://user-images.githubusercontent.com/84084372/199867243-ac59cb13-e791-43cc-aa74-11766ad1efb7.png" width="60%"></p>

#### 2.2 Train feature

feature | description
:--: | :--:
거리 | 광주광역시 9개 주요 정류장과의 거리
인구 | 해당 정류장 소재지(동) 주민등록 인구
통계량 | 주요 변수(정류장명, 노선명, 요일, 월, 시간)에 대한 요약 통계량
혼잡도 | 주요 변수(정류장명, 노션명, 요일)별 이용승객 min-max scaling
주말여부 | 주말여부 one-hot encoding
기상청 데이터 | 온도, 습도, 풍속, 강수량
요일 | weekday one-hot encoding

<p align="center"><img src="https://user-images.githubusercontent.com/84084372/199867455-1f0d841a-9c04-4532-8b3b-dccf26ee0c9c.png" width="80%"></p>

- Description

```
모델에 feature를 차례로 넣어보며 score를 파악
score 개선이 있는 것을 확인 하였음
```

#### 2.3 Ensemble algorithm

![image](https://user-images.githubusercontent.com/84084372/199868294-74b2b2c3-3859-4643-9d85-31d353767dbd.png)

- Description

```
초기 모델 RandomForest에서 부스팅 계열 LGBM으로 학습 모델 변경

- 학습 속도 15배 이상 개선
- error 약 20% 감소
```

#### 2.4 Hyperparameter tuning

- **Search algorithm**

  random search

- **Score**

  - RMSE : 2.3404

  - R2 : 0.9006

### 3. Web

![image](https://user-images.githubusercontent.com/84084372/199869772-e937c137-1154-44e0-ac0a-8143a7483439.png)

![image (1)](https://user-images.githubusercontent.com/84084372/199869766-d1db9833-ea44-43eb-b653-9f453e48ed14.png)

<br>

## Ⅳ. TEST

### 1. Real-time object detection

- **Link**

  https://user-images.githubusercontent.com/84084372/199408447-ee91aa5e-6fde-41b1-826b-5508998d791c.mp4

### 2. Web

- **Link**

  https://user-images.githubusercontent.com/84084372/199414700-e879d07b-c96e-4323-af01-57dbf2152fed.mp4
