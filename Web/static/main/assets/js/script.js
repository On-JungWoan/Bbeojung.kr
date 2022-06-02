function change() {
  let guIdx = document.getElementById('location').selectedIndex;
  // 동1 서2 남3 북4 광산5
  const guIdxDoc = {
    0: df,
    1: 동구,
    2: 서구,
    3: 남구,
    4: 북구,
    5: 광산구,
  };

  guIdxDoc[0].classList.add('displayNone');
  for(let i=1; i<=5; i++){
    guIdxDoc[i].classList.add('displayNone');
  }
  guIdxDoc[guIdx].classList.remove('displayNone');
}