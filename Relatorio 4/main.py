from writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer

productAnalyzer = ProductAnalyzer()

writeAJson(productAnalyzer.clienteQueMaisGastou(), "Cliente que mais gastou")
writeAJson(productAnalyzer.totalVendasNoDia(), "Total de vendas no dia")
writeAJson(productAnalyzer.produtoMaisVendido(), "Produto mais vendido")
writeAJson(productAnalyzer.produtosVendidosAcimaDeUmaUnidade(), "Produtos vendidos acima de uma unidade")