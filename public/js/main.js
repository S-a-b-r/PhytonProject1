const socket = io('http://localhost:8080')
var activeRoom = 'all';

document.getElementById('sendMessage').onclick = function(){
    const userName = document.getElementById('userName').value;
    const message = document.getElementById('message').value;
    const roomName = (document.getElementById('roomName').value) ? document.getElementById('roomName').value : 'all';
    if(message){
        socket.emit('message', {userName, roomName, message});
    }
}

document.getElementById('joinToRoom').onclick = function(){
    const roomName = document.getElementById('roomName').value;
    if(roomName){
        socket.emit('joinToRoom', {roomName});
        activeRoom = roomName;
    }
}
document.getElementById('leaveRoom').onclick = function(){
    const roomName = document.getElementById('roomName').value;
    if(roomName){
        socket.emit('leaveRoom', {roomName});
        activeRoom = 'all';
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
    if(data){
        document.getElementById('chat').innerHTML ='';
    }
    console.log('Прицепился к комнате', data);
}
function leaveToomHandler(data){
    console.log('Вышел из комнаты', data);
}

socket.on('getRoomMessages', getRoomMessagesHandler);
socket.on('joinToRoom', joinToRoomHandler);
socket.on('leaveRoom', leaveToomHandler);
socket.on('message', messageHandler);