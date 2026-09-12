from helpers import get_env

SHEIN_URL = get_env("SHEIN_URL", "https://www.shein.com/pt/")

# Terms used in the product search
SEARCH_TERM = get_env("SEARCH_TERM", "vestido")
SEARCH_TERM_NO_RESULTS = "xzzqwnaoexisteprodutoassim"

# Expected fragment in the name of the top product in the results (may change over time/stock)
EXPECTED_PRODUCT_NAME_FRAGMENT = "vestido"
