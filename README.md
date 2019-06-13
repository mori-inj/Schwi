# Schwi

* 유클리드 원론의 기하학 명제들을 초기조건에서 출발해 공리들을 순차적으로 적용해가며 논리적으로 증명  
* Python 사용  
* 이미지  
  <p align="center">
    서로 다른 두 점 A,B가 주어졌을때 AB를 한변으로 하는 정삼각형의 작도 가능성 증명  
    <img src="https://raw.githubusercontent.com/mori-inj/temp_md/master/geo.jpg" width="350"/>
    <img src="https://raw.githubusercontent.com/mori-inj/temp_md/master/geo_result.jpg" width="350"/>
  </p>
* 기본적으로 coq로 할 수 있는 일들과 유사(증명 보조 및 자동 증명)  
* 공리를 적용하고자 할 때 논리적으로 적용 가능한 공리인지 판단하고, 적용 가능하다면 결론에 해당하는 조건들을 현재 상태에 추가  
* 현재 상태의 조건들에 적용할 수 있는 공리들을 모두 적용해 새로운 상태들을 만들고 이를 반복해서 원하는 결론의 조건이 포함된 상태를 유도해 낼 수 있는지 검증  
* 증명 보조는 완료된 상태이고 자동 증명도 구현은 되었으나 자동 증명 시 실행 시간이 지나치게 긺(branching factor가 36 이상이므로 적절한 가지치기 필요)  
* 증명 과정이 상태를 정의하고 둘 수 있는 수들을 두고(공리를 적용하고) 목표로 하는 상태를 찾는 것(승리/결론)이므로 기존의 강화학습 방식을 적용해 자동 증명 과정을 최적화 하는 것이 목표  