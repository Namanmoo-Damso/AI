# CONTRIBUTING

이 리포지토리는 팀의 Git 컨벤션을 따릅니다. 상세 규칙은 노션에 정리되어 있으니(팀 문서) 참고하세요.

핵심 요약
- 브랜치: `dev`에서 개발 → PR → `main`으로 병합
- 커밋 메시지: `type(scope): subject` (예: `feat(api): 로그인 엔드포인트 추가`)
- PR 템플릿과 체크리스트를 사용하세요

로컬 설정
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env && edit .env
```

Pre-commit 설치
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

PR 체크리스트
- [ ] 브랜치 이름 규칙 준수
- [ ] `pre-commit` 훅 통과
- [ ] 변경 사항과 테스트 방법을 PR에 기재
- [ ] 관련 이슈 링크 포함

감사합니다.
