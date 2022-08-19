let n1 = parseFloat(prompt("Informe o primeiro operando"));
let n2 = parseFloat(prompt("Informe o segundo operando"));
let operador = prompt("Informe o tipo de operação(+, -, *, /, **)");

if (operador== '+'){
    const resultado = n1+n2;
    console.log("O resultado da soma é: "+ resultado);
}
if (operador== '-'){
    const resultado = n1-n2;
    console.log("O resultado da subtração é: "+ resultado);
}
if (operador== '*'){
    const resultado = n1*n2; 
    console.log("O resultado da múltiplicação é: "+ resultado);
}
if (operador== '/'){
    const resultado = parseInt(n1/n2);
    const resto = n1%n2;
    console.log("O resultado da divisão é: "+ resultado);
    console.log("O resto da divisão é :"+ resto);
}
if (operador== '**'){
    const resultado = n1**n2;
    console.log("O resultado da potenciação é: "+ resultado);
}