var a = eval(prompt('digite o primeiro valor: '))
var b = eval(prompt('digite o segundo valor: '))

var op = prompt('escolha a operação: \n"+" -> Adição\n"-" -> Subtração\n"*" -> Multiplicação\n"/" -> Divisão\n', '')
var result
var rest

switch(op){

    case '+':
        result = a + b
        console.log('Resultado da soma: ', result)
        break
    
    case '-':
        result = a - b
        console.log('Resultado da subtração: ', result)
        break

    case '*':
        result = a * b
        console.log('Resultado da multiplicação: ', result)
        break

    case '/':
        result = a / b
        console.log('Resultado da divisão: ', result)
        rest = a % b
        if(a%b != 0){
            console.log('\nResto da divisão: ', rest)
        }
        break
        }