function aprova(n1, n2, n3){
    media=n1+n2+n3;
    media/=3;
    media>=7?console.log("Aprovado!"):console.log("Reprovado!");
}

function paraPassar(n1, n2){
    pontos=n1+n2;
    n3=21-pontos;
    console.log("Faltam "+n3+" pontos para passar");
}

n1=8;
n2=5;

paraPassar(n1, n2);

n3=6;

aprova(n1, n2, n3);

n3=8;

aprova(n1, n2, n3);