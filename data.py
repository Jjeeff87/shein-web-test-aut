from helpers import get_env

SHEIN_URL = get_env("SHEIN_URL", "https://www.shein.com/pt/")

# Termos usados na busca de produtos
SEARCH_TERM = get_env("SEARCH_TERM", "vestido")
SEARCH_TERM_NO_RESULTS = "xzzqwnaoexisteprodutoassim"

# Fragmento esperado no nome do produto no topo dos resultados (pode mudar com o tempo/estoque)
EXPECTED_PRODUCT_NAME_FRAGMENT = "vestido"
