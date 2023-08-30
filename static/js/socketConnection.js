const rgbVideoEl = document.getElementById("rgb-video")
const flirVideoEl = document.getElementById("flir-video")

var socket = io();
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});

function sendVideoRequest(){
    socket.emit("video_request","aku adalah pesan yang yaa")
}

socket.on("message",function(message){
    console.log(message)
})

socket.on("rgb_video",function(frame){
    console.log(" rgb video grabbed")
    rgbVideoEl.src ="data:image/jpeg;base64,"+frame
})

socket.on("flir_video",function(frame){
    console.log(" flir video grabbed")
    flirVideoEl.src ="data:image/jpeg;base64,"+frame
})

sendVideoRequest()