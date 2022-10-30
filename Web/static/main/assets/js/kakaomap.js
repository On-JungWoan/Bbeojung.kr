var MARKER_WIDTH = 33, // 기본, 클릭 마커의 너비
    MARKER_HEIGHT = 36, // 기본, 클릭 마커의 높이
    OFFSET_X = 12, // 기본, 클릭 마커의 기준 X좌표
    OFFSET_Y = MARKER_HEIGHT, // 기본, 클릭 마커의 기준 Y좌표
    OVER_MARKER_WIDTH = 40, // 오버 마커의 너비
    OVER_MARKER_HEIGHT = 42, // 오버 마커의 높이
    OVER_OFFSET_X = 13, // 오버 마커의 기준 X좌표
    OVER_OFFSET_Y = OVER_MARKER_HEIGHT, // 오버 마커의 기준 Y좌표
    SPRITE_MARKER_URL = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markers_sprites2.png', // 스프라이트 마커 이미지 URL
    SPRITE_WIDTH = 126, // 스프라이트 이미지 너비
    SPRITE_HEIGHT = 146, // 스프라이트 이미지 높이
    SPRITE_GAP = 10; // 스프라이트 이미지에서 마커간 간격

var markerSize = new kakao.maps.Size(MARKER_WIDTH, MARKER_HEIGHT), // 기본, 클릭 마커의 크기
    markerOffset = new kakao.maps.Point(OFFSET_X, OFFSET_Y), // 기본, 클릭 마커의 기준좌표
    overMarkerSize = new kakao.maps.Size(OVER_MARKER_WIDTH, OVER_MARKER_HEIGHT), // 오버 마커의 크기
    overMarkerOffset = new kakao.maps.Point(OVER_OFFSET_X, OVER_OFFSET_Y), // 오버 마커의 기준 좌표
    spriteImageSize = new kakao.maps.Size(SPRITE_WIDTH, SPRITE_HEIGHT); // 스프라이트 이미지의 크기


var mapContainer = document.getElementById('map'), // 지도를 표시할 div  
    mapOption = { 
        center: new kakao.maps.LatLng(35.176985, 126.910237), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
 

// 마커를 표시할 위치와 content 객체<div> 배열입니</div>다 
var positions = [
    {
        content: '<div>전남대스포츠센터</div>',
        latlng: new kakao.maps.LatLng(35.17503333, 126.9124722)
    },
    {
        content: '<div>전남대스포츠센터</div>',
        latlng: new kakao.maps.LatLng(35.17497222, 126.9126472)
    },
    {
        content: '<div>효동초교입구</div>',
        latlng: new kakao.maps.LatLng(35.16975278, 126.9110389)
    },
    {
        content: '<div>효동초교입구</div>',
        latlng: new kakao.maps.LatLng(35.17071111, 126.9112444)
    },
    {
        content: '<div>전남대사거리(동)</div>',
        latlng: new kakao.maps.LatLng(35.168528, 126.905346)
    },
    {
        content: '<div>전남대사거리(동)</div>',
        latlng: new kakao.maps.LatLng(35.16846389, 126.9044611)
    },
    {
        content: '<div>고려고</div>',
        latlng: new kakao.maps.LatLng(35.193711, 126.899406)
    },
    {
        content: '<div>abc2</div>',
        latlng: new kakao.maps.LatLng(35.19311667, 126.8985806)
    },
    {
        content: '<div>abc3</div>',
        latlng: new kakao.maps.LatLng(35.18875556, 126.8990833)
    },
    {
        content: '<div>abc4</div>',
        latlng: new kakao.maps.LatLng(35.18889167, 126.8988778)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11250833, 126.8967361)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.14807778, 126.9128694)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.16468333, 126.9069722)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.16477778, 126.9073778)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.15506944, 126.9076972)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.19971111, 126.8998917)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.19863611, 126.8997389)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.15128056, 126.9135028)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.152984, 126.910886)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.13921389, 126.9018917)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.14048611, 126.90205)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.12663056, 126.89785)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.12683889, 126.8975361)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.142446, 126.902988)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.14312222, 126.9029222)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11798611, 126.898575)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11853611, 126.8990111)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.14322778, 126.9058722)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.14364444, 126.9071028)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.15332778, 126.9162722)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.18244444, 126.9090028)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.1822, 126.9091)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.15521111, 126.9132444)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11575, 126.8977972)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11437778, 126.8975444)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.13095, 126.89967)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.131783, 126.900075)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.13518611, 126.9016)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.13589167, 126.9014417)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.18716389, 126.9001889)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.18734444, 126.8998694)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.21667778, 126.8946361)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.211668, 126.89763)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.211237, 126.897828)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.10852222, 126.8785333)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.10889167, 126.8784028)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11071111, 126.8764944)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11076389, 126.8766417)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11040278, 126.8927222)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.11103056, 126.8941111)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.15699167, 126.9088417)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.16178056, 126.9076806)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.15133056, 126.9168917)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.18560278, 126.9055306)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.18496389, 126.905675)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.15891389, 126.9064389)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.15973056, 126.9065833)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.203616, 126.898557)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.203498, 126.898249)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.168528, 126.905346)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.16846389, 126.9044611)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.12125556, 126.8985361)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.12170389, 126.8987722)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.14861111, 126.9136167)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.14498056, 126.9090333)
    },
    {
        content: '<div>abc</div>',
        latlng: new kakao.maps.LatLng(35.14556, 126.909608)
    }
],
selectedMarker = null; // 클릭한 마커를 담을 변수;

