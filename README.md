# Shein — Automação de testes (busca de produtos shein.com/pt)

Testes automatizados em Python/Selenium para o fluxo de **busca de produtos** do
site [shein.com/pt](https://www.shein.com/pt/), seguindo a mesma linha dos
outros projetos (IKEA-WEB_TEST_AUT, Trotiurban), com algumas atualizações.

## Estrutura

| Arquivo/Pasta          | Papel                                                                          |
| ---------------------- | ------------------------------------------------------------------------------- |
| `data.py`               | URL do site e termos de busca, lidos do `.env` com fallback                     |
| `helpers.py`            | Utilitários: checar site no ar, digitação/pausas "humanizadas", leitura de `.env` |
| `common/base_page.py`   | `BasePage` com operações comuns (find, click, digitar humanizado)               |
| `SHEIN.py`              | Page Objects: `SheinHomePage`, `SheinSearchResultsPage`, `SheinProductPage`     |
| `conftest.py`           | Fixture do driver (Chrome) + screenshot automático em falha                    |
| `TestersiteShein.py`    | Testes pytest                                                                    |
| `.github/workflows/`    | CI: roda os testes a cada push/PR                                               |

## Novidades em relação ao padrão anterior (IKEA)

- Driver via **Selenium Manager** — sem precisar baixar/configurar chromedriver manualmente.
- Fixture `chrome_driver` em `conftest.py` no lugar de `setup_class`/`teardown_class`.
- Config por `.env` (`python-dotenv`) em vez de valores fixos no `data.py`.
- `BasePage` comum, reaproveitável entre projetos (Shein, Continente, IKEA...).
- Screenshot automático quando um teste falha (salvo em `screenshots/`).
- Workflow de CI (GitHub Actions) rodando a suíte a cada push/PR.

## Sobre a digitação "humanizada"

Em vez de preencher o campo de busca instantaneamente, `helpers.human_type` digita
caractere por caractere com pequenas pausas aleatórias, e `helpers.human_pause` insere
pausas curtas entre ações — deixando a automação com um ritmo mais parecido com o de
uma pessoa real interagindo com o site.

## Casos de teste

- Busca por um termo válido ("vestido") retorna resultados.
- Busca por um termo inexistente mostra mensagem de "sem resultados".
- Abrir o primeiro produto da lista exibe título e preço.
- Adicionar o primeiro produto ao carrinho.

## Instalação

```bash
pip install -r requirements.txt
cp .env.example .env   # ajuste SHEIN_URL / SEARCH_TERM se necessário
```

Requer o Chrome instalado localmente (o Selenium Manager cuida do driver automaticamente).

## Rodando os testes

```bash
pytest -v
```

## Aviso importante

Os locators em `SHEIN.py` são um ponto de partida (marcados com `TODO`) — a Shein
é um site bem dinâmico (JS pesado, proteção anti-bot, redirecionamento por região),
e não deu pra inspecionar o DOM real via fetch simples ao montar este projeto.
**Confirme/ajuste os seletores no site ao vivo antes de rodar de verdade.**

## Publicando no GitHub

```bash
git init
git add .
git commit -m "Automação de testes de busca de produtos - shein.com/pt"
git remote add origin <URL_DO_SEU_REPOSITORIO_GITHUB>
git push -u origin main
```
