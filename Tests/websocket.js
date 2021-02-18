var socket = new WebSocket('wss://dstream.binance.com/ws/<listenKey>')

var chat = {
    API_KEY = sv25WDcIdIGWmQsjK3euyJtHtsA0JpIQOR3Hp6Fi5sKcRYriVzQGCjzHNQFvnc6a
}

socket.send(message)

socket.onmessage = function(event) {
    var message = event.data;
    console.log(message)
}