var infowindow = new kakao.maps.InfoWindow({zIndex:1});

// 마커 이미지의 이미지 주소입니다
var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
    
function displayInfowindow(marker, title) {
    var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';

    infowindow.setContent(content);
    infowindow.open(map, marker);
}

function makeMarker(){
    for (var i = 0; i < positions.length; i ++) {
        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({
            map: map, // 마커를 표시할 지도
            position: positions[i].latlng // 마커의 위치
        });

        // 마커에 표시할 인포윈도우를 생성합니다 
        var infowindow = new kakao.maps.InfoWindow({
            content: positions[i].content // 인포윈도우에 표시할 내용
        });

        // 마커에 mouseover 이벤트와 mouseout 이벤트를 등록합니다
        // 이벤트 리스너로는 클로저를 만들어 등록합니다 
        // for문에서 클로저를 만들어 주지 않으면 마지막 마커에만 이벤트가 등록됩니다
        kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        kakao.maps.event.addListener(marker, 'click', function() {
            var link = 'http://localhost:8000/detail/%EB%B6%81%EA%B5%AC+4406+%EC%A7%84%EC%9B%9407/';
            location.href=link;
        });

        var listEl = document.getElementById('placesList'), 
        menuEl = document.getElementById('menu_wrap'),
        fragment = document.createDocumentFragment(), 
        bounds = new kakao.maps.LatLngBounds(), 
        listStr = '';

        var itemEl = document.createElement('li'),
            itemStr = '<span class="markerbg marker_' + (i+1) + '"></span>' +
                        '<div class="info">' +
                        '   <h5>' + positions[i].content + '</h5>';


        (function(marker, title) {
            kakao.maps.event.addListener(marker, 'mouseover', function() {
                displayInfowindow(marker, title);
            });

            kakao.maps.event.addListener(marker, 'mouseout', function() {
                infowindow.close();
            });
            kakao.maps.event.addListener(marker, 'click', function() {
                var link = 'http://localhost:8000/detail/%EB%B6%81%EA%B5%AC+4406+%EC%A7%84%EC%9B%9407/';
                location.href=link;
            });

            itemEl.onmouseover =  function () {
                displayInfowindow(marker, title);
            };

            itemEl.onmouseout =  function () {
                infowindow.close();
            };
            itemEl.onclick =  function () {
                var link = 'http://localhost:8000/detail/%EB%B6%81%EA%B5%AC+4406+%EC%A7%84%EC%9B%9407/';
                location.href=link;
            };

        })(marker, positions[i].content);          


        itemEl.innerHTML = itemStr;
        itemEl.className = 'item';

        fragment.appendChild(itemEl);
        listEl.appendChild(fragment);
    }
}



// 인포윈도우를 표시하는 클로저를 만드는 함수입니다 
function makeOverListener(map, marker, infowindow) {
    return function() {
        infowindow.open(map, marker);
    };
}

// 인포윈도우를 닫는 클로저를 만드는 함수입니다 
function makeOutListener(infowindow) {
    return function() {
        infowindow.close();
    };
}

/*====================================
             위치 재지정
=====================================*/
// 버튼을 클릭하면 아래 배열의 좌표들이 모두 보이게 지도 범위를 재설정합니다 
var points = [
    new kakao.maps.LatLng(35.176985, 126.910237)
];

// 지도를 재설정할 범위정보를 가지고 있을 LatLngBounds 객체를 생성합니다
var bounds = new kakao.maps.LatLngBounds();    

// LatLngBounds 객체에 좌표를 추가합니다
bounds.extend(points[0]);

function setBounds() {
    // LatLngBounds 객체에 추가된 좌표들을 기준으로 지도의 범위를 재설정합니다
    // 이때 지도의 중심좌표와 레벨이 변경될 수 있습니다
    map.setBounds(bounds);
}