$(function () {
    var canvas = $('.whiteboard')[0]
    var context = canvas.getContext('2d')
    var current = {
        color: 'black'
    }
    var drawing = false

    function drawLine(x0, y0, x1, y1, color) {
        context.beginPath()
        context.moveTo(x0, y0)
        context.lineTo(x1, y1)
        context.strokeStyle = color
        context.lineWidth = 2;
        context.stroke()
        context.closePath()
    }


})