// const draw = document.getElementById("draw");
// draw.addEventListener('click',function() {
$("canvas").ready(function() { 
    const canvas = document.getElementById("angle");
    const ctx = canvas.getContext("2d");
    ctx.strokeRect(50,25,2000,100);
    ctx.strokeRect(2110,25,340,100);
    ctx.beginPath();
    ctx.moveTo(50, 75);
    ctx.lineTo(2050, 75);
    ctx.moveTo(2400, 25);
    ctx.lineTo(2400, 125);
    ctx.moveTo(2110, 75);
    ctx.lineTo(2400, 75);
    ctx.moveTo(2270, 75);
    ctx.lineTo(2270,125);
    ctx.font = 'italic 35pt Calibri';
    ctx.fillText('B111-3', 2150, 68);
    ctx.font = 'italic 25pt Calibri';
    ctx.fillText('50*50*6', 2120, 118);
    ctx.fillText('1234', 2300, 118);
    ctx.fillText('2', 2410, 85);  
    ctx.stroke(); 
}); 




