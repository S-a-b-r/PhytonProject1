class Socket:
    def __init__(self, sio):

        messages = {
            'all': []
        }

        def getRoomMessages(roomName = None):
            if roomName in messages:
                return messages [roomName]
            return messages['all']

        @sio.event
        def connect(sid, environ):
            print('connect', sid)
        
        @sio.event
        def disconnect(sid):
            print('disconnect')

        @sio.event
        async def message(sid, data):
            roomName = data['roomName']
            if roomName:
                userName = data['userName']
                message = data['message']
                messages[roomName].append(dict(userName = userName, message = message))
                await sio.emit('message', room = roomName, data = dict(userName = userName, message = message))

        @sio.event
        async def joinToRoom(sid, data):
            roomName = data['roomName']
            sio.enter_room(sid, roomName )
            if not(roomName in messages):
                messages[roomName] = []
            await sio.emit('joinToRoom', room = sid, data = True)
            await sio.emit('getRoomMessages', room = sid, data = getRoomMessages(roomName))

        @sio.event
        async def leaveRoom(sid, data):
            sio.leave_room(sid, data['roomName'])
            await sio.emit('leaveRoom', room = sid, data = True)
            await sio.emit('getRoomMessages', room = sid, data = getRoomMessages())