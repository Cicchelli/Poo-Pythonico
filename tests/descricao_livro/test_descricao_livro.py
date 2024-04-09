from src.livro.livro import Livro


def test_descricao_livro():
    livro = Livro("Hary Potter e a Pedra Filosofal", "J.K. Rowling", 300)
    assert (
        repr(livro)
        == "O livro Hary Potter e a Pedra Filosofal de J.K. Rowling possui 300 páginas."
    )
