function busca(categoria) {
    if (categoria === "Frutas") buscaFrutas();
    else if (categoria === "Verduras") buscaVerduras();
    else if (categoria === "Legumes") buscaLegumes();
}

function buscaTodos() {
    buscarProdutos();
}

function buscaFrutas() {
    buscarProdutos("1");
}

function buscaVerduras() {
    buscarProdutos("2");
}

function buscaLegumes() {
    buscarProdutos("3");
}

function buscarProdutos(categoria = null) {
    fetch('http://localhost:3000/produtos')
        .then(response => response.json())
        .then(dados => {
            if (categoria) {
                dados = dados.filter(p => p.categoria == categoria);
            }
            renderizarProdutos(dados);
        });
}

function renderizarProdutos(produtos) {
    let pagina = "";

    produtos.forEach(produto => {
        pagina += `
            <div class="items">
                <h1 class="${produto.categoria}">${produto.nome}</h1>
                <img src="./imgs/${produto.nome}prod.png">
                <h1>R$${produto.valor}</h1>

                <select>
                    <option>Quilo</option>
                    <option>Duzia</option>
                    <option>Unidade</option>
                </select>

                <p><button class="comprar">Comprar</button></p>
            </div>
        `;
    });

    document.getElementById("catalogo").innerHTML = pagina;
}
