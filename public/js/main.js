const socket = io('http://localhost:8080')

document.getElementById('sendMessage').onclick = function(){
    const userName = document.getElementById('userName').value;
    const message = document.getElementById('message').value;
    const roomName = document.getElementById('roomName').value;
    if(message){
        socket.emit('message', {userName, roomName, message});
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
    if(data){
        document.getElementById('chat').innerHTML ='';
        const roomName = document.getElementById('roomName').value;
        document.getElementById('chatName').innerHTML = `Чат комнаты ${roomName}`;
    }
    console.log('Прицепился к комнате', data);
}

function leaveRoomHandler(data){
    document.getElementById('chat').innerHTML ='';
    document.getElementById('chatName').innerHTML = 'Общий чатик';
    console.log('Вышел из комнаты', data);
}


socket.on('getRoomMessages', getRoomMessagesHandler);
socket.on('joinToRoom', joinToRoomHandler);
socket.on('leaveRoom', leaveRoomHandler);
socket.on('message', messageHandler);