# KoWiki Interlang Parser

### 개요
이 프로젝트는 [parse-langlinks] 소스코드를 참고하였습니다.

[parse-langlinks]: https://github.com/billdthompson/parse-langlinks

### 데이터 다운로드

KoWiki Langlinks 파일 다운로드 주소
1. https://dumps.wikimedia.org/kowiki/latest/ 접속 후,
2. kowiki-latest-langlinks.sql.gz 클릭

### 실행 방법

```
python -s {SOURCE_FILE} -d {DESTINATION_FILE} -lang {TARGET_LANGUAGE}
```

### 저장 데이터 포맷
- Page ID
- Target Language
- Title

### Page ID 사용법
```
https://ko.wikipedia.org/?curid={PAGE_ID}
```