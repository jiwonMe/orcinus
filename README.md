# ORCINUS
> 해군교육사령부 인터넷 편지 시스템

[해군교육사령부 > 인터넷편지쓰기](https://www.edunavy.mil.kr:10003/themes/basic/sub2/4_5.jsp)


## 기술스택
- nginx, django, react

## 배포
- backend
  - ~~AWS LightSail~~(GCP로 이전)
  - Google Cloud Platform
  - [orcinus API](https://orcinus.jiwon.me/api/Orcinus)
- frontend
  - firebase
  - [orcinus API Testor](https://orcinusapi.web.app)

---

## Todos

- 예외처리 (서버에서 500에러 시 메시지)
- 폼 유효성 확인

---

## 서브프로젝트

- [NICE 본인인증 스크래핑](https://github.com/jiwonMe/k-on-cert)

---

## 참고 문서

- CORS 관련
  - [jay-ji.tistory.com/72](https://jay-ji.tistory.com/72)
  - [velog.io/@geunwoobaek/CORS-원인-및-해결방법](https://velog.io/@geunwoobaek/CORS-원인-및-해결방법)

- python 버전 관련
  - [Error: unsupported operand type(s) for +:´ dict´ and ´ dict´](https://www.programmersought.com/article/85406088911/)

- nginx HTTPS 적용
  - [🥑 letsencrypt nginx에 인증 적용하기(ssl)](https://velog.io/@may_soouu/letsencrypt-nginx%EC%97%90-%EC%9D%B8%EC%A6%9D-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0ssl)

- gunicorn 배포
  - [wikidocs: Django 자습 | 03) Nginx, Gunicorn 배포](https://wikidocs.net/6601)

- static 파일
  - [[Deploy] Django 프로젝트 배포하기 - 4. Static 파일](https://nachwon.github.io/django-deploy-4-static/)

- AWS LightSail
  - [[AWS 적응기-2] Lightsail instance 설정하기](https://velog.io/@mhc3357/AWS-%EC%A0%81%EC%9D%91%EA%B8%B0-2-Lightsail-instance-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)

- GCP
  - [GCP 배포](https://velog.io/@codren/GCP-%EB%B0%B0%ED%8F%AC)

- django 학습
  - [점프 투 장고](https://wikidocs.net/77522)

- git 사용법
  - [git commit/push 취소하기](https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html)