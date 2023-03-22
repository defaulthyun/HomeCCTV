# 인공지능을 이용한 Home CCTV

클라우드 AI 융합 전문가 양성 과정 – 기반기술 인프라 모듈프로젝트 3 

---
## 1. 기획의도

현재 홈케어 CCTV시장은 대부분, 고객에게 실시간 영상 확인 서비스 및 녹화본 영상 확인 서비스만을 제공한다. 고객이 실시간으로 영상을 확인하지 않는 한, 사고가
발생한 이후에 녹화된 사고 발생 시점의 영상을 확인해야 한다. 사고 중에는 빠른 대처가 중요한 경우가 있다. 예를 들어, 주택 내 화재 발생 시 발견과 대응이 늦어지면 대형
화재로 이어져 큰 피해가 발생할 수 있다. 또한, 고령자의 경우 낙상사고 발생 시 사고 발견이 지연 되면 부상의 정도가 악화되거나 심한 경우 사망에 이르는 경우도 있다.따라서 객체탐지 기능을 이용해 화재나 낙상사고가 발생하면 사용자에게 알림을 보내 빠른 사고 대처가 가능하게 하는 CCTV를 구현하고자 하였다.

---
## 2. 타겟선정 

외출 시 집에서 일어날 수 있는 혹시 모를 사고와 고령인의 안부가 걱정되는 이들

---
## 3. 목표 

객체 및 움직임 감지를 이용하여 사고발생 시 사용자에게 알림을 주는 AI 홈 CCTV
추후에 알림 등의 기능을 확장하여 다양한 상황에 대응할 수 있게 만드는 것이 목표

### 기능

- 손동작 인식을 이용하여 상황에 맞는 감지 모드를 실행 >> 후에 특정 상황에 어울리는 다양한 감지 모드를 만드는 것이 목표
    - 화재, 연기 객체 감지 
    - 낙상 움직임 감지


---
## 4. 시장분석 

주거침입 범죄를 막아주는 주거보안에 대한 관심이 높아지면서 사물인터넷(IoT)과 인공지능(AI) 기술이 적용된 ‘스마트홈 보안 서비스’가 주목받고 있다. 보안과 관련하여
다양한 서비스들이 지속적으로 출시되고 있으나 화재 감지나 낙상 감지를 접목한 서비스는 아직 활성화되고 있지 않은 실정이다. 이에 이번 3차 모듈 프로젝트를 통해 ‘화재
감지’와 ‘낙상 감지’ 서비스를 구현해보고자 한다. ‘화재 감지’와 ‘낙상 감지' 서비스를 구축함으로써 얻을 수 있는 기대효과는 사고 발생시 사용자에게 즉각적으로 알림을
전송하여 골든 타임 확보를 통해 피해규모를 최소화할 수 있을 것으로 예상한다. 


 < 낙상 관련 참고문헌 >

- 세계보건기구(WHO)에 따르면 낙상은 전 세계적으로 의도하지 않은 부상 및 사망의 두 번째 주요 원인입니다. 낙상은 또한 노인의 기능적 의존성을 자주 유발합니다. "65세 이상 인구의 약 28-35%가 매년 낙상하며 70세 이상 인구의 경우 32-42%로
증가합니다". 낙상의 발생률은 국가마다 다르며 선진국에서는 덜 빈번합니다. 멕시코에서는 60세 이상 노인의 33.5%가 인터뷰 전 1년 동안 적어도 한 번은 넘어졌다. 
(출처 : 대한응급의학회지)
 
- 낙상 유병률은 전 세계적으로 나이가 들면서 증가하며 실제로 중요한 건강 문제로 간주됩니다. 낙상은 가벼운 부상에서 심각한 부상의 20-30% 또는 심지어 사망으로 이어지기 때문에 종종 즉각적인 치료가 필요합니다 . 낙상 감지 시스템은 낙상이 발생하면 경고하여 그 결과를 완화합니다. 환자가 치료를 받는 데 필요한 시간을 개선하는 실시간 낙상 감지로 낙상의 부정적인 결과를 줄일 수 있습니다. 낙상이 빨리 감지되지 않으면 환자가 때때로 바닥에 누워 있어 추가적인 의학적 및 심리적 문제를 일으킵니다. 
(출처: MDPI)

