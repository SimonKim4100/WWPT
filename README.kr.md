# WWPT(Wuthering Waves Plate Tracker)
WWPT를 다운로드해 주셔서 감사합니다! <br>
이 프로그램이 최대한 사용자 친화적일 수 있도록 최선을 다했지만 한계가 많았습니다. 따라서 필요한 모든 단계를 안내하는 README 파일을 작성하겠습니다.

## 공지사항
1. 이 프로그램은 게임 파일에 손 대거나 변형하지 않습니다.
2. 데이터베이스는 제체 인증을 사용하므로 해킹을 시도하지 마세요 :)
3. **릴리스(빌드) 파일을 다운해주시고 레포지토리는 다운 받으실 필요 없습니다**. 빌드 파일은 초기 화면 가장 우측에 버전이 붙은 zip파일을 받으시면 됩니다.

## 실행방법
1. 'wwpt.exe'을 실행합니다. 사용자 이름을 묻는 창이 나타날겁니다. 사용자명은 제가 개인적으로 한 명씩 배부해드릴 겁니다. 처음에 사용자 아이디를 제대로 입력했으면 그 이후로는 더 이상 묻지 않습니다.
2. 사용자명이 입력되었으면, 프로그램은 윈도우의 우측 하단 트레이에 보관됩니다. 이후의 모든 실행에서 계속 트레이에 있을겁니다.
3. 트레이 펼치기 --> WWPT 우클릭 --> Settings 누르기 --> 플레이트 갯수 입력 후 save 누르기
4. 이렇게 하면 플레이트 갯수가 자동으로 데이터베이스에 저장됩니다.
5. 모바일로 돌아가서 어플을 새로고침하세요! 끝!

## 게으르시다면...
요약: `batch_maker.bat` 누르셈<br>
게임을 킬 때마다 wwpt.exe을 눌러야됩니다. 근데 이게 귀찮거든요, 그래서 자동화된 batch maker(batch_maker.bat)를 만들어뒀습니다. 이게 뭐하냐면, 게임 런처의 위치랑 exe 파일의 위치를 물어볼겁니다. 제대로 입력하시면 "launch_game_and_wwpt.bat"이 생성되고 이걸 누르면 게임 런처랑 exe를 동시에 실행시켜줍니다.<br>
*요고가 생성되었으면, 앞으로 둘을 따로 누를 필요 없이, 이거 하나만 누르면 됩니다.*<br>
주의하셔야될 점은, **파일의 위치**를 입력하는 것이지, 폴더의 위치가 아닙니다. 예를 들어, 제 파이썬 파일의 경로는 다음과 같겠죠:<br>
`C:\\Users\\username\\Desktop\\GIT\\WWPT\\wwpt.exe`<br>
그리고 이게 아닙니다:<br>
`C:\\Users\\username\\Desktop\\GIT\\WWPT`<br>
더블 슬래쉬를 썼는데 신경 안쓰고 하나로 하셔도 됩니다.

**경고**<br>
배치 파일이 생성된 후에는 런처와 EXE를 옮길 수 없습니다. 혹시 옮길 일이 생기면 다시 생성해주세요.

## APK 파일(안드로이드)
https://drive.google.com/file/d/194xSKdIEXHWDbp3ammzyCtfonitQerk2/view?usp=sharing <br>
걱정 마셈 직접 손으로 만든거라 악성코드는 없음<br>
<br>
Original Repo: https://github.com/SimonKim4100/WWPTm
