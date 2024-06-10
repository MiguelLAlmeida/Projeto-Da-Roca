function busca(categoria) {
    switch(categoria) {
        case 'Frutas':
            buscaFrutas();
            break;
        case 'Verduras':
            buscaVerduras();
            break;
        case 'Legumes':
            buscaLegumes();
            break;
    }
}

function buscaTodos(){
    fetch('http://localhost:3000/produtos')
        .then(response => {
            return response.json();
        })
        .then( (dados) => {
            Todos(dados)
        })
}
function buscaLegumes(){
    fetch('http://localhost:3000/produtos')
        .then(response => {
            return response.json();
        })
        .then( (dados) => {
            Legumes(dados)
        })
}
function buscaVerduras(){
    fetch('http://localhost:3000/produtos')
        .then(response => {
            return response.json();
        })
        .then( (dados) => {
            Verduras(dados)
        })
}
function buscaFrutas(){
    fetch('http://localhost:3000/produtos')
        .then(response => {
            return response.json();
        })
        .then( (dados) => {
            Frutas(dados)
        })
}
function Todos(produtos){
    pagina = ''
    for (let i in produtos){
        pagina += '<div class="items">'
        pagina += '<h1 class="'+produtos[i].categoria+'">'+produtos[i].nome+'</h1>'
        pagina += '<img src="./imgs/'+produtos[i].nome+'prod.png">'
        pagina += '<h1>R$'+produtos[i].valor+'</h1>'
        pagina += '<select name="" id="categorias">'
        pagina += '<option value="Quilo">Quilo</option>'
        pagina += '<option value="Duzia">Duzia</option>'
        pagina += '<option value="Unidade">Unidade</option>'
        pagina += '</select>'
        pagina += '<p><button class="comprar">Comprar</button></p>'
        pagina += '</div>'
    }
    document.getElementById("catalogo").innerHTML = pagina
}
function Verduras(produtos){
    pagina = ''
    for (let i in produtos){
        if (produtos[i].categoria == '2'){
            pagina += '<div class="items">'
            pagina += '<h1 class="'+produtos[i].categoria+'">'+produtos[i].nome+'</h1>'
            pagina += '<img src="./imgs/'+produtos[i].nome+'prod.png">'
            pagina += '<h1>R$'+produtos[i].valor+'</h1>'
            pagina += '<select name="" id="categorias">'
            pagina += '<option value="Quilo">Quilo</option>'
            pagina += '<option value="Duzia">Duzia</option>'
            pagina += '<option value="Unidade">Unidade</option>'
            pagina += '</select>'
            pagina += '<p><button class="comprar">Comprar</button></p>'
            pagina += '</div>'
        }  
    }
    document.getElementById("catalogo").innerHTML = pagina
}
function Frutas(produtos){
    pagina = ''
    for (let i in produtos){
        if (produtos[i].categoria == '1'){
            pagina += '<div class="items">'
            pagina += '<h1 class="'+produtos[i].categoria+'">'+produtos[i].nome+'</h1>'
            pagina += '<img src="./imgs/'+produtos[i].nome+'prod.png">'
            pagina += '<h1>R$'+produtos[i].valor+'</h1>'
            pagina += '<select name="" id="categorias">'
            pagina += '<option value="Quilo">Quilo</option>'
            pagina += '<option value="Duzia">Duzia</option>'
            pagina += '<option value="Unidade">Unidade</option>'
            pagina += '</select>'
            pagina += '<p><button class="comprar">Comprar</button></p>'
            pagina += '</div>'
        }  
    }
    document.getElementById("catalogo").innerHTML = pagina
}
function Legumes(produtos){
    pagina = ''
    for (let i in produtos){
        if (produtos[i].categoria == '3'){
            pagina += '<div class="items">'
            pagina += '<h1 class="'+produtos[i].categoria+'">'+produtos[i].nome+'</h1>'
            pagina += '<img src="./imgs/'+produtos[i].nome+'prod.png">'
            pagina += '<h1>R$'+produtos[i].valor+'</h1>'
            pagina += '<select name="" id="categorias">'
            pagina += '<option value="Quilo">Quilo</option>'
            pagina += '<option value="Duzia">Duzia</option>'
            pagina += '<option value="Unidade">Unidade</option>'
            pagina += '</select>'
            pagina += '<p><button class="comprar">Comprar</button></p>'
            pagina += '</div>'
        }  
    }
    document.getElementById("catalogo").innerHTML = pagina
}