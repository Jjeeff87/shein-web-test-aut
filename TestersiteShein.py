import data
import helpers
from SHEIN import SheinHomePage, SheinProductPage, SheinSearchResultsPage


class TestSheinSearch:
    """Testes automatizados da busca de produtos em shein.com/pt."""

    def setup_method(self):
        if not helpers.is_url_reachable(data.SHEIN_URL):
            print("Não foi possível conectar ao site da Shein. Verifique sua conexão.")

        self.driver.get(data.SHEIN_URL)
        self.home_page = SheinHomePage(self.driver)
        self.home_page.reject_cookies_if_present()

    def test_search_returns_results(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = SheinSearchResultsPage(self.driver)
        results_text = results_page.get_results_count_text()

        assert results_text != ""

    def test_search_with_no_results_shows_message(self):
        self.home_page.search_for(data.SEARCH_TERM_NO_RESULTS)

        results_page = SheinSearchResultsPage(self.driver)
        assert results_page.has_no_results_message()

    def test_open_first_product_shows_title_and_price(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = SheinSearchResultsPage(self.driver)
        results_page.open_first_product()

        product_page = SheinProductPage(self.driver)

        assert product_page.get_title() != ""
        assert product_page.is_price_displayed()

    def test_add_first_product_to_cart(self):
        self.home_page.search_for(data.SEARCH_TERM)

        results_page = SheinSearchResultsPage(self.driver)
        results_page.open_first_product()

        product_page = SheinProductPage(self.driver)
        product_page.add_to_cart()

        # Verificação simples; ajustar depois de confirmar o comportamento
        # exato do carrinho (ex.: contador no header, mini-cart, etc.).
        helpers.human_pause()
