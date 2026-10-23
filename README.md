# 💻 Network Programming Lab

파이썬(Python) 기반 네트워크 소켓 통신, 동시성 아키텍처 및 보안 메신저 구축 아카이브입니다.

---

## 📑 Hands-on Projects

### 1. [Python TCP 소켓 프로그래밍 및 멀티스레드/Queue 기반 통신 (2026-10-23)](./01_Python_Socket_Chat)
* **주요 기술:** Python TCP Socket, 튜플 언패킹, Multi-Threading (`threading.Thread`), Producer-Consumer 패턴 (`queue.Queue`)
* **핵심 트러블슈팅:** `accept()`/`recv()`/`input()` I/O 블로킹 현상 분리, Race Condition 방지를 위한 전송 스레드 일원화, Windows 환경 `accept()` 블로킹에 따른 `Ctrl+C` 먹통 현상 해결