- 노인의 낙상으로 인한 골절은 사망으로도 이어질 수 있다. 우리나라에서 낙상사고로 사망하는 65세 이상 노인은 한 해 83만여 명에 달하며 사고 사망원인 2위, 전체 질병 중에는 암에 이어 5위라고 한다. 최근 발표된 한국인 '질병부담' 순위에서도 7위에 진입, 간암과 위암보다도 높았다. 
(출처: 헬스코리아뉴스)

[고령자 안전사고 10건 중 6건이 낙상사고로 나타났어요! | 안전정보](https://www.consumer.go.kr/user/bbs/consumer/261/731/bbsDataView/3694.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)


< 화재 사고 참고문헌 > 

["조리 중 깜빡한 듯"…사망 발생 수원 아파트 화재, 주방서 시작](https://www.yna.co.kr/view/AKR20230307055400061)
[김제 단독주택 화재로 순직 성공일 소방사…전북도청장 엄수](https://www.newsis.com/view/?id=NISX20230307_0002216605)

---
## 5. 업무분담

이름 | 역할 |
:---:|:---:
강민성 | 모션감지(손동작), 팀장 
박상욱 | 넘어짐(움직임) 감지-데이터 수집/정제/학습 
윤면진 | 넘어짐(움직임) 감지-데이터 수집/정제/학습/시장분석 
현동엽 | 화재 감지-데이터 수집/정제/학습 
박소훈 | 화재 감지-데이터 수집/정제/학습/시장분석


---
## 6. 개발일정


일정 | 내용 
:---:|:---:
2023.03.08 수 | 주제확정, 팀역할분담 
2023.03.09 목 | 팀별 데이터 수집 및 계획 수립
2023.03.10 금 | 기본 모델 제작 
2023.03.13 월 | 기본 모델 제작 
2023.03.14 화 | 세부 프로세스 설계 
2023.03.15 수 | 모델 통합 및 최종 프로그램 제작 
2023.03.16 목 | 모델 통합 및 최종 프로그램 제작 
2023.03.17 금 | 발표 준비 및 제작
2023.03.20 화 | 프로젝트 발표


---
## 7. 개발 스펙

- 프레임워크 
    - tensorflow >= 2.11.0
    - keras >= 2.11.0
    - pytorch >= 1.21.1

- 사용된 모델 및 패키지
    - requirement.txt 참고

- 데이터 셋
    - 넘어짐 감지모델 데이터
        - [Multiple cameras fall dataset](http://www.iro.umontreal.ca/~labimage/Dataset/)
        - [HAR-UP](https://sites.google.com/up.edu.mx/har-up/)

- 화재감지 데이터 
    - Kaggle
        - [FIRE Dataset](https://www.kaggle.com/datasets/phylake1337/fire-dataset?datasetId=529007)
        - [Fire Detection Dataset](https://www.kaggle.com/datasets/atulyakumar98/test-dataset)
        - [Fire and Smoke Dataset](https://www.kaggle.com/datasets/dataclusterlabs/fire-and-smoke-dataset)
        - [Fire Detection from CCTV](https://www.kaggle.com/datasets/ritupande/fire-detection-from-cctv)
        - [Fire Images Database](https://www.kaggle.com/datasets/gondimjoaom/fire-images-database)
    - RoBoFlow
        - [YOLO5) fire-smoke-detection-2 Computer Vision Project](https://universe.roboflow.com/abdullah-erzin-bgpa3/fire-smoke-detection-2)
        - [YOLO8) synthetic fire-smoke Computer Vision Project](https://universe.roboflow.com/yunnan-university/synthetic-fire-smoke)
        - [YOLO8COLAB](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb)
        - [YOLO8CLI](https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/)


---
## 8. 참고문헌(기타)
- [[Cuda] Tensorflow GPU 딥러닝 개발 환경 구축 하기](https://angelplayer.tistory.com/310)
- [[Colab/ngrok/vscode] Colab GPU - VSCode SSH 연동하여 local vscode에서 GPU 사용하기](https://polarcompass.tistory.com/206)
- [📚 악명 높은 CORS 개념 & 해결법 - 정리 끝판왕 👏](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-CORS-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-%F0%9F%91%8F)
- [웹소켓 in Flask](https://my-repo.tistory.com/95)
