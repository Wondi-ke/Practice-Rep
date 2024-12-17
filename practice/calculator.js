function appendToDisplay(input) {
  document.getElementById("display").value += input;
}
function clearDisplay() {
  document.getElementById("display").value="";
}
function calculate() {
 
  try{
    document.getElementById("display").value=eval(display.value);
  }
  catch(error){
    display.value = "Error";
  }
}
function deleteDisplay() {
  document.getElementById("display").value=document.getElementById("display").value.slice(0,-1);
}


