/* Maquina de cafe:
1º Pedir o numero do produto
2º valor do produto
3º Inserir o cartao
4º Senha do cartao
5º Entregar o produto
*/

// Produtos disponiveis 
produtos = ['café', 'capuccino', 'café com leite','chocolate']
// Senha do cartão do usuário
senhaCorreta = 1234;

function pagamento(){
    //Insira o cartão
    alert('insira o cartao');
     //conferindo a senha
     senha = prompt("Digite sua senha: ")
     if (senha == senhaCorreta){
        alert('Senha confirmada. Espere a entrega do produto.');
    } else{
        alert('senha incorreta, por favor tente novamente');
        menuprincipal();
    }
}

// Inicio da função menu pricipal
function menuprincipal(){
     opcao = prompt('Menu: 1. Café (R$ 2,00) | 2. Capuccino (R$ 3,50) | 3.Café com Leite ( R$4,00 ) | 4. Chocolate ( R$4,50 ) | 5. Sair | Digite o número do produto:');
    // chamando a função "Menu principal"

    if (opcao == '1'){
      //opcao 1. café
     alert('voce escolheu: '+ produtos[0]);
     alert(produtos[0]+ ' R$ 2,00');
     pagamento();
    } else if (opcao == '2'){
         //opcao 2. capuccino
         alert('voce escolheu: '+ produtos[1]);
         alert(produtos[1]+ ' R$ 3,50');
         pagamento();
    } else if (opcao == '3'){
        //opcao 2. cafe com leite
        alert('voce escolheu: '+ produtos[2]);
        alert(produtos[2]+ ' R$ 4,00');
        pagamento();
        } else if (opcao == '4'){
        //opcao 2. chocolate
        alert('voce escolheu: '+ produtos[3]);
        alert(produtos[3]+ ' R$ 4,50');
        pagamento();
    } else if(opcao == 5){
         alert("obrigado pela preferencia");
         exit();
    } else {
        alert('Voce digitou uma opcao invalida. Por favor, tente novamente.');
        menuprincipal();
}
} // Aqui é o fim da função
menuprincipal();