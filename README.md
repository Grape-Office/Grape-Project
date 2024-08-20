# podoceheng
포도청 프로젝트   
이 프로젝트는 한국 커뮤니티에 특화된 OSINT(Open-Source INTelligence, 공개 출처 정보 수집) 툴입니다.

 ![mov](./mov_sample.gif)

# Usage
1. git clone
    ```bash
    git clone https://github.com/Grape-Office/Grape-Project.git
    cd Grape-Project
    ```
2. command
    ```bash
    python main.py [옵션] [유저명 1] [유저명 2] ...
    ```
    |옵션|설명|
    |:--|:--|
    |-v, --version|버전 확인|
    |-h, --help|도움말 확인|
    |-o, --output|결과를 파일로 출력|
    |-f, --fast|오탐방지 기능 끄기|
    |-d, --domain|입력된 도메인의 정보와 검색할 유저명 비교|
    |-p, --proxy|프록시를 사용해 HTTP 요청 보내기|

- example
    ```bash
    python3 main.py johndoe
    python3 main.py -v
    python3 main.py -h
    python3 main.py -o johndoe
    python3 main.py -f johndoe
    python3 main.py -d domain.com johndoe
    python3 main.py -p 127.0.0.1 johndoe
    ```

    오탐방지 기능을 끄고, "domain.com"의 도메인 정보와 유저명 "johndoe"를 비교하려면 다음과 같이 실행합니다.
    ```bash
    python main.py -f -d domain.com johndoe
    ```

    ![mov](./mov_sample.gif)

# Docker
1. Docker Image build
    ```bash
    sudo docker pull python:3.9-slim-buster
    sudo docker build -t podochung .
    ```
2. Docker Container execution
    ```bash
    docker run -d -t --privileged --name podo podochung
    docker exec -it -u root podo bash
    ```
    
    옵션과 유저명 사용법은 로컬 실행과 동일합니다.

- example
    ```bash
    python main.py tempuser
    python main.py -f -o -d naver.com tempuser
    ```

# Data Collecting
본 프로젝트 진행을 위해 기존에 존재하는 OSINT Tool을 리뷰하고 한국 커뮤니티 사이트 들을 조사했습니다. 이를 정리한 내용은 다음과 같습니다.

### 기존 OSINT Tool 리뷰
|Tool|결과 내보내기|ip proxy|Linux 지원|Windows 지원|Mobile 지원|Mac 지원|UI 정보|오탐 가능성|
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|Sherlock|O|X|O|O|X|O|X|O|
|Maigret|O|X|O|O|X|O|X|O|
|social-analyzer|O|X|O|O|X|O|O|O|
|nexfil|O|O|O|O|X|O|X|O|
|Snoop|O|X|O|O|O|O|O|?|
|NicknameFinder|O|X|O|O|X|O|X|O|
|Gideon|X|X|O|O|X|O|O|O|
|Arina-OSINT|X|X|O|O|X|O|X|O|
|Investigo|X|O|O|O|X|O|O|O|
|recon-ng|O|O|O|O|X|O|O|O|
|SocialPath|X|X|X|X|X|X|X|X|
|Telerecon|O|X|O|X|X|X|O|X|
|WhatsMyName|O|O|X|O|O|O|O|O|
|Usersearch|X|O|X|O|O|O|O|O|
|iDCrawl|O|X|O|O|O|O|O|X|
|OSINT Industries|O|X|O|O|O|O|O|X|

### 한국 커뮤니티 조사 Data 형식
```json
{
    "name": "사이트 이름",
    "url": "유저 매핑 형식 url {유저명}",
    "user_not_found": "유저를 찾을 수 없을 시 html 문구",
    "category": "사이트 분류"
}
```

# License
이 프로젝트는 MIT License를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
