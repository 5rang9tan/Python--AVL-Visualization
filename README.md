<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/5rang9tan/Python-AVL-Visualization">
    <img src="cubes/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Python AVL Tree Visualization</h3>

  <p align="center">
    파이썬을 통해 AVL 트리의 노드 생성 및 삭제 과정을 시각화합니다.
    <br />
    <a href="https://cubes.kr"><strong>공식 홈페이지 »</strong></a>
    <br />
    <br />
    <a href="mailto:taeyang@cubes.kr">버그 신고</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## 프로젝트 개요

AVL 트리는 이진 탐색 트리의 일종으로, 각 노드의 자식 노드의 높이 차이가 1 이하가 되도록 균형을 유지하는 자료 구조입니다. 이 프로젝트에서는 AVL 트리에 데이터를 추가하고 삭제하는 과정을 시각화하여 AVL 트리가 어떻게 균형을 유지하며 동작하는지를 확인할 수 있습니다.

### AVL 트리 노드 생성 과정

1. **루트 노드 확인**
   - 트리가 비어있으면 새로운 노드를 루트로 설정합니다.

2. **값 비교**
   - 추가할 노드의 값이 현재 노드의 값과 비교됩니다.
     - **왼쪽 서브트리**: 값이 현재 노드보다 작으면 왼쪽 서브트리로 진행합니다.
     - **오른쪽 서브트리**: 값이 현재 노드보다 크면 오른쪽 서브트리로 진행합니다.

3. **재귀적 호출**
   - 적절한 위치에 도달할 때까지 재귀적으로 호출하여 노드를 추가합니다.

4. **노드 추가**
   - 빈 자리를 발견하면 새로운 노드를 생성하여 해당 위치에 추가합니다.

5. **균형 조정**
   - 노드가 추가된 후 균형을 확인하고 필요에 따라 회전 연산을 수행하여 트리의 균형을 유지합니다.

6. **완료 메시지**
   - 노드가 성공적으로 추가되면, 성공 메시지를 반환합니다.
  
### AVL 트리 노드 삭제 과정

1. **노드 검색**
   - 삭제할 노드를 찾기 위해 트리를 탐색합니다.
   - 현재 노드의 값과 삭제할 값 비교:
     - **왼쪽 서브트리**: 삭제할 값이 현재 노드보다 작으면 왼쪽 서브트리로 이동합니다.
     - **오른쪽 서브트리**: 삭제할 값이 현재 노드보다 크면 오른쪽 서브트리로 이동합니다.

2. **노드 발견**
   - 삭제할 노드를 찾으면, 노드의 자식 수에 따라 삭제 방법을 결정합니다.

3. **자식 수에 따른 삭제 처리**
   - **차수가 2인 경우**:
     - 삭제할 노드가 두 자식을 가진 경우:
       - 오른쪽 서브트리의 최소값을 찾아 해당 노드의 값으로 대치합니다.
       - 최소값 노드를 삭제합니다.
   - **차수가 1인 경우**:
     - 삭제할 노드가 단일 자식 노드를 가진 경우:
       - 해당 노드를 삭제하고, 자식을 현재 노드의 위치로 대체합니다.
   - **차수가 0인 경우**:
     - 삭제할 노드가 자식이 없는 경우:
       - 해당 노드를 단순히 삭제합니다.

4. **균형 조정**
   - 노드를 삭제한 후 균형을 확인하고 필요에 따라 회전 연산을 수행하여 트리의 균형을 유지합니다.

5. **완료 메시지**
   - 삭제가 완료되면 성공 메시지를 반환합니다.

### 필요한 파이썬 확장 라이브러리

이 프로젝트를 실행하기 위해 필요한 파이썬 확장 라이브러리는 다음과 같습니다:

- `matplotlib`: 데이터 시각화를 위한 라이브러리
- `networkx`: 복잡한 네트워크를 생성하고 분석하기 위한 라이브러리
- `numpy`: 과학적 계산을 위한 라이브러리

#### 설치 방법

다음 명령어를 사용하여 필요한 라이브러리를 설치할 수 있습니다:

```bash
pip install matplotlib networkx numpy
```
## 사용 언어

- <img src="https://img.shields.io/badge/Operating System-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white">
- <img src="https://img.shields.io/badge/Language-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
- <img src="https://img.shields.io/badge/Project Encoding-%23121011?style=for-the-badge"><img src="https://img.shields.io/badge/UTF 8-EA2328?style=for-the-badge">

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## 사용 방법
1. Python 파일을 실행합니다.
2. plt show 창을 닫으면 다음 과정이 팝업됩니다.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

해당 소스코드는 MIT License를 사용합니다. 더 많은 정보는 `LICENSE.txt` 를 참고하십시오.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

  <a href="https://instagram.com/5rang9tan">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"><img src="https://img.shields.io/badge/@5rang9tan-515151?style=for-the-badge">
  </a>
  <a href="https://x.com/5rang9tan">
    <img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white"><img src="https://img.shields.io/badge/@5rang9tan-515151?style=for-the-badge">
  </a>
  <a href="https://threads.net/5rang9tan">
    <img src="https://img.shields.io/badge/Threads-000000?style=for-the-badge&logo=threads&logoColor=white"><img src="https://img.shields.io/badge/@5rang9tan-515151?style=for-the-badge">
  </a>
  <a href="mailto:﻿"taeyang@cubes.kr">
    <img src="https://img.shields.io/badge/mail-000000?style=for-the-badge&logo=gmail&logoColor=white"><img src="https://img.shields.io/badge/taeyang@cubes.kr-515151?style=for-the-badge">
  </a>
