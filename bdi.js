
var global=0;
function myFun(){
var val1 = document.getElementById('id1').value();
global += val1;

var val2 = document.getElementById('id2').value();
global += val2;

document.write(global);
}
