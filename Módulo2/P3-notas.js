{ //Média escolar.
    let nota1, nota2, nota3, resultado, situacao

    nota1 = eval(prompt("Digite a sua primeira nota = "))
    nota2 = eval(prompt("Digite a sua segunda nota = "))
    nota3 = eval(prompt("Digite a sua terceira nota = "))

    resultado = (nota1+nota2+nota3)/3
    situacao = (resultado>=7 ? 'Aprovado' : 'Reprovado')

    alert(situacao)
}

{ //Informa a nota que falta para ser aprovado.
    let nota1, nota2, nota3 

    nota1 = eval(prompt("Digite a sua primeira nota = "))
    nota2 = eval(prompt("Digite a sua segunda nota = "))
    
    nota3 = 21 - (nota1+nota2)  
    alert('A nota mínima necessária para ser aprovado é : ' + nota3)
}