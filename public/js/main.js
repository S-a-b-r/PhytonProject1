const socket = io('http://localhost:8080');
let actionRoom = 0;

document.getElementById('sendMessage').onclick = function(){
    const userName = document.getElementById('userName').value;
    const message = document.getElementById('message').value;
    const roomName = (document.getElementById('roomName').value)? document.getElementById('roomName').value : 0;
    if((message) && (roomName == actionRoom)){
        socket.emit('message', {userName, roomName, message});
        console.log(roomName);
        console.log(actionRoom);
    }
}

document.getElementById('joinToRoom').onclick = function(){
    const roomName = document.getElementById('roomName').value;
    if(roomName){
        socket.emit('joinToRoom', {roomName});
    }
}
document.getElementById('leaveRoom').onclick = function(){
    const roomName = document.getElementById('roomName').value;
    if(roomName){
        socket.emit('leaveRoom', {roomName});
    }
}

function getRoomMessagesHandler(data){
    if( data && data.length){
        data.forEach(element => {
            const {userName, message} = element;
            document.getElementById('chat').innerHTML += `<b>${userName ? userName:'NoName'}</b>: ${message}<br>`;
        });
    }
}
function messageHandler(data){
    const {userName, message} = data;
    document.getElementById('chat').innerHTML += `<b>${userName ? userName:'NoName'}</b>: ${message}<br>`;

}

function joinToRoomHandler(data){
    let roomName = document.getElementById('roomName').value;
    document.getElementById('chat').innerHTML ='';
    document.getElementById('chatName').innerHTML = `Чат группы ${roomName}`;
    actionRoom = roomName;
    console.log('Прицепился к комнате', data);
}
function leaveToomHandler(data){
    document.getElementById('chat').innerHTML ='';
    document.getElementById('chatName').innerHTML = 'Общий чат';
    document.getElementById('roomName').value = "";
    actionRoom = 0;
    console.log('Вышел из комнаты', data);
}

socket.on('getRoomMessages', getRoomMessagesHandler);
socket.on('joinToRoom', joinToRoomHandler);
socket.on('leaveRoom', leaveToomHandler);
socket.on('message', messageHandler);